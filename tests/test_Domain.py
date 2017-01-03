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
        domain_name = "test-domain.com"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.info(domain_name)
        test_uri = "{}/{}".format(self.test_uri, domain_name)

        mock_make_request.assert_called_with(test_uri)



    @patch('doboto.Domain.Domain.make_request')
    def test_destroy(self, mock_make_request):
        """
        test destroy method
        """
        domain_name = "test-domain.com"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.destroy(domain_name)
        test_uri = "{}/{}".format(self.test_uri, domain_name)

        mock_make_request.assert_called_with(test_uri, 'DELETE')


    @patch('doboto.Domain.Domain.make_request')
    def test_create(self, mock_make_request):
        """
        test create method
        """
        domain_obj = self.klass(self.test_url, self.test_token)
        datas = {"name": "test-domain.com", "ip_address": "1.2.3.4"}
        domain_obj.create(datas)
        test_uri = "{}".format(self.test_uri)

        mock_make_request.assert_called_with(test_uri, 'POST', attribs=datas)

        with self.assertRaises(ValueError):
            domain_obj.create()


    @patch('doboto.Domain.Domain.make_request')
    def test_list_records(self, mock_make_request):
        """
        test list_records method
        """
        domain_name = "test-domain.com"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.list_records(domain_name)
        test_uri = "{}/{}/records".format(self.test_uri, domain_name)

        mock_make_request.assert_called_with(test_uri)



    @patch('doboto.Domain.Domain.make_request')
    def test_get_record(self, mock_make_request):
        """
        test get_record method
        """
        domain_name = "test-domain.com"
        record_id = "4567"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.get_record(domain_name, record_id)
        test_uri = "{}/{}/records/{}".format(self.test_uri, domain_name, record_id)

        mock_make_request.assert_called_with(test_uri)



    @patch('doboto.Domain.Domain.make_request')
    def test_edit_record(self, mock_make_request):
        """
        test edit_record method
        """
        domain_name = "test-domain.com"
        record_id = "4567"
        datas = {"type": "AAAA", "name": "dat-v6-tho", "data": "::"}
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.edit_record(domain_name, record_id, datas)
        test_uri = "{}/{}/records/{}".format(self.test_uri, domain_name, record_id)

        mock_make_request.assert_called_with(test_uri, 'PUT', attribs=datas)

        with self.assertRaises(ValueError):
            domain_obj.edit_record(domain_name, record_id)


    @patch('doboto.Domain.Domain.make_request')
    def test_delete_record(self, mock_make_request):
        """
        test delete_record method
        """
        domain_name = "test-domain.com"
        record_id = "4567"
        domain_obj = self.klass(self.test_url, self.test_token)
        domain_obj.delete_record(domain_name, record_id)
        test_uri = "{}/{}/records/{}".format(self.test_uri, domain_name, record_id)

        mock_make_request.assert_called_with(test_uri, 'DELETE')
