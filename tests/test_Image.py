"""
This module contains tests for the Image class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Image


class TestImage(TestCase):
    """
    This class implements unittests for the Image class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/images".format(self.test_url)
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

        self.klass_name = "Image"
        self.klass = getattr(Image, self.klass_name)

    def test_class_exists(self):
        """
        Image class is defined
        """

        self.assertTrue(hasattr(Image, self.klass_name))

    def test_can_instantiate(self):
        """
        Image class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Image.Image.make_request')
    def test_info(self, mock_make_request):
        """
        info works with image id
        """

        mock_ret = {
            "id": 7555620,
            "name": "Nifty New Snapshot",
            "distribution": "Ubuntu",
            "slug": None,
            "public": False,
            "regions": [
                "nyc2",
                "nyc2"
            ],
            "created_at": "2014-11-04T22:23:02Z",
            "type": "snapshot",
            "min_disk_size": 20,
            "size_gigabytes": 2.34
        }

        mock_make_request.return_value = mock_ret
        image_id = 7555620
        image = self.klass(self.test_url, self.test_token)
        result = image.info(image_id)

        self.assertEqual(result, mock_ret)

        test_uri = "{}/{}".format(self.test_uri, image_id)
        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.Image.Image.make_request')
    def test_list_happy(self, mock_make_request):
        """
        list works with happy path
        """

        mock_ret = {
            "images": [
                {
                    "id": 7555620,
                    "name": "Nifty New Snapshot",
                    "distribution": "Ubuntu",
                    "slug": None,
                    "public": False,
                    "regions": [
                        "nyc2",
                        "nyc2"
                    ],
                    "created_at": "2014-11-04T22:23:02Z",
                    "type": "snapshot",
                    "min_disk_size": 20,
                    "size_gigabytes": 2.34
                }
            ],
            "links": {
                "pages": {
                    "last": "https://api.digitalocean.com/v2/images?page=56&per_page=1",
                    "next": "https://api.digitalocean.com/v2/images?page=2&per_page=1"
                }
            },
            "meta": {
                "total": 56
            }
        }

        mock_make_request.return_value = mock_ret
        image = self.klass(self.test_url, self.test_token)

        result = image.list("fee", "fie")
        self.assertEqual(result, mock_ret)
        mock_make_request.assert_called_with(
            self.test_uri, params={"type": "fee", "private": "fie"}
        )

        result = image.list()
        self.assertEqual(result, mock_ret)
        mock_make_request.assert_called_with(self.test_uri, params={})

    @patch('doboto.Image.Image.make_request')
    def test_list_actions(self, mock_make_request):
        """
        list the actions of a image
        """

        mock_ret = {
            "actions": [],
            "links": {},
            "meta": {
                "total": 0
            }
        }

        mock_make_request.return_value = mock_ret
        image_id = 7555620
        image = self.klass(self.test_url, self.test_token)
        result = image.list_actions(image_id)

        self.assertEqual(result, mock_ret)

        mock_make_request.assert_called_with(
            "%s/%s/actions" % (self.test_uri, image_id)
        )

    @patch('doboto.Image.Image.make_request')
    def test_update(self, mock_make_request):
        """
        update works with image id
        """

        mock_ret = {
            "id": 7555620,
            "name": "Nifty New Name",
            "distribution": "Ubuntu",
            "slug": None,
            "public": False,
            "regions": [
                "nyc2",
                "nyc2"
            ],
            "created_at": "2014-11-04T22:23:02Z",
            "type": "snapshot",
            "min_disk_size": 20,
            "size_gigabytes": 2.34
        }

        mock_make_request.return_value = mock_ret
        image_id = 7555620
        image = self.klass(self.test_url, self.test_token)
        result = image.update(image_id, "Nifty New Name")

        self.assertEqual(result, mock_ret)

        test_uri = "{}/{}".format(self.test_uri, image_id)
        mock_make_request.assert_called_with(
            test_uri, attribs={"name": "Nifty New Name"}, request_method="PUT"
        )

    @patch('doboto.Image.Image.make_request')
    def test_delete(self, mock_make_request):
        """
        destroy works with image id
        """

        image_id = 7555620
        image = self.klass(self.test_url, self.test_token)
        result = image.destroy(image_id)

        test_uri = "{}/{}".format(self.test_uri, image_id)
        mock_make_request.assert_called_with(
            test_uri, request_method="DELETE"
        )
