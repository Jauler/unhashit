
import hashlib

class SHA512Digester:
    def GetDigest(value):
        return hashlib.sha512(value).hexdigest()



