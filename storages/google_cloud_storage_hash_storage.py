
from google.cloud import storage
from threading import Lock;
import digests_pb2

class GoogleCloudStorageHashStorage:

    def __init__(self, bucket_name, validator):
        self.bucket_name = bucket_name;
        self.validator = validator
        self.storage_client = storage.Client()
        self.storage_lock = Lock();

    def GetValueForDigest(self, digest):
        if not self.validator.IsValid(digest):
            raise RuntimeError("Invalid digest")

        try:
            digest = digest.lower()
            self.storage_lock.acquire()
            prefix = digest[0:4]
            bucket = self.storage_client.get_bucket(self.bucket_name)
            blob = bucket.get_blob(prefix)
            if blob is None:
                return None

            stored_digests = digests_pb2.Digests()
            stored_digests.ParseFromString(blob.download_as_string())

            # search for value
            for stored_digest in stored_digests.digests:
                if stored_digest.digest.lower() == digest:
                    return stored_digest.value;

            return None

        finally:
            self.storage_lock.release()


    def AddNewDigestValue(self, digest, value):
        if not self.validator.IsValid(digest):
            raise RuntimeError("Invalid digest");

        try:
            digest = digest.lower()
            self.storage_lock.acquire()
            prefix = digest[0:4]
            bucket = self.storage_client.get_bucket(self.bucket_name)
            blob = bucket.get_blob(prefix)
            if blob is None:
                blob = bucket.blob(prefix)
                content = ""
            else:
                content = blob.download_as_string()

            stored_digests = digests_pb2.Digests()
            stored_digests.ParseFromString(content)

            # check for dublicate value
            for stored_digest in stored_digests.digests:
                if stored_digest.digest.lower() == digest:
                    return;

            stored_digest = stored_digests.digests.add()
            stored_digest.digest = digest
            stored_digest.value = value;

            blob.upload_from_string(stored_digests.SerializeToString());

        finally:
            self.storage_lock.release()

