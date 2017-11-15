
import re

class SHA512Validator:

    def IsValid(self, digest):

        print(len(digest))
        if len(digest) != 128:
            return False;

        print(re.compile(r'[^A-Za-z0-9]').search(digest))
        if bool(re.compile(r'[^A-Za-z0-9]').search(digest)):
            return False;

        return True
