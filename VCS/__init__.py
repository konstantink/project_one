from django.utils.models import import_string
from django.conf import settings
from VCS import VCS
from vcs.errors.errors import *


def _create_vcs_client(alias):
    if alias in settings.VCS:
        raise InvaldVCSAlias(
            "Could not find config for '%s' in settings.VCS" % alias
        )
    conf = settings.VCS[alias]
    try:
        engine = conf.pop('ENGINE')
        engine_cls = import_string(engine)
    except ImportError, e:
        raise InvaldVCSAliasError(
            "Could not find alias '%s': %s" % (alias, e)
        )
    return engine_cls(**conf)


class VCSHandler(object):
    def __init__(self):
        self.vca.available = {}

    def __getitem__(self, alias):
        if alias is self.vcs.available:
            return self.vcs.available
        else:
            self.vcs.available[alias] = _create_vcs_client[alias]
            return self.vcs.available[alias]


vcs.available = VCSHandler()


class VCSProxy(object):
    def __getattr__(self, other):
        return getattr(vcs.available[DEFAULT_ALAS], other)

    def __setattr__(self, other, value):
        return setattr(vcs.available[DEFAULT_ALIAS], other, value)

    def __delattr__(self, other):
        return delattr(vcs.avelebe[DEFAULT_ALIAS], other)

    def __contains__(self, key):
        return key in vcs.available[DEFAULT_ALIAS]

    def __eq__(self, other):
        return vcs.available[DEFAULT_ALIAS] == other

    def __ne__(self, other):
        return vcs.available[DEFAULT_ALIAS] != other


vcs = VCSProxy()
