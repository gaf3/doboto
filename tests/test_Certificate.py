"""
This module contains tests for the main DO class
"""

from unittest import TestCase
from mock import MagicMock, patch, call
from doboto import Certificate
from doboto.DOBOTOException import DOBOTOException


class TestCertificate(TestCase):

    """
    This class implements unittests for the main DO class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/certificates".format(self.test_url)
        self.test_reports = "{}/reports".format(self.test_url)
        self.test_do = "do"
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_do, self.test_token, self.test_url, self.test_agent)

        self.klass_name = "Certificate"
        self.klass = getattr(Certificate, self.klass_name)

    def test_class_exists(self):
        """
        Certificate class is defined
        """

        self.assertTrue(hasattr(Certificate, self.klass_name))

    def test_can_instantiate(self):
        """
        Certificate class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Certificate.Certificate.pages')
    def test_list(self, mock_pages):
        """
        list works with certificate id
        """

        certificate = self.klass(*self.instantiate_args)

        certificate.list()
        mock_pages.assert_called_with(self.test_uri, "certificates")


    @patch('doboto.Certificate.Certificate.request')
    def test_create(self, mock_request):
        """
        create works with parameter
        """

        certificate = self.klass(*self.instantiate_args)

        mock_request.return_value = {"id": 1, "people": "stuff"}

        datas = {"name": "secret", "private_key": "private",
                 "leaf_certificate": "tree", "certificate_chain": "chain"}
        self.assertEqual(
            certificate.create("secret", "private", "tree", "chain"),
            {"id": 1, "people": "stuff"}
        )

        mock_request.assert_called_with(self.test_uri, "certificate", 'POST', attribs=datas)

    def test_present(self):
        """
        present works with name
        """

        certificate = self.klass(*self.instantiate_args)

        certificate.list = MagicMock(return_value=[
            {"id": 1, "name": "people"},
            {"id": 2, "name": "stuff"},
            {"id": 3, "name": "things"}
        ])

        ids = [4]

        def create(name, private_key, leaf_certificate, certificate_chain):
            return {"id": ids.pop(0), "name": name}

        certificate.create = MagicMock(side_effect=create)

        exist = certificate.present("people", 1, 2, 3)
        self.assertEqual(exist, ({"id": 1, "name": "people"}, None))

        new = certificate.present("dogs", 1, 2, 3)
        self.assertEqual(new, ({"id": 4, "name": "dogs"}, {"id": 4, "name": "dogs"}))
        certificate.create.assert_has_calls([
            call("dogs", 1, 2, 3)
        ])

    @patch('doboto.Certificate.Certificate.request')
    def test_info(self, mock_request):
        """
        info works with certificate id
        """

        id = 12345
        certificate = self.klass(*self.instantiate_args)
        certificate.info(id)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_request.assert_called_with(test_uri, "certificate")

    @patch('doboto.Certificate.Certificate.request')
    def test_destroy(self, mock_request):
        """
        destroy works with certificate id
        """

        id = 12345
        certificate = self.klass(*self.instantiate_args)
        certificate.destroy(id)
        test_uri = "{}/{}".format(self.test_uri, id)

        mock_request.assert_called_with(test_uri, request_method='DELETE')
