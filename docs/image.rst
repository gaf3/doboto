.. DOBOTO documentation sub class file, created bysphinxter.py.

Image (do.image)
============================================

Images in DigitalOcean may refer to one of a few different kinds of dict's.

An image may refer to a snapshot that has been taken of a Droplet instance. It may also mean an image representing an automatic backup of a Droplet. The third category that it can represent is a public Linux distribution or application image that is used as a base to create Droplets.


List all, distribution, application, or user images.
----------------------------------------------------------------------------------------------------

.. method:: do.image.list(type=None, private=None)

- *type* - string - Can be "distribution" or "application" for images thereof.

- *private* - boolean - Set to True for user images


Returns:

- A list of Image dict's

  - *id* - number - A unique number that can be used to identify and reference a specific image.

  - *name* - string - The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question.

  - *type* - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".

  - *distribution* - string - This attribute describes the base distribution used for this image.

  - *slug* - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.

  - *public* - boolean - This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account.

  - *regions* - list - This attribute is a list of the regions that the image is available in. The regions are represented by their identifying slug values.

  - *min_disk_size* - number - The minimum 'disk' required for a size to use this image.

  - *size_gigabytes* - number - The size of the image in gigabytes.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-images>`_

* `<https://developers.digitalocean.com/documentation/v2/#list-all-distribution-images>`_

* `<https://developers.digitalocean.com/documentation/v2/#list-all-application-images>`_

* `<https://developers.digitalocean.com/documentation/v2/#list-a-user-s-images>`_



Retrieve an existing image by id or slug
----------------------------------------------------------------------------------------------------

.. method:: do.image.info(id_slug)

- *id_slug* - number / string - id or slug of the Image


Returns:

- An Image dict

  - *id* - number - A unique number that can be used to identify and reference a specific image.

  - *name* - string - The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question.

  - *type* - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".

  - *distribution* - string - This attribute describes the base distribution used for this image.

  - *slug* - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.

  - *public* - boolean - This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account.

  - *regions* - list - This attribute is a list of the regions that the image is available in. The regions are represented by their identifying slug values.

  - *min_disk_size* - number - The minimum 'disk' required for a size to use this image.

  - *size_gigabytes* - number - The size of the image in gigabytes.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-image-by-id>`_

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-image-by-slug>`_



Update an Image
----------------------------------------------------------------------------------------------------

.. method:: do.image.update(id, name)

- *id* - number - id of the Image

- *name* - string - The new name that you would like to use for the image.


Returns:

- An Image dict

  - *id* - number - A unique number that can be used to identify and reference a specific image.

  - *name* - string - The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question.

  - *type* - string - The kind of image, describing the duration of how long the image is stored. This is either "snapshot" or "backup".

  - *distribution* - string - This attribute describes the base distribution used for this image.

  - *slug* - nullable string - A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id.

  - *public* - boolean - This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account.

  - *regions* - list - This attribute is a list of the regions that the image is available in. The regions are represented by their identifying slug values.

  - *min_disk_size* - number - The minimum 'disk' required for a size to use this image.

  - *size_gigabytes* - number - The size of the image in gigabytes.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Image was created.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#update-an-image>`_



Delete an Image
----------------------------------------------------------------------------------------------------

.. method:: do.image.destroy(id)

- *id* - number - id of the Image


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-an-image>`_



Transfer an Image to another Region
----------------------------------------------------------------------------------------------------

.. method:: do.image.transfer(id, region, wait=False, poll=5, timeout=300)

- *id* - number - id of the Image

- *region* - string - The region slug that represents the region target.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dictt

  - *id* - number - A unique numeric ID that can be used to identify and reference an image action.

  - *status* - string - The current status of the image action. This will be either "in-progress", "completed", or "errored".

  - *type* - string - This is the type of the image action that the JSON dict represents. For example, this could be "transfer" to represent the state of an image transfer action.

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#transfer-an-image>`_



Convert an Image to a Snapshot
----------------------------------------------------------------------------------------------------

.. method:: do.image.convert(id, wait=False, poll=5, timeout=300)

- *id* - number - id of the Image

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique numeric ID that can be used to identify and reference an image action.

  - *status* - string - The current status of the image action. This will be either "in-progress", "completed", or "errored".

  - *type* - string - This is the type of the image action that the JSON dict represents. For example, this could be "transfer" to represent the state of an image transfer action.

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#convert-an-image-to-a-snapshot>`_



List all actions for an Image
----------------------------------------------------------------------------------------------------

.. method:: do.image.action_list(id)

- *id* - number - id of the Image


Returns:

- A list of Action dict's

  - *id* - number - A unique numeric ID that can be used to identify and reference an image action.

  - *status* - string - The current status of the image action. This will be either "in-progress", "completed", or "errored".

  - *type* - string - This is the type of the image action that the JSON dict represents. For example, this could be "transfer" to represent the state of an image transfer action.

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-actions-for-an-image>`_



Retrieve an existing Image Action
----------------------------------------------------------------------------------------------------

.. method:: do.image.action_info(id, action_id)

- *id* - number - id of the Image

- *action_id* - number - id of the Action


Returns:

- An Action dict

  - *id* - number - A unique numeric ID that can be used to identify and reference an image action.

  - *status* - string - The current status of the image action. This will be either "in-progress", "completed", or "errored".

  - *type* - string - This is the type of the image action that the JSON dict represents. For example, this could be "transfer" to represent the state of an image transfer action.

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-image-action>`_

