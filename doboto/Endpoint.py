"""This holds the Endpoint class."""

import json
import requests
from six import wraps
from .DOBOTOException import DOBOTOException

class Endpoint(object):

    """Base class for interacting with an endpoint of the DO API."""

    def __init__(self, token, agent):
        """Take token and sets its token for API authorization and agent for tracking."""
        self.token = token
        self.agent = agent

    def headers(self):
        """ Headers to use on API calls """

        return {
            'Authorization': "Bearer %s" % self.token,
            'User-Agent': self.agent,
            'Content-Type': 'application/json'
        }

    def request(self, request_url, expect=None, request_method='GET', attribs=None, params=None):
        """ Single API Call """

        headers = self.headers()

        requests_method = getattr(requests, request_method.lower())

        response = requests_method(
            request_url, params=params, data=json.dumps(attribs), headers=headers, timeout=60
        )

        if expect is None:

            if response.status_code != 204:
                raise DOBOTOException(result=response.json())

        else:

            result = response.json()

            if expect not in result:
                raise DOBOTOException(result=response.json())

            return result[expect]

    def pages(self, request_url, expect, params=None):
        """ Paged API Calls """

        if params is None:
            params = {}

        next_url = request_url
        headers = self.headers()
        params["per_page"] = 200
        items = []

        while next_url:

            result = requests.get(next_url, params=params, headers=headers, timeout=60).json()

            if expect not in result:
                raise DOBOTOException(result=result)

            items.extend(result[expect])

            if 'links' in result and \
               'pages' in result['links'] and \
               'next' in result['links']['pages']:

                next_url = result['links']['pages']['next']
                params = None

            else:

                next_url = None

        return items
