.. DOBOTO documentation sub class file, created bysphinxter.py.

FloatingIP (do.floating_ip)
============================================

Floating IP dict's represent a publicly-accessible static IP addresses that can be mapped to one of your Droplets. They can be used to create highly available setups or other configurations requiring movable addresses.

Floating IPs are bound to a specific region.


List all Floating IPs
----------------------------------------------------------------------------------------------------

.. method:: do.floating_ip.list()


Returns:

- A list of Floating IP dict's

  - *ip* - string - The public IP address of the Floating IP. It also serves as its identifier.

  - *region* - dict - The region that the Floating IP is reserved to. When you query a Floating IP, the entire region dict will be returned.

  - *droplet* - dict - The Droplet that the Floating IP has been assigned to. When you query a Floating IP, if it is assigned to a Droplet, the entire Droplet dict will be returned. If it is not assigned, the value will be null.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-floating-ips>`_



Create a new Floating IP assigned to a Droplet or Region
----------------------------------------------------------------------------------------------------

.. method:: do.floating_ip.create(droplet_id=None, region=None)

- *droplet_id* - int - The ID of Droplet that the Floating IP will be assigned to.

- *region* - string - The slug identifier for the region the Floating IP will be reserved to.


Returns:

- A Floating IP dict

  - *ip* - string - The public IP address of the Floating IP. It also serves as its identifier.

  - *region* - dict - The region that the Floating IP is reserved to. When you query a Floating IP, the entire region dict will be returned.

  - *droplet* - dict - The Droplet that the Floating IP has been assigned to. When you query a Floating IP, if it is assigned to a Droplet, the entire Droplet dict will be returned. If it is not assigned, the value will be null.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-floating-ip-assigned-to-a-droplet>`_

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-floating-ip-reserved-to-a-region>`_



Retrieve an existing Floating IP
----------------------------------------------------------------------------------------------------

.. method:: do.floating_ip.info(ip)

- *ip* - string - The public IP address of the Floating IP.


Returns:

- A Floating IP dict

  - *ip* - string - The public IP address of the Floating IP. It also serves as its identifier.

  - *region* - dict - The region that the Floating IP is reserved to. When you query a Floating IP, the entire region dict will be returned.

  - *droplet* - dict - The Droplet that the Floating IP has been assigned to. When you query a Floating IP, if it is assigned to a Droplet, the entire Droplet dict will be returned. If it is not assigned, the value will be null.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-floating-ip>`_



Delete a Floating IP
----------------------------------------------------------------------------------------------------

.. method:: do.floating_ip.destroy(ip)

- *ip* - string - The public IP address of the Floating IP.


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-floating-ips>`_



Assign a Floating IP to a Droplet
----------------------------------------------------------------------------------------------------

.. method:: do.floating_ip.assign(ip, droplet_id, wait=False, poll=5, timeout=300)

- *ip* - string - The public IP address of the Floating IP.

- *droplet_id* - int - The ID of Droplet that the Floating IP will be assigned to.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique numeric ID that can be used to identify and reference an action.

  - *status* - string - The current status of the action. This can be "in-progress", "completed", or "errored".

  - *type* - string - This is the type of action that the dict represents. For example, this could be "assign_ip" to represent the state of a Floating IP assign action.

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#assign-a-floating-ip-to-a-droplet>`_



Unassign a Floating IP
----------------------------------------------------------------------------------------------------

.. method:: do.floating_ip.unassign(ip, wait=False, poll=5, timeout=300)

- *ip* - string - The public IP address of the Floating IP.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- An Action dict

  - *id* - number - A unique numeric ID that can be used to identify and reference an action.

  - *status* - string - The current status of the action. This can be "in-progress", "completed", or "errored".

  - *type* - string - This is the type of action that the dict represents. For example, this could be "assign_ip" to represent the state of a Floating IP assign action.

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#unassign-a-floating-ip>`_



List all actions for a Floating IP
----------------------------------------------------------------------------------------------------

.. method:: do.floating_ip.action_list(ip)

- *ip* - string - The public IP address of the Floating IP.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks

- *timeout* - number - How many seconds before giving up


Returns:

- A list of Action dict's

  - *id* - number - A unique numeric ID that can be used to identify and reference an action.

  - *status* - string - The current status of the action. This can be "in-progress", "completed", or "errored".

  - *type* - string - This is the type of action that the dict represents. For example, this could be "assign_ip" to represent the state of a Floating IP assign action.

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-actions-for-a-floating-ip>`_



Retrieve an existing Floating IP Action
----------------------------------------------------------------------------------------------------

.. method:: do.floating_ip.action_info(ip, action_id)

- *ip* - string - The public IP address of the Floating IP.

- *action_id* - number - The id of the Action


Returns:

- An Action dict

  - *id* - number - A unique numeric ID that can be used to identify and reference an action.

  - *status* - string - The current status of the action. This can be "in-progress", "completed", or "errored".

  - *type* - string - This is the type of action that the dict represents. For example, this could be "assign_ip" to represent the state of a Floating IP assign action.

  - *started_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was initiated.

  - *completed_at* - string - A time value given in ISO8601 combined date and time format that represents when the action was completed.

  - *resource_id* - number - A unique identifier for the resource that the action is associated with.

  - *resource_type* - string - The type of resource that the action is associated with.

  - *region* - nullable string - (deprecated) A slug representing the region where the action occurred.

  - *region_slug* - nullable string - A slug representing the region where the action occurred.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-floating-ip-action>`_

