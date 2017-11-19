
from webapp2_extras import json

class JSONView:

    def __init__(self):
        self.default_error_code = 500
        self.error_codes = {
                KeyError: 400
                }

    def GetViewForSuccess(self):
        return [200, json.encode("success")]

    def GetViewForError(self, error):
        str_err_type = str(error[0])
        serializable_error = {
                "error" : str(error[1]),
                }

        if error[0] in self.error_codes:
            code = self.error_codes[error[0]]
        else:
            code = self.default_error_code

        return [code, json.encode(serializable_error)]

    def GetViewForValue(self, algo, digest, value):
        serializable_value = {
                "algorithm" : algo,
                "value" : value,
                "digest" : digest
                }
        return [200, json.encode(serializable_value)]

    def GetViewForDigest(self, algo, value, digest):
        serializable_digest = {
                "algorithm" : algo,
                "value" : value,
                "digest" : digest
                }
        return [200, json.encode(serializable_digest)]
