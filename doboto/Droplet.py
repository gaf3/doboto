"""This holds the Droplet class."""

from .Endpoint import Endpoint


class Droplet(Endpoint):

    """Class for interacting with droplets."""

    def __init__(self, url, token):
        """
        Take token and sets its URI for droplet interaction.
        """
        super(Droplet, self).__init__(token)
        self.uri = "%s/droplets" % url
        self.reports = "%s/reports" % url

    def list(self, tag_name=None):
        """
        list all droplets, or tagged droplets
        """
        if tag_name is not None:
            uri = "%s?tag_name=%s" % (self.uri, tag_name)
        else:
            uri = self.uri

        return self.make_request(uri)

    def neighbor_list(self, id):
        """
        list all droplets on the same physical hardware as this one
        """
        uri = "%s/%s/neighbors" % (self.uri, id)

        return self.make_request(uri)

    def droplet_neighbor_list(self):
        """
        list all droplets that are on the same physical hardware
        """
        uri = "%s/droplet_neighbors" % (self.reports)

        return self.make_request(uri)

    def create(self, attribs=None):
        """Create a droplet based off of parameters"""

        if attribs is None:
            attribs = {}

        return self.make_request(self.uri, 'POST', attribs=attribs)

    def info(self, id):
        """
        Retrieve droplet information
        """
        uri = "%s/%s" % (self.uri, id)
        return self.make_request(uri)

    def destroy(self, id=None, tag_name=None):
        """
        Destroy a droplet of tagged droplets
        """
        if tag_name is not None:
            uri = "%s?tag_name=%s" % (self.uri, tag_name)
        elif id is not None:
            uri = "%s/%s" % (self.uri, id)
        else:
            raise ValueError("id or tag_name must be specified")
        return self.make_request(uri, 'DELETE')

    def action(self, id=None, tag_name=None, type=None, attribs=None):
        """
        Generic action to reduce code elsewhere
        """

        if attribs is None:
            attribs = {}

        if tag_name is not None:
            uri = "%s/actions?tag_name=%s" % (self.uri, tag_name)
        elif id is not None:
            uri = "%s/%s/actions" % (self.uri, id)
        else:
            raise ValueError("id or tag_name must be specified")

        if type is None:
            raise ValueError("type must be specified")

        attribs["type"] = type

        return self.make_request(uri, 'POST', attribs=attribs)

    def backup_list(self, id):
        """
        Retrieve droplet backups information
        """
        uri = "%s/%s/backups" % (self.uri, id)
        return self.make_request(uri)

    def backup_enable(self, id=None, tag_name=None):
        """
        Enables backups by id or tag
        """

        return self.action(id=id, tag_name=tag_name, type="enable_backups")

    def backup_disable(self, id=None, tag_name=None):
        """
        Enables backups by id or tag
        """

        return self.action(id=id, tag_name=tag_name, type="disable_backups")

    def reboot(self, id):
        """
        Reboot a droplet
        """
        uri = "%s/%s/actions" % (self.uri, id)
        attribs = {"type": "reboot"}
        return self.make_request(uri, 'POST', attribs=attribs)

    def shutdown(self, id=None, tag_name=None):
        """
        Shuts down by id or tag
        """

        return self.action(id=id, tag_name=tag_name, type="shutdown")

    def power_on(self, id=None, tag_name=None):
        """
        Powers on by id or tag
        """

        return self.action(id=id, tag_name=tag_name, type="power_on")

    def power_off(self, id=None, tag_name=None):
        """
        Powers off by id or tag
        """

        return self.action(id=id, tag_name=tag_name, type="power_off")

    def power_cycle(self, id=None, tag_name=None):
        """
        Power cycles by id or tag
        """

        return self.action(id=id, tag_name=tag_name, type="power_cycle")

    def restore(self, id, image):
        """
        Restore a droplet from an backup image
        """
        uri = "%s/%s/actions" % (self.uri, id)

        try:
            image = int(image)
        except ValueError:
            pass

        attribs = {"type": "restore", "image": image}

        return self.make_request(uri, 'POST', attribs=attribs)

    def password_reset(self, id):
        """
        Issues a password_reset to a droplet
        """
        uri = "%s/%s/actions" % (self.uri, id)
        attribs = {"type": "password_reset"}
        return self.make_request(uri, 'POST', attribs=attribs)

    def resize(self, id, size, disk=False):
        """
        Issues a resize action to a droplet, requires size slug, and optional
        disk resize bool (default=False) to permenatntly resize droplet disk
        """
        uri = "%s/%s/actions" % (self.uri, id)
        disk = str(disk).lower()
        attribs = {"type": "resize", "size": "%s" % size, "disk": disk}
        return self.make_request(uri, 'POST', attribs=attribs)

    def rebuild(self, id, image):
        """
        Issues a rebuild action to a droplet, requires image name or image id
        """
        uri = "%s/%s/actions" % (self.uri, id)

        try:
            image = int(image)
        except ValueError:
            pass

        attribs = {"type": "rebuild", "image": image}
        return self.make_request(uri, 'POST', attribs=attribs)

    def rename(self, id, name):
        """
        Issues a rename action to a droplet, requires droplet id and a new name
        """
        uri = "%s/%s/actions" % (self.uri, id)
        attribs = {"type": "rename", "name": "%s" % name}
        return self.make_request(uri, 'POST', attribs=attribs)

    def kernel_list(self, id):
        """
        Retrieve droplet kernels information
        """
        uri = "%s/%s/kernels" % (self.uri, id)
        return self.make_request(uri)

    def kernel_update(self, id, kernel_id):
        """
        Specify a kernel id to change to for a droplet
        """
        uri = "%s/%s/actions" % (self.uri, id)
        attribs = {"type": "change_kernel", "kernel": kernel_id}
        return self.make_request(uri, 'POST', attribs=attribs)

    def ipv6_enable(self, id=None, tag_name=None):
        """
        Enables IPv6 by id or tag
        """

        return self.action(id=id, tag_name=tag_name, type="enable_ipv6")

    def private_networking_enable(self, id=None, tag_name=None):
        """
        Enables IPv6 by id or tag
        """

        return self.action(id=id, tag_name=tag_name, type="enable_private_networking")

    def snapshot_list(self, id):
        """
        Retrieve droplet snapshots information
        """
        uri = "%s/%s/snapshots" % (self.uri, id)
        return self.make_request(uri)

    def snapshot_create(self, id=None, tag_name=None, name=None):
        """
        Snaphot by id or tag with name
        """

        if name is None:
            raise ValueError("name must be specified")

        return self.action(id=id, tag_name=tag_name, type="snapshot", attribs={"name": name})

    def action_list(self, id):
        """
        Retrieve droplet actions information
        """
        uri = "%s/%s/actions" % (self.uri, id)
        return self.make_request(uri)

    def action_info(self, id, action_id):
        """
        Get the status of an droplet action
        """
        uri = "%s/%s/actions/%s" % (self.uri, id, action_id)
        return self.make_request(uri)
