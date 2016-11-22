"""This holds the Account class."""

from .Endpoint import Endpoint


class Account(Endpoint):

    """Class for interacting with account information."""

    def __init__(self, url, token):
        """Take token and sets its URI for account interaction."""
        super(Account, self).__init__(token)
        self.uri = "%s/account" % url

    def info(self):
        """
        Gets account info
        """

        return self.make_request(self.uri)
