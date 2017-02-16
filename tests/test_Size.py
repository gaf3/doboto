"""
This module contains tests for the Size class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Size


class TestSize(TestCase):
    """
    This class implements unittests for the Size class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/sizes".format(self.test_url)
        self.test_do = "do"
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_do, self.test_token, self.test_url, self.test_agent)

        self.klass_name = "Size"
        self.klass = getattr(Size, self.klass_name)

    def test_class_exists(self):
        """
        Size class is defined
        """

        self.assertTrue(hasattr(Size, self.klass_name))

    def test_can_instantiate(self):
        """
        Size class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Size.Size.pages')
    def test_list_happy(self, mock_pages):
        """
        list works with happy path
        """

        size = self.klass(*self.instantiate_args)
        result = size.list()

        mock_pages.assert_called_with(self.test_uri, "sizes")
