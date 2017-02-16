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
        self.test_do = "do"
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_do, self.test_token, self.test_url, self.test_agent)

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

    @patch('doboto.Image.Image.pages')
    def test_list_happy(self, mock_pages):
        """
        list works with happy path
        """

        image = self.klass(*self.instantiate_args)

        result = image.list("fee", "fie")
        mock_pages.assert_called_with(
            self.test_uri, "images", params={"type": "fee", "private": "fie"}
        )

        result = image.list()
        mock_pages.assert_called_with(self.test_uri, "images", params={})

    @patch('doboto.Image.Image.request')
    def test_info(self, mock_request):
        """
        info works with image id
        """

        id_slug = 7555620
        image = self.klass(*self.instantiate_args)
        result = image.info(id_slug)

        test_uri = "{}/{}".format(self.test_uri, id_slug)
        mock_request.assert_called_with(test_uri, "image")

    @patch('doboto.Image.Image.request')
    def test_update(self, mock_request):
        """
        update works with image id
        """

        id = 7555620
        image = self.klass(*self.instantiate_args)
        result = image.update(id, "Nifty New Name")

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_request.assert_called_with(
            test_uri, "image", attribs={"name": "Nifty New Name"}, request_method="PUT"
        )

    @patch('doboto.Image.Image.request')
    def test_destroy(self, mock_request):
        """
        destroy works with image id
        """

        id = 7555620
        image = self.klass(*self.instantiate_args)
        result = image.destroy(id)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_request.assert_called_with(
            test_uri, request_method="DELETE"
        )

    @patch('doboto.Image.Image.action_result')
    @patch('doboto.Image.Image.request')
    def test_convert(self, mock_request, mock_action_result):
        """
        convert works with image id
        """

        id = 7555620
        image = self.klass(*self.instantiate_args)
        mock_request.return_value = {}
        result = image.convert(id, True, 2, 3)

        test_uri = "{}/{}/actions".format(self.test_uri, id)
        mock_request.assert_called_with(
            test_uri, "action", attribs={"type": "convert"}, request_method="POST"
        )
        mock_action_result.assert_called_with({}, True, 2, 3)

    @patch('doboto.Image.Image.action_result')
    @patch('doboto.Image.Image.request')
    def test_transfer(self, mock_request, mock_action_result):
        """
        transfer works with image id and region
        """

        id = 7555620
        region = "lon1"
        image = self.klass(*self.instantiate_args)
        mock_request.return_value = {}
        result = image.transfer(id, region, True, 2, 3)

        test_uri = "{}/{}/actions".format(self.test_uri, id)
        mock_request.assert_called_with(
            test_uri, "action", attribs={"type": "transfer", "region": region},
            request_method="POST"
        )
        mock_action_result.assert_called_with({}, True, 2, 3)

    @patch('doboto.Image.Image.pages')
    def test_action_list(self, mock_pages):
        """
        list the actions of a image
        """

        id = 7555620
        image = self.klass(*self.instantiate_args)
        result = image.action_list(id)

        mock_pages.assert_called_with(
            "%s/%s/actions" % (self.test_uri, id), "actions"
        )

    @patch('doboto.Image.Image.request')
    def test_action_info(self, mock_request):
        """
        action_info works with image id
        """

        id = 12345
        action_id = 54321
        image = self.klass(*self.instantiate_args)
        image.action_info(id, action_id)
        test_uri = "{}/{}/actions/{}".format(
            self.test_uri, id, action_id)

        mock_request.assert_called_with(test_uri, "action")
