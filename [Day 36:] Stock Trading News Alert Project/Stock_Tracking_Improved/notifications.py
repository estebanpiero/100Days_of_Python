# notifications.py - Multi-channel notification system

import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from collections import defaultdict

logger = logging.getLogger(__name__)


class NotificationManager:
    def __init__(self, twilio_account_id, twilio_token, twilio_number, my_number,
                 smtp_server, smtp_port, sender_email, sender_password, receiver_email):
        # Twilio setup
        self.twilio_account_id = twilio_account_id
        self.twilio_token = twilio_token
        self.twilio_number = twilio_number
        self.my_number = my_number
        
        if self.twilio_account_id and self.twilio_token:
            try:
                from twilio.rest import Client
                self.twilio_client = Client(twilio_account_id, twilio_token)
            except ImportError:
                self.twilio_client = None
                logger.warning("Twilio not installed. SMS notifications disabled.")
        else:
            self.twilio_client = None
            logger.warning("Twilio credentials not provided. SMS notifications disabled.")
        
        # Email setup
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email
        
        # Alert throttling
        self.last_alert_time = defaultdict(lambda: None)
        self.cooldown_hours = 4
    
    def should_send_alert(self, symbol):
        """Check if enough time has passed since last alert"""
        if symbol not in self.last_alert_time or self.last_alert_time[symbol] is None:
            self.last_alert_time[symbol] = datetime.now()
            return True
        
        time_since_last = datetime.now() - self.last_alert_time[symbol]
        
        if time_since_last > timedelta(hours=self.cooldown_hours):
            self.last_alert_time[symbol] = datetime.now()
            return True
        
        logger.info(f"  Cooldown active for {symbol} (last alert: {time_since_last.seconds // 3600}h ago)")
        return False
    
    def send_sms(self, message):
        """Send SMS notification via Twilio"""
        if not self.twilio_client:
            logger.warning("SMS not sent: Twilio not configured")
            return False
        
        try:
            # Truncate message if too long (SMS limit is 1600 chars)
            if len(message) > 1500:
                message = message[:1500] + "..."
            
            msg = self.twilio_client.messages.create(
                body=message,
                from_=f"whatsapp:{self.twilio_number}",
                to=f"whatsapp:{self.my_number}"
            )
            
            logger.info(f"SMS sent successfully: {msg.sid}")
            return True
        
        except Exception as e:
            logger.error(f"Error sending SMS: {e}")
            return False
    
    def send_email(self, subject, body):
        """Send email notification"""
        if not all([self.smtp_server, self.sender_email, self.sender_password, self.receiver_email]):
            logger.warning("Email not sent: Email not configured")
            return False
        
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = self.receiver_email
            message['Subject'] = subject
            
            message.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, int(self.smtp_port)) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"Email sent successfully to {self.receiver_email}")
            return True
        
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return False
