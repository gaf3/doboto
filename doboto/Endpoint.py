"""This holds the Endpoint class."""

import json
import requests
from six import wraps


def paginate(func):
    """
    paginate wrapper function - adapted from github.com/Wiredcraft/dopy
    """

    @wraps(func)
    def wrapper(self, request_url, request_method='GET', attribs=None, params=None):
        """wrapper function"""
        if request_method != 'GET':
            return func(self, request_url, request_method, attribs, params)

        nxt = request_url
        out = {}

        while nxt is not None:
            result = func(self, nxt, 'GET', attribs, params)
            nxt = None

            if isinstance(result, dict):
                for key, value in result.items():
                    if key in out and isinstance(out[key], list):
                        out[key].extend(value)
                    else:
                        out[key] = value

                if 'links' in result \
                        and 'pages' in result['links'] \
                        and 'next' in result['links']['pages']:
                    nxt = result['links']['pages']['next']

        return out
    return wrapper


class Endpoint(object):

    """Base class for interacting with an endpoint of the DO API."""

    def __init__(self, token):
        """Take token and sets its token for API authorization."""
        self.token = token

    def process_response(self, response):
        """Process response."""
        if response.status_code == 204:
            return {'status': response.status_code}
        else:
            return response.json()

    @paginate
    def make_request(self, request_url, request_method='GET', attribs=None, params=None):
        """Make request to DO API."""
        headers = {'Authorization': "Bearer %s" % self.token,
                   'Content-Type': 'application/json'}

        requests_method = getattr(requests, request_method.lower())

        resp = requests_method(
            request_url, params=params, data=json.dumps(attribs), headers=headers, timeout=60
        )

        print resp

        return self.process_response(resp)
