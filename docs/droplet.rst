.. DOBOTO documentation sub class file, created bysphinxter.py.

Droplet (do.droplet)
============================================

A Droplet is a DigitalOcean virtual machine. With this class, you can list, create, or delete Droplets.

Some of the attributes will have an dict value. The region and image dict's will all contain the standard attributes of their associated types. Find more information about each of these dict's in their respective sections.


List all Droplets or all Droplets with a specific Tag.
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.list(tag_name=None)

- *tag_name* - string - Send to retrieve Droplet with this tag.


Returns:

- A list of Droplet dict's

  - *id* - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.

  - *name* - string - The human-readable name set for the Droplet instance.

  - *memory* - number - Memory of the Droplet in megabytes.

  - *vcpus* - number - The number of virtual CPUs.

  - *disk* - number - The size of the Droplet's disk in gigabytes.

  - *locked* - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.

  - *status* - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".

  - *backup_ids* - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.

  - *snapshot_ids* - list - A list of snapshot IDs of any snapshots created from the Droplet instance.

  - *features* - list - A list of features enabled on this Droplet.

  - *region* - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.

  - *image* - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.

  - *size* - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.

  - *size_slug* - string - The unique slug identifier for the size of this Droplet.

  - *networks* - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.

  - *kernel* - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.

  - *next_backup_window* - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.

  - *tags* - list - A list of Tags the Droplet has been tagged with.

  - *volume_ids* - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-droplets>`_

* `<https://developers.digitalocean.com/documentation/v2/#listing-droplets-by-tag>`_



List Neighbors for a Droplet running on the same physical server
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.neighbor_list(id)

- *id* - number - The id of the Droplet


Returns:

- A list of Droplet dict's

  - *id* - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.

  - *name* - string - The human-readable name set for the Droplet instance.

  - *memory* - number - Memory of the Droplet in megabytes.

  - *vcpus* - number - The number of virtual CPUs.

  - *disk* - number - The size of the Droplet's disk in gigabytes.

  - *locked* - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.

  - *status* - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".

  - *backup_ids* - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.

  - *snapshot_ids* - list - A list of snapshot IDs of any snapshots created from the Droplet instance.

  - *features* - list - A list of features enabled on this Droplet.

  - *region* - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.

  - *image* - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.

  - *size* - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.

  - *size_slug* - string - The unique slug identifier for the size of this Droplet.

  - *networks* - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.

  - *kernel* - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.

  - *next_backup_window* - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.

  - *tags* - list - A list of Tags the Droplet has been tagged with.

  - *volume_ids* - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-neighbors-for-a-droplet>`_



List all Droplet Neighbors, any droplets that are running on the same physical hardware
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.droplet_neighbor_list()


Returns:

- A list of neighbor lists of Droplet dict's

  - *id* - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.

  - *name* - string - The human-readable name set for the Droplet instance.

  - *memory* - number - Memory of the Droplet in megabytes.

  - *vcpus* - number - The number of virtual CPUs.

  - *disk* - number - The size of the Droplet's disk in gigabytes.

  - *locked* - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.

  - *status* - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".

  - *backup_ids* - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.

  - *snapshot_ids* - list - A list of snapshot IDs of any snapshots created from the Droplet instance.

  - *features* - list - A list of features enabled on this Droplet.

  - *region* - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.

  - *image* - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.

  - *size* - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.

  - *size_slug* - string - The unique slug identifier for the size of this Droplet.

  - *networks* - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.

  - *kernel* - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.

  - *next_backup_window* - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.

  - *tags* - list - A list of Tags the Droplet has been tagged with.

  - *volume_ids* - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-droplet-neighbors>`_



Create a new Droplet or multiple Droplets
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.create(attribs, wait=False, poll=5, timeout=300)

- *attribs* - dict - The data of the Droplet

  - *name* - string - The human-readable string you wish to use when displaying the Droplet name. The name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. The name set during creation will also determine the hostname for the Droplet in its internal configuration. - if single droplet

  - *names* - list - A list of human human-readable strings you wish to use when displaying the Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. Each name set during creation will also determine the hostname for the Droplet in its internal configuration. - if multiple droplets

  - *region* - string - The unique slug identifier for the region that you wish to deploy in. - true

  - *size* - string - The unique slug identifier for the size that you wish to select for this Droplet. - true

  - *image* - number (if using an image ID), or String (if using a public image slug) - The image ID of a public or private image, or the unique slug identifier for a public image. This image will be the base image for your Droplet. - true

  - *ssh_keys* - list - A list containing the IDs or fingerprints of the SSH keys that you wish to embed in the Droplet's root account upon creation. -

  - *backups* - bool - A boolean indicating whether automated backups should be enabled for the Droplet. Automated backups can only be enabled when the Droplet is created. -

  - *ipv6* - bool - A boolean indicating whether IPv6 is enabled on the Droplet. -

  - *private_networking* - bool - A boolean indicating whether private networking is enabled for the Droplet. Private networking is currently only available in certain regions. -

  - *user_data* - string - A string of the desired User Data for the Droplet. User Data is currently only available in regions with metadata listed in their features. -

  - *monitoring* - bool - A boolean indicating whether to install the DigitalOcean agent for monitoring. -

  - *volume* - list - A flat list including the unique string identifier for each Block Storage volume to be attached to the Droplet. At the moment a volume can only be attached to a single Droplet. -

  - *tags* - list - A flat list of tag names as strings to apply to the Droplet after it is created. Tag names can either be existing or new tags.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- A Droplet dict if name is sent, or a list of Droplet dict's in names is sent

  - *id* - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.

  - *name* - string - The human-readable name set for the Droplet instance.

  - *memory* - number - Memory of the Droplet in megabytes.

  - *vcpus* - number - The number of virtual CPUs.

  - *disk* - number - The size of the Droplet's disk in gigabytes.

  - *locked* - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.

  - *status* - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".

  - *backup_ids* - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.

  - *snapshot_ids* - list - A list of snapshot IDs of any snapshots created from the Droplet instance.

  - *features* - list - A list of features enabled on this Droplet.

  - *region* - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.

  - *image* - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.

  - *size* - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.

  - *size_slug* - string - The unique slug identifier for the size of this Droplet.

  - *networks* - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.

  - *kernel* - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.

  - *next_backup_window* - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.

  - *tags* - list - A list of Tags the Droplet has been tagged with.

  - *volume_ids* - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-droplet>`_

* `<https://developers.digitalocean.com/documentation/v2/#create-multiple-droplets>`_



Create a new Droplet or multiple Droplets if not already existing
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.present(attribs, wait=False, poll=5, timeout=300)

- *attribs* - dict - The data of the Droplet

  - *name* - string - The human-readable string you wish to use when displaying the Droplet name. The name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. The name set during creation will also determine the hostname for the Droplet in its internal configuration. - if single droplet

  - *names* - list - A list of human human-readable strings you wish to use when displaying the Droplet name. Each name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. Each name set during creation will also determine the hostname for the Droplet in its internal configuration. - if multiple droplets

  - *region* - string - The unique slug identifier for the region that you wish to deploy in. - true

  - *size* - string - The unique slug identifier for the size that you wish to select for this Droplet. - true

  - *image* - number (if using an image ID), or String (if using a public image slug) - The image ID of a public or private image, or the unique slug identifier for a public image. This image will be the base image for your Droplet. - true

  - *ssh_keys* - list - A list containing the IDs or fingerprints of the SSH keys that you wish to embed in the Droplet's root account upon creation. -

  - *backups* - bool - A boolean indicating whether automated backups should be enabled for the Droplet. Automated backups can only be enabled when the Droplet is created. -

  - *ipv6* - bool - A boolean indicating whether IPv6 is enabled on the Droplet. -

  - *private_networking* - bool - A boolean indicating whether private networking is enabled for the Droplet. Private networking is currently only available in certain regions. -

  - *user_data* - string - A string of the desired User Data for the Droplet. User Data is currently only available in regions with metadata listed in their features. -

  - *monitoring* - bool - A boolean indicating whether to install the DigitalOcean agent for monitoring. -

  - *volume* - list - A flat list including the unique string identifier for each Block Storage volume to be attached to the Droplet. At the moment a volume can only be attached to a single Droplet. -

  - *tags* - list - A flat list of tag names as strings to apply to the Droplet after it is created. Tag names can either be existing or new tags.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- A tuple of two Droplet dict's if name is sent (second is None if already present), or a tuple of two lists of Droplet dict's if names is sent, the first being all, the second being those created, (empty if all are present)

  - *id* - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.

  - *name* - string - The human-readable name set for the Droplet instance.

  - *memory* - number - Memory of the Droplet in megabytes.

  - *vcpus* - number - The number of virtual CPUs.

  - *disk* - number - The size of the Droplet's disk in gigabytes.

  - *locked* - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.

  - *status* - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".

  - *backup_ids* - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.

  - *snapshot_ids* - list - A list of snapshot IDs of any snapshots created from the Droplet instance.

  - *features* - list - A list of features enabled on this Droplet.

  - *region* - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.

  - *image* - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.

  - *size* - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.

  - *size_slug* - string - The unique slug identifier for the size of this Droplet.

  - *networks* - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.

  - *kernel* - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.

  - *next_backup_window* - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.

  - *tags* - list - A list of Tags the Droplet has been tagged with.

  - *volume_ids* - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.



Retrieve an existing Droplet by id
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.info(id)

- *id* - number - The id of the Droplet to retrieve


Returns:

- A Droplet dict

  - *id* - number - A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation.

  - *name* - string - The human-readable name set for the Droplet instance.

  - *memory* - number - Memory of the Droplet in megabytes.

  - *vcpus* - number - The number of virtual CPUs.

  - *disk* - number - The size of the Droplet's disk in gigabytes.

  - *locked* - boolean - A boolean value indicating whether the Droplet has been locked, preventing actions by users.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Droplet was created.

  - *status* - string - A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".

  - *backup_ids* - list - A list of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation.

  - *snapshot_ids* - list - A list of snapshot IDs of any snapshots created from the Droplet instance.

  - *features* - list - A list of features enabled on this Droplet.

  - *region* - dict - The region that the Droplet instance is deployed in. When setting a region, the value should be the slug identifier for the region. When you query a Droplet, the entire region dict will be returned.

  - *image* - dict - The base image used to create the Droplet instance. When setting an image, the value is set to the image id or slug. When querying the Droplet, the entire image dict will be returned.

  - *size* - dict - The current size dict describing the Droplet. When setting a size, the value is set to the size slug. When querying the Droplet, the entire size dict will be returned. Note that the disk volume of a droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.

  - *size_slug* - string - The unique slug identifier for the size of this Droplet.

  - *networks* - dict - The details of the network that are configured for the Droplet instance. This is an dict that contains keys for IPv4 and IPv6. The value of each of these is a list that contains dict's describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.

  - *kernel* - nullable dict - The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.

  - *next_backup_window* - nullable dict - The details of the Droplet's backups feature, if backups are configured for the Droplet. This dict contains keys for the start and end times of the window during which the backup will start.

  - *tags* - list - A list of Tags the Droplet has been tagged with.

  - *volume_ids* - list - A flat list including the unique identifier for each Block Storage volume attached to the Droplet.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-droplet-by-id>`_



Delete a Droplet by id or Droplets by tag
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.destroy(id=None, tag_name=None)

- *id* - number - Send only to destroy a single Droplet by id

- *tag_name* - string - Send only to destroy all Droplets with this tag.


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-droplet>`_

* `<https://developers.digitalocean.com/documentation/v2/#deleting-droplets-by-tag>`_



List backups for a Droplet
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.backup_list(id)

- *id* - number - The id of the Droplet


Returns:

- A list of Backup dict's

  - *id* - number - A unique number used to identify and reference a specific image.

  - *name* - string - The display name of the image. This is shown in the web UI and is generally a descriptive title for the image in question.

  - *type* - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".

  - *distribution* - string - The base distribution used for this image.

  - *slug* - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.

  - *public* - boolean - A boolean value that indicates whether the image in question is public. An image that is public is available to all accounts. A non-public image is only accessible from your account.

  - *regions* - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.

  - *min_disk_size* - number - The minimum 'disk' required for a size to use this image.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-backups-for-a-droplet>`_



Enable Backups
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.backup_enable(id=None, tag_name=None, wait=False, poll=5, timeout=300)

- *id* - number - Send only to reference a single Droplet by id

- *tag_name* - string - Send only to reference all Droplets with this tag.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- If by id, an Action dict. If by tag, a list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#enable-backups>`_



Disable Backups
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.backup_disable(id=None, tag_name=None, wait=False, poll=5, timeout=300)

- *id* - number - Send only to reference a single Droplet by id

- *tag_name* - string - Send only to reference all Droplets with this tag.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- If by id, an Action dict. If by tag, a list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#disable-backups>`_



Reboot a Droplet
----------------------------------------------------------------------------------------------------


A reboot action is an attempt to reboot the Droplet in a graceful way, similar to using the reboot command from the console.


.. method:: do.droplet.reboot(id, wait=False, poll=5, timeout=300)

- *id* - number - The id of the Droplet

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#reboot-a-droplet>`_



Shutdown a Droplet
----------------------------------------------------------------------------------------------------


A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the shutdown command from the console. Since a shutdown command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a power off action to ensure the Droplet is off.


.. method:: do.droplet.shutdown(id=None, tag_name=None, wait=False, poll=5, timeout=300)

- *id* - number - Send only to reference a single Droplet by id

- *tag_name* - string - Send only to reference all Droplets with this tag.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- If by id, an Action dict. If by tag, a list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#reboot-a-droplet>`_



Power On a Droplet
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.power_on(id=None, tag_name=None, wait=False, poll=5, timeout=300)

- *id* - number - Send only to reference a single Droplet by id

- *tag_name* - string - Send only to reference all Droplets with this tag.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- If by id, an Action dict. If by tag, a list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#power-on-a-droplet>`_



Power Off a Droplet
----------------------------------------------------------------------------------------------------


A power_off event is a hard shutdown and should only be used if the shutdown action is not successful. It is similar to cutting the power on a server and could lead to complications.


.. method:: do.droplet.power_off(id=None, tag_name=None, wait=False, poll=5, timeout=300)

- *id* - number - Send only to reference a single Droplet by id

- *tag_name* - string - Send only to reference all Droplets with this tag.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- If by id, an Action dict. If by tag, a list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#power-off-a-droplet>`_



Power Cycle a Droplet
----------------------------------------------------------------------------------------------------


A powercycle action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.


.. method:: do.droplet.power_cycle(id=None, tag_name=None, wait=False, poll=5, timeout=300)

- *id* - number - Send only to reference a single Droplet by id

- *tag_name* - string - Send only to reference all Droplets with this tag.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- If by id, an Action dict. If by tag, a list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#power-cycle-a-droplet>`_



Restore a Droplet
----------------------------------------------------------------------------------------------------


A Droplet restoration will rebuild an image using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.


.. method:: do.droplet.restore(id, image, wait=False, poll=5, timeout=300)

- *id* - number - The id of the Droplet

- *image* - string if an image slug. number if an image ID. - An image slug or ID. This represents the image that the Droplet will use as a base.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#restore-a-droplet>`_



Password Reset a Droplet
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.password_reset(id, wait=False, poll=5, timeout=300)

- *id* - number - The id of the Droplet

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#password-reset-a-droplet>`_



Resize a Droplet
----------------------------------------------------------------------------------------------------


If a permanent resize, with disk changes included, is desired, set the "disk" attribute to True. The Droplet must be powered off prior to resizing.


.. method:: do.droplet.resize(id, size, disk=False, wait=False, poll=5, timeout=300)

- *id* - number - The id of the Droplet

- *disk* - bool - Whether to increase disk size

- *size* - string - The size slug that you want to resize to. - true

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#resize-a-droplet>`_



Rebuild a Droplet
----------------------------------------------------------------------------------------------------


A rebuild action functions just like a new create.


.. method:: do.droplet.rebuild(id, image, wait=False, poll=5, timeout=300)

- *id* - number - The id of the Droplet

- *image* - string if an image slug. number if an image ID. - An image slug or ID. This represents the image that the Droplet will use as a base.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#rebuild-a-droplet>`_



Rename a Droplet
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.rename(id, name, wait=False, poll=5, timeout=300)

- *id* - number - The id of the Droplet

- *name* - string - The new name for the Droplet.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#rename-a-droplet>`_



List all available Kernels for a Droplet
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.kernel_list(id)

- *id* - number - The id of the Droplet


Returns:

- A list of Kernel dict's

  - *id* - number - A unique number used to identify and reference a specific kernel.

  - *name* - string - The display name of the kernel. This is shown in the web UI and is generally a descriptive title for the kernel in question.

  - *version* - string - A standard kernel version string representing the version, patch, and release information.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-available-kernels-for-a-droplet>`_



Change the Kernel
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.kernel_update(id, kernel_id, wait=False, poll=5, timeout=300)

- *id* - number - The id of the Droplet

- *kernel* - number - A unique number used to identify and reference a specific kernel. - true

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#change-the-kernel>`_



Enable IPv6
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.ipv6_enable(id=None, tag_name=None, wait=False, poll=5, timeout=300)

- *id* - number - Send only to reference a single Droplet by id

- *tag_name* - string - Send only to reference all Droplets with this tag.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- If by id, an Action dict. If by tag, a list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#enable-ipv6>`_



Enable Private Networking
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.private_networking_enable(id=None, tag_name=None, wait=False, poll=5, timeout=300)

- *id* - number - Send only to reference a single Droplet by id

- *tag_name* - string - Send only to reference all Droplets with this tag.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- If by id, an Action dict. If by tag, a list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#enable-private-networking>`_



List snapshots for a Droplet
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.snapshot_list(id)

- *id* - number - The id of the Droplet


Returns:

- A list of Image dict's

  - *id* - number - A unique number used to identify and reference a specific image.

  - *name* - string - The display name of the image. This is shown in the web UI and is generally a descriptive title for the image in question.

  - *type* - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".

  - *distribution* - string - The base distribution used for this image.

  - *slug* - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.

  - *public* - boolean - A boolean value that indicates whether the image in question is public. An image that is public is available to all accounts. A non-public image is only accessible from your account.

  - *regions* - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.

  - *min_disk_size* - number - The minimum 'disk' required for a size to use this image.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-snapshots-for-a-droplet>`_



List all Droplet Actions
----------------------------------------------------------------------------------------------------


Droplet actions are tasks that can be executed on a Droplet. These can be things like rebooting, resizing, snapshotting, etc.

Droplet action requests are generally targeted at one of the "actions" endpoints for a specific Droplet. The specific actions are usually initiated by sending a POST request with the action and arguments as parameters.

Droplet action requests create a Droplet actions dict, which can be used to get information about the status of an action. Creating a Droplet action is asynchronous. The HTTP call will return the action dict before the action has finished processing on the Droplet. The current status of an action can be retrieved from either the Droplet actions endpoint or the global actions endpoint. If a Droplet action is uncompleted it may block the creation of a subsequent action for that Droplet, the locked attribute of the Droplet will be true and attempts to create a Droplet action will fail with a status of 422.


.. method:: do.droplet.action_list(id)

- *id* - number - The id of the Droplet


Returns:

- A list of Action dict's

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#droplet-actions>`_



Retrieve a Droplet Action
----------------------------------------------------------------------------------------------------

.. method:: do.droplet.action_info(id, action_id)

- *id* - number - The id of the Droplet

- *action_id* - number - The id of the Action


Returns:

- An Action dict

  - *id* - number - A unique identifier for each Droplet action event. This is used to reference a specific action that was requested.

  - *status* - string - The current status of the action. The value of this attribute will be "in-progress", "completed", or "errored".

  - *type* - string - The type of action that the event is executing (reboot, power_off, etc.).

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-a-droplet-action>`_

