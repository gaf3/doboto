"""
This module contains tests for the main LoadBalancer class
"""

from unittest import TestCase
from mock import MagicMock, patch, call
from doboto import LoadBalancer
from doboto.exception import DOBOTOException, DOBOTOPollingException


class TestLoadBalancer(TestCase):

    """
    This class implements unittests for the main DO class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com"
        self.test_uri = "{}/load_balancers".format(self.test_url)
        self.test_do = "do"
        self.test_token = "abc123"
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_do, self.test_token, self.test_url, self.test_agent)

        self.klass_name = "LoadBalancer"
        self.klass = getattr(LoadBalancer, self.klass_name)

    def test_class_exists(self):
        """
        LoadBalancer class is defined
        """

        self.assertTrue(hasattr(LoadBalancer, self.klass_name))

    def test_can_instantiate(self):
        """
        LoadBalancer class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    @patch('doboto.LoadBalancer.LoadBalancer.pages')
    def test_list(self, mock_pages):
        """
        test list method
        """

        load_balancer = self.klass(*self.instantiate_args)
        load_balancer.list()
        test_uri = "{}".format(self.test_uri)

        mock_pages.assert_called_with(test_uri, "load_balancers")

    @patch('time.sleep')
    @patch('doboto.LoadBalancer.LoadBalancer.request')
    def test_create(self, mock_request, mock_sleep):
        """
        test create method
        """
        load_balancer = self.klass(*self.instantiate_args)
        datas = {"name": "test-loadbalancer.com"}
        load_balancer.create(datas)
        test_uri = "{}".format(self.test_uri)

        mock_request.assert_called_with(test_uri, "load_balancer", 'POST', attribs=datas)

        load_balancer = self.klass(*self.instantiate_args)

        # Standard

        mock_request.return_value = {"id": 1, "people": "stuff", "ip": ""}

        datas = {"name": "test.com", "region": "nyc3"}
        self.assertEqual(load_balancer.create(datas), {"id": 1, "people": "stuff", "ip": ""})

        mock_request.assert_called_with(self.test_uri, "load_balancer", 'POST', attribs=datas)

        # Wait

        load_balancer.info = MagicMock(side_effect=[
            Exception("Not yet"), {"stuff": "things", "ip": "1"}
        ])

        self.assertEqual(
            load_balancer.create(datas, wait=True, poll=2),
            {"stuff": "things", "ip": "1"}
        )

        mock_sleep.assert_has_calls([call(2), call(2)])
        load_balancer.info.assert_has_calls([call(1), call(1)])

        # Wait with bad poll

        load_balancer.info.side_effect = [Exception("Not yet"), {"stuff": "things", "ip": "1"}]

        self.assertEqual(
            load_balancer.create(datas, wait=True, poll=0),
            {"stuff": "things", "ip": "1"}
        )

        mock_sleep.assert_has_calls([call(1), call(1)])

        # Wait with timeout and error

        mock_request.return_value = {"id": 2, "people": "stuff", "ip": ""}
        load_balancer.info.side_effect = [Exception("Not yet")]

        self.assertRaisesRegexp(
            DOBOTOPollingException,
            "DO API Timeout: Not yet while polling:.*stuff",
            load_balancer.create, datas, wait=True, poll=4, timeout=-1
        )

        # Wait with timeout

        load_balancer.info.side_effect = [{"stuff": "things", "ip": ""}]

        self.assertRaisesRegexp(
            DOBOTOPollingException,
            "DO API Timeout while polling:.*stuff",
            load_balancer.create, datas, wait=True, poll=4, timeout=-1
        )

    def test_present(self):
        """
        test present method
        """
        load_balancer = self.klass(*self.instantiate_args)

        load_balancer.list = MagicMock(return_value=[{"name": "people"}])
        load_balancer.create = MagicMock(return_value={"name": "things"})

        self.assertEqual(
            load_balancer.present({"name": "people"}),
            (
                {"name": "people"},
                None
            )
        )

        self.assertEqual(
            load_balancer.present({"name": "stuff"}),
            (
                 {"name": "things"},
                 {"name": "things"}
            )
        )
        load_balancer.create.assert_has_calls([
            call({"name": "stuff"}, False, 5, 300),
        ])

        self.assertRaisesRegexp(
            ValueError,
            "name must be specified",
            load_balancer.present, {}
        )

    @patch('doboto.LoadBalancer.LoadBalancer.request')
    def test_info(self, mock_request):
        """
        test info method
        """
        id = 1234
        load_balancer = self.klass(*self.instantiate_args)
        load_balancer.info(id)
        test_uri = "{}/{}".format(self.test_uri, id)

        mock_request.assert_called_with(test_uri, "load_balancer")

    @patch('doboto.LoadBalancer.LoadBalancer.request')
    def test_update(self, mock_request):
        """
        test update method
        """
        id = 1234
        datas = {"name": "test-loadbalancer.com"}
        load_balancer = self.klass(*self.instantiate_args)
        load_balancer.update(id, datas)
        test_uri = "{}/{}".format(self.test_uri, id)

        mock_request.assert_called_with(test_uri, "load_balancer", 'PUT', attribs=datas)

    @patch('doboto.LoadBalancer.LoadBalancer.request')
    def test_destroy(self, mock_request):
        """
        test destroy method
        """
        id = 1234
        load_balancer = self.klass(*self.instantiate_args)
        load_balancer.destroy(id)
        test_uri = "{}/{}".format(self.test_uri, id)

        mock_request.assert_called_with(test_uri, request_method='DELETE')

    @patch('doboto.LoadBalancer.LoadBalancer.request')
    def test_droplet_add(self, mock_request):
        """
        test droplet_add method
        """
        id = 1234
        droplet_ids = [5, 6, 7]
        load_balancer = self.klass(*self.instantiate_args)
        load_balancer.droplet_add(id, droplet_ids)
        test_uri = "{}/{}/droplets".format(self.test_uri, id)

        mock_request.assert_called_with(
            test_uri, request_method='POST', attribs={"droplet_ids": droplet_ids}
        )

    @patch('doboto.LoadBalancer.LoadBalancer.request')
    def test_droplet_remove(self, mock_request):
        """
        test droplet_remove method
        """
        id = 1234
        droplet_ids = [5, 6, 7]
        load_balancer = self.klass(*self.instantiate_args)
        load_balancer.droplet_remove(id, droplet_ids)
        test_uri = "{}/{}/droplets".format(self.test_uri, id)

        mock_request.assert_called_with(
            test_uri, request_method='DELETE', attribs={"droplet_ids": droplet_ids}
        )

    @patch('doboto.LoadBalancer.LoadBalancer.request')
    def test_forwarding_rule_add(self, mock_request):
        """
        test forwarding_rule_add method
        """
        id = 1234
        forwarding_rules = [5, 6, 7]
        load_balancer = self.klass(*self.instantiate_args)
        load_balancer.forwarding_rule_add(id, forwarding_rules)
        test_uri = "{}/{}/forwarding_rules".format(self.test_uri, id)

        mock_request.assert_called_with(
            test_uri, request_method='POST', attribs={"forwarding_rules": forwarding_rules}
        )

    @patch('doboto.LoadBalancer.LoadBalancer.request')
    def test_forwarding_rule_remove(self, mock_request):
        """
        test forwarding_rule_add method
        """
        id = 1234
        forwarding_rules = [5, 6, 7]
        load_balancer = self.klass(*self.instantiate_args)
        load_balancer.forwarding_rule_remove(id, forwarding_rules)
        test_uri = "{}/{}/forwarding_rules".format(self.test_uri, id)

        mock_request.assert_called_with(
            test_uri, request_method='DELETE', attribs={"forwarding_rules": forwarding_rules}
        )
