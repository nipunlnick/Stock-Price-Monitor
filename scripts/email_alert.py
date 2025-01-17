from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

def email_alert(current_price, last_price, price_diff, percentage_diff):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender = os.getenv("SENDER_EMAIL")
    recipient = os.getenv("RECIPIENT_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    subject = 'Apple Stock Price Alert'
    body = f'The current price of Apple stock is ${current_price}'
    body += f'\nThe price changed by ${price_diff:.2f}'
    body += f'\nThe percentage difference is {percentage_diff:.2f}%'
    body += f'\nThis is an automated email alert.'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['from']= sender
    msg['to'] = recipient
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
        
    print('Email alert sent successfully!')
