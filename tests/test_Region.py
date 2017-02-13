"""
This module contains tests for the Region class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Region


class TestRegion(TestCase):
    """
    This class implements unittests for the Region class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/regions".format(self.test_url)
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_token, self.test_url, self.test_agent)

        self.klass_name = "Region"
        self.klass = getattr(Region, self.klass_name)

    def test_class_exists(self):
        """
        Region class is defined
        """

        self.assertTrue(hasattr(Region, self.klass_name))

    def test_can_instantiate(self):
        """
        Region class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Region.Region.pages')
    def test_list_happy(self, mock_pages):
        """
        list works with happy path
        """

        region = self.klass(*self.instantiate_args)
        result = region.list()

        mock_pages.assert_called_with(self.test_uri, "regions")
