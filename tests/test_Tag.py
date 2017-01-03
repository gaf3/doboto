"""
This module contains tests for the Tag class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Tag


class TestTag(TestCase):
    """
    This class implements unittests for the Tag class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/tags".format(self.test_url)
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

        self.klass_name = "Tag"
        self.klass = getattr(Tag, self.klass_name)

    def test_class_exists(self):
        """
        Tag class is defined
        """

        self.assertTrue(hasattr(Tag, self.klass_name))

    def test_can_instantiate(self):
        """
        Tag class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Tag.Tag.make_request')
    def test_create_happy(self, mock_make_request):
        """
        create works with happy path
        """

        test_name = "bob"
        tag = self.klass(self.test_url, self.test_token)
        tag.create(test_name)

        mock_make_request.assert_called_with(self.test_uri, 'POST', {'name': test_name})

    @patch('doboto.Tag.Tag.make_request')
    def test_destroy_happy(self, mock_make_request):
        """
        destroy works with happy path
        """

        test_name = "bob"
        tag = self.klass(self.test_url, self.test_token)
        tag.destroy(test_name)
        test_uri = "{}/{}".format(self.test_uri, test_name)

        mock_make_request.assert_called_with(test_uri, 'DELETE')

    @patch('doboto.Tag.Tag.make_request')
    def test_rename_happy(self, mock_make_request):
        """
        rename works with happy path
        """

        test_name = "bob"
        test_new_name = "sally"
        tag = self.klass(self.test_url, self.test_token)
        tag.rename(test_name, test_new_name)
        test_uri = "{}/{}".format(self.test_uri, test_name)

        mock_make_request.assert_called_with(test_uri, 'PUT', {'name': test_new_name})

    @patch('doboto.Tag.Tag.make_request')
    def test_list_happy(self, mock_make_request):
        """
        list works with happy path
        """

        extra_data = {'droplet': 'some data', 'your aunt': 'bessie', 'a moose once bit': 'my sister'}
        tag_names = ['alpha', 'beta', 'gamma']
        mock_ret = {'tags': [{'name': _, 'resources': extra_data} for _ in tag_names]}


        mock_make_request.return_value = mock_ret
        tag = self.klass(self.test_uri, self.test_token)
        result = tag.list()

        self.assertListEqual(result, tag_names)

    @patch('doboto.Tag.Tag.make_request')
    def test_list_happy_without_tags(self, mock_make_request):
        """
        list method works when no tags are returned
        """

        mock_ret = {'status': 'you suck, go away'}

        mock_make_request.return_value = mock_ret

        tag = self.klass(self.test_uri, self.test_token)
        result = tag.list()

        self.assertDictEqual(result, mock_ret)
