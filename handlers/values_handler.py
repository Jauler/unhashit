
import sys
import webapp2


class ValuesHandler(webapp2.RequestHandler):
    def get(self, **kwargs):
        viewer = kwargs["view"]
        try:
            algorithm = kwargs["algorithm"];
            digest = self.request.get("digest")

            storage = self.app.config[algorithm + "_storage"]
            value = storage.GetValueForDigest(digest)

            code, view = viewer.GetViewForValue(algorithm, digest, value)

        except:
            error = sys.exc_info()
            code, view = viewer.GetViewForError(error)

        self.response.set_status(code)
        self.response.out.write(view);


    def put(self, **kwargs):
        try:
            algorithm = kwargs["algorithm"]
            storage = self.app.config[algorithm + "_storage"]
            digest = self.request.get("digest")
            value = self.request.get("value")

            storage = self.app.config[algorithm + "_storage"]
            storage.AddNewDigestValue(digest, value)

            code, view = viewer.GetViewForSuccess()

        except:
            error = sys.exc_info()
            code, view = viewer.GetViewForError(error)

        self.response.set_status(code)
        self.response.out.write(view);



