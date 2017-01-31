"""This holds the Domain class."""

from .Endpoint import Endpoint


class Domain(Endpoint):

    """Class for interacting with domains."""

    def __init__(self, url, token):
        """
        Take token and sets its URI for domain interaction.
        """
        super(Domain, self).__init__(token)
        self.uri = "{}/domains".format(url)

    def create(self, name, ip_address):
        """Create a domain based off of parameters"""

        attribs = {
            "name": name,
            "ip_address": ip_address
        }

        return self.make_request(self.uri, 'POST', attribs=attribs)

    def list(self):
        """
        list all domains
        """
        return self.make_request(self.uri)

    def info(self, name):
        """
        Retrieve domain information
        """
        uri = "{}/{}".format(self.uri, name)
        return self.make_request(uri)

    def destroy(self, name):
        """
        Destroy a domain
        """

        uri = "{}/{}".format(self.uri, name)
        return self.make_request(uri, 'DELETE')

    def records(self, name):
        """
        Retrieve all domain records
        """
        uri = "{}/{}/records".format(self.uri, name)
        return self.make_request(uri)

    def record_info(self, name, record_id):
        """
        Retrieve specific domain record
        """
        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.make_request(uri)

    def record_update(self, name, record_id, attribs=None):
        """
        Update specific domain record
        """

        if attribs is None:
            raise ValueError("Must supply a data to edit")

        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.make_request(uri, 'PUT', attribs=attribs)

    def record_destroy(self, name, record_id):
        """
        Delete specific domain record
        """

        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.make_request(uri, 'DELETE')
