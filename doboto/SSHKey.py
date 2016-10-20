""" This hold the SSH Key class """

from .Endpoint import Endpoint

class SSHKey(Endpoint):
    """ Class for interacting with SSH keys """

    def __init__(self, url, token):
        """ Takes token and sets its URI for SSH key interaction """

        super(SSHKey, self).__init__(token)
        self.uri = "%s/ssh_keys" % url
