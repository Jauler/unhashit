
import re

class SHA256Validator:

    def IsValid(digest):
        if len(digest) != 32:
            return False;

        if bool(re.compile(r'[^A-Za-z0-9]').search(digest)):
            return False;

        return True
