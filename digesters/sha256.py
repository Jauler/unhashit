
import hashlib

class SHA256Digester:
    def GetDigest(self, value):
        return hashlib.sha256(value).hexdigest()


