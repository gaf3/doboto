"""This holds the Droplet class."""

from .Endpoint import Endpoint


class Droplet(Endpoint):

    """Class for interacting with droplets."""

    def __init__(self, url, token):
        """Take token and sets its URI for droplet interaction."""
        super(Droplet, self).__init__(token)
        self.uri = "%s/droplets" % url

    def info(self, droplet_id):
        """Retrieve droplet information"""
        uri = self.uri + "/%s" % droplet_id

        return self.make_request(uri)

    def list(self):
        """list all droplets"""
        return self.make_request(self.uri)

    def list_kernels(self, droplet_id):
        """Retrieve droplet kernels information"""
        uri = self.uri + "/%s/kernels" % droplet_id

        return self.make_request(uri)

    def list_snapshots(self, droplet_id):
        """Retrieve droplet snapshots information"""
        uri = self.uri + "/%s/snapshots" % droplet_id

        return self.make_request(uri)

    def list_backups(self, droplet_id):
        """Retrieve droplet backups information"""
        uri = self.uri + "/%s/backups" % droplet_id

        return self.make_request(uri)

    def list_actions(self, droplet_id):
        """Retrieve droplet actions information"""
        uri = self.uri + "/%s/actions" % droplet_id

        return self.make_request(uri)

    def destroy(self, droplet_id):
        """Destroy droplet"""
        raise NotImplementedError("we should implement this!")

    def create(self, params={}):
        """Create a droplet based off of parameters"""
        