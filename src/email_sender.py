import smtplib
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

        self.send_email(msg)

    def send_email(self, msg):
        s = smtplib.SMTP(self.local_addr, 587)
        s.connect(self.local_addr, 587)
        s.login(self.my_email, self.my_password)
        s.send_message(msg)
        s.quit()
