"""This holds the Action class."""

from .Endpoint import Endpoint


class Action(Endpoint):

    """Class for interacting with actions."""

    def __init__(self, url, token):
        """Take token and sets its URI for action interaction."""
        super(Action, self).__init__(token)
        self.uri = "%s/actions" % url

    def list(self):
        """list all actions"""

        return self.pages(self.uri, "actions")

    def info(self, id):
        """
        Retrieve action information
        """
        uri = "%s/%s" % (self.uri, id)
        return self.request(uri, "action")
