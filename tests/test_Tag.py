"""
This module contains tests for the Tag class
"""

from unittest import TestCase
from mock import MagicMock, patch, call
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
        self.test_do = "do"
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_do, self.test_token, self.test_url, self.test_agent)

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

    @patch('doboto.Tag.Tag.pages')
    def test_list(self, mock_pages):
        """
        list works with nuttin
        """

        tag = self.klass(*self.instantiate_args)
        result = tag.list()

        mock_pages.assert_called_with(self.test_uri, "tags")

    @patch('doboto.Tag.Tag.pages')
    def test_name_list_happy(self, mock_pages):
        """
        name_list works with happy path
        """

        extra_data = {
            'droplet': 'some data', 'your aunt': 'bessie', 'a moose once bit': 'my sister'
        }
        names = ['alpha', 'beta', 'gamma']
        mock_ret = [{'name': _, 'resources': extra_data} for _ in names]

        mock_pages.return_value = mock_ret
        tag = self.klass(*self.instantiate_args)
        result = tag.name_list()

        mock_pages.assert_called_with(self.test_uri, "tags")

        self.assertListEqual(result, names)

    @patch('doboto.Tag.Tag.request')
    def test_create_happy(self, mock_request):
        """
        create works with happy path
        """

        test_name = "bob"
        tag = self.klass(*self.instantiate_args)
        tag.create(test_name)

        mock_request.assert_called_with(self.test_uri, "tag", 'POST', {'name': test_name})

    def test_present(self):
        """
        test present method
        """
        tag = self.klass(*self.instantiate_args)

        tag.list = MagicMock(return_value=[{"name": "people"}])
        tag.create = MagicMock(return_value={"name": "things"})

        self.assertEqual(
            tag.present("people"),
            (
                {"name": "people"},
                None
            )
        )

        self.assertEqual(
            tag.present("stuff"),
            (
                 {"name": "things"},
                 {"name": "things"}
            )
        )
        tag.create.assert_has_calls([
            call("stuff"),
        ])

    @patch('doboto.Tag.Tag.request')
    def test_info(self, mock_request):
        """
        info works with name
        """

        name = "hay"
        tag = self.klass(*self.instantiate_args)
        result = tag.info(name)

        test_uri = "{}/{}".format(self.test_uri, name)
        mock_request.assert_called_with(test_uri, "tag")

    @patch('doboto.Tag.Tag.request')
    def test_update_happy(self, mock_request):
        """
        update works with happy path
        """

        test_name = "bob"
        test_new_name = "sally"
        tag = self.klass(*self.instantiate_args)
        tag.update(test_name, test_new_name)
        test_uri = "{}/{}".format(self.test_uri, test_name)

        mock_request.assert_called_with(test_uri, "tag", 'PUT', {'name': test_new_name})

    @patch('doboto.Tag.Tag.request')
    def test_destroy_happy(self, mock_request):
        """
        destroy works with happy path
        """

        test_name = "bob"
        tag = self.klass(*self.instantiate_args)
        tag.destroy(test_name)
        test_uri = "{}/{}".format(self.test_uri, test_name)

        mock_request.assert_called_with(test_uri, request_method='DELETE')

    @patch('doboto.Tag.Tag.request')
    def test_attach_happy(self, mock_request):
        """
        update works with happy path
        """

        test_name = "bob"
        resources = "sally"
        tag = self.klass(*self.instantiate_args)
        tag.attach(test_name, resources)
        test_uri = "{}/{}/resources".format(self.test_uri, test_name)

        mock_request.assert_called_with(
            test_uri, request_method='POST', attribs={'resources': resources}
        )

    @patch('doboto.Tag.Tag.request')
    def test_detach_happy(self, mock_request):
        """
        update works with happy path
        """

        test_name = "bob"
        resources = "sally"
        tag = self.klass(*self.instantiate_args)
        tag.detach(test_name, resources)
        test_uri = "{}/{}/resources".format(self.test_uri, test_name)

        mock_request.assert_called_with(
            test_uri,  request_method='DELETE', attribs={'resources': resources}
        )
