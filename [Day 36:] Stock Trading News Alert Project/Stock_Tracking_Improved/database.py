# database.py - SQLite database operations

import sqlite3
import csv
import logging
from datetime import datetime
import os

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, db_name='stocks.db'):
        self.db_name = db_name
        self.init_database()
    
    def get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_name)
    
    def init_database(self):
        """Initialize SQLite database with tables"""
        conn = self.get_connection()
        c = conn.cursor()
        
        # Stock prices table
        c.execute('''CREATE TABLE IF NOT EXISTS stock_prices
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      date TEXT NOT NULL,
                      symbol TEXT NOT NULL,
                      closing_price REAL NOT NULL,
                      volume INTEGER,
                      change_percent REAL,
                      created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                      UNIQUE(date, symbol))''')
        
        # Alerts table
        c.execute('''CREATE TABLE IF NOT EXISTS alerts
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      timestamp TEXT NOT NULL,
                      symbol TEXT NOT NULL,
                      alert_type TEXT NOT NULL,
                      message TEXT,
                      sent INTEGER DEFAULT 0,
                      created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
        
        # Portfolio holdings table
        c.execute('''CREATE TABLE IF NOT EXISTS portfolio
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      symbol TEXT UNIQUE NOT NULL,
                      shares REAL NOT NULL,
                      cost_basis REAL NOT NULL,
                      purchase_date TEXT,
                      created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
        
        # Create indexes for performance
        c.execute('CREATE INDEX IF NOT EXISTS idx_stock_symbol ON stock_prices(symbol)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_stock_date ON stock_prices(date)')
        c.execute('CREATE INDEX IF NOT EXISTS idx_alert_symbol ON alerts(symbol)')
        
        conn.commit()
        conn.close()
        
        logger.info("Database initialized successfully")
    
    def save_stock_data(self, symbol, date, closing_price, volume, change_percent):
        """Save daily stock data"""
        conn = self.get_connection()
        c = conn.cursor()
        
        try:
            c.execute("""INSERT OR REPLACE INTO stock_prices 
                        (date, symbol, closing_price, volume, change_percent) 
                        VALUES (?, ?, ?, ?, ?)""",
                     (date, symbol, closing_price, volume, change_percent))
            conn.commit()
            logger.debug(f"Saved data for {symbol} on {date}")
        except Exception as e:
            logger.error(f"Error saving stock data for {symbol}: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    def save_alert(self, symbol, alert_type, message, sent=0):
        """Save alert to database"""
        conn = self.get_connection()
        c = conn.cursor()
        
        try:
            timestamp = datetime.now().isoformat()
            c.execute("""INSERT INTO alerts 
                        (timestamp, symbol, alert_type, message, sent) 
                        VALUES (?, ?, ?, ?, ?)""",
                     (timestamp, symbol, alert_type, message, sent))
            conn.commit()
            logger.debug(f"Saved alert for {symbol}")
        except Exception as e:
            logger.error(f"Error saving alert for {symbol}: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    def get_latest_price(self, symbol):
        """Get latest closing price for a symbol"""
        conn = self.get_connection()
        c = conn.cursor()
        
        c.execute("""SELECT closing_price FROM stock_prices 
                    WHERE symbol=? ORDER BY date DESC LIMIT 1""", (symbol,))
        result = c.fetchone()
        conn.close()
        
        return result[0] if result else None
    
    def get_historical_prices(self, symbol, days):
        """Get historical prices for a symbol"""
        conn = self.get_connection()
        c = conn.cursor()
        
        c.execute("""SELECT date, closing_price, volume FROM stock_prices 
                    WHERE symbol=? ORDER BY date DESC LIMIT ?""", 
                 (symbol, days))
        results = c.fetchall()
        conn.close()
        
        return results
    
    def get_price_history(self, symbol, days):
        """Get price history as list of floats"""
        results = self.get_historical_prices(symbol, days)
        return [row[1] for row in reversed(results)]
    
    def get_volume_history(self, symbol, days):
        """Get volume history"""
        results = self.get_historical_prices(symbol, days)
        return [row[2] for row in reversed(results)]
    
    def export_to_csv(self, symbol, days=30):
        """Export historical data to CSV"""
        conn = self.get_connection()
        c = conn.cursor()
        
        c.execute("""SELECT date, symbol, closing_price, volume, change_percent 
                    FROM stock_prices 
                    WHERE symbol=? ORDER BY date DESC LIMIT ?""", 
                 (symbol, days))
        data = c.fetchall()
        conn.close()
        
        # Ensure exports directory exists
        os.makedirs('exports', exist_ok=True)
        
        filename = f'exports/{symbol}_history_{datetime.now().strftime("%Y%m%d")}.csv'
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Symbol', 'Closing Price', 'Volume', 'Change %'])
            writer.writerows(data)
        
        logger.info(f"Exported {len(data)} records to {filename}")
        return filename
    
    def add_portfolio_holding(self, symbol, shares, cost_basis, purchase_date=None):
        """Add a stock position to portfolio"""
        conn = self.get_connection()
        c = conn.cursor()
        
        if not purchase_date:
            purchase_date = datetime.now().strftime('%Y-%m-%d')
        
        try:
            c.execute("""INSERT OR REPLACE INTO portfolio 
                        (symbol, shares, cost_basis, purchase_date) 
                        VALUES (?, ?, ?, ?)""",
                     (symbol, shares, cost_basis, purchase_date))
            conn.commit()
            logger.info(f"Added {shares} shares of {symbol} to portfolio")
        except Exception as e:
            logger.error(f"Error adding portfolio holding: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    def get_portfolio_holdings(self):
        """Get all portfolio holdings"""
        conn = self.get_connection()
        c = conn.cursor()
        
        c.execute("SELECT symbol, shares, cost_basis, purchase_date FROM portfolio")
        results = c.fetchall()
        conn.close()
        
        return [
            {
                'symbol': row[0],
                'shares': row[1],
                'cost_basis': row[2],
                'purchase_date': row[3]
            }
            for row in results
        ]
