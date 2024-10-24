import smtplib
from common.logger import logger
from common.secret_handler import secret_handler
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EMailNotifier:
    def __init__(self, email_sender: str, email_password: str, email_receiver: str):
        self.sender = email_sender
        self.password = email_password
        self.receiver = email_receiver
        self.mail = MIMEMultipart()
        self.mail['From'] = self.sender
        self.mail['To'] = self.receiver

    def send_email(self, subject: str, message: str):
        self.mail['Subject'] = subject
        self.mail.attach(MIMEText(message, 'plain'))
        try:
            server = smtplib.SMTP_SSL("smtp.163.com", 465)
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, self.mail.as_string())
            logger.debug("Succeed to send email")
        except Exception as ex:
            logger.error(f"Fail to send email due to {ex}")
        finally:
            server.quit()


if __name__ == "__main__":
    email_notifier = EMailNotifier()
    email_notifier.send_email("Test", "Test")
    email_notifier.send_email("New Test", "New Test")

