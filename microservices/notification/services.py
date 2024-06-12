import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import settings
from .schemas import Notification

def send_email(notification: Notification):
    msg = MIMEMultipart()
    msg['From'] = settings.from_email
    msg['To'] = notification.recipient_email
    msg['Subject'] = notification.subject

    msg.attach(MIMEText(notification.message, 'plain'))

    with smtplib.SMTP(settings.smtp_server, settings.smtp_port) as server:
        server.starttls()
        server.login(settings.smtp_username, settings.smtp_password)
        server.send_message(msg)
