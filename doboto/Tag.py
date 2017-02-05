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

    def list(self):
        """
        List all tags
        """

        return self.pages(self.uri, "tags")

    def name_list(self):
        """
        This call will provide a list of all tag names
        """

        tags = self.pages(self.uri, "tags")

        return [_['name'] for _ in tags]

    def create(self, name):
        """
        Create a new tag
        """
        attribs = {'name': name}

        return self.request(self.uri, "tag", 'POST', attribs)

    def info(self, name):
        """
        Retrieve a tag
        """

        uri = "%s/%s" % (self.uri, name)
        return self.request(uri, "tag")

    def update(self, name, new_name):
        """
        This call provides a way to rename an existing tag
        """

        uri = "{}/{}".format(self.uri, name)
        attribs = {'name': new_name}

        return self.request(uri, "tag", 'PUT', attribs)

    def destroy(self, name):
        """
        Removes a named tag from all resources it is associated with, and
        deletes the tag itself
        """

        uri = "{}/{}".format(self.uri, name)

        return self.request(uri, request_method='DELETE')

    def attach(self, name, resources):
        """
        This call provides a way to attach resources to a tag
        """

        uri = "{}/{}/resources".format(self.uri, name)
        attribs = {'resources': resources}

        return self.request(uri, request_method='POST', attribs=attribs)

    def detach(self, name, resources):
        """
        This call provides a way to detach resources to a tag
        """

        uri = "{}/{}/resources".format(self.uri, name)
        attribs = {'resources': resources}

        return self.request(uri, request_method='DELETE', attribs=attribs)
