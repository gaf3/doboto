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
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

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

    @patch('doboto.Account.Account.make_request')
    def test_info(self, mock_make_request):
        """
        info gets it
        """

        mock_ret = {
            "account": {
                "droplet_limit": 25,
                "floating_ip_limit": 5,
                "email": "sammy@digitalocean.com",
                "uuid": "b6fr89dbf6d9156cace5f3c78dc9851d957381ef",
                "email_verified": True,
                "status": "active",
                "status_message": ""
            }
        }

        mock_make_request.return_value = mock_ret
        account = self.klass(*self.instantiate_args)
        result = account.info()

        self.assertEqual(result, mock_ret)
        mock_make_request.assert_called_with(self.test_uri)
