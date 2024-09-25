import smtplib

from email.message import EmailMessage


class SendEmail:

    def __init__(self) -> None:

        self.my_email = "hudgens1073@gmail.com"

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
        s = smtplib.SMTP("localhost")
        s.send_message(msg)
        s.quit()
