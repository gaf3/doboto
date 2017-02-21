.. DOBOTO documentation sub class file, created bysphinxter.py.

Tag (do.tag)
============================================

A Tag is a label that can be applied to a resource (currently only Droplets) in order to better organize or facilitate the lookups and actions on it.

Tags have two attributes, a user defined name attribute and an embedded resources attribute with information about resources that have been taggedself.


List all tags
----------------------------------------------------------------------------------------------------


Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is droplet id.


.. method:: do.tag.list()


Returns:

- A list of Tag dict's

  - *name* - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.

  - *resources* - list - An list of Resource dict's

    - *resource_id* - string - The identifier of a resource

    - *resource_type* - string - The type of the resource



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-tags>`_



List all tag names
----------------------------------------------------------------------------------------------------

.. method:: do.tag.name_list()


Returns:

- A list of Tag names



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-tags>`_



Create a new Tag
----------------------------------------------------------------------------------------------------


Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is droplet id.


.. method:: do.tag.create(name)

- *name* - string - name of the Tag


Returns:

- A Tag dict

  - *name* - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.

  - *resources* - list - An list of Resource dict's

    - *resource_id* - string - The identifier of a resource

    - *resource_type* - string - The type of the resource



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-tag>`_



Create a new Tag if not already present
----------------------------------------------------------------------------------------------------


Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is droplet id.


.. method:: do.tag.present(name)

- *name* - string - name of the Tag


Returns:

- A tuple of Tag dict's, the intended and created (None if already exists)

  - *name* - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.

  - *resources* - list - An list of Resource dict's

    - *resource_id* - string - The identifier of a resource

    - *resource_type* - string - The type of the resource



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-tag>`_



Retrieve a Tag
----------------------------------------------------------------------------------------------------


Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is droplet id.


.. method:: do.tag.info(name)

- *name* - string - name of the Tag


Returns:

- A Tag dict

  - *name* - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.

  - *resources* - list - An list of Resource dict's

    - *resource_id* - string - The identifier of a resource

    - *resource_type* - string - The type of the resource



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-a-tag>`_



Update a Tag
----------------------------------------------------------------------------------------------------


Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is droplet id.


.. method:: do.tag.update(name, new_name)

- *name* - string - name of the Tag currently

- *new_name* - string - desired name of the Tag


Returns:

- A Tag dict

  - *name* - string - Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag.

  - *resources* - list - An list of Resource dict's

    - *resource_id* - string - The identifier of a resource

    - *resource_type* - string - The type of the resource



Related:

* `<https://developers.digitalocean.com/documentation/v2/#update-a-tag>`_



Delete a Tag
----------------------------------------------------------------------------------------------------

.. method:: do.tag.destroy(name)

- *name* - string - name of the Tag


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-tag>`_



Tag a Resorce
----------------------------------------------------------------------------------------------------


Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is droplet id.


.. method:: do.tag.attach(name, resources)

- *name* - string - name of the Tag

- *resources* - list - An list of Resource dict's

  - *resource_id* - string - The identifier of a resource

  - *resource_type* - string - The type of the resource


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#tag-a-resource>`_



Untag a Resource
----------------------------------------------------------------------------------------------------


Currently only a resource_type of 'droplet' is supported.  Thus, resource_id is droplet id.


.. method:: do.tag.detach(name, resources)

- *name* - string - name of the Tag

- *resources* - list - An list of Resource dict's

  - *resource_id* - string - The identifier of a resource

  - *resource_type* - string - The type of the resource


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#untag-a-resource>`_

