
import webapp2


class DigestsHandler(webapp2.RequestHandler):

    def get(self, **kwargs):
        viewer = kwargs["view"]
        try:
            algorithm = kwargs["algorithm"];
            value = kwargs["value"]
            digester = self.app.config[algorithm + "_digester"]
            digest = digester.GetDigest(value)

            storage = self.app.config[algorithm]["storage"]
            storage.AddNewDigestValue(digest, value)

            view = viewer.GetViewForDigest(digest)

        except:
            error = sys.exc_info[0]
            view = viewer.GetViewForError(error)

        self.response.out.write(view);

