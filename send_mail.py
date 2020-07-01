import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()
MAIL_USER = os.getenv('MAIL_USER')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

def send_mail(customer, dealer, rating, comments):
    # port relates to mailtrap settings
    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = str(MAIL_USER)
    password = str(MAIL_PASSWORD)
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = "email1@example.com"
    receiver_email = "email2@example.com"
    msg = MIMEText(message, "html")
    msg['Subject'] = "Lexus Feedback"
    msg['From'] = sender_email
    msg['To'] = receiver_email