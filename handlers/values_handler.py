
import sys
import webapp2


class ValuesHandler(webapp2.RequestHandler):
    def setViewer(viewer)
        self.viewer = viewer

    def get(self, **kwargs):
        viewer = kwargs["view"]
        try:
            algorithm = kwargs["algorithm"];
            validator = self.app.config["algorithm_" + algorithm]["validator"]
            digest = kwargs["digest"]

            storage = self.app.config["algorithm_" + algorithm]["storage"]
            value = storage.GetValueForDigest(digest)

            view = viewer.GetViewForValue(value)

        except:
            error = sys.exc_info[0]
            view = viewer.GetViewForError(error)

        self.response.out.write(view);

    def put(self, **kwargs):
        try:
            algorithm = kwargs["algorithm"]
            validator = self.app.config["algorithm_" + algorithm]["validator"]
            digest = kwargs["digest"]
            value = kwargs["value"]

            storage = self.app.config[algorithm]["storage"]
            storage.AddNewDigestValue(digest, value)

            view = viewer.GetSuccessView()

        except:
            error = sys.exc_info[0]
            view = viewer.GetViewForError(error)

        self.response.out.write(view);


