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

    def list(self):
        """
        list all domains
        """
        return self.pages(self.uri, "domains")

    def create(self, name, ip_address):
        """Create a domain based off of parameters"""

        attribs = {
            "name": name,
            "ip_address": ip_address
        }

        return self.request(self.uri, "domain", 'POST', attribs=attribs)

    def info(self, name):
        """
        Retrieve domain information
        """
        uri = "{}/{}".format(self.uri, name)
        return self.request(uri, "domain")

    def destroy(self, name):
        """
        Destroy a domain
        """

        uri = "{}/{}".format(self.uri, name)
        return self.request(uri, request_method='DELETE')

    def record_list(self, name):
        """
        Retrieve all domain records
        """
        uri = "{}/{}/records".format(self.uri, name)
        return self.pages(uri, "domain_records")

    def record_create(self, name, attribs):
        """
        Create domain record
        """
        uri = "{}/{}/records".format(self.uri, name)
        return self.request(uri, "domain_record", 'POST', attribs=attribs)

    def record_info(self, name, record_id):
        """
        Retrieve specific domain record
        """
        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.request(uri, "domain_record")

    def record_update(self, name, record_id, attribs):
        """
        Update specific domain record
        """

        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.request(uri, "domain_record", 'PUT', attribs=attribs)

    def record_destroy(self, name, record_id):
        """
        Delete specific domain record
        """

        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.request(uri, request_method='DELETE')
