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
        return self.make_request(self.uri)

    def info(self, domain_name):
        """
        Retrieve domain information
        """
        uri = "{}/{}".format(self.uri, domain_name)
        return self.make_request(uri)

    def destroy(self, domain_name):
        """
        Destroy a domain
        """

        uri = "{}/{}".format(self.uri, domain_name)
        return self.make_request(uri, 'DELETE')

    def create(self, attribs=None):
        """Create a domain based off of parameters"""

        if attribs is None:
            raise ValueError("Must supply a domain name and address")

        return self.make_request(self.uri, 'POST', attribs=attribs)

    def list_records(self, domain_name):
        """
        Retrieve all domain records
        """
        uri = "{}/{}/records".format(self.uri, domain_name)
        return self.make_request(uri)

    def get_record(self, domain_name, record_id):
        """
        Retrieve specific domain record
        """
        uri = "{}/{}/records/{}".format(self.uri, domain_name, record_id)
        return self.make_request(uri)

    def edit_record(self, domain_name, record_id, attribs=None):
        """
        Update specific domain record
        """

        if attribs is None:
            raise ValueError("Must supply a data to edit")

        uri = "{}/{}/records/{}".format(self.uri, domain_name, record_id)
        return self.make_request(uri, 'PUT', attribs=attribs)

    def delete_record(self, domain_name, record_id):
        """
        Delete specific domain record
        """

        uri = "{}/{}/records/{}".format(self.uri, domain_name, record_id)
        return self.make_request(uri, 'DELETE')
