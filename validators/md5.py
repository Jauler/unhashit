
import re

class MD5Validator:

    def GetRequiredLength():
        return 32

    def IsValid(self, digest):
        if len(digest) != 32:
            return False;

        if bool(re.compile(r'[^A-Fa-f0-9]').search(digest)):
            return False;

        return True
