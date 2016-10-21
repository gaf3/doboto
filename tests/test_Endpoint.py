"""
This module contains tests for the base Endpoint class
"""

from unittest import TestCase
from doboto import Endpoint


class TestEndpoint(TestCase):
    """
    This class implements unittests for the base Endpoint class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com/"
        self.test_token = "abc123"
        self.instantiate_args = (self.test_token,)

        self.klass_name = "Endpoint"
        self.klass = getattr(Endpoint, self.klass_name)
        self.klass_attrs = ('ssh_key')

    def test_class_exists(self):
        """
        Endpoint class is defined
        """

        self.assertTrue(hasattr(Endpoint, self.klass_name))

    def test_can_instantiate(self):
        """
        Endpoint class can be instantiated
        """

        self.klass(*self.instantiate_args)

    def test_process_response(self):
        """
        Endpoint process response can properly do the response
        """

        endpoint = self.klass(*self.instantiate_args)

        class FakeResponse():

            def json(self):
                return {}

        response = FakeResponse()

        response.status_code = 202
        self.assertEqual(endpoint.process_response(response), {})

        response.status_code = 204
        self.assertEqual(endpoint.process_response(response), {'status': 204})
