import smtplib
from email.mime.text import MIMEText

def send_alert_email(frame_path):
    sender_email = "your_email@gmail.com"
    receiver_email = "target_email@gmail.com"
    password = "your_password"

    msg = MIMEText(f"Violation detected! See captured frame: {frame_path}")
    msg['Subject'] = 'Deepfake Violation Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)
