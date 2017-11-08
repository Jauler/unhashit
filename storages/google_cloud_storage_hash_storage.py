

class GoogleCloudStorageHashStorage:

    def __init__(self, bucket, validator):
        self.bucket = bucket;
        self.validator = validator

    def GetValueForDigest(self, digest):
        if not self.validator.IsValid(digest):
            raise RuntimeError("Invalid digest");

        #TODO: query storage
        return None


    def AddNewDigestValue(self, digest, value):
        if not self.validator.IsValid(digest):
            raise RuntimeError("Invalid digest");

        #store digest, value pair
        return None

