# config_manager.py - Configuration management

import yaml
import os
import logging

logger = logging.getLogger(__name__)


class ConfigManager:
    @staticmethod
    def load_config(config_file='config.yaml'):
        """Load configuration from YAML file"""
        if not os.path.exists(config_file):
            logger.warning(f"Config file {config_file} not found. Creating default config.")
            ConfigManager.create_default_config(config_file)
        
        try:
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
            
            logger.info(f"Configuration loaded from {config_file}")
            return config
        
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return ConfigManager.get_default_config()
    
    @staticmethod
    def get_default_config():
        """Return default configuration"""
        return {
            'stocks': [
                {'symbol': 'TSLA', 'company': 'tesla', 'target': 300.00, 'stop_loss': 200.00},
                {'symbol': 'INTC', 'company': 'intel', 'target': 50.00, 'stop_loss': 30.00},
                {'symbol': 'AAPL', 'company': 'apple', 'target': 200.00, 'stop_loss': 150.00},
                {'symbol': 'NVDA', 'company': 'nvidia', 'target': 150.00, 'stop_loss': 100.00},
                {'symbol': 'FTNT', 'company': 'fortinet', 'target': 80.00, 'stop_loss': 50.00},
                {'symbol': 'AMD', 'company': 'amd', 'target': 180.00, 'stop_loss': 120.00},
                {'symbol': 'SPY', 'company': 'spy', 'target': 500.00, 'stop_loss': 400.00}
            ],
            'alerts': {
                'threshold': 1.0,
                'cooldown_hours': 4,
                'channels': ['email']
            },
            'api': {
                'rate_limit_delay': 12,
                'max_retries': 3
            },
            'schedule': {
                'market_close_check': '16:00',
                'daily_report': '17:00',
                'chart_generation': '17:30'
            }
        }
    
    @staticmethod
    def create_default_config(config_file='config.yaml'):
        """Create default configuration file"""
        config = ConfigManager.get_default_config()
        
        try:
            with open(config_file, 'w') as f:
                yaml.dump(config, f, default_flow_style=False, sort_keys=False)
            
            logger.info(f"Default config created at {config_file}")
        
        except Exception as e:
            logger.error(f"Error creating config file: {e}")
