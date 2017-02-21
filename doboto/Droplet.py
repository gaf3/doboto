"""This holds the Droplet class."""

import time
import copy
from .Endpoint import Endpoint
from .exception import DOBOTOException, DOBOTOPollingException


class Droplet(Endpoint):
    """
    description:
        A Droplet is a DigitalOcean virtual machine. With this class, you can list, create, or
        delete Droplets.

        Some of the attributes will have an dict value. The region and image dict's will all
        contain the standard attributes of their associated types. Find more information about each
        of these dict's in their respective sections.

    related: https://developers.digitalocean.com/documentation/v2/#droplets
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for droplet interaction.
        """
        super(Droplet, self).__init__(token, agent)
        self.do = do
        self.uri = "%s/droplets" % url
        self.reports = "%s/reports" % url

    def list(self, tag_name=None):
        """
        description: List all Droplets or all Droplets with a specific Tag.

        in:
            - tag_name - string - Send to retrieve Droplet with this tag.

        out:
            A list of Droplet dict's:
                - id - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.
                - name - string - The human-readable name set for the Droplet instance.
                - memory - number - Memory of the Droplet in megabytes.
                - vcpus - number - The number of virtual CPUs.
                - disk - number - The size of the Droplet's disk in gigabytes.
                - locked - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.
                - status - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".
                - backup_ids - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.
                - snapshot_ids - list - A list of snapshot IDs of any snapshots created from the Droplet instance.
                - features - list - A list of features enabled on this Droplet.
                - region - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.
                - image - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.
                - size - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.
                - size_slug - string - The unique slug identifier for the size of this Droplet.
                - networks - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.
                - kernel - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.
                - next_backup_window - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.
                - tags - list - A list of Tags the Droplet has been tagged with.
                - volume_ids - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.

        related:
            - https://developers.digitalocean.com/documentation/v2/#list-all-droplets
            - https://developers.digitalocean.com/documentation/v2/#listing-droplets-by-tag
        """  # nopep8
        if tag_name is not None:
            uri = "%s?tag_name=%s" % (self.uri, tag_name)
        else:
            uri = self.uri

        return self.pages(uri, "droplets")

    def neighbor_list(self, id):
        """
        description: List Neighbors for a Droplet running on the same physical server

        in:
            - id - number - The id of the Droplet

        out:
            A list of Droplet dict's:
                - id - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.
                - name - string - The human-readable name set for the Droplet instance.
                - memory - number - Memory of the Droplet in megabytes.
                - vcpus - number - The number of virtual CPUs.
                - disk - number - The size of the Droplet's disk in gigabytes.
                - locked - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.
                - status - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".
                - backup_ids - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.
                - snapshot_ids - list - A list of snapshot IDs of any snapshots created from the Droplet instance.
                - features - list - A list of features enabled on this Droplet.
                - region - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.
                - image - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.
                - size - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.
                - size_slug - string - The unique slug identifier for the size of this Droplet.
                - networks - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.
                - kernel - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.
                - next_backup_window - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.
                - tags - list - A list of Tags the Droplet has been tagged with.
                - volume_ids - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.

        related: https://developers.digitalocean.com/documentation/v2/#list-neighbors-for-a-droplet
        """  # nopep8
        uri = "%s/%s/neighbors" % (self.uri, id)

        return self.pages(uri, "droplets")

    def droplet_neighbor_list(self):
        """
        description:
            List all Droplet Neighbors, any droplets that are running on the same physical hardware

        out:
            A list of neighbor lists of Droplet dict's:
                - id - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.
                - name - string - The human-readable name set for the Droplet instance.
                - memory - number - Memory of the Droplet in megabytes.
                - vcpus - number - The number of virtual CPUs.
                - disk - number - The size of the Droplet's disk in gigabytes.
                - locked - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.
                - status - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".
                - backup_ids - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.
                - snapshot_ids - list - A list of snapshot IDs of any snapshots created from the Droplet instance.
                - features - list - A list of features enabled on this Droplet.
                - region - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.
                - image - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.
                - size - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.
                - size_slug - string - The unique slug identifier for the size of this Droplet.
                - networks - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.
                - kernel - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.
                - next_backup_window - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.
                - tags - list - A list of Tags the Droplet has been tagged with.
                - volume_ids - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-droplet-neighbors
        """  # nopep8
        uri = "%s/droplet_neighbors" % (self.reports)

        return self.pages(uri, "neighbors")

    def ready(self, droplet, attribs):
        """
        Determine if a droplet is ready
        """

        if droplet["status"] == "new":
            return False

        if "private_networking" in attribs and attribs["private_networking"]:
            found = False
            for v4 in droplet["networks"]["v4"]:
                if v4["type"] == "private":
                    found = True
            if not found:
                return False

        if "ipv6" in attribs and attribs["ipv6"] and "v6" not in droplet["networks"]:
            return False

        if "tags" in attribs and attribs["tags"] and len(attribs["tags"]) != len(droplet["tags"]):
            return False

        return True

    def create(self, attribs, wait=False, poll=5, timeout=300):
        """
        description: Create a new Droplet or multiple Droplets

        in:
            - attribs - dict - The data of the Droplet:
                - name - string - The human-readable string you wish to use when displaying the Droplet name. The name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. The name set during creation will also determine the hostname for the Droplet in its internal configuration. - if single droplet
                - names - list - A list of human human-readable strings you wish to use when displaying the Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. Each name set during creation will also determine the hostname for the Droplet in its internal configuration. - if multiple droplets
                - region - string - The unique slug identifier for the region that you wish to deploy in. - true
                - size - string - The unique slug identifier for the size that you wish to select for this Droplet. - true
                - image - number (if using an image ID), or String (if using a public image slug) - The image ID of a public or private image, or the unique slug identifier for a public image. This image will be the base image for your Droplet. - true
                - ssh_keys - list - A list containing the IDs or fingerprints of the SSH keys that you wish to embed in the Droplet's root account upon creation. -
                - backups - bool - A boolean indicating whether automated backups should be enabled for the Droplet. Automated backups can only be enabled when the Droplet is created. -
                - ipv6 - bool - A boolean indicating whether IPv6 is enabled on the Droplet. -
                - private_networking - bool - A boolean indicating whether private networking is enabled for the Droplet. Private networking is currently only available in certain regions. -
                - user_data - string - A string of the desired User Data for the Droplet. User Data is currently only available in regions with metadata listed in their features. -
                - monitoring - bool - A boolean indicating whether to install the DigitalOcean agent for monitoring. -
                - volume - list - A flat list including the unique string identifier for each Block Storage volume to be attached to the Droplet. At the moment a volume can only be attached to a single Droplet. -
                - tags - list - A flat list of tag names as strings to apply to the Droplet after it is created. Tag names can either be existing or new tags.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            A Droplet dict if name is sent, or a list of Droplet dict's in names is sent:
                - id - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.
                - name - string - The human-readable name set for the Droplet instance.
                - memory - number - Memory of the Droplet in megabytes.
                - vcpus - number - The number of virtual CPUs.
                - disk - number - The size of the Droplet's disk in gigabytes.
                - locked - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.
                - status - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".
                - backup_ids - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.
                - snapshot_ids - list - A list of snapshot IDs of any snapshots created from the Droplet instance.
                - features - list - A list of features enabled on this Droplet.
                - region - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.
                - image - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.
                - size - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.
                - size_slug - string - The unique slug identifier for the size of this Droplet.
                - networks - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.
                - kernel - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.
                - next_backup_window - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.
                - tags - list - A list of Tags the Droplet has been tagged with.
                - volume_ids - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.

        related:
            - https://developers.digitalocean.com/documentation/v2/#create-a-new-droplet
            - https://developers.digitalocean.com/documentation/v2/#create-multiple-droplets
        """  # nopep8

        if poll < 1:
            poll = 1

        if "name" in attribs:

            droplet = self.request(self.uri, "droplet", 'POST', attribs=attribs)

            if not wait:
                return droplet

            start_time = time.time()

            while not self.ready(droplet, attribs):

                time.sleep(poll)
                try:
                    droplet = self.info(droplet["id"])
                except Exception as exception:
                    if time.time() - start_time > timeout:
                        raise DOBOTOPollingException(polling=droplet, error=exception)

                if time.time() - start_time > timeout:
                    raise DOBOTOPollingException(polling=droplet)

            return droplet

        elif "names" in attribs:

            droplets = self.request(self.uri, "droplets", 'POST', attribs=attribs)

            if not wait:
                return droplets

            start_time = time.time()

            info = [index for index, droplet in enumerate(droplets)
                    if not self.ready(droplet, attribs)]

            while len(info) > 0:

                time.sleep(poll)

                for index in info:
                    try:
                        droplets[index] = self.info(droplets[index]["id"])
                    except Exception as exception:
                        if time.time() - start_time > timeout:
                            raise DOBOTOPollingException(polling=droplets, error=exception)

                    if time.time() - start_time > timeout:
                        raise DOBOTOPollingException(polling=droplets)

                info = [index for index, droplet in enumerate(droplets)
                        if not self.ready(droplet, attribs)]

            return droplets

        else:

            raise ValueError("name or names must be specified")

    def present(self, attribs, wait=False, poll=5, timeout=300):
        """
        description: Create a new Droplet or multiple Droplets if not already existing

        in:
            - attribs - dict - The data of the Droplet:
                - name - string - The human-readable string you wish to use when displaying the Droplet name. The name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. The name set during creation will also determine the hostname for the Droplet in its internal configuration. - if single droplet
                - names - list - A list of human human-readable strings you wish to use when displaying the Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. Each name set during creation will also determine the hostname for the Droplet in its internal configuration. - if multiple droplets
                - region - string - The unique slug identifier for the region that you wish to deploy in. - true
                - size - string - The unique slug identifier for the size that you wish to select for this Droplet. - true
                - image - number (if using an image ID), or String (if using a public image slug) - The image ID of a public or private image, or the unique slug identifier for a public image. This image will be the base image for your Droplet. - true
                - ssh_keys - list - A list containing the IDs or fingerprints of the SSH keys that you wish to embed in the Droplet's root account upon creation. -
                - backups - bool - A boolean indicating whether automated backups should be enabled for the Droplet. Automated backups can only be enabled when the Droplet is created. -
                - ipv6 - bool - A boolean indicating whether IPv6 is enabled on the Droplet. -
                - private_networking - bool - A boolean indicating whether private networking is enabled for the Droplet. Private networking is currently only available in certain regions. -
                - user_data - string - A string of the desired User Data for the Droplet. User Data is currently only available in regions with metadata listed in their features. -
                - monitoring - bool - A boolean indicating whether to install the DigitalOcean agent for monitoring. -
                - volume - list - A flat list including the unique string identifier for each Block Storage volume to be attached to the Droplet. At the moment a volume can only be attached to a single Droplet. -
                - tags - list - A flat list of tag names as strings to apply to the Droplet after it is created. Tag names can either be existing or new tags.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            A tuple of two Droplet dict's if name is sent (second is None if already present), or a tuple of two lists of Droplet dict's if names is sent, the first being all, the second being those created, (empty if all are present):
                - id - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.
                - name - string - The human-readable name set for the Droplet instance.
                - memory - number - Memory of the Droplet in megabytes.
                - vcpus - number - The number of virtual CPUs.
                - disk - number - The size of the Droplet's disk in gigabytes.
                - locked - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.
                - status - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".
                - backup_ids - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.
                - snapshot_ids - list - A list of snapshot IDs of any snapshots created from the Droplet instance.
                - features - list - A list of features enabled on this Droplet.
                - region - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.
                - image - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.
                - size - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.
                - size_slug - string - The unique slug identifier for the size of this Droplet.
                - networks - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.
                - kernel - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.
                - next_backup_window - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.
                - tags - list - A list of Tags the Droplet has been tagged with.
                - volume_ids - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.

        related:
            - https://developers.digitalocean.com/documentation/v2/#create-a-new-droplet
            - https://developers.digitalocean.com/documentation/v2/#create-multiple-droplets
        """  # nopep8

        droplets = self.list()

        if "name" in attribs:

            existing = None
            for droplet in droplets:
                if attribs["name"] == droplet["name"]:
                    existing = droplet
                    break

            if existing is not None:
                return (existing, None)

            created = self.create(attribs, wait, poll, timeout)
            return (created, created)

        elif "names" in attribs:

            existing = []
            existing_lookup = {}
            create = copy.deepcopy(attribs)
            create["names"] = []

            for name in attribs["names"]:
                exists = False
                for droplet in droplets:
                    if name == droplet["name"]:
                        exists = True
                        existing.append(droplet)
                        existing_lookup[name] = droplet
                        break
                if not exists:
                    create["names"].append(name)

            if not create["names"]:
                return (existing, [])

            created = self.create(create, wait, poll, timeout)
            created_lookup = {droplet["name"]: droplet for droplet in created}

            merged = []

            for name in attribs["names"]:
                if name in existing_lookup:
                    merged.append(existing_lookup[name])
                elif name in created_lookup:
                    merged.append(created_lookup[name])
                else:
                    raise DOBOTOException("Requested droplet '%s' not found" % name, created)

            return (merged, created)

        else:

            raise ValueError("name or names must be specified")

    def info(self, id):
        """
        description: Retrieve an existing Droplet by id

        in:
            - id - number - The id of the Droplet to retrieve

        out:
            A Droplet dict:
                - id - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.
                - name - string - The human-readable name set for the Droplet instance.
                - memory - number - Memory of the Droplet in megabytes.
                - vcpus - number - The number of virtual CPUs.
                - disk - number - The size of the Droplet's disk in gigabytes.
                - locked - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.
                - status - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".
                - backup_ids - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.
                - snapshot_ids - list - A list of snapshot IDs of any snapshots created from the Droplet instance.
                - features - list - A list of features enabled on this Droplet.
                - region - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.
                - image - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.
                - size - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.
                - size_slug - string - The unique slug identifier for the size of this Droplet.
                - networks - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.
                - kernel - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.
                - next_backup_window - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.
                - tags - list - A list of Tags the Droplet has been tagged with.
                - volume_ids - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-droplet-by-id
        """  # nopep8
        uri = "%s/%s" % (self.uri, id)
        return self.request(uri, "droplet")

    def destroy(self, id=None, tag_name=None):
        """
        description: Delete a Droplet by id or Droplets by tag

        in:
            - id - number - Send only to destroy a single Droplet by id
            - tag_name - string - Send only to destroy all Droplets with this tag.

        out: None. A DOBOTOException is thrown if an issue is encountered.

        related:
            - https://developers.digitalocean.com/documentation/v2/#delete-a-droplet
            - https://developers.digitalocean.com/documentation/v2/#deleting-droplets-by-tag
        """
        if tag_name is not None:
            uri = "%s?tag_name=%s" % (self.uri, tag_name)
        elif id is not None:
            uri = "%s/%s" % (self.uri, id)
        else:
            raise ValueError("id or tag_name must be specified")
        return self.request(uri, request_method='DELETE')

    def action(
        self, id=None, tag_name=None, type=None, attribs=None,
        wait=False, poll=5, timeout=300
    ):
        """
        Generic action to reduce code elsewhere
        """

        if attribs is None:
            attribs = {}

        if type is None:
            raise ValueError("type must be specified")

        attribs["type"] = type

        if id is not None:
            uri = "%s/%s/actions" % (self.uri, id)
            return self.action_result(
                self.request(uri, "action", 'POST', attribs=attribs),
                wait, poll, timeout
            )
        elif tag_name is not None:
            uri = "%s/actions?tag_name=%s" % (self.uri, tag_name)
            return self.actions_result(
                self.request(uri, "actions", 'POST', attribs=attribs),
                wait, poll, timeout
            )
        else:
            raise ValueError("id or tag_name must be specified")

    def backup_list(self, id):
        """
        description: List backups for a Droplet

        in:
            - id - number - The id of the Droplet

        out:
            A list of Backup dict's:
                - id - number - A unique number used to identify and reference a specific image.
                - name - string - The display name of the image. This is shown in the web UI and is generally a descriptive title for the image in question.
                - type - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".
                - distribution - string - The base distribution used for this image.
                - slug - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.
                - public - boolean - A boolean value that indicates whether the image in question is public. An image that is public is available to all accounts. A non-public image is only accessible from your account.
                - regions - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - min_disk_size - number - The minimum 'disk' required for a size to use this image.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.

        related: https://developers.digitalocean.com/documentation/v2/#list-backups-for-a-droplet
        """  # nopep8
        uri = "%s/%s/backups" % (self.uri, id)
        return self.pages(uri, "backups")

    def backup_enable(self, id=None, tag_name=None, wait=False, poll=5, timeout=300):
        """
        description: Enable Backups

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#enable-backups
        """  # nopep8

        return self.action(
            id=id, tag_name=tag_name, type="enable_backups",
            wait=wait, poll=poll, timeout=timeout
        )

    def backup_disable(self, id=None, tag_name=None, wait=False, poll=5, timeout=300):
        """
        description: Disable Backups

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#disable-backups
        """  # nopep8

        return self.action(
            id=id, tag_name=tag_name, type="disable_backups",
            wait=wait, poll=poll, timeout=timeout
        )

    def reboot(self, id, wait=False, poll=5, timeout=300):
        """
        description: Reboot a Droplet

            A reboot action is an attempt to reboot the Droplet in a graceful way, similar to using the reboot command from the console.

        in:
            - id - number - The id of the Droplet
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#reboot-a-droplet
        """  # nopep8
        uri = "%s/%s/actions" % (self.uri, id)
        attribs = {"type": "reboot"}
        return self.action_result(
            self.request(uri, "action", 'POST', attribs=attribs),
            wait, poll, timeout
        )

    def shutdown(self, id=None, tag_name=None, wait=False, poll=5, timeout=300):
        """
        description: Shutdown a Droplet

            A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to
            using the shutdown command from the console. Since a shutdown command can fail, this
            action guarantees that the command is issued, not that it succeeds. The preferred way
            to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by
            a power off action to ensure the Droplet is off.

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
            - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
            - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
            - type - string - The type of action that the event is executing (reboot, power_off, etc.).
            - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
            - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
            - resource_id - number - A unique identifier for the resource that the action is associated with.
            - resource_type - string - The type of resource that the action is associated with.
            - region - nullable string - (deprecated) A slug representing the region where the action occurred.
            - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#reboot-a-droplet
        """  # nopep8

        return self.action(
            id=id, tag_name=tag_name, type="shutdown",
            wait=wait, poll=poll, timeout=timeout
        )

    def power_on(self, id=None, tag_name=None, wait=False, poll=5, timeout=300):
        """
        description: Power On a Droplet

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#power-on-a-droplet
        """  # nopep8

        return self.action(
            id=id, tag_name=tag_name, type="power_on",
            wait=wait, poll=poll, timeout=timeout
        )

    def power_off(self, id=None, tag_name=None, wait=False, poll=5, timeout=300):
        """
        description: Power Off a Droplet

            A power_off event is a hard shutdown and should only be used if the shutdown action is
            not successful. It is similar to cutting the power on a server and could lead to
            complications.

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#power-off-a-droplet
        """  # nopep8

        return self.action(
            id=id, tag_name=tag_name, type="power_off",
            wait=wait, poll=poll, timeout=timeout
        )

    def power_cycle(self, id=None, tag_name=None, wait=False, poll=5, timeout=300):
        """
        description: Power Cycle a Droplet

            A powercycle action is similar to pushing the reset button on a physical machine, it's
            similar to booting from scratch.

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#power-cycle-a-droplet
        """  # nopep8

        return self.action(
            id=id, tag_name=tag_name, type="power_cycle",
            wait=wait, poll=poll, timeout=timeout
        )

    def restore(self, id, image, wait=False, poll=5, timeout=300):
        """
        description: Restore a Droplet

            A Droplet restoration will rebuild an image using a backup image. The image ID that is
            passed in must be a backup of the current Droplet instance. The operation will leave
            any embedded SSH keys intact.

        in:
            - id - number - The id of the Droplet
            - image - string if an image slug. number if an image ID. - An image slug or ID. This represents the image that the Droplet will use as a base.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#restore-a-droplet
        """  # nopep8
        uri = "%s/%s/actions" % (self.uri, id)

        try:
            image = int(image)
        except ValueError:
            pass

        attribs = {"type": "restore", "image": image}

        return self.action_result(
            self.request(uri, "action", 'POST', attribs=attribs),
            wait, poll, timeout
        )

    def password_reset(self, id, wait=False, poll=5, timeout=300):
        """
        description: Password Reset a Droplet

        in:
            - id - number - The id of the Droplet
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
            - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
            - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
            - type - string - The type of action that the event is executing (reboot, power_off, etc.).
            - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
            - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
            - resource_id - number - A unique identifier for the resource that the action is associated with.
            - resource_type - string - The type of resource that the action is associated with.
            - region - nullable string - (deprecated) A slug representing the region where the action occurred.
            - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#password-reset-a-droplet
        """  # nopep8
        uri = "%s/%s/actions" % (self.uri, id)
        attribs = {"type": "password_reset"}
        return self.action_result(
            self.request(uri, "action", 'POST', attribs=attribs),
            wait, poll, timeout
        )

    def resize(self, id, size, disk=False, wait=False, poll=5, timeout=300):
        """
        description: Resize a Droplet

            If a permanent resize, with disk changes included, is desired, set the "disk" attribute
            to True. The Droplet must be powered off prior to resizing.

        in:
            - id - number - The id of the Droplet
            - disk - bool - Whether to increase disk size
            - size - string - The size slug that you want to resize to. - true
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#resize-a-droplet
        """  # nopep8
        uri = "%s/%s/actions" % (self.uri, id)
        disk = str(disk).lower()
        attribs = {"type": "resize", "size": "%s" % size, "disk": disk}
        return self.action_result(
            self.request(uri, "action", 'POST', attribs=attribs),
            wait, poll, timeout
        )

    def rebuild(self, id, image, wait=False, poll=5, timeout=300):
        """
        description: Rebuild a Droplet

            A rebuild action functions just like a new create.

        in:
            - id - number - The id of the Droplet
            - image - string if an image slug. number if an image ID. - An image slug or ID. This represents the image that the Droplet will use as a base.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#rebuild-a-droplet
        """  # nopep8
        uri = "%s/%s/actions" % (self.uri, id)

        try:
            image = int(image)
        except ValueError:
            pass

        attribs = {"type": "rebuild", "image": image}
        return self.action_result(
            self.request(uri, "action", 'POST', attribs=attribs),
            wait, poll, timeout
        )

    def rename(self, id, name, wait=False, poll=5, timeout=300):
        """
        description: Rename a Droplet

        in:
            - id - number - The id of the Droplet
            - name - string - The new name for the Droplet.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#rename-a-droplet
        """  # nopep8
        uri = "%s/%s/actions" % (self.uri, id)
        attribs = {"type": "rename", "name": "%s" % name}
        return self.action_result(
            self.request(uri, "action", 'POST', attribs=attribs),
            wait, poll, timeout
        )

    def kernel_list(self, id):
        """
        description: List all available Kernels for a Droplet

        in:
            - id - number - The id of the Droplet

        out:
            A list of Kernel dict's:
                - id - number - A unique number used to identify and reference a specific kernel.
                - name - string - The display name of the kernel. This is shown in the web UI and is generally a descriptive title for the kernel in question.
                - version - string - A standard kernel version string representing the version, patch, and release information.

        related: https://developers.digitalocean.com/documentation/v2/#list-all-available-kernels-for-a-droplet
        """  # nopep8
        uri = "%s/%s/kernels" % (self.uri, id)
        return self.pages(uri, "kernels")

    def kernel_update(self, id, kernel_id, wait=False, poll=5, timeout=300):
        """
        description: Change the Kernel

        in:
            - id - number - The id of the Droplet
            - kernel - number - A unique number used to identify and reference a specific kernel. - true
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            An Action dict:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#change-the-kernel
        """  # nopep8
        uri = "%s/%s/actions" % (self.uri, id)
        attribs = {"type": "change_kernel", "kernel": kernel_id}
        return self.action_result(
            self.request(uri, "action", 'POST', attribs=attribs),
            wait, poll, timeout
        )

    def ipv6_enable(self, id=None, tag_name=None, wait=False, poll=5, timeout=300):
        """
        description: Enable IPv6

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#enable-ipv6
        """  # nopep8
        return self.action(
            id=id, tag_name=tag_name, type="enable_ipv6",
            wait=wait, poll=poll, timeout=timeout
        )

    def private_networking_enable(self, id=None, tag_name=None, wait=False, poll=5, timeout=300):
        """
        description: Enable Private Networking

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#enable-private-networking
        """  # nopep8
        return self.action(
            id=id, tag_name=tag_name, type="enable_private_networking",
            wait=wait, poll=poll, timeout=timeout
        )

    def snapshot_list(self, id):
        """
        description: List snapshots for a Droplet

        in:
            - id - number - The id of the Droplet

        out:
            A list of Image dict's:
                - id - number - A unique number used to identify and reference a specific image.
                - name - string - The display name of the image. This is shown in the web UI and is generally a descriptive title for the image in question.
                - type - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".
                - distribution - string - The base distribution used for this image.
                - slug - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.
                - public - boolean - A boolean value that indicates whether the image in question is public. An image that is public is available to all accounts. A non-public image is only accessible from your account.
                - regions - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.
                - min_disk_size - number - The minimum 'disk' required for a size to use this image.
                - created_at - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.

        related: https://developers.digitalocean.com/documentation/v2/#list-snapshots-for-a-droplet
        """  # nopep8
        uri = "%s/%s/snapshots" % (self.uri, id)
        return self.pages(uri, "snapshots")

    def snapshot_create(
        self, id=None, tag_name=None, snapshot_name=None,
        wait=False, poll=5, timeout=300
    ):
        """
        description: Snapshot a Droplet

            At the time of this writing, snapshotting by tag is not working properly and is not
            recommended.

        in:
            - id - number - Send only to reference a single Droplet by id
            - tag_name - string - Send only to reference all Droplets with this tag.
            - wait - boolean - Whether to wait until the droplet is ready
            - poll - number - Number of seconds between checks (min 1 sec)
            - timeout - number - How many seconds before giving up

        out:
            If by id, an Action dict. If by tag, a list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#snapshot-a-droplet
        """  # nopep8
        if snapshot_name is None:
            raise ValueError("snapshot_name must be specified")

        return self.action(
            id=id, tag_name=tag_name, type="snapshot", attribs={"name": snapshot_name},
            wait=wait, poll=poll, timeout=timeout
        )

    def action_list(self, id):
        """
        description: List all Droplet Actions

            Droplet actions are tasks that can be executed on a Droplet. These can be things like
            rebooting, resizing, snapshotting, etc.

            Droplet action requests are generally targeted at one of the "actions" endpoints for a
            specific Droplet. The specific actions are usually initiated by sending a POST request
            with the action and arguments as parameters.

            Droplet action requests create a Droplet actions dict, which can be used to get
            information about the status of an action. Creating a Droplet action is asynchronous.
            The HTTP call will return the action dict before the action has finished processing
            on the Droplet. The current status of an action can be retrieved from either the
            Droplet actions endpoint or the global actions endpoint. If a Droplet action is
            uncompleted it may block the creation of a subsequent action for that Droplet, the
            locked attribute of the Droplet will be true and attempts to create a Droplet action
            will fail with a status of 422.

        in:
            - id - number - The id of the Droplet

        out:
            A list of Action dict's:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#droplet-actions
        """  # nopep8
        uri = "%s/%s/actions" % (self.uri, id)
        return self.pages(uri, "actions")

    def action_info(self, id, action_id):
        """
        description: Retrieve a Droplet Action

        in:
            - id - number - The id of the Droplet
            - action_id - number - The id of the Action

        out:
            An Action dict:
                - id - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.
                - status - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".
                - type - string - The type of action that the event is executing (reboot, power_off, etc.).
                - started_at - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.
                - completed_at - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.
                - resource_id - number - A unique identifier for the resource that the action is associated with.
                - resource_type - string - The type of resource that the action is associated with.
                - region - nullable string - (deprecated) A slug representing the region where the action occurred.
                - region_slug - nullable string - A slug representing the region where the action occurred.

        related: https://developers.digitalocean.com/documentation/v2/#retrieve-a-droplet-action
        """  # nopep8
        uri = "%s/%s/actions/%s" % (self.uri, id, action_id)
        return self.request(uri, "action")
