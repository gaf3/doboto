"""This holds the DO class."""

from .Account import Account
from .Action import Action
from .Volume import Volume
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
        self.account = Account(token, url, agent)
        self.action = Action(token, url, agent)
        self.volume = Volume(token, url, agent)
        self.domain = Domain(token, url, agent)
        self.droplet = Droplet(token, url, agent)
        self.image = Image(token, url, agent)
        self.snapshot = Snapshot(token, url, agent)
        self.region = Region(token, url, agent)
        self.size = Size(token, url, agent)
        self.floating_ip = FloatingIP(token, url, agent)
        self.ssh_key = SSHKey(token, url, agent)
        self.tag = Tag(token, url, agent)
