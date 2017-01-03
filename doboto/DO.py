"""This holds the DO class."""

from .Account import Account
from .Action import Action
from .Domain import Domain
from .Droplet import Droplet
from .Image import Image
from .Region import Region
from .Size import Size
from .SSHKey import SSHKey
from .Tag import Tag
from .Volume import Volume


class DO(object):
    """Overall class for interacting with the DO API."""

    def __init__(self, url, token):
        """Take URL and token, and create a sub instance for each endpoint."""
        self.account = Account(url, token)
        self.action = Action(url, token)
        self.domain = Domain(url, token)
        self.droplet = Droplet(url, token)
        self.image = Image(url, token)
        self.region = Region(url, token)
        self.size = Size(url, token)
        self.ssh_key = SSHKey(url, token)
        self.tag = Tag(url, token)
        self.volume = Volume(url, token)
