"""
This module contains tests for the Action class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import Action


class TestAction(TestCase):
    """
    This class implements unittests for the Action class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/actions".format(self.test_url)
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

        self.klass_name = "Action"
        self.klass = getattr(Action, self.klass_name)

    def test_class_exists(self):
        """
        Action class is defined
        """

        self.assertTrue(hasattr(Action, self.klass_name))

    def test_can_instantiate(self):
        """
        Action class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.Action.Action.pages')
    def test_list(self, mock_pages):
        """
        list works with happy path
        """

        action = self.klass(self.test_url, self.test_token)
        result = action.list()

        mock_pages.assert_called_with(self.test_uri, "actions")

    @patch('doboto.Action.Action.request')
    def test_info(self, mock_request):
        """
        info works with action id
        """

        id = 12345
        action = self.klass(self.test_url, self.test_token)
        result = action.info(id)

        test_uri = "{}/{}".format(self.test_uri, id)
        mock_request.assert_called_with(test_uri, "action")
