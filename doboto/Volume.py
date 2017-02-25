"""This holds the Volume class."""

import time
from .Endpoint import Endpoint
from .exception import DOBOTOException, DOBOTONotFoundException, DOBOTOPollingException


class Volume(Endpoint):
    """
    description:

        Block Storage volumes provide expanded storage capacity for your Droplets and can be moved
        between Droplets within a specific region. Volumes function as raw block devices, meaning
        they appear to the operating system as locally attached storage which can be formatted
        using any file system supported by the OS. They may be created in sizes from 1GiB to 16TiB.

    related: https://developers.digitalocean.com/documentation/v2/#block-storage
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for volume interaction.
        """
        super(Volume, self).__init__(token, agent)
        self.do = do
        self.uri = "{}/volumes".format(url)

    def list(self, region=None):
        """
        description: List all volumes

        in:
            - region - string - Region slug for listing on snapshots from that region - optional

        out:
            A list of Volume dict's:
                - id - string - The unique identifier for the Block Storage volume.
                - region - dict - The region that the Block Storage volume is located in. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned.
                - droplet_ids - list - A list containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet.
                - name - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
                - description - string - An optional free-form text field to describe a Block Storage volume.
                - size_gigabytes - number - The size of the Block Storage volume in GiB (1024^3).
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Block Storage volume was created.
                - droplet_ids - list - This attribute is a list of the Droplets that the volume is attached to.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-block-storage-volumes
        """  # nopep8
        if region is not None:
            return self.pages(self.uri, "volumes", params={"region": region})
        else:
            return self.pages(self.uri, "volumes")

    def create(self, attribs, wait=False, poll=5, timeout=300):
        """
        description: Create a new volume

        in:
            - attribs - dict - Volume information to create by:
                - size_gigabytes - number - The size of the Block Storage volume in GiB (1024^3). - required
                - name - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters. - required
                - description - string - An optional free-form text field to describe a Block Storage volume. -
                - region - string - The region where the Block Storage volume will be created. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned. Should not be specified with a snapshot_id. -
                - snapshot_id - string - The unique identifier for the volume snapshot from which to create the volume. Should not be specified with a region_id. -
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            A Volume dict:
                - id - string - The unique identifier for the Block Storage volume.
                - region - dict - The region that the Block Storage volume is located in. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned.
                - droplet_ids - list - A list containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet.
                - name - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
                - description - string - An optional free-form text field to describe a Block Storage volume.
                - size_gigabytes - number - The size of the Block Storage volume in GiB (1024^3).
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Block Storage volume was created.
                - droplet_ids - list - This attribute is a list of the Droplets that the volume is attached to.

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-block-storage-volume
        """  # nopep8

        volume = self.request(self.uri, "volume", 'POST', attribs=attribs)

        if not wait:
            return volume

        if poll < 1:
            poll = 1

        start_time = time.time()

        while True:

            time.sleep(poll)

            try:
                volume = self.info(volume["id"])
                break
            except DOBOTONotFoundException as exception:
                pass
            except Exception as exception:
                if time.time() - start_time > timeout:
                    raise DOBOTOPollingException(polling=volume, error=exception)

            if time.time() - start_time > timeout:
                raise DOBOTOPollingException(polling=volume)

        return volume

    def present(self, attribs, wait=False, poll=5, timeout=300):
        """
        description: Create a new volume if name not already present

        in:
            - attribs - dict - Volume information to create by:
                - size_gigabytes - number - The size of the Block Storage volume in GiB (1024^3). - required
                - name - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters. - required
                - description - string - An optional free-form text field to describe a Block Storage volume. -
                - region - string - The region where the Block Storage volume will be created. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned. Should not be specified with a snapshot_id. -
                - snapshot_id - string - The unique identifier for the volume snapshot from which to create the volume. Should not be specified with a region_id. -
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            A tuple of Volume dict's, the intended and created (None if already exists):
                - id - string - The unique identifier for the Block Storage volume.
                - region - dict - The region that the Block Storage volume is located in. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned.
                - droplet_ids - list - A list containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet.
                - name - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
                - description - string - An optional free-form text field to describe a Block Storage volume.
                - size_gigabytes - number - The size of the Block Storage volume in GiB (1024^3).
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Block Storage volume was created.
                - droplet_ids - list - This attribute is a list of the Droplets that the volume is attached to.

        related: https://developers.digitalocean.com/documentation/v2/#create-a-new-block-storage-volume
        """  # nopep8
        volumes = self.list()

        existing = None
        for volume in volumes:
            if attribs["name"] == volume["name"]:
                existing = volume
                break

        if existing is not None:
            return (existing, None)

        created = self.create(attribs, wait, poll, timeout)
        return (created, created)

    def info(self, id=None, name=None, region=None):
        """
        description: Retrieve an existing volume by id or name and region

        in:
            - id - number - The id of the volume
            - name - string - The name of the volume if no id
            - region - string - The region slug of the volume if no id

        out:
            A Volume dict:
                - id - string - The unique identifier for the Block Storage volume.
                - region - dict - The region that the Block Storage volume is located in. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned.
                - droplet_ids - list - A list containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet.
                - name - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
                - description - string - An optional free-form text field to describe a Block Storage volume.
                - size_gigabytes - number - The size of the Block Storage volume in GiB (1024^3).
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Block Storage volume was created.
                - droplet_ids - list - This attribute is a list of the Droplets that the volume is attached to.

        related:
            - https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-block-storage-volume
            - https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-block-storage-volume-by-name
        """  # nopep8
        if id is not None:
            return self.request("{}/{}".format(self.uri, id), "volume")
        elif name is not None and region is not None:
            return self.request(self.uri, "volumes", params={"name": name, "region": region})[0]
        else:
            raise ValueError("Must supply an id or name and region")

    def destroy(self, id=None, name=None, region=None):
        """
        description: Delete a volume by id or name and region

        in:
            - id - number - The id of the volume
            - name - string - The name of the volume if no id
            - region - string - The region slug of the volume if no id

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related:
            - https://developers.digitalocean.com/documentation/v2/#delete-a-block-storage-volume
            - https://developers.digitalocean.com/documentation/v2/#delete-a-block-storage-volume-by-name
        """  # nopep8
        if id is not None:
            return self.request("{}/{}".format(self.uri, id), request_method="DELETE")
        elif name is not None and region is not None:
            return self.request(
                self.uri, request_method="DELETE", params={"name": name, "region": region}
            )
        else:
            raise ValueError("Must supply an id or name and region")

    def snapshot_list(self, id):
        """
        description: List snapshots for a volume

        in:
            - id - number - The id of the volume

        out:
            A list of Image dict's:
                - id - string - The unique identifier for the snapshot.
                - name - string - A human-readable name for the snapshot.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the snapshot was created.
                - regions - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - resource_id - string - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - min_disk_size - number - The minimum size in GB required for a volume or Droplet to use this snapshot.
                - size_gigabytes - number - The billable size of the snapshot in gigabytes.

        related: https://developers.digitalocean.com/documentation/v2/#list-snapshots-for-a-volume
        """  # nopep8
        uri = "{}/{}/snapshots".format(self.uri, id)
        return self.pages(uri, "snapshots")

    def snapshot_create(self, id, snapshot_name, wait=False, poll=5, timeout=300):
        """
        description: Create a snapshot for a volume

        in:
            - id - number - The id of the volume
            - snapshot_name - string - The name of the snapshot
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Image dict:
                - id - string - The unique identifier for the snapshot.
                - name - string - A human-readable name for the snapshot.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the snapshot was created.
                - regions - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - resource_id - string - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - min_disk_size - number - The minimum size in GB required for a volume or Droplet to use this snapshot.
                - size_gigabytes - number - The billable size of the snapshot in gigabytes.

        related: https://developers.digitalocean.com/documentation/v2/#create-snapshot-from-a-volume
        """  # nopep8

        uri = "{}/{}/snapshots".format(self.uri, id)

        attribs = {"name": snapshot_name}
        return self.request(uri, "snapshot", 'POST', attribs=attribs)

    def attach(
        self, id=None, name=None, region=None, droplet_id=None, wait=False, poll=5, timeout=300
    ):
        """
        description: Attach a volume by id or name to a droplet

        in:
            - id - number - The id of the volume
            - name - string - The name of the volume if no id
            - region - string - The region slug of the volume if no id
            - droplet_id - number - The id of the droplet
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - int - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "attach_volume" to represent the state of a volume attach action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - nullable int - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - dict - The region where the resources acted upon are located.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related:
            - https://developers.digitalocean.com/documentation/v2/#attach-a-block-storage-volume-to-a-droplet
            - https://developers.digitalocean.com/documentation/v2/#attach-a-block-storage-volume-to-a-droplet-by-name
        """  # nopep8

        attribs = {
            "type": "attach",
            "droplet_id": droplet_id
        }

        if region is not None:
            attribs["region"] = region

        if id is not None:
            return self.action_result(
                self.request(
                    "{}/{}/actions".format(self.uri, id), "action", "POST", attribs=attribs
                ),
                wait, poll, timeout
            )
        elif name is not None:
            attribs["volume_name"] = name
            return self.action_result(
                self.request(
                    "{}/actions".format(self.uri), "action", "POST", attribs=attribs
                ),
                wait, poll, timeout
            )
        else:
            raise ValueError("Must supply an id or name")

    def detach(
        self, id=None, name=None, region=None, droplet_id=None, wait=False, poll=5, timeout=300
    ):
        """
        description: Remove a volume by id or name from a droplet

        in:
            - id - number - The id of the volume
            - name - string - The name of the volume if no id
            - region - string - The region slug of the volume if no id
            - droplet_id - number - The id of the droplet
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - int - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "attach_volume" to represent the state of a volume attach action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - nullable int - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - dict - The region where the resources acted upon are located.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related:
            - https://developers.digitalocean.com/documentation/v2/#remove-a-block-storage-volume-from-a-droplet
            - https://developers.digitalocean.com/documentation/v2/#remove-a-block-storage-volume-from-a-droplet-by-name
        """  # nopep8

        attribs = {
            "type": "detach",
            "droplet_id": droplet_id
        }

        if region is not None:
            attribs["region"] = region

        if id is not None:
            return self.action_result(
                self.request(
                    "{}/{}/actions".format(self.uri, id), "action", "POST", attribs=attribs
                ),
                wait, poll, timeout
            )
        elif name is not None:
            attribs["volume_name"] = name
            return self.action_result(
                self.request(
                    "{}/actions".format(self.uri), "action", "POST", attribs=attribs
                ),
                wait, poll, timeout
            )
        else:
            raise ValueError("Must supply an id or name")

    def resize(self, id, size, region=None, wait=False, poll=5, timeout=300):
        """
        description: Resize a volume

        in:
            - id - number - The id of the volume
            - size_gigabytes - int - The new size of the Block Storage volume in GiB (1024^3). - true
            - region - string - The slug identifier for the region the volume is located in. -

        out:
            An Action dict:
                - id - int - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "attach_volume" to represent the state of a volume attach action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - nullable int - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - dict - The region where the resources acted upon are located.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#resize-a-volume
        """  # nopep8
        attribs = {
            "type": "resize",
            "size_gigabytes": size
        }

        if region is not None:
            attribs["region"] = region

        uri = "{}/{}/actions".format(self.uri, id)
        return self.action_result(
            self.request(uri, "action", 'POST', attribs=attribs),
            wait, poll, timeout
        )

    def action_list(self, id):
        """
        description: List all actions for a volume

        in:
            - id - number - The id of the volume

        out:
            A list of Action dict's:
                - id - int - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "attach_volume" to represent the state of a volume attach action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - nullable int - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - dict - The region where the resources acted upon are located.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-actions-for-a-volume
        """  # nopep8
        uri = "{}/{}/actions".format(self.uri, id)
        return self.pages(uri, "actions")

    def action_info(self, id, action_id):
        """
        description: Retrieve an existing volume action

        in:
            - id - number - The id of the volume
            - action_id - number - The id of the action

        out:
            An Action dict:
                - id - int - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "attach_volume" to represent the state of a volume attach action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - nullable int - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - dict - The region where the resources acted upon are located.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-volume-action
        """  # nopep8
        uri = "{}/{}/actions/{}".format(self.uri, id, action_id)
        return self.request(uri, "action")
