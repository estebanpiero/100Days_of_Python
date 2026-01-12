# portfolio.py - Portfolio management

import logging

logger = logging.getLogger(__name__)


class Portfolio:
    def __init__(self, database):
        self.db = database
    
    def add_position(self, symbol, shares, cost_basis, purchase_date=None):
        """Add stock position to portfolio"""
        self.db.add_portfolio_holding(symbol, shares, cost_basis, purchase_date)
    
    def get_holdings(self):
        """Get all portfolio holdings"""
        return self.db.get_portfolio_holdings()
    
    def has_holdings(self):
        """Check if portfolio has any holdings"""
        return len(self.get_holdings()) > 0
    
    def calculate_portfolio_value(self):
        """Calculate total portfolio value"""
        holdings = self.get_holdings()
        total_value = 0
        
        for holding in holdings:
            symbol = holding['symbol']
            shares = holding['shares']
            current_price = self.db.get_latest_price(symbol)
            
            if current_price:
                total_value += shares * current_price
        
        return total_value
    
    def calculate_gains_losses(self):
        """Calculate unrealized gains/losses"""
        holdings = self.get_holdings()
        results = {}
        
        for holding in holdings:
            symbol = holding['symbol']
            shares = holding['shares']
            cost_basis = holding['cost_basis']
            current_price = self.db.get_latest_price(symbol)
            
            if current_price:
                current_value = shares * current_price
                cost = shares * cost_basis
                gain_loss = current_value - cost
                gain_loss_pct = (gain_loss / cost) * 100 if cost > 0 else 0
                
                results[symbol] = {
                    'shares': shares,
                    'cost_basis': cost_basis,
                    'current_price': current_price,
                    'current_value': current_value,
                    'cost': cost,
                    'gain_loss': gain_loss,
                    'gain_loss_pct': gain_loss_pct
                }
        
        return results
    
    def get_summary(self):
        """Get portfolio summary as formatted string"""
        holdings = self.get_holdings()
        
        if not holdings:
            return "No holdings in portfolio.\n"
        
        gains_losses = self.calculate_gains_losses()
        total_value = self.calculate_portfolio_value()
        total_cost = sum(h['shares'] * h['cost_basis'] for h in holdings)
        total_gain_loss = total_value - total_cost
        total_gain_loss_pct = (total_gain_loss / total_cost * 100) if total_cost > 0 else 0
        
        summary = ""
        
        for symbol, data in gains_losses.items():
            summary += f"{symbol}:\n"
            summary += f"  Shares: {data['shares']:.2f}\n"
            summary += f"  Cost Basis: ${data['cost_basis']:.2f}\n"
            summary += f"  Current Price: ${data['current_price']:.2f}\n"
            summary += f"  Current Value: ${data['current_value']:.2f}\n"
            summary += f"  Gain/Loss: ${data['gain_loss']:.2f} ({data['gain_loss_pct']:.2f}%)\n\n"
        
        summary += "-" * 60 + "\n"
        summary += f"Total Portfolio Value: ${total_value:.2f}\n"
        summary += f"Total Cost: ${total_cost:.2f}\n"
        summary += f"Total Gain/Loss: ${total_gain_loss:.2f} ({total_gain_loss_pct:.2f}%)\n"
        
        return summary
