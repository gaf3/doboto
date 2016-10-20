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

    def make_request(self, request_url, request_method='GET', attribs=None):
        """Make request to DO API."""
        headers = {'Authorization': "Bearer %s" % self.token,
                   'Content-Type': 'application/json'}

        if request_method == 'POST':
            resp = requests.post(request_url,
                                 data=json.dumps(attribs),
                                 headers=headers,
                                 timeout=60)
            json_response = self.process_response(resp)
        elif request_method == 'DELETE':
            resp = requests.delete(request_url,
                                   data=json.dumps(attribs),
                                   headers=headers,
                                   timeout=60)
            json_response = self.process_response(resp)
        elif request_method == 'PUT':
            resp = requests.put(request_url,
                                headers=headers,
                                params=attribs,
                                timeout=60)
            json_response = resp.json()
        elif request_method == 'GET':
            resp = requests.get(request_url,
                                headers=headers,
                                params=attribs,
                                timeout=60)
            print resp
            json_response = resp.json()

        return json_response
