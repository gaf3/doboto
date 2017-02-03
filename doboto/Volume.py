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
            return self.pages(self.uri, "volumes", params={"region": region})
        else:
            return self.pages(self.uri, "volumes")

    def create(self, attribs=None):
        """Create a volume based off of parameters"""

        if attribs is None:
            attribs = {}

        return self.request(self.uri, "volume", 'POST', attribs=attribs)

    def info(self, id=None, name=None, region=None):
        """
        Retrieve volume information by id or name
        """

        if id is not None:
            return self.request("{}/{}".format(self.uri, id), "volume")
        elif name is not None and region is not None:
            return self.request(self.uri, "volume", params={"name": name, "region": region})
        else:
            raise ValueError("Must supply an id or name and region")

    def destroy(self, id=None, name=None, region=None):
        """
        Destroy a volume by id or name
        """
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
        Retrieve volume snapshots information
        """
        uri = "{}/{}/snapshots".format(self.uri, id)
        return self.pages(uri, "snapshots")

    def snapshot_create(self, id, snapshot_name):
        """
        Take a snapshot of a volume.
        Must supply snapshot name
        """

        uri = "{}/{}/snapshots".format(self.uri, id)

        attribs = {"name": snapshot_name}
        return self.request(uri, "snapshot", 'POST', attribs=attribs)

    def attach(self, id=None, name=None, region=None, droplet_id=None):
        """
        Attach a volume to a droplet by id or name
        """

        attribs = {
            "type": "attach",
            "droplet_id": droplet_id
        }

        if region is not None:
            attribs["region"] = region

        if id is not None:
            return self.request(
                "{}/{}/actions".format(self.uri, id), "action", "POST", attribs=attribs
            )
        elif name is not None:
            attribs["volume_name"] = name
            return self.request(
                "{}/actions".format(self.uri), "action", "POST", attribs=attribs
            )
        else:
            raise ValueError("Must supply an id or name")

    def detach(self, id=None, name=None, region=None, droplet_id=None):
        """
        Detach a volume to a droplet by id or name
        """

        attribs = {
            "type": "detach",
            "droplet_id": droplet_id
        }

        if region is not None:
            attribs["region"] = region

        if id is not None:
            return self.request(
                "{}/{}/actions".format(self.uri, id), "action", "POST", attribs=attribs
            )
        elif name is not None:
            attribs["volume_name"] = name
            return self.request(
                "{}/actions".format(self.uri), "action", "POST", attribs=attribs
            )
        else:
            raise ValueError("Must supply an id or name")

    def resize(self, id, size, region=None):
        """
        Resize a volume
        """
        attribs = {
            "type": "resize",
            "size_gigabytes": size
        }

        if region is not None:
            attribs["region"] = region

        uri = "{}/{}/actions".format(self.uri, id)
        return self.request(uri, "action", 'POST', attribs=attribs)

    def action_list(self, id):
        """
        Retrieve volume actions information
        """
        uri = "{}/{}/actions".format(self.uri, id)
        return self.pages(uri, "actions")

    def action_info(self, id, action_id):
        """
        Get the status of an volume action
        """
        uri = "{}/{}/actions/{}".format(self.uri, id, action_id)
        return self.request(uri, "action")
