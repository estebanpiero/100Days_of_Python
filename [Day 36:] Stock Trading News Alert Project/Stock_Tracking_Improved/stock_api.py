# stock_api.py - API interaction with caching and retry logic

import requests
import json
import os
from datetime import datetime, timedelta
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

logger = logging.getLogger(__name__)


class StockAPI:
    def __init__(self, stock_api_key, news_api_key, stock_web, news_web):
        self.stock_api_key = stock_api_key
        self.news_api_key = news_api_key
        self.stock_web = stock_web
        self.news_web = news_web
        self.cache_dir = 'cache'
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def _get_cache_path(self, symbol, data_type='stock'):
        """Get cache file path"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        return os.path.join(self.cache_dir, f"{symbol}_{data_type}_{date_str}.json")
    
    def _load_from_cache(self, symbol, data_type='stock'):
        """Load data from cache if available"""
        cache_path = self._get_cache_path(symbol, data_type)
        
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'r') as f:
                    cached_data = json.load(f)
                
                # Check if cache is still valid (same day)
                cache_date = cached_data.get('cached_at', '')
                if cache_date.startswith(datetime.now().strftime('%Y-%m-%d')):
                    logger.info(f"  Using cached data for {symbol}")
                    return cached_data.get('data')
            except Exception as e:
                logger.warning(f"Error reading cache for {symbol}: {e}")
        
        return None
    
    def _save_to_cache(self, symbol, data, data_type='stock'):
        """Save data to cache"""
        cache_path = self._get_cache_path(symbol, data_type)
        
        try:
            cache_data = {
                'cached_at': datetime.now().isoformat(),
                'data': data
            }
            
            with open(cache_path, 'w') as f:
                json.dump(cache_data, f)
            
            logger.debug(f"  Cached data for {symbol}")
        except Exception as e:
            logger.warning(f"Error saving cache for {symbol}: {e}")
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def get_stock_data(self, symbol):
        """Fetch stock data with caching and retry logic"""
        # Check cache first
        cached_data = self._load_from_cache(symbol, 'stock')
        if cached_data:
            return cached_data
        
        # Fetch from API
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': self.stock_api_key,
        }
        
        try:
            response = requests.get(self.stock_web, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Check for API errors
            if 'Error Message' in data:
                logger.error(f"API Error for {symbol}: {data['Error Message']}")
                return None
            
            if 'Note' in data:
                logger.warning(f"API limit reached: {data['Note']}")
                return None
            
            time_series = data.get('Time Series (Daily)')
            
            if time_series:
                # Cache the data
                self._save_to_cache(symbol, time_series, 'stock')
            
            return time_series
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error for {symbol}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error fetching {symbol}: {e}")
            return None
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def get_news(self, company_name):
        """Fetch news articles with retry logic"""
        # Check cache first
        cached_news = self._load_from_cache(company_name, 'news')
        if cached_news:
            return cached_news
        
        params = {
            'apikey': self.news_api_key,
            'qInTitle': company_name,
        }
        
        try:
            response = requests.get(self.news_web, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            articles = data.get('articles', [])[:3]
            
            # Cache the news
            self._save_to_cache(company_name, articles, 'news')
            
            return articles
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error for news ({company_name}): {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error fetching news for {company_name}: {e}")
            return []
