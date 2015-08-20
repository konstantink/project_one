import sys
import os
from django.utils.models import import_string
from django.conf import settings
import pysvn


class Client(object):

    def __init__(self, user, password, urls):
        self.user = user
        self.password = password
        self.urls = urls
        self.client = pysvn.Client()

    def get_settings_conf(self, user, password, urls):
        value_user = settings.VCS[user]
        value_password = settings.VCS[password]
        value_urls = settings.VCS[urls]
        if self.user is None:
            full_user = value_user.pop('USER')
            self.user = import_string(full_user)
        if self.password is None:
            full_password = value_password.pop('PASSWORD')
            self.password = import_string(full_password)
        if self.urls is None:
            full_urls = value_urls.pop('LOCATION')
            self.urls = import_string(full_urls)
        return self.user, self.password, self.urls

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
        self.client.export('file://' + self.urls)

    def get_tag(self):
        client.copy('http://svnurl.com/svn/trunk', 'http://svnurl.com/svn/tag/%s' % tag_name)
