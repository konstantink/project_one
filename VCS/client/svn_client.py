import sys
import os
import pysvn
from VCS import VCS


class Client(object):
    def __init__(self):
        self.client = pysvn.Client()

    def get_login(realm, username, may_save):
        name = raw_input("Enter your svn login : ")
        password = getpass.getpass("Enter your svn password :")
        return True, name, password, True

    self.client.callback_get_login = get_login

    log_message = "reason for change"

    def get_log_message(Client):
        return True, log_message

    self.client.callback_get_log_message = get_log_message

    def export(Client):
        self.client.export('file://'+ svnpath)



