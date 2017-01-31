"""
This module contains tests for the main Domain class
"""

from unittest import TestCase
from mock import MagicMock, patch
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
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

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

    @patch('doboto.Domain.Domain.make_request')
    def test_create(self, mock_make_request):
        """
        test create method
        """
        domain_obj = self.klass(self.test_url, self.test_token)
        datas = {"name": "test-domain.com", "ip_address": "1.2.3.4"}
        domain_obj.create("test-domain.com", "1.2.3.4")
        test_uri = "{}".format(self.test_uri)

        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

    @patch('doboto.Domain.Domain.make_request')
    def test_list(self, mock_make_request):
        """
        test list method
        """

        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.list()
        test_uri = "{}".format(self.test_uri)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Domain.Domain.make_request')
    def test_info(self, mock_make_request):
        """
        test info method
        """
        name = "test-domain.com"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.info(name)
        test_uri = "{}/{}".format(self.test_uri, name)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Domain.Domain.make_request')
    def test_destroy(self, mock_make_request):
        """
        test destroy method
        """
        name = "test-domain.com"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.destroy(name)
        test_uri = "{}/{}".format(self.test_uri, name)

        mock_make_request.assert_called_with(test_uri, 'DELETE')

    @patch('doboto.Domain.Domain.make_request')
    def test_records(self, mock_make_request):
        """
        test records method
        """
        name = "test-domain.com"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.records(name)
        test_uri = "{}/{}/records".format(self.test_uri, name)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Domain.Domain.make_request')
    def test_record_info(self, mock_make_request):
        """
        test record_info method
        """
        name = "test-domain.com"
        record_id = "4567"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.record_info(name, record_id)
        test_uri = "{}/{}/records/{}".format(self.test_uri, name, record_id)

        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Domain.Domain.make_request')
    def test_record_update(self, mock_make_request):
        """
        test record_update method
        """
        name = "test-domain.com"
        record_id = "4567"
        datas = {"type": "AAAA", "name": "dat-v6-tho", "data": "::"}
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.record_update(name, record_id, datas)
        test_uri = "{}/{}/records/{}".format(self.test_uri, name, record_id)

        mock_make_request.assert_called_with(test_uri, 'PUT', attribs=datas)

        with self.assertRaises(ValueError):
            domain_obj.record_update(name, record_id)

    @patch('doboto.Domain.Domain.make_request')
    def test_record_destroy(self, mock_make_request):
        """
        test record_destroy method
        """
        name = "test-domain.com"
        record_id = 4567
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.record_destroy(name, record_id)
        test_uri = "{}/{}/records/{}".format(self.test_uri, name, record_id)

        mock_make_request.assert_called_with(test_uri, 'DELETE')
