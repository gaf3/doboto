""" This holds the Droplet class """

from .Endpoint import Endpoint

class Droplet(Endpoint):
    """ Class for interacting with droplets """

    def __init__(self, url, token):
        """ Takes token and sets its URI for droplet interaction """

        super(Droplet, self).__init__(token)
        self.uri = "%s/droplets" % url
