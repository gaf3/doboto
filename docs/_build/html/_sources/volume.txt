.. DOBOTO documentation sub class file, created bysphinxter.py.

Volume (do.volume)
============================================

Block Storage volumes provide expanded storage capacity for your Droplets and can be moved between Droplets within a specific region. Volumes function as raw block devices, meaning they appear to the operating system as locally attached storage which can be formatted using any file system supported by the OS. They may be created in sizes from 1GiB to 16TiB.

Data Structures
-----------------------

Volume
^^^^^^^^^^^^^^^^^^^^^^^^^

- *id* - string - The unique identifier for the Block Storage volume.

- *region* - dict - The region that the Block Storage volume is located in. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned.

- *droplet_ids* - list - A list containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet.

- *name* - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.

- *description* - string - An optional free-form text field to describe a Block Storage volume.

- *size_gigabytes* - number - The size of the Block Storage volume in GiB (1024^3).

- *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Block Storage volume was created.

- *droplet_ids* - list - This attribute is a list of the Droplets that the volume is attached to.



List all volumes
----------------------------------------------------------------------------------------------------

.. method:: do.volume.list(region=None)

- *region* - string - Region slug for listing on snapshots from that region - optional


Returns:

- A list of Volume data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-block-storage-volumes>`_



Create a new volume
----------------------------------------------------------------------------------------------------

.. method:: do.volume.create(attribs, wait=False, poll=5, timeout=300)

- *attribs* - dict - Volume information to create by

  - *size_gigabytes* - number - The size of the Block Storage volume in GiB (1024^3). - required

  - *name* - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters. - required

  - *description* - string - An optional free-form text field to describe a Block Storage volume.

  - *region* - string - The region where the Block Storage volume will be created. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned. Should not be specified with a snapshot_id.

  - *snapshot_id* - string - The unique identifier for the volume snapshot from which to create the volume. Should not be specified with a region_id.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- A Volume data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-block-storage-volume>`_



Create a new volume if name not already present
----------------------------------------------------------------------------------------------------

.. method:: do.volume.present(attribs, wait=False, poll=5, timeout=300)

- *attribs* - dict - Volume information to create by

  - *size_gigabytes* - number - The size of the Block Storage volume in GiB (1024^3). - required

  - *name* - string - A human-readable name for the Block Storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters. - required

  - *description* - string - An optional free-form text field to describe a Block Storage volume.

  - *region* - string - The region where the Block Storage volume will be created. When setting a region, the value should be the slug identifier for the region. When you query a Block Storage volume, the entire region dict will be returned. Should not be specified with a snapshot_id.

  - *snapshot_id* - string - The unique identifier for the volume snapshot from which to create the volume. Should not be specified with a region_id.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- A tuple of Volume data structures, the intended and created (None if already exists)



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-block-storage-volume>`_



Retrieve an existing volume by id or name and region
----------------------------------------------------------------------------------------------------

.. method:: do.volume.info(id=None, name=None, region=None)

- *id* - number - The id of the volume

- *name* - string - The name of the volume if no id

- *region* - string - The region slug of the volume if no id


Returns:

- A Volume data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-block-storage-volume>`_

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-block-storage-volume-by-name>`_



Delete a volume by id or name and region
----------------------------------------------------------------------------------------------------

.. method:: do.volume.destroy(id=None, name=None, region=None)

- *id* - number - The id of the volume

- *name* - string - The name of the volume if no id

- *region* - string - The region slug of the volume if no id


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-block-storage-volume>`_

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-block-storage-volume-by-name>`_



List snapshots for a volume
----------------------------------------------------------------------------------------------------

.. method:: do.volume.snapshot_list(id)

- *id* - number - The id of the volume


Returns:

- A list of Image data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-snapshots-for-a-volume>`_



Create a snapshot for a volume
----------------------------------------------------------------------------------------------------

.. method:: do.volume.snapshot_create(id, snapshot_name, wait=False, poll=5, timeout=300)

- *id* - number - The id of the volume

- *snapshot_name* - string - The name of the snapshot

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- An Image data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-snapshot-from-a-volume>`_



Attach a volume by id or name to a droplet
----------------------------------------------------------------------------------------------------

.. method:: do.volume.attach(id=None, name=None, region=None, droplet_id=None, wait=False, poll=5, timeout=300)

- *id* - number - The id of the volume

- *name* - string - The name of the volume if no id

- *region* - string - The region slug of the volume if no id

- *droplet_id* - number - The id of the droplet

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- An Action data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#attach-a-block-storage-volume-to-a-droplet>`_

* `<https://developers.digitalocean.com/documentation/v2/#attach-a-block-storage-volume-to-a-droplet-by-name>`_



Remove a volume by id or name from a droplet
----------------------------------------------------------------------------------------------------

.. method:: do.volume.detach(id=None, name=None, region=None, droplet_id=None, wait=False, poll=5, timeout=300)

- *id* - number - The id of the volume

- *name* - string - The name of the volume if no id

- *region* - string - The region slug of the volume if no id

- *droplet_id* - number - The id of the droplet

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- An Action data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#remove-a-block-storage-volume-from-a-droplet>`_

* `<https://developers.digitalocean.com/documentation/v2/#remove-a-block-storage-volume-from-a-droplet-by-name>`_



Resize a volume
----------------------------------------------------------------------------------------------------

.. method:: do.volume.resize(id, size, region=None, wait=False, poll=5, timeout=300)

- *id* - number - The id of the volume

- *size_gigabytes* - int - The new size of the Block Storage volume in GiB (1024^3). - true

- *region* - string - The slug identifier for the region the volume is located in. -


Returns:

- An Action data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#resize-a-volume>`_



List all actions for a volume
----------------------------------------------------------------------------------------------------

.. method:: do.volume.action_list(id)

- *id* - number - The id of the volume


Returns:

- A list of Action data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-actions-for-a-volume>`_



Retrieve an existing volume action
----------------------------------------------------------------------------------------------------

.. method:: do.volume.action_info(id, action_id)

- *id* - number - The id of the volume

- *action_id* - number - The id of the action


Returns:

- An Action data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-volume-action>`_

