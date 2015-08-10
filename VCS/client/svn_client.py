import sys, os
from VCS import VCS


class Client(object):
    def __init__(self,url_or_path, *args, **kwargs):
        self.__url_or_path = url_or_path
        self.__username = kwargs.pop('username', None)
        self.__password = kwargs.pop('password', None)

    def run_command():
        """
        Запускает команды
        """
        pass

    def export(self, to_path, revision=None):
        cmd = []

        if revision is not None:
            cmd += ['-r', str(revision)]

        cmd += [self.__url_or_path, to_path]

        self.run_command('export', cmd)


