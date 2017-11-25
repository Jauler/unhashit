
import hashlib

class MD5Digester:
    def GetDigest(self, value):
        return hashlib.md5(value).hexdigest()


