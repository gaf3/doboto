"""This holds the SSH Key class."""

from .Endpoint import Endpoint


class SSHKey(Endpoint):

    """Class for interacting with SSH keys."""

    def __init__(self, url, token):
        """Take token and sets its URI for SSH key interaction."""
        super(SSHKey, self).__init__(token)
        self.uri = "%s/account/keys" % url

    def create(self, name, public_key):
        """Create SSH Key"""
        attribs = {'name': name,
                   'public_key': public_key}

        return self.make_request(self.uri, 'POST', attribs)

    def list(self):
        """list SSH Keys"""

        return self.make_request(self.uri)

    def retrieve(self, ssh_id):
        """Retrieve SSH Key"""

    def update(self, ssh_id):
        """Update SSH Key"""

    def destroy(self, ssh_id):
        """Destroy SSH Key"""
