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
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

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

    @patch('doboto.Size.Size.make_request')
    def test_list_happy(self, mock_make_request):
        """
        list works with happy path
        """

        mock_ret = {
            "sizes": [
                {
                    "slug": "512mb",
                    "memory": 512,
                    "vcpus": 1,
                    "disk": 20,
                    "transfer": 1.0,
                    "price_monthly": 5.0,
                    "price_hourly": 0.00744,
                    "regions": [
                        "nyc1",
                        "sgp1",
                        "ams1",
                        "ams2",
                        "sfo1",
                        "nyc2",
                        "lon1",
                        "nyc3",
                        "ams3"
                    ],
                    "available": True
                }
            ]
        }

        mock_make_request.return_value = mock_ret
        size = self.klass(self.test_uri, self.test_token)
        result = size.list()

        self.assertEqual(result, mock_ret)
