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

    def info(self, droplet_id):
        """
        Retrieve droplet information
        """
        uri = "%s/%s" % (self.uri,droplet_id)
        return self.make_request(uri)

    def list(self, tag_name=None):
        """
        list all droplets, or tagged droplets
        """
        if self.tag_name is not None:
            uri = "%s?tag_name=%s" % (self.uri, self.tag_name)
        else:
            uri = self.uri

        return self.make_request(uri)

    def list_kernels(self, droplet_id):
        """
        Retrieve droplet kernels information
        """
        uri = "%s/%s/kernels" % (self.uri, droplet_id)
        return self.make_request(uri)

    def list_snapshots(self, droplet_id):
        """
        Retrieve droplet snapshots information
        """
        uri =  "%s/%s/snapshots" % (self.uri, droplet_id)
        return self.make_request(uri)

    def list_backups(self, droplet_id):
        """
        Retrieve droplet backups information
        """
        uri = "%s/%s/backups" % (self.uri, droplet_id)
        return self.make_request(uri)

    def list_actions(self, droplet_id):
        """
        Retrieve droplet actions information
        """
        uri = "%s/%s/actions" % (self.uri, droplet_id)
        return self.make_request(uri)

    def get_action(self, droplet_id, action_id):
        """
        Get the status of an droplet action
        """
        uri = "%s/%s/actions/%s" % (self.uri, self.droplet_id, self.action_id)
        return self.make_request(uri)

    def destroy(self, droplet_id, tag_name=None):
        """
        Destroy a droplet of tagged droplets
        """
        if self.tag_name is not None:
            uri = "%s?tag_name=%s" % (self.uri, self.tag_name)
        else:
            uri = "%s/%s" % (self.uri, self.droplet_id)
        return self.make_request(uri, 'DELETE')

    def create(self, attribs={}):
        """Create a droplet based off of parameters"""
        return self.make_request(self.uri, 'POST', attribs=attribs)

    def backups(self, droplet_id, action, tag_name=None):
        """
        Enable or disabled backups for a droplet, or tagged droplets
        """
        if self.tag_name is not None:
            uri = "%s/actions?tag_name=%s" % (self.uri, self.tag_name)
        else:
            uri = "%s/%s/actions" % (self.uri, self.droplet_id)

        action = str(self.action).lower()

        if action == "on":
            act = "enable_backups"
        elif action == "off":
            act = "disable_backups"
        else:
            raise ValueError(
                "Action should be: 'on' or 'off', got: %s" % action)

        attribs = {"type": action}

        return self.make_request(uri, 'POST', attribs=attribs)

    def reboot(self, droplet_id):
        """
        Reboot a droplet
        """
        uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        attribs = {"type": "reboot"}
        return self.make_request(uri, 'POST', attribs=attribs)

    def power(self, droplet_id, action, tag_name=None):
        """
        Power action for a droplet, or tagged droplets
        """
        if self.tag_name is not None:
            uri = "%s/actions?tag_name=%s" % (self.uri, self.tag_name)
        else:
            uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        action = str(self.action).lower()

        if action == "on":
            act = "power_on"
        elif action == "off":
            act = "power_off"
        elif action == "cycle":
            act = "power_cycle"
        else:
            raise ValueError(
                "Action should be: 'on', 'off', or 'cycle' got: %s" % action)

        attribs = {"type": action}

        return self.make_request(uri, 'POST', attribs=attribs)

    def shutdown(self, droplet_id, tag_name=None):
        """
        Shutdown a droplet, or tagged droplets
        """
        if self.tag_name is not None:
            uri = "%s/actions?tag_name=%s" % (self.uri, self.tag_name)
        else:
            uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        attribs = {"type": "shutdown"}
        return self.make_request(uri, 'POST', attribs=attribs)

    def restore(self, droplet_id, image):
        """
        Restore a droplet from an backup image
        """
        uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        image = self.image
        attribs = {"type": "restore", "image": image}
        return self.make_request(uri, 'POST', attribs=attribs)

    def password_reset(self, droplet_id):
        """
        Issues a password_reset to a droplet
        """
        uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        attribs = {"type": "password_reset"}
        return self.make_request(uri, 'POST', attribs=attribs)

    def resize(self, droplet_id, size, disk=False):
        """
        Issues a resize action to a droplet, requires size slug, and optional
        disk resize bool (default=False) to permenatntly resize droplet disk
        """
        uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        size = self.size
        disk = str(self.disk).lower()
        attribs = {"type": "resize", "size": "%s" % size, "disk": disk}
        return self.make_request(uri, 'POST', attribs=attribs)

    def rebuild(self, droplet_id, image):
        """
        Issues a rebuild action to a droplet, requires image name or image id 
        """
        uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        if isinstance(self.image, int):
            attribs = {"type": "rebuild", "image": self.image}
        else:
            attribs = {"type": "rebuild", "image": "%s" % self.image}
        return self.make_request(uri, 'POST', attribs=attribs)

    def rename(self, droplet_id, name):
        """
        Issues a rename action to a droplet, requires droplet id and a new name
        """
        uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        name = self.name
        attribs = {"type": "rename", "name": "%s" % name}
        return self.make_request(uri, 'POST', attribs=attribs)

    def change_kernel(self, droplet_id, kernel_id):
        """
        Specify a kernel id to change to for a droplet
        """
        uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        attribs = {"type": "change_kernel", "kernel": kernel_id}
        return self.make_request(uri, 'POST', attribs=attribs)

    def enable_ipv6(self, droplet_id, tag_name=None):
        """
        Enable IPv6 for a droplet, or tagged droplets
        """
        if self.tag_name is not None:
            uri = "%s/actions?tag_name=%s" % (self.uri, self.tag_name)
        else:
            uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        attribs = {"type": "enable_ipv6"}
        return self.make_request(uri, 'POST', attribs=attribs)

    def enable_private_networking(self, droplet_id, tag_name=None):
        """
        Enable Private Networking for a droplet, or tagged droplets
        """
        if self.tag_name is not None:
            uri = "%s/actions?tag_name=%s" % (self.uri, self.tag_name)
        else:
            uri = "%s/%s/actions" % (self.uri, self.droplet_id)
        attribs = {"type": "enable_private_networking"}
        return self.make_request(uri, 'POST', attribs=attribs)

    def take_snapshot(self, droplet_id, name, tag_name=None):
        """
        Take a snapshot of a droplet or tagged droplets.
        Must supply snapshot name
        """
        if self.tag_name is not None:
            uri = "%s/actions?tag_name=%s" % (self.uri, self.tag_name)
        else:
            uri = "%s/%s/actions" % (self.uri, self.droplet_id)

        attribs = {"type": "snapshot", "name": "%s" % self.name}
        return self.make_request(uri, 'POST', attribs=attribs)
