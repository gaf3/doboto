"""This holds the Image class."""

from .Endpoint import Endpoint


class Image(Endpoint):

    """Class for interacting with images."""

    def __init__(self, url, token):
        """Take token and sets its URI for image interaction."""
        super(Image, self).__init__(token)
        self.uri = "%s/images" % url

    def info(self, image_id):
        """Retrieve image information"""
        uri = self.uri + "/%s" % image_id

        return self.make_request(uri)

    def list(self, kind=None, private=None):
        """list all images"""

        params = {}

        if kind is not None:
            params["type"] = kind

        if private is not None:
            params["private"] = private

        return self.make_request(self.uri, params=params)

    def list_actions(self, image_id_slug):
        """Retrieve image actions information"""
        uri = self.uri + "/%s/actions" % image_id_slug

        return self.make_request(uri)

    def update(self, image_id, name):
        """Updates an image's name"""
        uri = self.uri + "/%s" % image_id

        return self.make_request(uri, request_method="PUT", attribs={"name": name})

    def destroy(self, image_id):
        """Destroy image"""
        uri = self.uri + "/%s" % image_id

        return self.make_request(uri, request_method="DELETE")
