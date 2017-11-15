
import hashlib

class SHA512Digester:
    def GetDigest(self, value):
        return hashlib.sha512(value).hexdigest()



