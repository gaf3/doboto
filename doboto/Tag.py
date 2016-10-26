"""
This holds the Tag class.
"""

from .Endpoint import Endpoint


class Tag(Endpoint):
    """
    Class for interacting with tags.
    """

    def __init__(self, url, token):
        """
        Take token and sets its URI for tag interaction.
        """
        super(Tag, self).__init__(token)
        self.uri = "{}/tags".format(url)

    def create(self, name):
        """
        Create a new tag
        """
        attribs = {'name': name}

        return self.make_request(self.uri, 'POST', attribs)

    def destroy(self, name):
        """
        Removes a named tag from all resources it is associated with, and
        deletes the tag itself
        """

        uri = "{}/{}".format(self.uri, name)

        return self.make_request(uri, 'DELETE')

    def rename(self, name, new_name):
        """
        This call provides a way to rename an existing tag
        """

        uri = "{}/{}".format(self.uri, name)
        attribs = {'name': new_name}

        return self.make_request(uri, 'PUT', attribs)

    def list(self):
        """
        This call will provide a list of all tag names
        """

        result = self.make_request(self.uri, 'GET')

        if 'tags' in result:
            ret_val = [_['name'] for _ in result['tags']]
        else:
            ret_val = result

        return ret_val
