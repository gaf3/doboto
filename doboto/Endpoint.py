"""This holds the Endpoint class."""


class Endpoint(object):
    """Base class for interacting with an endpoint of the DO API."""

    def __init__(self, token):
        """Take token and sets its token for API authorization."""
        self.token = token
