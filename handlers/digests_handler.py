
import sys
import webapp2


class DigestsHandler(webapp2.RequestHandler):

    def get(self, **kwargs):
        viewer = kwargs["view"]
        try:
            algorithm = kwargs["algorithm"];
            value = self.request.get("value")
            digester = self.app.config[algorithm + "_digester"]
            digest = digester.GetDigest(value)

            storage = self.app.config[algorithm + "_storage"]
            storage.AddNewDigestValue(digest, value)

            code, view = viewer.GetViewForDigest(algorithm, value, digest)

        except:
            error = sys.exc_info()
            code, view = viewer.GetViewForError(error)

        self.response.set_status(code)
        self.response.out.write(view);

