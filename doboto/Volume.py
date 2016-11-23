"""This holds the Volume class."""

from .Endpoint import Endpoint


class Volume(Endpoint):

    """Class for interacting with volumes."""

    def __init__(self, url, token):
        """
        Take token and sets its URI for volume interaction.
        """
        super(Volume, self).__init__(token)
        self.uri = "{}/volumes".format(url)

    def list(self, region=None):
        """
        list all volumes, or by region volumes
        """
        if region is not None:
            return self.make_request(self.uri, params={"region": region})
        else:
            return self.make_request(self.uri)

    def create(self, attribs=None):
        """Create a volume based off of parameters"""

        if attribs is None:
            attribs = {}

        return self.make_request(self.uri, 'POST', attribs=attribs)

    def info(self, volume_id=None, region=None, volume_name=None):
        """
        Retrieve volume information by id or name
        """

        if volume_id is not None:
            return self.make_request("{}/{}".format(self.uri, volume_id))
        elif volume_name is not None and region is not None:
            return self.make_request(self.uri, params={"name": volume_name, "region": region})
        else:
            raise ValueError("Must supply an id or name and region")

    def list_snapshots(self, volume_id):
        """
        Retrieve volume snapshots information
        """
        uri = "{}/{}/snapshots".format(self.uri, volume_id)
        return self.make_request(uri)

    def take_snapshot(self, volume_id, snapshot_name):
        """
        Take a snapshot of a volume.
        Must supply snapshot name
        """

        uri = "{}/{}/snapshots".format(self.uri, volume_id)

        attribs = {"name": snapshot_name}
        return self.make_request(uri, 'POST', attribs=attribs)

    def destroy(self, volume_id=None, region=None, volume_name=None):
        """
        Destroy a volume by id or name
        """
        if volume_id is not None:
            return self.make_request("{}/{}".format(self.uri, volume_id), "DELETE")
        elif volume_name is not None and region is not None:
            return self.make_request(
                self.uri, "DELETE", params={"name": volume_name, "region": region}
            )
        else:
            raise ValueError("Must supply an id or name and region")

    def attach(self, droplet_id, region, volume_id=None, volume_name=None):
        """
        Attach a volume to a droplet by id or name
        """

        attribs = {
            "type": "attach",
            "droplet_id": droplet_id,
            "region": region
        }

        if volume_id is not None:
            return self.make_request(
                "{}/{}/actions".format(self.uri, volume_id), "POST", attribs=attribs
            )
        elif volume_name is not None:
            attribs["volume_name"] = volume_name
            return self.make_request(
                "{}/actions".format(self.uri), "POST", attribs=attribs
            )
        else:
            raise ValueError("Must supply an id or name")

    def detach(self, droplet_id, region, volume_id=None, volume_name=None):
        """
        Detach a volume to a droplet by id or name
        """

        attribs = {
            "type": "detach",
            "droplet_id": droplet_id,
            "region": region
        }

        if volume_id is not None:
            return self.make_request(
                "{}/{}/actions".format(self.uri, volume_id), "POST", attribs=attribs
            )
        elif volume_name is not None:
            attribs["volume_name"] = volume_name
            return self.make_request(
                "{}/actions".format(self.uri), "POST", attribs=attribs
            )
        else:
            raise ValueError("Must supply an id or name")

    def resize(self, size, region, volume_id):
        """
        Resize a volume
        """
        attribs = {
            "type": "resize",
            "region": region,
            "size_gigabytes": size
        }

        uri = "{}/{}/actions".format(self.uri, volume_id)
        return self.make_request(uri, 'POST', attribs=attribs)

    def list_actions(self, volume_id):
        """
        Retrieve volume actions information
        """
        uri = "{}/{}/actions".format(self.uri, volume_id)
        return self.make_request(uri)

    def get_action(self, volume_id, action_id):
        """
        Get the status of an volume action
        """
        uri = "{}/{}/actions/{}".format(self.uri, volume_id, action_id)
        return self.make_request(uri)
