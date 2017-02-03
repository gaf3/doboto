"""
This holds the FloatingIP class.
"""

from .Endpoint import Endpoint


class FloatingIP(Endpoint):
    """
    Class for interacting with floating IPs.
    """

    def __init__(self, url, token):
        """
        Take token and sets its URI for floating ip interaction.
        """
        super(FloatingIP, self).__init__(token)
        self.uri = "{}/floating_ips".format(url)

    def list(self):
        """
        List all floating IPs
        """

        return self.pages(self.uri, "floating_ips")

    def create(self, droplet_id=None, region=None):
        """
        Create a new floating ip
        """
        attribs = {}

        if droplet_id is not None:
            attribs["droplet_id"] = droplet_id
        elif region is not None:
            attribs["region"] = region
        else:
            raise ValueError("droplet_id or region must be specified")

        return self.request(self.uri, "floating_ip", 'POST', attribs)

    def info(self, ip):
        """
        Retrieve a floating ip
        """

        uri = "%s/%s" % (self.uri, ip)
        return self.request(uri, "floating_ip")

    def destroy(self, ip):
        """
        deletes the floating ip itself
        """

        uri = "{}/{}".format(self.uri, ip)

        return self.request(uri, request_method='DELETE')

    def assign(self, ip, droplet_id):
        """
        This call provides a way to assign a floating ip to a droplet
        """

        uri = "{}/{}/actions".format(self.uri, ip)
        attribs = {'type': 'assign', 'droplet_id': droplet_id}

        return self.request(uri, "action", 'POST', attribs)

    def unassign(self, ip):
        """
        This call provides a way to unassign a floating ip from a droplet
        """

        uri = "{}/{}/actions".format(self.uri, ip)
        attribs = {'type': 'unassign'}

        return self.request(uri, "action", 'POST', attribs)

    def action_list(self, ip):
        """Retrieve floating ip actions information"""
        uri = self.uri + "/%s/actions" % ip

        return self.pages(uri, "actions")

    def action_info(self, ip, action_id):
        """
        Get the status of an floating ip action
        """
        uri = "%s/%s/actions/%s" % (self.uri, ip, action_id)
        return self.request(uri, "action")
