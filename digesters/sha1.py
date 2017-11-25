
import hashlib

class SHA1Digester:
    def GetDigest(self, value):
        return hashlib.sha1(value).hexdigest()


