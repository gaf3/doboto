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
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_token, self.test_url, self.test_agent)

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

    @patch('doboto.FloatingIP.FloatingIP.pages')
    def test_list(self, mock_pages):
        """
        list works with nuttin
        """

        floating_ip = self.klass(*self.instantiate_args)
        result = floating_ip.list()

        mock_pages.assert_called_with(self.test_uri, "floating_ips")

    @patch('doboto.FloatingIP.FloatingIP.request')
    def test_create_happy(self, mock_request):
        """
        create works with happy path
        """

        droplet_id = 1234
        floating_ip = self.klass(*self.instantiate_args)
        floating_ip.create(droplet_id=droplet_id)

        mock_request.assert_called_with(
            self.test_uri, "floating_ip", 'POST', {'droplet_id': droplet_id}
        )

        region = 'nyc2'
        floating_ip.create(region=region)

        mock_request.assert_called_with(self.test_uri, "floating_ip", 'POST', {'region': region})

        with self.assertRaises(ValueError):
            floating_ip.create()

    @patch('doboto.FloatingIP.FloatingIP.request')
    def test_info(self, mock_request):
        """
        info works with ip
        """

        ip = "1.2.3.4"
        floating_ip = self.klass(*self.instantiate_args)
        result = floating_ip.info(ip)

        test_uri = "{}/{}".format(self.test_uri, ip)
        mock_request.assert_called_with(test_uri, "floating_ip")

    @patch('doboto.FloatingIP.FloatingIP.request')
    def test_destroy(self, mock_request):
        """
        info works with ip
        """

        ip = "1.2.3.4"
        floating_ip = self.klass(*self.instantiate_args)
        result = floating_ip.destroy(ip)

        test_uri = "{}/{}".format(self.test_uri, ip)
        mock_request.assert_called_with(test_uri, request_method='DELETE')

    @patch('doboto.FloatingIP.FloatingIP.request')
    def test_assign(self, mock_request):
        """
        assign works with happy path
        """

        ip = "1.2.3.4"
        droplet_id = 1234
        floating_ip = self.klass(*self.instantiate_args)
        floating_ip.assign(ip, droplet_id)
        test_uri = "{}/{}/actions".format(self.test_uri, ip)
        attribs = {
            'type': 'assign',
            'droplet_id': droplet_id,
        }

        mock_request.assert_called_with(test_uri, "action", 'POST', attribs)

    @patch('doboto.FloatingIP.FloatingIP.request')
    def test_unassign(self, mock_request):
        """
        unassign works with happy path
        """

        ip = "1.2.3.4"
        floating_ip = self.klass(*self.instantiate_args)
        floating_ip.unassign(ip)
        test_uri = "{}/{}/actions".format(self.test_uri, ip)
        attribs = {
            'type': 'unassign'
        }

        mock_request.assert_called_with(test_uri, "action", 'POST', attribs)

    @patch('doboto.FloatingIP.FloatingIP.pages')
    def test_action_list(self, mock_pages):
        """
        list the actions of a floating ip
        """

        ip = "1.2.3.4"
        floating_ip = self.klass(*self.instantiate_args)
        result = floating_ip.action_list(ip)

        mock_pages.assert_called_with(
            "%s/%s/actions" % (self.test_uri, ip), "actions"
        )

    @patch('doboto.FloatingIP.FloatingIP.request')
    def test_action_info(self, mock_request):
        """
        action_info works with ip
        """

        ip = "1.2.3.4"
        action_id = 54321
        floating_ip = self.klass(*self.instantiate_args)
        floating_ip.action_info(ip, action_id)
        test_uri = "{}/{}/actions/{}".format(
            self.test_uri, ip, action_id)

        mock_request.assert_called_with(test_uri, "action")
