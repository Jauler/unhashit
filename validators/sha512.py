
import re

class SHA512Validator:

    def GetRequiredLength():
        return 128

    def IsValid(self, digest):

        if len(digest) != 128:
            return False;

        if bool(re.compile(r'[^A-Za-z0-9]').search(digest)):
            return False;

        return True
