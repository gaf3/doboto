"""This holds the Image class."""

from .Endpoint import Endpoint


class Image(Endpoint):
    """
    description:

        Images in DigitalOcean may refer to one of a few different kinds of dict's.

        An image may refer to a snapshot that has been taken of a Droplet instance. It may also
        mean an image representing an automatic backup of a Droplet. The third category that it can
        represent is a public Linux distribution or application image that is used as a base to
        create Droplets.

    related: https://developers.digitalocean.com/documentation/v2/#images
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for floating ip interaction.
        """
        super(Image, self).__init__(token, agent)
        self.do = do
        self.uri = "%s/images" % url

    def list(self, type=None, private=None):
        """
        description: List all, distribution, application, or user images.

        in:
            - type - string - Can be "distribution" or "application" for images thereof.
            - private - boolean - Set to True for user images

        out:
            A list of Image dict's:
                - id - number - A unique number that can be used to identify and reference a specific image.
                - name - string - The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question.
                - type - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".
                - distribution - string - This attribute describes the base distribution used for this image.
                - slug - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.
                - public - boolean - This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account.
                - regions - list - This attribute is a list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - min_disk_size - number - The minimum 'disk' required for a size to use this image.
                - size_gigabytes - number - The size of the image in gigabytes.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.

        related:
            - https://developers.digitalocean.com/documentation/v2/#list-all-images
            - https://developers.digitalocean.com/documentation/v2/#list-all-distribution-images
            - https://developers.digitalocean.com/documentation/v2/#list-all-application-images
            - https://developers.digitalocean.com/documentation/v2/#list-a-user-s-images
        """  # nopep8

        params = {}

        if type is not None:
            params["type"] = type

        if private is not None:
            params["private"] = private

        return self.pages(self.uri, "images", params=params)

    def info(self, id_slug):
        """
        description: Retrieve an existing image by id or slug

        in:
            - id_slug - number / string - id or slug of the Image

        out:
            An Image dict:
                - id - number - A unique number that can be used to identify and reference a specific image.
                - name - string - The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question.
                - type - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".
                - distribution - string - This attribute describes the base distribution used for this image.
                - slug - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.
                - public - boolean - This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account.
                - regions - list - This attribute is a list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - min_disk_size - number - The minimum 'disk' required for a size to use this image.
                - size_gigabytes - number - The size of the image in gigabytes.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.

        related:
            - https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-image-by-id
            - https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-image-by-slug
        """  # nopep8
        uri = self.uri + "/%s" % id_slug

        return self.request(uri, "image")

    def update(self, id, name):
        """
        description: Update an Image

        in:
            - id - number - id of the Image
            - name - string - The new name that you would like to use for the image.

        out:
            An Image dict:
                - id - number - A unique number that can be used to identify and reference a specific image.
                - name - string - The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question.
                - type - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".
                - distribution - string - This attribute describes the base distribution used for this image.
                - slug - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.
                - public - boolean - This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account.
                - regions - list - This attribute is a list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - min_disk_size - number - The minimum 'disk' required for a size to use this image.
                - size_gigabytes - number - The size of the image in gigabytes.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.

        related: https://developers.digitalocean.com/documentation/v2/#update-an-image
        """  # nopep8
        uri = self.uri + "/%s" % id

        return self.request(uri, "image", request_method="PUT", attribs={"name": name})

    def destroy(self, id):
        """
        description: Delete an Image

        in:
            - id - number - id of the Image

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#delete-an-image
        """  # nopep8
        uri = self.uri + "/%s" % id

        return self.request(uri, request_method="DELETE")

    def transfer(self, id, region, wait=False, poll=5, timeout=300):
        """
        description: Transfer an Image to another Region

        in:
            - id - number - id of the Image
            - region - string - The region slug that represents the region target.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dictt:
                - id - number - A unique numeric ID that can be used to identify and reference an image action.
                - status - string - The current status of the image action. This will be either "in-progress", "completed", or "errored".
                - type - string - This is the type of the image action that the JSON dict represents. For example, this could be "transfer" to represent the state of an image transfer action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#transfer-an-image
        """  # nopep8
        uri = self.uri + "/%s/actions" % id

        return self.action_result(
            self.request(
                uri, "action", request_method="POST", attribs={"type": "transfer", "region": region}
            ), wait, poll, timeout
        )

    def convert(self, id, wait=False, poll=5, timeout=300):
        """
        description: Convert an Image to a Snapshot

        in:
            - id - number - id of the Image
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique numeric ID that can be used to identify and reference an image action.
                - status - string - The current status of the image action. This will be either "in-progress", "completed", or "errored".
                - type - string - This is the type of the image action that the JSON dict represents. For example, this could be "transfer" to represent the state of an image transfer action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#convert-an-image-to-a-snapshot
        """  # nopep8
        uri = self.uri + "/%s/actions" % id

        return self.action_result(
            self.request(uri, "action", request_method="POST", attribs={"type": "convert"}),
            wait, poll, timeout
        )

    def action_list(self, id):
        """
        description: List all actions for an Image

        in:
            - id - number - id of the Image

        out:
            A list of Action dict's:
                - id - number - A unique numeric ID that can be used to identify and reference an image action.
                - status - string - The current status of the image action. This will be either "in-progress", "completed", or "errored".
                - type - string - This is the type of the image action that the JSON dict represents. For example, this could be "transfer" to represent the state of an image transfer action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-actions-for-an-image
        """  # nopep8
        uri = self.uri + "/%s/actions" % id

        return self.pages(uri, "actions")

    def action_info(self, id, action_id):
        """
        description: Retrieve an existing Image Action

        in:
            - id - number - id of the Image
            - action_id - number - id of the Action

        out:
            An Action dict:
                - id - number - A unique numeric ID that can be used to identify and reference an image action.
                - status - string - The current status of the image action. This will be either "in-progress", "completed", or "errored".
                - type - string - This is the type of the image action that the JSON dict represents. For example, this could be "transfer" to represent the state of an image transfer action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-image-action
        """  # nopep8
        uri = "%s/%s/actions/%s" % (self.uri, id, action_id)
        return self.request(uri, "action")
