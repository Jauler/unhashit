import os
from google.appengine.api import app_identity
from google.appengine.api import mail

class GAEMailSender:
    def SendMail(self, recipient, subject, content):
        sender = 'jauleris@gmail.com'.format(app_identity.get_application_id())
        message = mail.EmailMessage(sender=sender, subject=subject)
        message.to = recipient
        message.body = content
        message.send()
