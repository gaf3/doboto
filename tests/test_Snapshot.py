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

    @patch('doboto.Snapshot.Snapshot.make_request')
    def test_info(self, mock_make_request):
        """
        info works with snapshot id
        """

        mock_ret = {
            "snapshot": {
                "id": 7555620,
                "name": "Nifty New Snapshot",
                "regions": [
                    "nyc2",
                    "nyc2"
                ],
                "created_at": "2014-11-04T22:23:02Z",
                "min_disk_size": 20,
                "size_gigabytes": 2.34
            }
        }

        mock_make_request.return_value = mock_ret
        id = 7555620
        snapshot = self.klass(self.test_url, self.test_token)
        result = snapshot.info(id)

        self.assertEqual(result, mock_ret)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Snapshot.Snapshot.make_request')
    def test_list_happy(self, mock_make_request):
        """
        list works with happy path
        """

        mock_ret = {
            "snapshots": [
                {
                    "id": 7555620,
                    "name": "Nifty New Snapshot",
                    "regions": [
                        "nyc2",
                        "nyc2"
                    ],
                    "created_at": "2014-11-04T22:23:02Z",
                    "min_disk_size": 20,
                    "size_gigabytes": 2.34
                }
            ],
            "links": {
                "pages": {
                    "last": "https://api.digitalocean.com/v2/snapshots?page=56&per_page=1",
                    "next": "https://api.digitalocean.com/v2/snapshots?page=2&per_page=1"
                }
            },
            "meta": {
                "total": 56
            }
        }

        mock_make_request.return_value = mock_ret
        snapshot = self.klass(self.test_url, self.test_token)

        result = snapshot.list("fee")
        self.assertEqual(result, mock_ret)
        mock_make_request.assert_called_with(
            self.test_uri, params={"resource_type": "fee"}
        )

        result = snapshot.list()
        self.assertEqual(result, mock_ret)
        mock_make_request.assert_called_with(self.test_uri, params={})

    @patch('doboto.Snapshot.Snapshot.make_request')
    def test_destroy(self, mock_make_request):
        """
        destroy works with snapshot id
        """

        id = 7555620
        snapshot = self.klass(self.test_url, self.test_token)
        result = snapshot.destroy(id)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_make_request.assert_called_with(
            test_uri, request_method="DELETE"
        )
