"""
This module contains tests for the Endpoint class
"""

from unittest import TestCase
from mock import Mock, MagicMock, patch
from doboto import Endpoint
from doboto.Endpoint import paginate

import requests


class TestEndpoint(TestCase):
    """
    This class implements unittests for the Endpoint class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_token = "abc123"
        self.instantiate_args = (self.test_token, )

        self.klass_name = "Endpoint"
        self.klass = getattr(Endpoint, self.klass_name)

    def test_paginate(self):
        """
        Verify pagination processes repsonse and forwards requests
        """

        fake_requests = []
        fake_responses = [
            {
                "a": 1,
                "b": [2, 3, 4],
                "c": {
                    "d": 5,
                    "e": 6
                },
                "f": 7,
                "links": {
                    "pages": {
                        "next": "things"
                    }
                }
            },
            {
                "b": [5, 6],
                "c": {
                    "d": 8
                },
                "f": 9,
                "links": {
                    "pages": {
                        "next": "things"
                    }
                }
            },
            {
                "links": {
                    "pages": {
                    }
                }
            },
            []
        ]

        @paginate
        def fake_request(self, request_url, request_method='GET', attribs=None, params=None):

            if request_method == "SELF":
                return {
                    "self": self,
                    "request_url": request_url,
                    "request_method": request_method,
                    "attribs": attribs,
                    "params": params
                }

            fake_requests.append(
                {
                    "request_url": request_url,
                    "attribs": attribs,
                    "params": params
                }
            )

            return fake_responses.pop(0)

        # Make sure no url returns a dict

        result = fake_request(self, None)
        self.assertEqual(result, {})

        # Method other than GET is untouched

        result = fake_request(
            self, request_url="people", request_method="SELF", attribs=1, params=2
        )
        self.assertEqual(
            result,
            {
                "self": self,
                "request_url": "people",
                "request_method": "SELF",
                "attribs": 1,
                "params": 2
            }
        )

        # Call so it cycles

        result = fake_request(
            self, request_url="stuff", request_method="GET", attribs=10, params=11
        )
        self.assertEqual(
            result,
            {
                "a": 1,
                "b": [2, 3, 4, 5, 6],
                "c": {
                    "d": 8
                },
                "f": 9,
                "links": {
                    "pages": {
                    }
                }
            }
        )
        self.assertEqual(fake_requests, [
            {
                "request_url": "stuff",
                "attribs": 10,
                "params": 11
            },
            {
                "request_url": "things",
                "attribs": 10,
                "params": 11
            },
            {
                "request_url": "things",
                "attribs": 10,
                "params": 11
            }
        ])

        result = fake_request(
            self, request_url="stuff", request_method="GET", attribs=10, params=11
        )
        self.assertEqual(result, {})

    def test_class_exists(self):
        """
        Endpoint class is defined
        """

        self.assertTrue(hasattr(Endpoint, self.klass_name))

    def test_can_instantiate(self):
        """
        Endpoint class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)

    def test_process_response(self):
        """
        Responses return status if 204, else pass through
        """

        response = MagicMock()
        response.status_code = 200
        response.json = MagicMock(return_value={"a": 1})

        endpoint = self.klass(*self.instantiate_args)
        self.assertEqual(endpoint.process_response(response), {"a": 1})

        response.status_code = 204
        self.assertEqual(endpoint.process_response(response), {"status": 204})

    @patch('requests.get')
    def test_make_request(self, mock_get):

        endpoint = self.klass(*self.instantiate_args)
        response = MagicMock()
        response.status_code = 200
        response.json = MagicMock(return_value={"a": 1})
        mock_get.return_value = response

        response = endpoint.make_request(request_url="people", attribs={"b": 2}, params={"c": 2})

        mock_get.assert_called_with(
            "people",
            params={"c": 2},
            data='{"b": 2}',
            headers={
                'Authorization': "Bearer %s" % self.test_token,
                'Content-Type': 'application/json'
            },
            timeout=60
        )
