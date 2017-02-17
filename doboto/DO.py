"""This holds the DO class."""

from .Account import Account
from .Action import Action
from .Volume import Volume
from .Certificate import Certificate
from .Domain import Domain
from .Droplet import Droplet
from .Image import Image
from .Snapshot import Snapshot
from .Region import Region
from .Size import Size
from .FloatingIP import FloatingIP
from .SSHKey import SSHKey
from .Tag import Tag


class DO(object):
    """
    description:
        Main class to instantiate.

    in:
        token - string - Your DO API token. Create through your account UI on the main site
        url - string - URL to use instead of the main.  Used for experimentation
        agent - string - Agent to use instead of DOBOTO.  Used by the DOBOTO Ansible modules

    related: https://developers.digitalocean.com/documentation/v2/#introduction
    """

    def __init__(self, token, url="https://api.digitalocean.com/v2/", agent="DOBOTO"):
        """Take URL and token, and create a sub instance for each endpoint."""
        self.account = Account(self, token, url, agent)
        self.action = Action(self, token, url, agent)
        self.volume = Volume(self, token, url, agent)
        self.certificate = Certificate(self, token, url, agent)
        self.domain = Domain(self, token, url, agent)
        self.droplet = Droplet(self, token, url, agent)
        self.image = Image(self, token, url, agent)
        self.snapshot = Snapshot(self, token, url, agent)
        self.region = Region(self, token, url, agent)
        self.size = Size(self, token, url, agent)
        self.floating_ip = FloatingIP(self, token, url, agent)
        self.ssh_key = SSHKey(self, token, url, agent)
        self.tag = Tag(self, token, url, agent)
