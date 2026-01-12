# main.py - Main orchestration file

import os
import time
import logging
from datetime import datetime
from dotenv import load_dotenv
import schedule

# CREATE DIRECTORIES FIRST (before logging setup)
def create_directories():
    """Create necessary directories if they don't exist"""
    directories = ['logs', 'cache', 'charts', 'exports']
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
    
    print("✓ Directories created/verified")

# Create directories BEFORE anything else
create_directories()

# Load environment variables
load_dotenv()

# Setup logging (NOW the logs directory exists)
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'stock_tracker.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

from stock_api import StockAPI
from database import Database
from analytics import Analytics
from notifications import NotificationManager
from portfolio import Portfolio
from visualization import Visualizer
from config_manager import ConfigManager


class StockTracker:
    def __init__(self):
        """Initialize the stock tracker"""
        logger.info("Initializing Stock Tracker...")
        
        # Load configuration
        self.config = ConfigManager.load_config()
        
        # Initialize components
        self.stock_api = StockAPI(
            stock_api_key=os.getenv('STOCK_API_KEY'),
            news_api_key=os.getenv('NEWS_API_KEY'),
            stock_web=os.getenv('STOCK_WEB'),
            news_web=os.getenv('NEWS_WEB')
        )
        
        self.db = Database()
        self.analytics = Analytics(self.db)
        self.notifier = NotificationManager(
            twilio_account_id=os.getenv('TWILIO_ACCOUNT_ID'),
            twilio_token=os.getenv('TWILIO_TOKEN'),
            twilio_number=os.getenv('TWILIO_NUMBER'),
            my_number=os.getenv('USER_NUMBER'),
            smtp_server=os.getenv('SMTP_SERVER'),
            smtp_port=os.getenv('SMTP_PORT'),
            sender_email=os.getenv('SENDER_EMAIL'),
            sender_password=os.getenv('SENDER_PASSWORD'),
            receiver_email=os.getenv('RECEIVER_EMAIL')
        )
        
        self.visualizer = Visualizer(self.db)
        self.portfolio = Portfolio(self.db)
        
        # Load stocks from config
        self.stocks = self.config.get('stocks', {})
        self.alert_threshold = self.config.get('alerts', {}).get('threshold', 1.0)
        self.alert_channels = self.config.get('alerts', {}).get('channels', ['sms'])
        
        logger.info(f"Loaded {len(self.stocks)} stocks to track")
    
    def check_stock(self, symbol, company_name, config):
        """Check a single stock and send alerts if needed"""
        try:
            logger.info(f"Checking {symbol} ({company_name})...")
            
            # Get stock data (with caching)
            stock_data = self.stock_api.get_stock_data(symbol)
            
            if not stock_data:
                logger.warning(f"No data available for {symbol}")
                return
            
            # Calculate price changes
            price_info = self._calculate_price_change(stock_data)
            
            # Save to database
            self.db.save_stock_data(
                symbol=symbol,
                date=datetime.now().strftime('%Y-%m-%d'),
                closing_price=price_info['yesterday'],
                volume=price_info.get('volume', 0),
                change_percent=price_info['percent']
            )
            
            # Calculate technical indicators
            ma_7 = self.analytics.calculate_moving_average(symbol, period=7)
            ma_30 = self.analytics.calculate_moving_average(symbol, period=30)
            rsi = self.analytics.calculate_rsi(symbol, period=14)
            trend = self.analytics.detect_trend(symbol, days=5)
            
            # Check price targets and stop losses
            target_alert = self._check_price_targets(symbol, price_info['yesterday'], config)
            
            # Check volume spikes
            volume_alert = self._check_volume_spike(symbol, price_info.get('volume', 0))
            
            # Determine if alert is needed
            should_alert = False
            alert_reasons = []
            
            if price_info['percent'] > self.alert_threshold:
                should_alert = True
                alert_reasons.append(f"Price change: {price_info['percent']:.2f}%")
            
            if target_alert:
                should_alert = True
                alert_reasons.append(target_alert)
            
            if volume_alert:
                should_alert = True
                alert_reasons.append(volume_alert)
            
            # Check if RSI indicates overbought/oversold
            if rsi and (rsi > 70 or rsi < 30):
                should_alert = True
                alert_reasons.append(f"RSI: {rsi:.1f} ({'Overbought' if rsi > 70 else 'Oversold'})")
            
            # Log the check results (Handle None values properly)
            rsi_display = f"{rsi:.1f}" if rsi is not None else "N/A"
            logger.info(f"  {symbol} - Price: ${price_info['yesterday']:.2f}, "
                       f"Change: {price_info['direction']} {price_info['percent']:.2f}%, "
                       f"RSI: {rsi_display}, Trend: {trend}")
            
            # Send alerts if needed and cooldown has passed
            if should_alert and self.notifier.should_send_alert(symbol):
                # Get news articles
                articles = self.stock_api.get_news(company_name)
                
                # Analyze sentiment
                sentiment = self.analytics.analyze_news_sentiment(articles)
                
                # Format alert message
                alert_message = self._format_alert_message(
                    symbol=symbol,
                    company_name=company_name,
                    price_info=price_info,
                    articles=articles,
                    ma_7=ma_7,
                    ma_30=ma_30,
                    rsi=rsi,
                    trend=trend,
                    sentiment=sentiment,
                    alert_reasons=alert_reasons
                )
                
                # Send via configured channels
                if 'sms' in self.alert_channels:
                    self.notifier.send_sms(alert_message)
                
                if 'email' in self.alert_channels:
                    self.notifier.send_email(
                        subject=f"🚨 Stock Alert: {symbol} {price_info['direction']} {price_info['percent']:.2f}%",
                        body=alert_message
                    )
                
                # Save alert to database
                self.db.save_alert(
                    symbol=symbol,
                    alert_type='PRICE_CHANGE',
                    message=alert_message,
                    sent=1
                )
                
                logger.info(f"  ✓ Alert sent for {symbol}")
            
            # Add delay to respect API rate limits
            time.sleep(self.config.get('api', {}).get('rate_limit_delay', 12))
            
        except Exception as e:
            logger.error(f"Error checking {symbol}: {e}", exc_info=True)
    
    def _calculate_price_change(self, stock_data):
        """Calculate price difference and percentage"""
        data_list = [value for (key, value) in stock_data.items()]
        
        yesterday_data = data_list[0]
        daybefore_data = data_list[1]
        
        yesterday_closing_price = float(yesterday_data['4. close'])
        daybefore_closing_price = float(daybefore_data['4. close'])
        yesterday_volume = int(yesterday_data['5. volume'])
        
        difference = yesterday_closing_price - daybefore_closing_price
        diff_percent = (abs(difference) / yesterday_closing_price) * 100
        
        direction = "🔺" if difference > 0 else "🔻"
        
        return {
            'yesterday': yesterday_closing_price,
            'daybefore': daybefore_closing_price,
            'difference': difference,
            'percent': diff_percent,
            'direction': direction,
            'volume': yesterday_volume
        }
    
    def _check_price_targets(self, symbol, current_price, config):
        """Check if price hits targets or stop losses"""
        if 'target' in config and current_price >= config['target']:
            return f"🎯 TARGET HIT! Reached ${current_price:.2f}"
        
        if 'stop_loss' in config and current_price <= config['stop_loss']:
            return f"🛑 STOP LOSS! Dropped to ${current_price:.2f}"
        
        return None
    
    def _check_volume_spike(self, symbol, current_volume):
        """Check for unusual trading volume"""
        avg_volume = self.analytics.get_average_volume(symbol, days=10)
        
        if avg_volume and current_volume > avg_volume * 2.0:
            return f"⚡ VOLUME SPIKE: {current_volume/avg_volume:.1f}x average"
        
        return None
    
    def _format_alert_message(self, symbol, company_name, price_info, articles, 
                             ma_7, ma_30, rsi, trend, sentiment, alert_reasons):
        """Format comprehensive alert message"""
        message = f"🚨 STOCK ALERT: {symbol}\n"
        message += "=" * 40 + "\n\n"
        
        # Alert reasons
        message += "📌 Alert Reasons:\n"
        for reason in alert_reasons:
            message += f"  • {reason}\n"
        message += "\n"
        
        # Price information
        message += f"💰 Price: ${price_info['yesterday']:.2f}\n"
        message += f"📊 Change: {price_info['direction']} ${abs(price_info['difference']):.2f} ({price_info['percent']:.2f}%)\n"
        message += f"📈 Volume: {price_info['volume']:,}\n\n"
        
        # Technical indicators
        message += "📈 Technical Indicators:\n"
        if ma_7:
            message += f"  • MA(7): ${ma_7:.2f}\n"
        if ma_30:
            message += f"  • MA(30): ${ma_30:.2f}\n"
        if rsi:
            message += f"  • RSI: {rsi:.1f}\n"
        message += f"  • Trend: {trend}\n\n"
        
        # News sentiment
        if articles:
            message += f"📰 News Sentiment: {sentiment}\n"
            message += "Top Headlines:\n"
            for i, article in enumerate(articles[:3], 1):
                title = article.get('title', 'No title')[:60]
                message += f"  {i}. {title}...\n"
        
        return message
    
    def run_all_checks(self):
        """Run checks for all configured stocks"""
        logger.info("=" * 60)
        logger.info(f"STOCK PRICE TRACKER - Starting run at {datetime.now()}")
        logger.info("=" * 60)
        
        for stock_config in self.stocks:
            symbol = stock_config['symbol']
            company_name = stock_config['company']
            self.check_stock(symbol, company_name, stock_config)
        
        logger.info("=" * 60)
        logger.info("Stock monitoring complete!")
        logger.info("=" * 60)
    
    def generate_daily_report(self):
        """Generate comprehensive daily report"""
        logger.info("Generating daily report...")
        
        report = "📊 DAILY STOCK REPORT\n"
        report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += "=" * 60 + "\n\n"
        
        for stock_config in self.stocks:
            symbol = stock_config['symbol']
            
            # Get latest data
            latest_price = self.db.get_latest_price(symbol)
            
            if not latest_price:
                continue
            
            # Calculate metrics
            ma_7 = self.analytics.calculate_moving_average(symbol, period=7)
            rsi = self.analytics.calculate_rsi(symbol, period=14)
            trend = self.analytics.detect_trend(symbol, days=5)
            
            report += f"{symbol}:\n"
            report += f"  Price: ${latest_price:.2f}\n"
            
            if ma_7:
                report += f"  MA(7): ${ma_7:.2f}\n"
            if rsi:
                report += f"  RSI: {rsi:.1f}\n"
            
            report += f"  Trend: {trend}\n\n"
        
        # Portfolio summary
        if hasattr(self, 'portfolio') and self.portfolio.has_holdings():
            report += "\n💼 PORTFOLIO SUMMARY\n"
            report += "-" * 60 + "\n"
            portfolio_summary = self.portfolio.get_summary()
            report += portfolio_summary
        
        # Send report via email
        if 'email' in self.alert_channels:
            self.notifier.send_email(
                subject=f"Daily Stock Report - {datetime.now().strftime('%Y-%m-%d')}",
                body=report
            )
        
        logger.info("Daily report generated and sent")
        
        return report
    
    def generate_charts(self):
        """Generate charts for all stocks"""
        logger.info("Generating charts...")
        
        for stock_config in self.stocks:
            symbol = stock_config['symbol']
            try:
                self.visualizer.create_price_chart(symbol, days=30)
                self.visualizer.create_technical_chart(symbol, days=30)
                logger.info(f"  ✓ Charts created for {symbol}")
            except Exception as e:
                logger.error(f"  ✗ Error creating charts for {symbol}: {e}")
        
        logger.info("Chart generation complete")
    
    def export_data(self, symbol=None, days=30):
        """Export historical data to CSV"""
        if symbol:
            symbols = [symbol]
        else:
            symbols = [s['symbol'] for s in self.stocks]
        
        for sym in symbols:
            try:
                self.db.export_to_csv(sym, days)
                logger.info(f"  ✓ Data exported for {sym}")
            except Exception as e:
                logger.error(f"  ✗ Error exporting data for {sym}: {e}")


def main():
    """Main entry point"""
    print("=" * 60)
    print("🚀 STOCK TRACKER - Initializing...")
    print("=" * 60)
    
    # Initialize tracker
    tracker = StockTracker()
    
    # Run immediate check
    tracker.run_all_checks()
    
    # Generate daily report
    tracker.generate_daily_report()
    
    # Generate charts
    tracker.generate_charts()
    
    # Setup scheduled jobs
    schedule.every().day.at("16:00").do(tracker.run_all_checks)  # Market close
    schedule.every().day.at("17:00").do(tracker.generate_daily_report)
    schedule.every().day.at("17:30").do(tracker.generate_charts)
    
    # Optional: Run during trading hours
    # schedule.every().hour.do(tracker.run_all_checks)
    
    logger.info("Scheduler started. Press Ctrl+C to exit.")
    
    # Keep running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        logger.info("Shutting down...")


if __name__ == "__main__":
    main()
