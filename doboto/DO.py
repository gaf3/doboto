"""This holds the DO class."""

from .Droplet import Droplet
from .SSHKey import SSHKey
from .Image import Image
from .Region import Region


class DO(object):
    """Overall class for interacting with the DO API."""

    def __init__(self, url, token):
        """Take URL and token, and create a sub instance for each endpoint."""
        self.droplet = Droplet(url, token)
        self.ssh_key = SSHKey(url, token)
        self.image = Image(url, token)
        self.region = Region(url, token)
