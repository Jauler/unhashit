
import sys
import webapp2
from storages.registration import Registration


class DigestsHandler(webapp2.RequestHandler):

    def get(self, **kwargs):
        viewer = kwargs["view"]
        try:
            algorithm = kwargs["algorithm"];
            value = self.request.get("value")
            digester = self.app.config[algorithm + "_digester"]
            digest = digester.GetDigest(value)
            db = self.app.config["registrations_db"];
            mailsender = self.app.config["mail_sender"]

            storage = self.app.config[algorithm + "_storage"]
            storage.AddNewDigestValue(digest, value)

            regs = Registration.Read(db, algorithm, digest)
            for reg in regs:
                subject = self.app.config["found hash_message_subject"];
                message = self.app.config["found_hash_message_template"];
                message = message.replace("@@ALGORITHM_PLACEHOLDER@@", algorithm)
                message = message.replace("@@DIGEST_PLACEHOLDER@@", digest)
                message = message.replace("@@VALUE_PLACEHOLDER@@", value)
                mailsender.SendMail(reg.GetEmail(), subject, message)
                reg.Delete(db)

            code, view = viewer.GetViewForDigest(algorithm, value, digest)

        except:
            error = sys.exc_info()
            code, view = viewer.GetViewForError(error)

        self.response.set_status(code)
        self.response.out.write(view);

