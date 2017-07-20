.. DOBOTO documentation sub class file, created bysphinxter.py.

Snapshot (do.snapshot)
============================================

Snapshots are saved instances of a Droplet or a volume, which is reflected in the resource_type attribute. In order to avoid problems with compressing filesystems, each defines a min_disk_size attribute which is the minimum size of the Droplet or volume disk when creating a new resource from the saved snapshot.

Data Structures
-----------------------

Snapshot
^^^^^^^^^^^^^^^^^^^^^^^^^

- *id* - string - The unique identifier for the snapshot.

- *name* - string - A human-readable name for the snapshot.

- *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the snapshot was created.

- *regions* - list - A list of the regions that the image is available in. The regions are represented by their identifying slug values.

- *resource_id* - string - A unique identifier for the resource that the action is associated with.

- *resource_type* - string - The type of resource that the action is associated with.

- *min_disk_size* - number - The minimum size in GB required for a volume or Droplet to use this snapshot.

- *size_gigabytes* - number - The billable size of the snapshot in gigabytes.



List all, droplet, or volume snapshots
----------------------------------------------------------------------------------------------------

.. method:: do.snapshot.list(resource_type=None)

- *resource_type* - string - Can be "droplet" or "volume" for snapshots thereof.


Returns:

- A list of Snapshot data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-snapshots>`_

* `<https://developers.digitalocean.com/documentation/v2/#list-all-droplet-snapshots>`_

* `<https://developers.digitalocean.com/documentation/v2/#list-all-volume-snapshots>`_



Retrieve an existing snapshot by id
----------------------------------------------------------------------------------------------------

.. method:: do.snapshot.info(id)

- *id* - number - id of the Snapshot


Returns:

- A Snapshot data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-snapshot-by-id>`_



Delete a snapshot
----------------------------------------------------------------------------------------------------

.. method:: do.snapshot.destroy(id)

- *id* - number - id of the Snapshot


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-an-snapshot>`_

