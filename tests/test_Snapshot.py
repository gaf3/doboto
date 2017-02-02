"""
This module contains tests for the Snapshot class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Snapshot


class TestSnapshot(TestCase):
    """
    This class implements unittests for the Snapshot class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/snapshots".format(self.test_url)
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

        self.klass_name = "Snapshot"
        self.klass = getattr(Snapshot, self.klass_name)

    def test_class_exists(self):
        """
        Snapshot class is defined
        """

        self.assertTrue(hasattr(Snapshot, self.klass_name))

    def test_can_instantiate(self):
        """
        Snapshot class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Snapshot.Snapshot.pages')
    def test_list_happy(self, mock_pages):
        """
        list works with happy path
        """

        snapshot = self.klass(self.test_url, self.test_token)

        result = snapshot.list("fee")
        mock_pages.assert_called_with(
            self.test_uri, "snapshots", params={"resource_type": "fee"}
        )

        result = snapshot.list()
        mock_pages.assert_called_with(self.test_uri, "snapshots", params={})

    @patch('doboto.Snapshot.Snapshot.request')
    def test_info(self, mock_request):
        """
        info works with snapshot id
        """

        id = 7555620
        snapshot = self.klass(self.test_url, self.test_token)
        result = snapshot.info(id)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_request.assert_called_with(test_uri, "snapshot")

    @patch('doboto.Snapshot.Snapshot.request')
    def test_destroy(self, mock_request):
        """
        destroy works with snapshot id
        """

        id = 7555620
        snapshot = self.klass(self.test_url, self.test_token)
        result = snapshot.destroy(id)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_request.assert_called_with(
            test_uri, request_method="DELETE"
        )
