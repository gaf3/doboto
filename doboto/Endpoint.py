"""This holds the Endpoint class."""

import requests
import json


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

    def make_request(
        self,
        request_url,
        request_method='GET',
        attribs=None,
        params=None
    ):
        """Make request to DO API."""
        headers = {'Authorization': "Bearer %s" % self.token,
                   'Content-Type': 'application/json'}

        requests_method = getattr(requests, request_method.lower())
        # TODO: Throw meaningful exception if not found

        resp = requests_method(
            request_url,
            params=params,
            data=json.dumps(attribs),
            headers=headers,
            timeout=60
        )
        return self.process_response(resp)
