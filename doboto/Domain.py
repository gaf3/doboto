"""This holds the Domain class."""

from .Endpoint import Endpoint


class Domain(Endpoint):
    """
    description:
        Domain resources are domain names that you have purchased from a domain name registrar that
        you are managing through the DigitalOcean DNS interface.

        This resource establishes top-level control over each domain. Actions that affect
        individual domain records should be taken on the [Domain Records] resource.

    related: https://developers.digitalocean.com/documentation/v2/#domains
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for domain interaction.
        """
        super(Domain, self).__init__(token, agent)
        self.do = do
        self.uri = "{}/domains".format(url)

    def list(self):
        """
        description: List all Domains

        out:
            A list of Domain dict's:
                - name - string - The name of the domain itself. This should follow the standard domain format of domain.TLD. For instance, example.com is a valid domain name.
                - ttl - number - This value is the time to live for the records on this domain, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested.
                - zone_file - string - This attribute contains the complete contents of the zone file for the selected domain. Individual domain record resources should be used to get more granular control over records. However, this attribute can also be used to get information about the SOA record, which is created automatically and is not accessible as an individual record resource.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-domains
        """  # nopep8
        return self.pages(self.uri, "domains")

    def create(self, name, ip_address):
        """
        description: Create a new Domain

        in:
            - name - string - The domain name to add to the DigitalOcean DNS management interface. The name must be unique in DigitalOcean's DNS system. The request will fail if the name has already been taken.
            - ip_address - string - This attribute contains the IP address you want the domain to point to.

        out:
            A Domain dict:
                - name - string - The name of the domain itself. This should follow the standard domain format of domain.TLD. For instance, example.com is a valid domain name.
                - ttl - number - This value is the time to live for the records on this domain, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested.
                - zone_file - string - This attribute contains the complete contents of the zone file for the selected domain. Individual domain record resources should be used to get more granular control over records. However, this attribute can also be used to get information about the SOA record, which is created automatically and is not accessible as an individual record resource.

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-domain
        """  # nopep8

        attribs = {
            "name": name,
            "ip_address": ip_address
        }

        return self.request(self.uri, "domain", 'POST', attribs=attribs)

    def present(self, name, ip_address):
        """
        description: Create a new Domain if name doesn't already exist

        in:
            - name - string - The domain name to add to the DigitalOcean DNS management interface. The name must be unique in DigitalOcean's DNS system. The request will fail if the name has already been taken.
            - ip_address - string - This attribute contains the IP address you want the domain to point to.

        out:
            A tuple of Domain dict's, the intended, and created (None if already exists):
                - name - string - The name of the domain itself. This should follow the standard domain format of domain.TLD. For instance, example.com is a valid domain name.
                - ttl - number - This value is the time to live for the records on this domain, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested.
                - zone_file - string - This attribute contains the complete contents of the zone file for the selected domain. Individual domain record resources should be used to get more granular control over records. However, this attribute can also be used to get information about the SOA record, which is created automatically and is not accessible as an individual record resource.

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-domain
        """  # nopep8

        domains = self.list()

        existing = None
        for domain in domains:
            if name == domain["name"]:
                existing = domain
                break

        if existing is not None:
            return (existing, None)

        created = self.create(name, ip_address)
        return (created, created)

    def info(self, name):
        """
        description: Retrieve an existing Domain

        in:
            - name - string - The name of the domain to retrieve

        out:
            A Domain dict:
                - name - string - The name of the domain itself. This should follow the standard domain format of domain.TLD. For instance, example.com is a valid domain name.
                - ttl - number - This value is the time to live for the records on this domain, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested.
                - zone_file - string - This attribute contains the complete contents of the zone file for the selected domain. Individual domain record resources should be used to get more granular control over records. However, this attribute can also be used to get information about the SOA record, which is created automatically and is not accessible as an individual record resource.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-domain
        """  # nopep8
        uri = "{}/{}".format(self.uri, name)
        return self.request(uri, "domain")

    def destroy(self, name):
        """
        description: Delete a Domain

        in:
            - name - string - The name of the domain to destroy

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#delete-a-domain
        """  # nopep8

        uri = "{}/{}".format(self.uri, name)
        return self.request(uri, request_method='DELETE')

    def record_list(self, name):
        """
        description: List all Domain Records

        in:
            - name - string - The name of the domain, the Domain Records of which to retrieve

        out:
            A list of Domain Record dict's:
                - id - number - A unique identifier for each domain record.
                - type - string - The type of the DNS record (A, CNAME, TXT, ...).
                - name - string - The name to use for the DNS record.
                - data - string - The value to use for the DNS record.
                - priority - nullable number - The priority for SRV and MX records.
                - port - nullable number - The port for SRV records.
                - weight - nullable number - The weight for SRV records.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-domain-records
        """  # nopep8
        uri = "{}/{}/records".format(self.uri, name)
        return self.pages(uri, "domain_records")

    def record_create(self, name, attribs):
        """
        description: Create a new Domain Record

        in:
            - name - string - The name of the domain
            - attribs - dict - The data of the Domain Record in the following format:
                - type - string - The record type (A, MX, CNAME, etc). - All Records
                - name - string - The host name, alias, or service being defined by the record. - A, AAAA, CNAME, TXT, SRV
                - data - string - Variable data depending on record type. See the [Domain Records]() section for more detail on each record type. - A, AAAA, CNAME, MX, TXT, SRV, NS
                - priority - nullable number - The priority of the host (for SRV and MX records. null otherwise). - MX, SRV
                - port - nullable number - The port that the service is accessible on (for SRV records only. null otherwise). - SRV
                - weight - nullable number - The weight of records with the same priority (for SRV records only. null otherwise). - SRV

        out:
            A Domain Record dict:
                - id - number - A unique identifier for each domain record.
                - type - string - The type of the DNS record (A, CNAME, TXT, ...).
                - name - string - The name to use for the DNS record.
                - data - string - The value to use for the DNS record.
                - priority - nullable number - The priority for SRV and MX records.
                - port - nullable number - The port for SRV records.
                - weight - nullable number - The weight for SRV records.

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-domain-record
        """  # nopep8
        uri = "{}/{}/records".format(self.uri, name)
        return self.request(uri, "domain_record", 'POST', attribs=attribs)

    def record_info(self, name, record_id):
        """
        description: Retrieve an existing Domain Record

        in:
            - name - string - The name of the domain
            - record_id - number - The id of the domain record to retrieve

        out:
            A Domain Record dict:
                - id - number - A unique identifier for each domain record.
                - type - string - The type of the DNS record (A, CNAME, TXT, ...).
                - name - string - The name to use for the DNS record.
                - data - string - The value to use for the DNS record.
                - priority - nullable number - The priority for SRV and MX records.
                - port - nullable number - The port for SRV records.
                - weight - nullable number - The weight for SRV records.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-domain-record
        """  # nopep8
        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.request(uri, "domain_record")

    def record_update(self, name, record_id, attribs):
        """
        description: Update a Domain Record

        in:
            - name - string - The name of the domain
            - record_id - number - The id of the domain record to update
            - attribs - dict - The data of the Domain Record in the following format:
                - type - string - The record type (A, MX, CNAME, etc). - All Records
                - name - string - The host name, alias, or service being defined by the record. - A, AAAA, CNAME, TXT, SRV
                - data - string - Variable data depending on record type. See the [Domain Records]() section for more detail on each record type. - A, AAAA, CNAME, MX, TXT, SRV, NS
                - priority - nullable number - The priority of the host (for SRV and MX records. null otherwise). - MX, SRV
                - port - nullable number - The port that the service is accessible on (for SRV records only. null otherwise). - SRV
                - weight - nullable number - The weight of records with the same priority (for SRV records only. null otherwise). - SRV

        out:
            A Domain Record dict:
                - id - number - A unique identifier for each domain record.
                - type - string - The type of the DNS record (A, CNAME, TXT, ...).
                - name - string - The name to use for the DNS record.
                - data - string - The value to use for the DNS record.
                - priority - nullable number - The priority for SRV and MX records.
                - port - nullable number - The port for SRV records.
                - weight - nullable number - The weight for SRV records.

        related: https://developers.digitalocean.com/documentation/v2/#update-a-domain-record
        """  # nopep8

        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.request(uri, "domain_record", 'PUT', attribs=attribs)

    def record_destroy(self, name, record_id):
        """
        description: Delete a Domain Record

        in:
            - name - string - The name of the domain
            - record_id - number - The id of the domain record to destroy

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#delete-a-domain-record
        """  # nopep8

        uri = "{}/{}/records/{}".format(self.uri, name, record_id)
        return self.request(uri, request_method='DELETE')
