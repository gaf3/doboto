"""This holds the Size class."""

from .Endpoint import Endpoint


class Size(Endpoint):

    """Class for interacting with sizes."""

    def __init__(self, url, token):
        """Take token and sets its URI for size interaction."""
        super(Size, self).__init__(token)
        self.uri = "%s/sizes" % url

    def list(self):
        """list all sizes"""

        return self.make_request(self.uri)
