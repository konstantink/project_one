import sys
import os
from django.utils.models import import_string
from django.conf import settings
import pysvn


class Client(object):

    def __init__(self, user, password, urls, get_login = None, get_log_message = None):
        self.user = user
        self.password = password
        self.urls = urls
        self.client = pysvn.Client()
        self.get_login = get_login
        self.get_log_message = get_log_message

    def get_login(self, *args):
        return True, self.user, self.password, True

    def get_client(self):
        self.client.callback_get_login = self.get_login
        return self.client

    log_message = "reason for change"

    def get_log_message(self):
        return True, log_message

    def get_log_message_client(self):
        self.client.callback_get_log_message = self.get_log_message
        return self.client

    def export(self):
        self.client.export(self.urls)

    def get_tag(self):
        client.copy(self.urls + 'trunk', self.urls + 'tag/%s' % tag_name)
