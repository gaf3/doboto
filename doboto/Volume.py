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

    def create(self, attribs=None):
        """Create a volume based off of parameters"""

        if attribs is None:
            attribs = {}

        return self.make_request(self.uri, 'POST', attribs=attribs)

    def list(self, region=None):
        """
        list all volumes, or by region volumes
        """
        if region is not None:
            return self.make_request(self.uri, params={"region": region})
        else:
            return self.make_request(self.uri)

    def info(self, id=None, name=None, region=None):
        """
        Retrieve volume information by id or name
        """

        if id is not None:
            return self.make_request("{}/{}".format(self.uri, id))
        elif name is not None and region is not None:
            return self.make_request(self.uri, params={"name": name, "region": region})
        else:
            raise ValueError("Must supply an id or name and region")

    def snapshots(self, id):
        """
        Retrieve volume snapshots information
        """
        uri = "{}/{}/snapshots".format(self.uri, id)
        return self.make_request(uri)

    def snapshot(self, id, snapshot_name):
        """
        Take a snapshot of a volume.
        Must supply snapshot name
        """

        uri = "{}/{}/snapshots".format(self.uri, id)

        attribs = {"name": snapshot_name}
        return self.make_request(uri, 'POST', attribs=attribs)

    def destroy(self, id=None, name=None, region=None):
        """
        Destroy a volume by id or name
        """
        if id is not None:
            return self.make_request("{}/{}".format(self.uri, id), "DELETE")
        elif name is not None and region is not None:
            return self.make_request(
                self.uri, "DELETE", params={"name": name, "region": region}
            )
        else:
            raise ValueError("Must supply an id or name and region")

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
            return self.make_request(
                "{}/{}/actions".format(self.uri, id), "POST", attribs=attribs
            )
        elif name is not None:
            attribs["volume_name"] = name
            return self.make_request(
                "{}/actions".format(self.uri), "POST", attribs=attribs
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
            return self.make_request(
                "{}/{}/actions".format(self.uri, id), "POST", attribs=attribs
            )
        elif name is not None:
            attribs["volume_name"] = name
            return self.make_request(
                "{}/actions".format(self.uri), "POST", attribs=attribs
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
        return self.make_request(uri, 'POST', attribs=attribs)

    def actions(self, id):
        """
        Retrieve volume actions information
        """
        uri = "{}/{}/actions".format(self.uri, id)
        return self.make_request(uri)

    def action_info(self, id, action_id):
        """
        Get the status of an volume action
        """
        uri = "{}/{}/actions/{}".format(self.uri, id, action_id)
        return self.make_request(uri)
