import smtplib, ssl
from credentials import my_secrets

from email.message import EmailMessage


class SendEmail:

    def __init__(self) -> None:

        self.my_email = my_secrets.get("username")
        self.my_password = my_secrets.get("password")
        self.local_addr = my_secrets.get("local")

    def create_email_content(self):
        text_file = "isItThere.txt"
        with open(text_file) as fp:
            msg = EmailMessage()
            msg.set_content(fp.read())

        msg["Jobs currently posted for Japan"] = f"The contents of {text_file}"
        msg["From"] = self.my_email
        msg["To"] = self.my_email

        self.send_mail(msg)

    def send_mail(self, msg):
        port = 465
        context = ssl._create_unverified_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(self.my_email, self.my_password)
            server.sendmail(self.my_email, self.my_email, msg)
