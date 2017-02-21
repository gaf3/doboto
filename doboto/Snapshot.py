"""This holds the Snapshot class."""

from .Endpoint import Endpoint


class Snapshot(Endpoint):
    """
    description:

        Snapshots are saved instances of a Droplet or a volume, which is reflected in the
        resource_type attribute. In order to avoid problems with compressing filesystems, each
        defines a min_disk_size attribute which is the minimum size of the Droplet or volume disk
        when creating a new resource from the saved snapshot.

    related: https://developers.digitalocean.com/documentation/v2/#snapshots
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for floating ip interaction.
        """
        super(Snapshot, self).__init__(token, agent)
        self.do = do
        self.uri = "%s/snapshots" % url

    def list(self, resource_type=None):
        """
        description: List all, droplet, or volume snapshots

        in:
            - resource_type - string - Can be "droplet" or "volume" for snapshots thereof.

        out:
            A list of Snapshot dict's:
                - id - string - The unique identifier for the snapshot.
                - name - string - A human-readable name for the snapshot.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the snapshot was created.
                - regions - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - resource_id - string - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - min_disk_size - number - The minimum size in GB required for a volume or Droplet to use this snapshot.
                - size_gigabytes - number - The billable size of the snapshot in gigabytes.

        related:
            - https://developers.digitalocean.com/documentation/v2/#list-all-snapshots
            - https://developers.digitalocean.com/documentation/v2/#list-all-droplet-snapshots
            - https://developers.digitalocean.com/documentation/v2/#list-all-volume-snapshots
        """  # nopep8

        params = {}

        if resource_type is not None:
            params["resource_type"] = resource_type

        return self.pages(self.uri, "snapshots", params=params)

    def info(self, id):
        """
        description: Retrieve an existing snapshot by id

        in:
            - id - number - id of the Snapshot

        out:
            A Snapshot dict:
                - id - string - The unique identifier for the snapshot.
                - name - string - A human-readable name for the snapshot.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the snapshot was created.
                - regions - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - resource_id - string - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - min_disk_size - number - The minimum size in GB required for a volume or Droplet to use this snapshot.
                - size_gigabytes - number - The billable size of the snapshot in gigabytes.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-snapshot-by-id
        """  # nopep8
        uri = self.uri + "/%s" % id

        return self.request(uri, "snapshot")

    def destroy(self, id):
        """
        description: Delete a snapshot

        in:
            - id - number - id of the Snapshot

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#delete-an-snapshot
        """  # nopep8
        uri = self.uri + "/%s" % id

        return self.request(uri, request_method="DELETE")
