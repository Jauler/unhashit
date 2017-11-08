# Copyright 2011 webapp2 AUTHORS.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import webapp2_extras

from handlers/digests_handler import DigestsHandler
from handlers/values_handler import ValuesHandler
from digesters/sha256 import SHA256Digester
from digesters/sha512 import SHA512Digester
from validators/sha256 import SHA256Validator
from validators/sha512 import SHA512Validator
from storages/google_cloud_storage_hash_storage import GoogleCloudStorageHashStorage
from views/JSONView import JSONView
from views/XMLView import XMLView

config = {
    "SHA256_digester" : SHA256Digester(),
    "SHA256_storage" : GoogleCloudStorageHashStorage("SHA256_digests"),
    "SHA256_validator" : SHA256Validator(),

    "SHA512_digester" : SHA512Digester(),
    "SHA512_storage" : GoogleCloudStorageHashStorage("SHA512_digests"),
    "SHA512_validator" : SHA512Validator(),
};

app = webapp2.WSGIApplication(
    [
        webapp2.Route('/HashReversing/JSON/<algorithm>/digest', DigestsHandler, defaults = {"view" : JSONView()}, name='digest'),
        webapp2.Route('/HashReversing/JSON/<algorithm>/value', ValuesHandler, defaults = {"view" : JSONView()}, name='value'),
        webapp2.Route('/HashReversing/XML/<algorithm>/digest', DigestsHandler, defaults = {"view" : XMLView()}, name='digest'),
        webapp2.Route('/HashReversing/XML/<algorithm>/value', ValuesHandler, defaults = {"view" : XMLView()}, name='value'),
    ], config=config)
