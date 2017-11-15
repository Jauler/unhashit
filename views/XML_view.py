

class XMLView:

    def GetViewForSuccess(self):
        return [200, ""]

    def GetViewForError(self, error):
        return [200, ""]

    def GetViewForValue(self, value):
        return [200, ""]

    def GetViewForDigest(self, digest):
        return [200, ""]
