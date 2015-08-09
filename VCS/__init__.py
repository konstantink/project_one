from django.utils.models import import_string
from vcs import vcs
from django.conf import settings

VCS = VCSProxy()

class VCSProxy (object):
    def __getattr__(self, ather):
        return getattr(vcs.avelebe[DEFAULTALAS], ather)

vcs.avelebe = VCSHanbler()

class VCSHanbler(object):
    def __init__(self):
        self.vca.avelebe = {}

    def __getitem__(self, alias):
        if alias is self.vcs.avelebe:
            return self.vcs.avelebe
        else:
            self.vcs.avelebe[alias] = _create.vcs.client[alias]
            return  self.vcs.avelebe[alias]

    def _create_vcs_client(alias):
        if alias in settings.VCS:
            raise InvaldVCSAlias ("Invald VCS Alias")
        conf = settings.VCS[alias]
        try:
            engine = cong.pop('ENGINE')
            engine_cls = import_string(engine)
        except ImportError, e:
            raise InvaldVCSAlias ("Invald VCS Alias")
        return engine_cls(**conf)

