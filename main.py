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
import os

from handlers.digests_handler import DigestsHandler
from handlers.values_handler import ValuesHandler
from handlers.notification_handler import NotificationHandler
from digesters.sha256 import SHA256Digester
from digesters.sha512 import SHA512Digester
from digesters.sha1 import SHA1Digester
from digesters.md5 import MD5Digester
from validators.sha256 import SHA256Validator
from validators.sha512 import SHA512Validator
from validators.sha1 import SHA1Validator
from validators.md5 import MD5Validator
from storages.google_cloud_storage_hash_storage import GoogleCloudStorageHashStorage
from storages.mysql_db import MySQLDB
from views.JSON_view import JSONView
from views.XML_view import XMLView



if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    from mail.GAE_mail_sender import GAEMailSender
    MailSender = GAEMailSender
else:
    from mail.smtp_mail_sender import SMTPMailSender
    MailSender = SMTPMailSender

config = {
    "SHA256_digester" : SHA256Digester(),
    "SHA256_storage" : GoogleCloudStorageHashStorage("sha256_digests", SHA256Validator()),
    "SHA256_validator" : SHA256Validator(),

    "SHA512_digester" : SHA512Digester(),
    "SHA512_storage" : GoogleCloudStorageHashStorage("sha512_digests", SHA512Validator()),
    "SHA512_validator" : SHA512Validator(),

    "MD5_digester" : MD5Digester(),
    "MD5_storage" : GoogleCloudStorageHashStorage("md5_digests", MD5Validator()),
    "MD5_validator" : MD5Validator(),

    "SHA1_digester" : SHA1Digester(),
    "SHA1_storage" : GoogleCloudStorageHashStorage("sha1_digests", SHA1Validator()),
    "SHA1_validator" : SHA1Validator(),

    "registrations_db" : MySQLDB(),
    "mail_sender" : MailSender(),
    "found hash_message_subject" : "Your hash value has been found.",
    "found_hash_message_template" : "We are writing to inform you that value for @@ALGORITHM_PLACEHOLDER@@ hash @@DIGEST_PLACEHOLDER@@ hash been found. The value is \"@@VALUE_PLACEHOLDER@@\" (without quites)"
};

app = webapp2.WSGIApplication(
    [
        webapp2.Route('/HashReversing/JSON/<algorithm>/digest', DigestsHandler, defaults = {"view" : JSONView()}, name='digest'),
        webapp2.Route('/HashReversing/JSON/<algorithm>/value', ValuesHandler, defaults = {"view" : JSONView()}, name='value'),
        webapp2.Route('/HashReversing/JSON/<algorithm>/notification', NotificationHandler, defaults = {"view" : JSONView()}, name='digest'),
        webapp2.Route('/HashReversing/XML/<algorithm>/digest', DigestsHandler, defaults = {"view" : XMLView()}, name='digest'),
        webapp2.Route('/HashReversing/XML/<algorithm>/value', ValuesHandler, defaults = {"view" : XMLView()}, name='value'),
    ], config=config)
