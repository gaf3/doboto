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

    def __init__(self, token, url, agent):
        """
        Takes token and agent and sets its URI for floating ip interaction.
        """
        super(SSHKey, self).__init__(token, agent)
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
        """

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
        """
        attribs = {'name': name,
                   'public_key': public_key}

        return self.request(self.uri, "ssh_key", 'POST', attribs=attribs)

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
        """

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
        """


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
        """

        uri = "%s/%s" % (self.uri, id_fingerprint)

        return self.request(uri, request_method='DELETE')
