""" This hold the DO class """

from .Droplet import Droplet
from .SSHKey import SSHKey

class DO(object):
    """ Overall class for interacting with the DO API. """

    def __init__(self, url, token):
        """ Takes in a URL and token and creates sub instances for each end point """

        self.droplet = Droplet(url, token)
        self.ssh_key = SSHKey(url, token)