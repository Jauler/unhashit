
import re

class SHA256Validator:

    def GetRequiredLength():
        return 64

    def IsValid(self, digest):
        if len(digest) != 64:
            return False;

        if bool(re.compile(r'[^A-Za-z0-9]').search(digest)):
            return False;

        return True
