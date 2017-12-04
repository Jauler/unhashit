import smtplib
import os

class SMTPMailSender:

    def __init__(self):
        self.server = os.environ.get('SMTP_SERVER_ADDRESS');
        self.username = os.environ.get('SMTP_SERVER_USERNAME');
        self.password = os.environ.get('SMTP_SERVER_PASSWORD');

    def SendMail(self, recipient, subject, message):
        server = smtplib.SMTP(self.server);
        server.set_debuglevel(1)
        print(self.username)
        print(self.password)
        server.login(self.username, self.password);
        server.sendmail('no-reply@unhashit.com', [recipient], "Subject: " + subject + "\n\n" + message);

