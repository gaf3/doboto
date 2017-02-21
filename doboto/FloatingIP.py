"""
This holds the FloatingIP class.
"""

from .Endpoint import Endpoint


class FloatingIP(Endpoint):
    """
    description:

        Floating IP dict's represent a publicly-accessible static IP addresses that can be mapped
        to one of your Droplets. They can be used to create highly available setups or other
        configurations requiring movable addresses.

        Floating IPs are bound to a specific region.

    related: https://developers.digitalocean.com/documentation/v2/#floating-ips
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for floating ip interaction.
        """
        super(FloatingIP, self).__init__(token, agent)
        self.do = do
        self.uri = "{}/floating_ips".format(url)

    def list(self):
        """
        description: List all Floating IPs

        out:
            A list of Floating IP dict's:
                - ip - string - The public IP address of the Floating IP. It also serves as its identifier.
                - region - dict - The region that the Floating IP is reserved to. When you query a Floating IP, the entire region dict will be returned.
                - droplet - dict - The Droplet that the Floating IP has been assigned to. When you query a Floating IP, if it is assigned to a Droplet, the entire Droplet dict will be returned. If it is not assigned, the value will be null.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-floating-ips
        """  # nopep8

        return self.pages(self.uri, "floating_ips")

    def create(self, droplet_id=None, region=None):
        """
        description: Create a new Floating IP assigned to a Droplet or Region

        in:
            - droplet_id - int - The ID of Droplet that the Floating IP will be assigned to.
            - region - string - The slug identifier for the region the Floating IP will be reserved to.

        out:
            A Floating IP dict:
            - ip - string - The public IP address of the Floating IP. It also serves as its identifier.
            - region - dict - The region that the Floating IP is reserved to. When you query a Floating IP, the entire region dict will be returned.
            - droplet - dict - The Droplet that the Floating IP has been assigned to. When you query a Floating IP, if it is assigned to a Droplet, the entire Droplet dict will be returned. If it is not assigned, the value will be null.

        related:
            - https://developers.digitalocean.com/documentation/v2/#create-a-new-floating-ip-assigned-to-a-droplet
            - https://developers.digitalocean.com/documentation/v2/#create-a-new-floating-ip-reserved-to-a-region
        """  # nopep8
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
        description: Retrieve an existing Floating IP

        in:
            - ip - string - The public IP address of the Floating IP.

        out:
            A Floating IP dict:
            - ip - string - The public IP address of the Floating IP. It also serves as its identifier.
            - region - dict - The region that the Floating IP is reserved to. When you query a Floating IP, the entire region dict will be returned.
            - droplet - dict - The Droplet that the Floating IP has been assigned to. When you query a Floating IP, if it is assigned to a Droplet, the entire Droplet dict will be returned. If it is not assigned, the value will be null.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-floating-ip
        """  # nopep8

        uri = "%s/%s" % (self.uri, ip)
        return self.request(uri, "floating_ip")

    def destroy(self, ip):
        """
        description: Delete a Floating IP

        in:
            - ip - string - The public IP address of the Floating IP.

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related: https://developers.digitalocean.com/documentation/v2/#delete-a-floating-ips
        """  # nopep8

        uri = "{}/{}".format(self.uri, ip)

        return self.request(uri, request_method='DELETE')

    def assign(self, ip, droplet_id, wait=False, poll=5, timeout=300):
        """
        description: Assign a Floating IP to a Droplet

        in:
            - ip - string - The public IP address of the Floating IP.
            - droplet_id - int - The ID of Droplet that the Floating IP will be assigned to.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "assign_ip" to represent the state of a Floating IP assign action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#assign-a-floating-ip-to-a-droplet
        """  # nopep8

        uri = "{}/{}/actions".format(self.uri, ip)
        attribs = {'type': 'assign', 'droplet_id': droplet_id}

        return self.action_result(
            self.request(uri, "action", 'POST', attribs),
            wait, poll, timeout
        )

    def unassign(self, ip, wait=False, poll=5, timeout=300):
        """
        description: Unassign a Floating IP

        in:
            - ip - string - The public IP address of the Floating IP.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "assign_ip" to represent the state of a Floating IP assign action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#unassign-a-floating-ip
        """  # nopep8

        uri = "{}/{}/actions".format(self.uri, ip)
        attribs = {'type': 'unassign'}

        return self.action_result(
            self.request(uri, "action", 'POST', attribs),
            wait, poll, timeout
        )

    def action_list(self, ip):
        """
        description: List all actions for a Floating IP

        in:
            - ip - string - The public IP address of the Floating IP.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            A list of Action dict's:
                - id - number - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "assign_ip" to represent the state of a Floating IP assign action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-actions-for-a-floating-ip
        """  # nopep8
        uri = self.uri + "/%s/actions" % ip

        return self.pages(uri, "actions")

    def action_info(self, ip, action_id):
        """
        description: Retrieve an existing Floating IP Action

        in:
            - ip - string - The public IP address of the Floating IP.
            - action_id - number - The id of the Action

        out:
            An Action dict:
                - id - number - A unique numeric ID that can be used to identify and reference an action.
                - status - string - The current status of the action. This can be "in-progress", "completed", or "errored".
                - type - string - This is the type of action that the dict represents. For example, this could be "assign_ip" to represent the state of a Floating IP assign action.
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-floating-ip-action
        """  # nopep8
        uri = "%s/%s/actions/%s" % (self.uri, ip, action_id)
        return self.request(uri, "action")
