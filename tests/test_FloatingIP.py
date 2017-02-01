"""
This module contains tests for the FloatingIP class
"""

from unittest import TestCase
from mock import MagicMock, patch
from doboto import FloatingIP


class TestFloatingIP(TestCase):
    """
    This class implements unittests for the FloatingIP class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/floating_ips".format(self.test_url)
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

        self.klass_name = "FloatingIP"
        self.klass = getattr(FloatingIP, self.klass_name)

    def test_class_exists(self):
        """
        FloatingIP class is defined
        """

        self.assertTrue(hasattr(FloatingIP, self.klass_name))

    def test_can_instantiate(self):
        """
        FloatingIP class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.FloatingIP.FloatingIP.make_request')
    def test_create_happy(self, mock_make_request):
        """
        create works with happy path
        """

        droplet_id = 1234
        floating_ip = self.klass(self.test_url, self.test_token)
        floating_ip.create(droplet_id=droplet_id)

        mock_make_request.assert_called_with(self.test_uri, 'POST', {'droplet_id': droplet_id})

        region = 'nyc2'
        floating_ip.create(region=region)

        mock_make_request.assert_called_with(self.test_uri, 'POST', {'region': region})

        with self.assertRaises(ValueError):
            floating_ip.create()

    @patch('doboto.FloatingIP.FloatingIP.make_request')
    def test_list(self, mock_make_request):
        """
        list works with nuttin
        """

        mock_ret = [{
            "ip": "1.2.3.4",
            "region": "nyc2",
            "droplet_id": 1234
        }]

        mock_make_request.return_value = mock_ret
        floating_ip = self.klass(self.test_url, self.test_token)
        result = floating_ip.list()

        self.assertEqual(result, mock_ret)

        mock_make_request.assert_called_with(self.test_uri)

    @patch('doboto.FloatingIP.FloatingIP.make_request')
    def test_info(self, mock_make_request):
        """
        info works with name
        """

        mock_ret = {
            "ip": "1.2.3.4",
            "region": "nyc2",
            "droplet_id": 1234
        }

        mock_make_request.return_value = mock_ret
        ip = "1.2.3.4"
        floating_ip = self.klass(self.test_url, self.test_token)
        result = floating_ip.info(ip)

        self.assertEqual(result, mock_ret)

        test_uri = "{}/{}".format(self.test_uri, ip)
        mock_make_request.assert_called_with(test_uri)

    @patch('doboto.FloatingIP.FloatingIP.make_request')
    def test_destroy(self, mock_make_request):
        """
        info works with name
        """

        ip = "1.2.3.4"
        floating_ip = self.klass(self.test_url, self.test_token)
        result = floating_ip.destroy(ip)

        test_uri = "{}/{}".format(self.test_uri, ip)
        mock_make_request.assert_called_with(test_uri, 'DELETE')

    @patch('doboto.FloatingIP.FloatingIP.make_request')
    def test_assign(self, mock_make_request):
        """
        assign works with happy path
        """

        ip = "1.2.3.4"
        droplet_id = 1234
        floating_ip = self.klass(self.test_url, self.test_token)
        floating_ip.assign(ip, droplet_id)
        test_uri = "{}/{}/actions".format(self.test_uri, ip)
        attribs = {
            'type': 'assign',
            'droplet_id': droplet_id,
        }

        mock_make_request.assert_called_with(test_uri, 'POST', attribs)

    @patch('doboto.FloatingIP.FloatingIP.make_request')
    def test_unassign(self, mock_make_request):
        """
        unassign works with happy path
        """

        ip = "1.2.3.4"
        floating_ip = self.klass(self.test_url, self.test_token)
        floating_ip.unassign(ip)
        test_uri = "{}/{}/actions".format(self.test_uri, ip)
        attribs = {
            'type': 'unassign'
        }

        mock_make_request.assert_called_with(test_uri, 'POST', attribs)

    @patch('doboto.FloatingIP.FloatingIP.make_request')
    def test_actions(self, mock_make_request):
        """
        list the actions of a floating ip
        """

        mock_ret = {
            "actions": [],
            "links": {},
            "meta": {
                "total": 0
            }
        }

        mock_make_request.return_value = mock_ret
        ip = "1.2.3.4"
        floating_ip = self.klass(self.test_url, self.test_token)
        result = floating_ip.actions(ip)

        self.assertEqual(result, mock_ret)

        mock_make_request.assert_called_with(
            "%s/%s/actions" % (self.test_uri, ip)
        )

    @patch('doboto.FloatingIP.FloatingIP.make_request')
    def test_action_info(self, mock_make_request):
        """
        action_info works with ip
        """

        ip = "1.2.3.4"
        action_id = 54321
        floating_ip = self.klass(self.test_url, self.test_token)
        floating_ip.action_info(ip, action_id)
        test_uri = "{}/{}/actions/{}".format(
            self.test_uri, ip, action_id)

        mock_make_request.assert_called_with(test_uri)
