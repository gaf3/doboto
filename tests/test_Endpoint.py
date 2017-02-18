"""
This module contains tests for the Endpoint class
"""

from unittest import TestCase
from mock import Mock, MagicMock, patch, call
from doboto import Endpoint
from doboto.exception import DOBOTOException, DOBOTONotFoundException, DOBOTOPollingException

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
        self.test_agent = "Unit"
        self.instantiate_args = (self.test_token, self.test_agent)

        self.klass_name = "Endpoint"
        self.klass = getattr(Endpoint, self.klass_name)

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

    def test_headers(self):

        endpoint = self.klass(*self.instantiate_args)

        self.assertEqual(
            endpoint.headers(),
            {
                'Authorization': "Bearer %s" % self.test_token,
                'User-Agent': self.test_agent,
                'Content-Type': 'application/json'
            }
        )

    @patch('requests.get')
    def test_request(self, mock_get):

        endpoint = self.klass(*self.instantiate_args)
        response = MagicMock()
        response.status_code = 200
        response.json = MagicMock(return_value={"people": {"a": 1}})
        mock_get.return_value = response

        result = endpoint.request("people", "people", attribs={"b": 2}, params={"c": 2})
        self.assertEqual(result, {"a": 1})

        mock_get.assert_called_with(
            "people",
            params={"c": 2},
            data='{"b": 2}',
            headers={
                'Authorization': "Bearer %s" % self.test_token,
                'User-Agent': self.test_agent,
                'Content-Type': 'application/json'
            },
            timeout=60
        )

        self.assertRaises(
            DOBOTOException, endpoint.request, "people", "stuff"
        )

        response = MagicMock()
        response.status_code = 204
        mock_get.return_value = response
        result = endpoint.request("people")
        self.assertIsNone(result)

        response.status_code = 202
        self.assertRaises(DOBOTOException, endpoint.request, "people")

        endpoint = self.klass(*self.instantiate_args)
        response = MagicMock()
        response.status_code = 200
        response.json = MagicMock(return_value={"id": "not_found"})
        mock_get.return_value = response

        self.assertRaises(
            DOBOTONotFoundException, endpoint.request, "people", "stuff"
        )

    @patch('requests.get')
    def test_pages(self, mock_get):

        fake_requests = []
        fake_responses = [
            MagicMock(),
            MagicMock(),
            MagicMock()
        ]

        fake_responses[0].json = MagicMock(return_value={
            "people": [1, 2, 3],
            "links": {
                "pages": {
                    "next": "stuff"
                }
            }
        })

        fake_responses[1].json = MagicMock(return_value={
            "people": [4, 5, 6],
            "links": {
                "pages": {
                    "next": "things"
                }
            }
        })

        fake_responses[2].json = MagicMock(return_value={
            "people": [],
            "links": {
                "pages": {
                }
            }
        })

        def fake_get(*args, **kwargs):

            fake_requests.append({
                "url": args[0],
                "params": kwargs["params"]
            })
            return fake_responses.pop(0)

        mock_get.side_effect = fake_get

        endpoint = self.klass(*self.instantiate_args)
        response = MagicMock()
        mock_get.return_value = response

        result = endpoint.pages("people", "people", params={"c": 2})
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
        self.assertEqual(fake_requests, [
            {
                "url": "people",
                "params": {"c": 2, 'per_page': 200}
            },
            {
                "url": "stuff",
                "params": None
            },
            {
                "url": "things",
                "params": None
            }
        ])

        mock_get.assert_called_with(
            "things",
            params=None,
            headers={
                'Authorization': "Bearer %s" % self.test_token,
                'User-Agent': self.test_agent,
                'Content-Type': 'application/json'
            },
            timeout=60
        )

        fake_responses = [
            MagicMock()
        ]

        fake_responses[0].json = MagicMock(return_value={
            "people": [1, 2, 3],
            "links": {
                "pages": {
                    "next": "stuff"
                }
            }
        })

        self.assertRaises(
            DOBOTOException, endpoint.pages, "people", "items"
        )

    @patch('time.sleep')
    def test_action_result(self, mock_sleep):
        """
        action_result polls an action until complete
        """

        endpoint = self.klass(*self.instantiate_args)

        # Standard

        self.assertEqual(
            endpoint.action_result({"id": 1, "status": "in-progress"}, False, 2, 3),
            {"id": 1, "status": "in-progress"}
        )

        # Wait

        endpoint.do = MagicMock()
        endpoint.do.action = MagicMock()
        endpoint.do.action.info = MagicMock(
            side_effect=[Exception("Not yet"), {"id": 1, "status": "completed"}]
        )

        self.assertEqual(
            endpoint.action_result({"id": 1, "status": "in-progress"}, True, 2, 3),
            {"id": 1, "status": "completed"}
        )
        mock_sleep.assert_has_calls([call(2), call(2)])
        endpoint.do.action.info.assert_has_calls([call(1), call(1)])

        # Wait with bad poll

        endpoint.do.action.info.side_effect = [
            Exception("Not yet"), {"id": 1, "status": "completed"}
        ]

        self.assertEqual(
            endpoint.action_result({"id": 1, "status": "in-progress"}, True, 0, 3),
            {"id": 1, "status": "completed"}
        )
        mock_sleep.assert_has_calls([call(1), call(1)])

        # Wait with timeout and error

        endpoint.do.action.info.side_effect = [Exception("Not yet")]

        self.assertRaisesRegexp(
            DOBOTOPollingException,
            "DO API Timeout: Not yet while polling:.*status",
            endpoint.action_result, {"id": 1, "status": "in-progress"},
            wait=True, poll=4, timeout=-1
        )

        # Wait with timeout

        endpoint.do.action.info.side_effect = [{"id": 1, "status": "in-progress"}]

        self.assertRaisesRegexp(
            DOBOTOPollingException,
            "DO API Timeout while polling:.*status",
            endpoint.action_result, {"id": 1, "status": "in-progress"},
            wait=True, poll=4, timeout=-1
        )

    @patch('time.sleep')
    def test_actions_result(self, mock_sleep):
        """
        actions_result polls an action until complete
        """

        endpoint = self.klass(*self.instantiate_args)

        # Standard

        self.assertEqual(
            endpoint.actions_result([
                {"id": 1, "status": "completed"},
                {"id": 2, "status": "completed"}
            ], False, 2, 3),
            [
                {"id": 1, "status": "completed"},
                {"id": 2, "status": "completed"}
            ]
        )

        # Wait

        endpoint.do = MagicMock()
        endpoint.do.action = MagicMock()
        endpoint.do.action.info = MagicMock(
            side_effect=[
                Exception("Not yet"),
                Exception("Not yet"),
                {"id": 1, "status": "completed"},
                {"id": 2, "status": "completed"}
            ]
        )

        self.assertEqual(
            endpoint.actions_result([
                {"id": 1, "status": "in-progress"},
                {"id": 2, "status": "in-progress"}
            ], True, 2, 3),
            [
                {"id": 1, "status": "completed"},
                {"id": 2, "status": "completed"}
            ]
        )
        mock_sleep.assert_has_calls([call(2), call(2)])
        endpoint.do.action.info.assert_has_calls([call(1), call(2), call(1), call(2)])

        # Wait with bad poll

        endpoint.do.action.info.side_effect = [
            Exception("Not yet"),
            Exception("Not yet"),
            {"id": 1, "status": "completed"},
            {"id": 2, "status": "completed"}
        ]

        self.assertEqual(
            endpoint.actions_result([
                {"id": 1, "status": "in-progress"},
                {"id": 2, "status": "in-progress"}
            ], True, 0, 3),
            [
                {"id": 1, "status": "completed"},
                {"id": 2, "status": "completed"}
            ]
        )
        mock_sleep.assert_has_calls([call(1), call(1)])

        # Wait with timeout and error

        endpoint.do.action.info.side_effect = [Exception("Not yet")]

        self.assertRaisesRegexp(
            DOBOTOPollingException,
            "DO API Timeout: Not yet while polling:.*status",
            endpoint.actions_result, [{"id": 1, "status": "in-progress"}],
            wait=True, poll=4, timeout=-1
        )

        # Wait with timeout

        endpoint.do.action.info.side_effect = [
            {"id": 1, "status": "completed"}
        ]

        self.assertRaisesRegexp(
            DOBOTOPollingException,
            "DO API Timeout while polling:.*status",
            endpoint.actions_result, [{"id": 1, "status": "in-progress"}],
            wait=True, poll=4, timeout=-1
        )
