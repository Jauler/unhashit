
import sys
import webapp2
import re
from storages.registration import Registration


class NotificationHandler(webapp2.RequestHandler):

    def post(self, **kwargs):
        viewer = kwargs["view"]
        try:
            db = self.app.config["registrations_db"];

            email = self.request.POST.get("email")
            print(email)
            algorithm = self.request.POST.get("algorithm")
            print(algorithm)
            digest = self.request.POST.get("digest")
            print(digest)

            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise RuntimeError("Invalid email")

            validator = self.app.config[algorithm + "_validator"]
            if not validator.IsValid(digest):
                raise RuntimeError("Invalid digest")

            #check for uniqueness
            exists = False;
            regs = Registration.Read(db, algorithm, digest)
            for reg in regs:
                if reg.GetEmail().lower() == email.lower():
                    exists = True;
                    break;

            if not exists:
                reg = Registration(email, algorithm, digest);
                reg.Write(db);

            code, view = viewer.GetViewForSuccess()

        except:
            error = sys.exc_info()
            code, view = viewer.GetViewForError(error)

        self.response.set_status(code)
        self.response.out.write(view);

