"""This holds the SSH Key class."""

from .Endpoint import Endpoint


class SSHKey(Endpoint):
    """
    description:

        DigitalOcean allows you to add SSH public keys to the interface so that you can embed your
        public key into a Droplet at the time of creation. Only the public key is required to take
        advantage of this functionality.

    related: https://developers.digitalocean.com/documentation/v2/#ssh-keys
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for floating ip interaction.
        """
        super(SSHKey, self).__init__(token, agent)
        self.do = do
        self.uri = "%s/account/keys" % url

    def list(self):
        """
        description: List all Keys

        out:
            A list of SSH Key dict's:
                - id - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.
                - fingerprint - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.
                - public_key - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.
                - name - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-keys
        """  # nopep8

        return self.pages(self.uri, "ssh_keys")

    def create(self, name, public_key):
        """
        description: Create a new Key

        in:
            - name - string - The name to give the new SSH key in your account.
            - public_key - string - A string containing the entire public key.

        out:
            An SSH Key dict:
                - id - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.
                - fingerprint - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.
                - public_key - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.
                - name - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-key
        """  # nopep8
        attribs = {'name': name,
                   'public_key': public_key}

        return self.request(self.uri, "ssh_key", 'POST', attribs=attribs)

    def present(self, name, public_key):
        """
        description: Create a new Key if name not already present

        in:
            - name - string - The name to give the new SSH key in your account.
            - public_key - string - A string containing the entire public key.

        out:
            A tuple of of SSH Key dict, the intended and created (None if already exists):
                - id - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.
                - fingerprint - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.
                - public_key - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.
                - name - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-key
        """  # nopep8

        ssh_keys = self.list()

        existing = None
        for ssh_key in ssh_keys:
            if name == ssh_key["name"]:
                existing = ssh_key
                break

        if existing is not None:
            return (existing, None)

        created = self.create(name, public_key)
        return (created, created)

    def info(self, id_fingerprint):
        """
        description: Retrieve an existing Key

        in:
            - id_fingerprint - number / string - id or fingerprint of the key

        out:
            An SSH Key dict:
                - id - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.
                - fingerprint - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.
                - public_key - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.
                - name - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-key
        """  # nopep8

        uri = "%s/%s" % (self.uri, id_fingerprint)
        return self.request(uri, "ssh_key")

    def update(self, id_fingerprint, name):
        """
        description: Update a Key

        in:
            - id_fingerprint - number / string - id or fingerprint of the key
            - name - string - The name to give the new SSH key in your account.

        out:
            An SSH Key dict:
                - id - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.
                - fingerprint - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.
                - public_key - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.
                - name - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.

        related: https://developers.digitalocean.com/documentation/v2/#update-a-key
        """  # nopep8

        uri = "%s/%s" % (self.uri, id_fingerprint)
        attribs = {'name': name}

        return self.request(uri, "ssh_key", 'PUT', attribs=attribs)

    def destroy(self, id_fingerprint):
        """
        description: Destroy a Key

        in:
            - id_fingerprint - number / string - id or fingerprint of the key

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#destroy-a-key
        """  # nopep8

        uri = "%s/%s" % (self.uri, id_fingerprint)

        return self.request(uri, request_method='DELETE')
