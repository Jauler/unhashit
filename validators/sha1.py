
import re

class SHA1Validator:

    def GetRequiredLength():
        return 40

    def IsValid(self, digest):
        if len(digest) != 40:
            return False;

        if bool(re.compile(r'[^A-Fa-f0-9]').search(digest)):
            return False;

        return True
