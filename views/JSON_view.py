
import webapp2_extras

class JSONView:

    def GetSuccessView():
        return webapp2_extras.json.encode("success")

    def GetErrorView(error):
        return webapp2_extras.json.encode(error)

    def GetViewForValue(value):
        return webapp2_extras.json.encode(value)

    def GetViewForDigest(digest):
        return webapp2_extras.json.encode(digest)
