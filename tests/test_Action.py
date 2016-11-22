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

    @patch('doboto.Action.Action.make_request')
    def test_list(self, mock_make_request):
        """
        list works with happy path
        """

        mock_ret = {
            "actions": [
                {
                    "id": 36804636,
                    "status": "completed",
                    "type": "create",
                    "started_at": "2014-11-14T16:29:21Z",
                    "completed_at": "2014-11-14T16:30:06Z",
                    "resource_id": 3164444,
                    "resource_type": "droplet",
                    "region": "nyc3",
                    "region_slug": "nyc3"
                }
            ],
            "links": {
                "pages": {
                    "last": "https://api.digitalocean.com/v2/actions?page=159&per_page=1",
                    "next": "https://api.digitalocean.com/v2/actions?page=2&per_page=1"
                }
            },
            "meta": {
                "total": 159
            }
        }

        mock_make_request.return_value = mock_ret
        action = self.klass(self.test_uri, self.test_token)
        result = action.list()

        self.assertEqual(result, mock_ret)
