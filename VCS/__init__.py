from django.utils.module_loading import import_by_path
from django.conf import settings
from VCS.errors.errors import InvaldVCSAlias, InvaldVCSAliasError

DEFAULT_ALIAS = 'default'

def _create_vcs_client(alias):
    if alias in settings.VCS:
        raise InvaldVCSAlias(
            "Could not find config for '%s' in settings.VCS" % alias
        )
    conf = settings.VCS[alias]
    try:
        engine = conf.pop('ENGINE')
        engine_cls = import_by_path(engine)
    except ImportError, e:
        raise InvaldVCSAliasError(
            "Could not find alias '%s': %s" % (alias, e)
        )
    return engine_cls(**conf)


class VCSHandler(object):
    def __init__(self):
        self.vcs_available = {}

    def __getitem__(self, alias):
        if alias is self.vcs_available:
            return self.vcs_available
        else:
            self.vcs_available[alias] = _create_vcs_client(alias)
            return self.vcs_available[alias]


vcs_available = VCSHandler()


class VCSProxy(object):
    def __getattr__(self, other):
        return getattr(vcs_available[DEFAULT_ALIAS], other)

    def __setattr__(self, other, value):
        return setattr(vcs_available[DEFAULT_ALIAS], other, value)

    def __delattr__(self, other):
        return delattr(vcs_available[DEFAULT_ALIAS], other)

    def __contains__(self, key):
        return key in vcs_available[DEFAULT_ALIAS]

    def __eq__(self, other):
        return vcs_available[DEFAULT_ALIAS] == other

    def __ne__(self, other):
        return vcs_available[DEFAULT_ALIAS] != other


vcs = VCSProxy()
