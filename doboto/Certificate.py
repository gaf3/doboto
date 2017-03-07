"""This holds the Certificate class."""

import time
import copy
from .Endpoint import Endpoint


class Certificate(Endpoint):

    """
    description:
        SSL certificates may be uploaded to DigitalOcean where they will be placed in a fully
        encrypted and isolated storage system. They may then be used to perform SSL termination
        on Load Balancers.

    related: https://developers.digitalocean.com/documentation/v2/#certificates
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for certificate interaction.
        """
        super(Certificate, self).__init__(token, agent)
        self.do = do
        self.uri = "%s/certificates" % url
        self.reports = "%s/reports" % url

    def list(self, tag_name=None):
        """
        description: List all Certificates

        out:
            A list of Certificate dict's:
                - id - string - A unique ID that can be used to identify and reference a certificate.
                - name - string - A unique human-readable name referring to a certificate.
                - not_after - string - A time value given in ISO8601 combined date and time format that represents the certificate's expiration date.
                - sha1_fingerprint - string - A unique identifier generated from the SHA-1 fingerprint of the certificate.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the certificate was created.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-certificates
        """  # nopep8

        return self.pages(self.uri, "certificates")

    def create(self, name, private_key, leaf_certificate, certificate_chain):
        """
        description: Create a new Certificate or multiple Certificates

        in:
            - name - string - A unique human-readable name referring to a certificate. - true
            - private_key - string - The contents of a PEM-formatted private-key corresponding to the SSL certificate. - true
            - leaf_certificate - string - The contents of a PEM-formatted public SSL certificate. - true
            - certificate_chain - string - The full PEM-formatted trust chain between the certificate authority's certificate and your domain's SSL certificate. - true

        out:
            A Certificate dict:
                - id - string - A unique ID that can be used to identify and reference a certificate.
                - name - string - A unique human-readable name referring to a certificate.
                - not_after - string - A time value given in ISO8601 combined date and time format that represents the certificate's expiration date.
                - sha1_fingerprint - string - A unique identifier generated from the SHA-1 fingerprint of the certificate.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the certificate was created.
        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-certificates
        """  # nopep8

        attribs = {
            "name": name,
            "private_key": private_key,
            "leaf_certificate": leaf_certificate,
            "certificate_chain": certificate_chain
        }

        return self.request(self.uri, "certificate", 'POST', attribs=attribs)

    def present(self, name, private_key, leaf_certificate, certificate_chain):
        """
        description: Create a new Certificate if not already existing

        in:
            - name - string - A unique human-readable name referring to a certificate. - true
            - private_key - string - The contents of a PEM-formatted private-key corresponding to the SSL certificate. - true
            - leaf_certificate - string - The contents of a PEM-formatted public SSL certificate. - true
            - certificate_chain - string - The full PEM-formatted trust chain between the certificate authority's certificate and your domain's SSL certificate. - true

        out:
            A tuple of two Certificate dict's (second is None if already present):
                - id - string - A unique ID that can be used to identify and reference a certificate.
                - name - string - A unique human-readable name referring to a certificate.
                - not_after - string - A time value given in ISO8601 combined date and time format that represents the certificate's expiration date.
                - sha1_fingerprint - string - A unique identifier generated from the SHA-1 fingerprint of the certificate.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the certificate was created.
        """  # nopep8

        certificates = self.list()

        existing = None
        for certificate in certificates:
            if name == certificate["name"]:
                existing = certificate
                break

        if existing is not None:
            return (existing, None)

        created = self.create(name, private_key, leaf_certificate, certificate_chain)
        return (created, created)

    def info(self, id):
        """
        description: Retrieve an existing Certificate by id

        in:
            - id - number - The id of the Certificate to retrieve

        out:
            A Certificate dict:
                - id - string - A unique ID that can be used to identify and reference a certificate.
                - name - string - A unique human-readable name referring to a certificate.
                - not_after - string - A time value given in ISO8601 combined date and time format that represents the certificate's expiration date.
                - sha1_fingerprint - string - A unique identifier generated from the SHA-1 fingerprint of the certificate.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the certificate was created.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-certificates
        """  # nopep8

        return self.request("%s/%s" % (self.uri, id), "certificate")

    def destroy(self, id=None, tag_name=None):
        """
        description: Delete a Certificate

        in:
            - id - number - The id of the Certificate to destroy

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#delete-a-certificates
        """  # nopep8

        return self.request("%s/%s" % (self.uri, id), request_method='DELETE')
