
import re

class SHA512Validator:

    def IsValid(digest):
        if len(digest) != 64:
            return False;

        if bool(re.compile(r'[^A-Za-z0-9]').search(digest)):
            return False;

        return True
