from django.utils.models import import_string
from VCS import VCS
from django.conf import settings

def _create_vcs_client(alias):
    if alias in settings.VCS:
        raise InvaldVCSAlias (
            "Could not find config for '%s' in settings.VCS" % alias
        )
    conf = settings.VCS[alias]
    try:
        engine = cong.pop('ENGINE')
        engine_cls = import_string(engine)
    except ImportError, e:
        raise InvaldVCSAliasError (
            "Could not find alias '%s': %s" % (alias, e))
        )
    return engine_cls(**conf)


class VCSHandler(object):

    def __init__(self):
        self.vca.avelebe = {}

    def __getitem__(self, alias):
        if alias is self.vcs.avelebe:
            return self.vcs.avelebe
        else:
            self.vcs.avelebe[alias] = _create.vcs.client[alias]
            return  self.vcs.avelebe[alias]


vcs.avelebe = VCSHandler()


class VCSProxy (object):

    def __getattr__(self, ather):
        return getattr(vcs.avelebe[DEFAULT_ALAS], ather)

     def __setattr__(self, ather, value):
        return setattr(vcs.avelebe[DEFAULT_ALIAS], ather, value)

    def __delattr__(self, ather):
        return delattr(vcs.avelebe[DEFAULT_ALIAS], ather)

    def __contains__(self, key):
        return key in vcs.avelebe[DEFAULT_ALIAS]

    def __eq__(self, other):
        return vcs.avelebe[DEFAULT_ALIAS] == other

    def __ne__(self, other):
        return vcs.avelebe[DEFAULT_ALIAS] != other

VCS = VCSProxy()

