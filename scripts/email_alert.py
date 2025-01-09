import smtplib
from email.mime.text import MIMEText

def email_alert(current_price, last_price, price_diff, percentage_diff):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender = 'pvnipunlakshitha@gmail.com'
    receipient = 'nipunl1sandu@gmail.com'
    password = 'nsxi jned afzi mojp'

    subject = 'Apple Stock Price Alert'
    body = f'The current price of Apple stock is ${current_price}'
    body += f'\nThe price changed by ${price_diff:.2f}'
    body += f'\nThe percentage difference is {percentage_diff:.2f}%'
    body += f'\nThis is an automated email alert.'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['from']= sender
    msg['to'] = receipient
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receipient, msg.as_string())
        server.quit()
        
    print('Email alert sent successfully!')
