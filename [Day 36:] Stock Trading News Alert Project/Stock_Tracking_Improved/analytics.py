# analytics.py - Technical analysis and indicators (No TextBlob)

import logging

logger = logging.getLogger(__name__)


class Analytics:
    def __init__(self, database):
        self.db = database
        
        # Sentiment keywords for news analysis
        self.positive_keywords = [
            'surge', 'soar', 'rally', 'gain', 'rise', 'jump', 'climb', 'boost',
            'growth', 'profit', 'beat', 'exceed', 'strong', 'positive', 'bullish',
            'upgrade', 'outperform', 'success', 'win', 'breakthrough', 'record',
            'high', 'improved', 'expansion', 'innovation', 'optimistic', 'recovered',
            'up', 'increase', 'advance', 'better', 'excellent', 'outstanding'
        ]
        
        self.negative_keywords = [
            'plunge', 'plummet', 'drop', 'fall', 'decline', 'loss', 'crash', 'sink',
            'weak', 'disappoint', 'miss', 'negative', 'bearish', 'downgrade', 'concern',
            'warning', 'risk', 'fear', 'worry', 'trouble', 'problem', 'challenge',
            'low', 'underperform', 'struggle', 'fail', 'crisis', 'threat', 'volatile',
            'down', 'decrease', 'worse', 'poor', 'bad', 'terrible'
        ]
    
    def calculate_moving_average(self, symbol, period=7):
        """Calculate simple moving average"""
        prices = self.db.get_price_history(symbol, period)
        
        if len(prices) < period:
            return None
        
        ma = sum(prices[-period:]) / period
        return ma
    
    def calculate_rsi(self, symbol, period=14):
        """Calculate Relative Strength Index"""
        prices = self.db.get_price_history(symbol, period + 1)
        
        if len(prices) < period + 1:
            return None
        
        gains = []
        losses = []
        
        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        if len(gains) < period:
            return None
        
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def detect_trend(self, symbol, days=5):
        """Detect if stock is in uptrend or downtrend"""
        prices = self.db.get_price_history(symbol, days)
        
        if len(prices) < days:
            return "INSUFFICIENT_DATA"
        
        # Count how many days price increased
        increasing = sum(1 for i in range(1, len(prices)) if prices[i] > prices[i-1])
        
        if increasing >= days * 0.7:
            return "UPTREND"
        elif increasing <= days * 0.3:
            return "DOWNTREND"
        
        return "SIDEWAYS"
    
    def get_average_volume(self, symbol, days=10):
        """Get average trading volume"""
        volumes = self.db.get_volume_history(symbol, days)
        
        if not volumes or len(volumes) == 0:
            return None
        
        # Filter out None values
        valid_volumes = [v for v in volumes if v is not None]
        
        if not valid_volumes:
            return None
        
        return sum(valid_volumes) / len(valid_volumes)
    
    def calculate_volatility(self, symbol, days=30):
        """Calculate price volatility (standard deviation)"""
        prices = self.db.get_price_history(symbol, days)
        
        if len(prices) < 2:
            return None
        
        mean = sum(prices) / len(prices)
        variance = sum((p - mean) ** 2 for p in prices) / len(prices)
        std_dev = variance ** 0.5
        
        return std_dev
    
    def analyze_news_sentiment(self, articles):
        """
        Analyze sentiment of news articles using keyword-based approach
        Returns: POSITIVE, NEGATIVE, or NEUTRAL
        """
        if not articles:
            return "NEUTRAL"
        
        positive_count = 0
        negative_count = 0
        
        for article in articles:
            try:
                # Get title and description
                text = (article.get('title', '') + ' ' + article.get('description', '')).lower()
                
                if not text.strip():
                    continue
                
                # Count positive keywords
                for keyword in self.positive_keywords:
                    if keyword in text:
                        positive_count += 1
                
                # Count negative keywords
                for keyword in self.negative_keywords:
                    if keyword in text:
                        negative_count += 1
                
            except Exception as e:
                logger.warning(f"Error analyzing sentiment: {e}")
        
        # Calculate sentiment score
        total_keywords = positive_count + negative_count
        
        if total_keywords == 0:
            return "NEUTRAL"
        
        sentiment_score = (positive_count - negative_count) / total_keywords
        
        # Determine sentiment
        if sentiment_score > 0.2:
            return "POSITIVE"
        elif sentiment_score < -0.2:
            return "NEGATIVE"
        else:
            return "NEUTRAL"
    
    def calculate_support_resistance(self, symbol, days=30):
        """Calculate support and resistance levels"""
        prices = self.db.get_price_history(symbol, days)
        
        if len(prices) < 10:
            return None, None
        
        # Simple support/resistance calculation
        support = min(prices)
        resistance = max(prices)
        
        return support, resistance
