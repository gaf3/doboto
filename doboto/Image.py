"""This holds the Image class."""

from .Endpoint import Endpoint


class Image(Endpoint):

    """Class for interacting with images."""

    def __init__(self, url, token):
        """Take token and sets its URI for image interaction."""
        super(Image, self).__init__(token)
        self.uri = "%s/images" % url

    def list(self, type=None, private=None):
        """list images"""

        params = {}

        if type is not None:
            params["type"] = type

        if private is not None:
            params["private"] = private

        return self.pages(self.uri, "images", params=params)

    def info(self, id_slug):
        """Retrieve image information"""
        uri = self.uri + "/%s" % id_slug

        return self.request(uri, "image")

    def update(self, id, name):
        """Updates an image's name"""
        uri = self.uri + "/%s" % id

        return self.request(uri, "image", request_method="PUT", attribs={"name": name})

    def destroy(self, id):
        """Destroy image"""
        uri = self.uri + "/%s" % id

        return self.request(uri, request_method="DELETE")

    def convert(self, id):
        """Convert an image to a snapshot"""
        uri = self.uri + "/%s/actions" % id

        return self.request(uri, "action", request_method="POST", attribs={"type": "convert"})

    def transfer(self, id, region):
        """Transfer an image to a region"""
        uri = self.uri + "/%s/actions" % id

        return self.request(
            uri, "action", request_method="POST", attribs={"type": "transfer", "region": region}
        )

    def action_list(self, id):
        """Retrieve image actions information"""
        uri = self.uri + "/%s/actions" % id

        return self.pages(uri, "actions")

    def action_info(self, id, action_id):
        """
        Get the status of an image action
        """
        uri = "%s/%s/actions/%s" % (self.uri, id, action_id)
        return self.request(uri, "action")
