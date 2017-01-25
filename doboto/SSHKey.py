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

        return self.make_request(self.uri, 'POST', attribs=attribs)

    def list(self):
        """list SSH Keys"""

        return self.make_request(self.uri)

    def info(self, id_fingerprint):
        """Retrieve SSH Key"""

        uri = "%s/%s" % (self.uri, id_fingerprint)
        return self.make_request(uri)

    def update(self, id_fingerprint, name):
        """Update SSH Key"""

        uri = "%s/%s" % (self.uri, id_fingerprint)
        attribs = {'name': name}

        return self.make_request(uri, 'PUT', attribs=attribs)

    def destroy(self, id_fingerprint):
        """Destroy SSH Key"""

        uri = "%s/%s" % (self.uri, id_fingerprint)

        return self.make_request(uri, 'DELETE')
