import sys
import os
from django.conf import settings
import pysvn


class Client(object):

    def __init__(self, user, password, urls):
        self.user = user
        self.password = password
        self.urls = urls
        self.client = pysvn.Client()
        self.client.callback_get_login = lambda *args: True, self.user, self.password, True
        self.client.callback_get_log_message = lambda *args: True, self.log_message

    # def get_login(self, *args):
    #     return True, self.user, self.password, True

    log_message = "reason for change"

    # def get_log_message(self):
    #     return True, self.log_message

    def export(self):
        self.client.export(self.urls)

    def get_tag(self, tag_name=None):
        self.client.copy(self.urls + 'trunk', self.urls + 'tag/%s' % tag_name)
