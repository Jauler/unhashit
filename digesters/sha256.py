
import hashlib

class SHA256Digester:
    def GetDigest(value):
        return hashlib.sha256(value).hexdigest()


