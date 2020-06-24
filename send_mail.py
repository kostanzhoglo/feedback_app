import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    # port relates to mailtrap settings
    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = ''
    password = ''
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = "email1@example.com"
    receiver_email = "email2@example.com"
    msg = MIMEText(message, "html")
    msg['Subject'] = "Lexus Feedback"
    msg['From'] = sender_email
    msg['To'] = receiver_email