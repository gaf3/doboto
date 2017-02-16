"""
This module contains tests for the Account class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Account


class TestAccount(TestCase):
    """
    This class implements unittests for the Account class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/account".format(self.test_url)
        self.test_do = "do"
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_do, self.test_token, self.test_url, self.test_agent)

        self.klass_name = "Account"
        self.klass = getattr(Account, self.klass_name)

    def test_class_exists(self):
        """
        Account class is defined
        """

        self.assertTrue(hasattr(Account, self.klass_name))

    def test_can_instantiate(self):
        """
        Account class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Endpoint.Endpoint.request')
    def test_info(self, mock_request):
        """
        info calls request
        """

        account = self.klass(*self.instantiate_args)
        account.info()

        mock_request.assert_called_with(
            self.test_uri, "account"
        )
