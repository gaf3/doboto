"""This holds the Snapshot class."""

from .Endpoint import Endpoint


class Snapshot(Endpoint):

    """Class for interacting with snapshots."""

    def __init__(self, url, token):
        """Take token and sets its URI for snapshot interaction."""
        super(Snapshot, self).__init__(token)
        self.uri = "%s/snapshots" % url

    def list(self, resource_type=None):
        """list snapshots"""

        params = {}

        if resource_type is not None:
            params["resource_type"] = resource_type

        return self.pages(self.uri, "snapshots", params=params)

    def info(self, id):
        """Retrieve snapshot information"""
        uri = self.uri + "/%s" % id

        return self.request(uri, "snapshot")

    def destroy(self, id):
        """Destroy snapshot"""
        uri = self.uri + "/%s" % id

        return self.request(uri, request_method="DELETE")
