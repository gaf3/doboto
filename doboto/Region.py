"""This holds the Region class."""

from .Endpoint import Endpoint


class Region(Endpoint):

    """Class for interacting with regions."""

    def __init__(self, url, token):
        """Take token and sets its URI for region interaction."""
        super(Region, self).__init__(token)
        self.uri = "%s/regions" % url

    def list(self, type=None, private=None):
        """list all Regions"""

        return self.make_request(self.uri)
