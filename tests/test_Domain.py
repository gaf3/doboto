"""
This module contains tests for the main Domain class
"""

from unittest import TestCase
from mock import MagicMock, patch, call
from doboto import Domain


class TestDomain(TestCase):

    """
    This class implements unittests for the main DO class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/domains".format(self.test_url)
        self.test_do = "do"
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_do, self.test_token, self.test_url, self.test_agent)

        self.klass_name = "Domain"
        self.klass = getattr(Domain, self.klass_name)

    def test_class_exists(self):
        """
        Domain class is defined
        """

        self.assertTrue(hasattr(Domain, self.klass_name))

    def test_can_instantiate(self):
        """
        Domain class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Domain.Domain.pages')
    def test_list(self, mock_pages):
        """
        test list method
        """

        domain_obj = self.klass(*self.instantiate_args)
        domain_obj.list()
        test_uri = "{}".format(self.test_uri)

        mock_pages.assert_called_with(test_uri, "domains")

    @patch('doboto.Domain.Domain.request')
    def test_create(self, mock_request):
        """
        test create method
        """
        domain_obj = self.klass(*self.instantiate_args)
        datas = {"name": "test-domain.com", "ip_address": "1.2.3.4"}
        domain_obj.create("test-domain.com", "1.2.3.4")
        test_uri = "{}".format(self.test_uri)

        mock_request.assert_called_with(test_uri, "domain", 'POST', attribs=datas)

    def test_present(self):
        """
        test present method
        """
        domain_obj = self.klass(*self.instantiate_args)

        domain_obj.list = MagicMock(return_value=[{"name": "people"}])
        domain_obj.create = MagicMock(return_value={"name": "things"})

        self.assertEqual(
            domain_obj.present("people", "1.2.3.4"),
            (
                {"name": "people"},
                None
            )
        )

        self.assertEqual(
            domain_obj.present("stuff", "1.2.3.4"),
            (
                 {"name": "things"},
                 {"name": "things"}
            )
        )
        domain_obj.create.assert_has_calls([
            call("stuff", "1.2.3.4"),
        ])

    @patch('doboto.Domain.Domain.request')
    def test_info(self, mock_request):
        """
        test info method
        """
        name = "test-domain.com"
        domain_obj = self.klass(*self.instantiate_args)
        domain_obj.info(name)
        test_uri = "{}/{}".format(self.test_uri, name)

        mock_request.assert_called_with(test_uri, "domain")

    @patch('doboto.Domain.Domain.request')
    def test_destroy(self, mock_request):
        """
        test destroy method
        """
        name = "test-domain.com"
        domain_obj = self.klass(*self.instantiate_args)
        domain_obj.destroy(name)
        test_uri = "{}/{}".format(self.test_uri, name)

        mock_request.assert_called_with(test_uri, request_method='DELETE')

    @patch('doboto.Domain.Domain.pages')
    def test_record_list(self, mock_pages):
        """
        test record_list method
        """
        name = "test-domain.com"
        domain_obj = self.klass(*self.instantiate_args)
        domain_obj.record_list(name)
        test_uri = "{}/{}/records".format(self.test_uri, name)

        mock_pages.assert_called_with(test_uri, "domain_records")

    @patch('doboto.Domain.Domain.request')
    def test_record_create(self, mock_request):
        """
        test record_create method
        """
        name = "test-domain.com"
        datas = {"type": "AAAA", "name": "dat-v6-tho", "data": "::"}
        domain_obj = self.klass(*self.instantiate_args)
        domain_obj.record_create(name, datas)
        test_uri = "{}/{}/records".format(self.test_uri, name)

        mock_request.assert_called_with(test_uri, "domain_record", 'POST', attribs=datas)

    @patch('doboto.Domain.Domain.request')
    def test_record_info(self, mock_request):
        """
        test record_info method
        """
        name = "test-domain.com"
        record_id = 4567
        domain_obj = self.klass(*self.instantiate_args)
        domain_obj.record_info(name, record_id)
        test_uri = "{}/{}/records/{}".format(self.test_uri, name, record_id)

        mock_request.assert_called_with(test_uri, "domain_record")

    @patch('doboto.Domain.Domain.request')
    def test_record_update(self, mock_request):
        """
        test record_update method
        """
        name = "test-domain.com"
        record_id = "4567"
        datas = {"type": "AAAA", "name": "dat-v6-tho", "data": "::"}
        domain_obj = self.klass(*self.instantiate_args)
        domain_obj.record_update(name, record_id, datas)
        test_uri = "{}/{}/records/{}".format(self.test_uri, name, record_id)

        mock_request.assert_called_with(test_uri, "domain_record", 'PUT', attribs=datas)

    @patch('doboto.Domain.Domain.request')
    def test_record_destroy(self, mock_request):
        """
        test record_destroy method
        """
        name = "test-domain.com"
        record_id = 4567
        domain_obj = self.klass(*self.instantiate_args)
        domain_obj.record_destroy(name, record_id)
        test_uri = "{}/{}/records/{}".format(self.test_uri, name, record_id)

        mock_request.assert_called_with(test_uri, request_method='DELETE')
