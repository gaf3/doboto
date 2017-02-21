"""
This holds the Tag class.
"""

from .Endpoint import Endpoint


class Tag(Endpoint):
    """
    description:

        A Tag is a label that can be applied to a resource (currently only Droplets) in order to
        better organize or facilitate the lookups and actions on it.

        Tags have two attributes, a user defined name attribute and an embedded resources attribute
        with information about resources that have been taggedself.

    related: https://developers.digitalocean.com/documentation/v2/#tags
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for tag interaction.
        """
        super(Tag, self).__init__(token, agent)
        self.do = do
        self.uri = "{}/tags".format(url)

    def list(self):
        """
        description: List all tags

            Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is
            droplet id.

        out:
            A list of Tag dict's:
                - name - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.
                - resources - list - An list of Resource dict's:
                    - resource_id - string - The identifier of a resource
                    - resource_type - string - The type of the resource

        related: https://developers.digitalocean.com/documentation/v2/#list-all-tags
        """  # nopep8
        return self.pages(self.uri, "tags")

    def name_list(self):
        """
        description: List all tag names

        out: A list of Tag names

        related: https://developers.digitalocean.com/documentation/v2/#list-all-tags
        """  # nopep8
        tags = self.pages(self.uri, "tags")

        return [_['name'] for _ in tags]

    def create(self, name):
        """
        description: Create a new Tag

            Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is
            droplet id.

        in:
            - name - string - name of the Tag

        out:
            A Tag dict:
                - name - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.
                - resources - list - An list of Resource dict's:
                    - resource_id - string - The identifier of a resource
                    - resource_type - string - The type of the resource

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-tag
        """  # nopep8
        attribs = {'name': name}

        return self.request(self.uri, "tag", 'POST', attribs)

    def present(self, name):
        """
        description: Create a new Tag if not already present

            Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is
            droplet id.

        in:
            - name - string - name of the Tag

        out:
            A tuple of Tag dict's, the intended and created (None if already exists):
                - name - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.
                - resources - list - An list of Resource dict's:
                    - resource_id - string - The identifier of a resource
                    - resource_type - string - The type of the resource

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-tag
        """  # nopep8

        tags = self.list()

        existing = None
        for tag in tags:
            if name == tag["name"]:
                existing = tag
                break

        if existing is not None:
            return (existing, None)

        created = self.create(name)
        return (created, created)

    def info(self, name):
        """
        description: Retrieve a Tag

            Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is
            droplet id.

        in:
            - name - string - name of the Tag

        out:
            A Tag dict:
                - name - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.
                - resources - list - An list of Resource dict's:
                    - resource_id - string - The identifier of a resource
                    - resource_type - string - The type of the resource

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-a-tag
        """  # nopep8
        uri = "%s/%s" % (self.uri, name)
        return self.request(uri, "tag")

    def update(self, name, new_name):
        """
        description: Update a Tag

            Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is
            droplet id.

        in:
            - name - string - name of the Tag currently
            - new_name - string - desired name of the Tag

        out:
            A Tag dict:
                - name - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.
                - resources - list - An list of Resource dict's:
                    - resource_id - string - The identifier of a resource
                    - resource_type - string - The type of the resource

        related: https://developers.digitalocean.com/documentation/v2/#update-a-tag
        """  # nopep8
        uri = "{}/{}".format(self.uri, name)
        attribs = {'name': new_name}

        return self.request(uri, "tag", 'PUT', attribs)

    def destroy(self, name):
        """
        description: Delete a Tag

        in:
            - name - string - name of the Tag

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#delete-a-tag
        """  # nopep8
        uri = "{}/{}".format(self.uri, name)

        return self.request(uri, request_method='DELETE')

    def attach(self, name, resources):
        """
        description: Tag a Resorce

            Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is
            droplet id.

        in:
            - name - string - name of the Tag
            - resources - list - An list of Resource dict's:
                - resource_id - string - The identifier of a resource
                - resource_type - string - The type of the resource

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#tag-a-resource
        """  # nopep8
        uri = "{}/{}/resources".format(self.uri, name)
        attribs = {'resources': resources}

        return self.request(uri, request_method='POST', attribs=attribs)

    def detach(self, name, resources):
        """
        description: Untag a Resource

            Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is
            droplet id.

        in:
            - name - string - name of the Tag
            - resources - list - An list of Resource dict's:
                - resource_id - string - The identifier of a resource
                - resource_type - string - The type of the resource

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#untag-a-resource
        """  # nopep8
        uri = "{}/{}/resources".format(self.uri, name)
        attribs = {'resources': resources}

        return self.request(uri, request_method='DELETE', attribs=attribs)
