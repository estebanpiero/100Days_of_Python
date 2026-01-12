# visualization.py - Chart generation

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import logging
import os

logger = logging.getLogger(__name__)

# Set style
plt.style.use('seaborn-v0_8-darkgrid')


class Visualizer:
    def __init__(self, database):
        self.db = database
        self.charts_dir = 'charts'
        
        # Ensure charts directory exists
        os.makedirs(self.charts_dir, exist_ok=True)
    
    def create_price_chart(self, symbol, days=30):
        """Generate price chart"""
        data = self.db.get_historical_prices(symbol, days)
        
        if not data:
            logger.warning(f"No data available to create chart for {symbol}")
            return None
        
        dates = [datetime.strptime(row[0], '%Y-%m-%d') for row in reversed(data)]
        prices = [row[1] for row in reversed(data)]
        
        fig, ax = plt.subplots(figsize=(14, 7))
        
        ax.plot(dates, prices, marker='o', linewidth=2, markersize=4, color='#2E86AB')
        
        ax.set_title(f'{symbol} - {days} Day Price History', fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Price ($)', fontsize=12)
        
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=max(1, days // 10)))
        
        plt.xticks(rotation=45)
        ax.grid(True, alpha=0.3)
        
        # Add price labels
        for i in range(0, len(dates), max(1, len(dates) // 5)):
            ax.annotate(f'${prices[i]:.2f}', 
                       xy=(dates[i], prices[i]),
                       xytext=(0, 10), 
                       textcoords='offset points',
                       ha='center',
                       fontsize=8,
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))
        
        plt.tight_layout()
        
        filename = f'{self.charts_dir}/{symbol}_price_{days}d.png'
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Created price chart: {filename}")
        return filename
    
    def create_technical_chart(self, symbol, days=30):
        """Generate chart with technical indicators"""
        from analytics import Analytics
        
        data = self.db.get_historical_prices(symbol, days)
        
        if not data:
            logger.warning(f"No data available to create technical chart for {symbol}")
            return None
        
        dates = [datetime.strptime(row[0], '%Y-%m-%d') for row in reversed(data)]
        prices = [row[1] for row in reversed(data)]
        
        analytics = Analytics(self.db)
        
        # Calculate moving averages for each day
        ma7_values = []
        ma30_values = []
        
        for i in range(len(prices)):
            if i >= 6:
                ma7 = sum(prices[max(0, i-6):i+1]) / min(7, i+1)
                ma7_values.append(ma7)
            else:
                ma7_values.append(None)
            
            if i >= 29:
                ma30 = sum(prices[max(0, i-29):i+1]) / min(30, i+1)
                ma30_values.append(ma30)
            else:
                ma30_values.append(None)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
        
        # Price and MA chart
        ax1.plot(dates, prices, label='Price', linewidth=2, color='#2E86AB')
        
        # Plot MAs
        if any(ma7_values):
            ax1.plot(dates, ma7_values, label='MA(7)', linewidth=1.5, color='#F18F01', linestyle='--')
        if any(ma30_values):
            ax1.plot(dates, ma30_values, label='MA(30)', linewidth=1.5, color='#C73E1D', linestyle='--')
        
        ax1.set_title(f'{symbol} - Technical Analysis', fontsize=16, fontweight='bold')
        ax1.set_ylabel('Price ($)', fontsize=12)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Volume chart
        volumes = [row[2] if row[2] else 0 for row in reversed(data)]
        ax2.bar(dates, volumes, color='#6C757D', alpha=0.5)
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylabel('Volume', fontsize=12)
        ax2.grid(True, alpha=0.3)
        
        # Format x-axis
        for ax in [ax1, ax2]:
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
            ax.xaxis.set_major_locator(mdates.DayLocator(interval=max(1, days // 10)))
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        filename = f'{self.charts_dir}/{symbol}_technical_{days}d.png'
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Created technical chart: {filename}")
        return filename
