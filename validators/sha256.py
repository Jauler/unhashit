
import re

class SHA256Validator:

    def GetRequiredLength():
        return 64

    def IsValid(self, digest):
        if len(digest) != 64:
            return False;

        if bool(re.compile(r'[^A-Fa-f0-9]').search(digest)):
            return False;

        return True
