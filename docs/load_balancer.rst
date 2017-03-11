.. DOBOTO documentation sub class file, created bysphinxter.py.

LoadBalancer (do.load_balancer)
============================================

Load Balancers provide a way to distribute traffic across multiple Droplets. You can list, create, or delete Load Balancers as well as add or remove Droplets, forwarding rules, and other configuration details.

Data Structures
-----------------------

Health Check
^^^^^^^^^^^^^^^^^^^^^^^^^

- *protocol* - string - The protocol used for health checks sent to the backend Droplets. The possible values are "http" or "tcp".

- *port* - int - An integer representing the port on the backend Droplets on which the health check will attempt a connection.

- *path* - string - The path on the backend Droplets to which the Load Balancer instance will send a request.

- *check_interval_seconds* - int - The number of seconds between between two consecutive health checks.

- *response_timeout_seconds* - int - The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed.

- *unhealthy_threshold* - int - The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool.

- *healthy_threshold* - int - The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool.

Load Balancer
^^^^^^^^^^^^^^^^^^^^^^^^^

- *id* - string - A unique ID that can be used to identify and reference a Load Balancer.

- *name* - string - A human-readable name for a Load Balancer instance.

- *ip* - string - An attribute containing the public-facing IP address of the Load Balancer.

- *algorithm* - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections".

- *status* - string - A status string indicating the current state of the Load Balancer. This can be "new", "active", or "errored".

- *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the Load Balancer was created.

- *forwarding_rules* - list - Forwarding Role data structures

- *health_check* - list - Health check data structures

- *sticky_sessions* - list - Sticky Session data structures

- *region* - object - The region where the Load Balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned.

- *tag* - string - The name of a Droplet tag corresponding to Droplets assigned to the Load Balancer.

- *droplet_ids* - array of integers - An array containing the IDs of the Droplets assigned to the Load Balancer.

- *redirect_http_to_https* - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.

Forwaring Rule
^^^^^^^^^^^^^^^^^^^^^^^^^

- *entry_protocol* - string - The protocol used for traffic to the Load Balancer. The possible values are "http", "https", or "tcp".

- *entry_port* - int - An integer representing the port on which the Load Balancer instance will listen.

- *target_protocol* - string - The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are "http", "https", or "tcp".

- *target_port* - int - An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.

- *certificate_id* - string - The ID of the TLS certificate used for SSL termination if enabled.

- *tls_passthrough* - bool - A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets.

Sticky Session
^^^^^^^^^^^^^^^^^^^^^^^^^

- *type* - string - An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are "cookies" or "none".

- *cookie_name* - string - The name of the cookie sent to the client. This attribute is only returned when using "cookies" for the sticky sessions type.

- *cookie_ttl_seconds* - string - The number of seconds until the cookie set by the Load Balancer expires. This attribute is only returned when using "cookies" for the sticky sessions type.



List all Load Balancers
----------------------------------------------------------------------------------------------------

.. method:: do.load_balancer.list()


Returns:

- A list of Load Balancer data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-load_balancers>`_



Create a new Load Balancer
----------------------------------------------------------------------------------------------------

.. method:: do.load_balancer.create(attribs, wait=False, poll=5, timeout=300)

- attribs

  - *name* - string - A human-readable name for a Load Balancer instance.

  - *algorithm* - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections".

  - *forwarding_rules* - list - Forwarding Role data structures

  - *health_check* - list - Health check data structures

  - *sticky_sessions* - list - Sticky Session data structures

  - *region* - object - The region where the Load Balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned.

  - *tag* - string - The name of a Droplet tag corresponding to Droplets assigned to the Load Balancer.

  - *droplet_ids* - array of integers - An array containing the IDs of the Droplets assigned to the Load Balancer.

  - *redirect_http_to_https* - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- A Load Balancer data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-load_balancers>`_

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-load-balancer-with-droplet-tag>`_



Create a new Load Balancer if not already existing
----------------------------------------------------------------------------------------------------

.. method:: do.load_balancer.present(attribs, wait=False, poll=5, timeout=300)

- attribs

  - *name* - string - A human-readable name for a Load Balancer instance.

  - *algorithm* - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections".

  - *forwarding_rules* - list - Forwarding Role data structures

  - *health_check* - list - Health check data structures

  - *sticky_sessions* - list - Sticky Session data structures

  - *region* - object - The region where the Load Balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned.

  - *tag* - string - The name of a Droplet tag corresponding to Droplets assigned to the Load Balancer.

  - *droplet_ids* - array of integers - An array containing the IDs of the Droplets assigned to the Load Balancer.

  - *redirect_http_to_https* - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.

- *wait* - boolean - Whether to wait until the droplet is ready

- *poll* - number - Number of seconds between checks (min 1 sec)

- *timeout* - number - How many seconds before giving up


Returns:

- A tuple of two Load Balancer data structures (second is None if already present)



Retrieve an existing Load Balancer by id
----------------------------------------------------------------------------------------------------

.. method:: do.load_balancer.info(id)

- *id* - number - The id of the Load Balancer to retrieve


Returns:

- A LoadBalancer data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-load_balancers>`_



Update a Load Balancer
----------------------------------------------------------------------------------------------------

.. method:: do.load_balancer.update(id, attribs)

- *name* - string - A human-readable name for a Load Balancer instance.

- *algorithm* - string - The load balancing algorithm used to determine which backend Droplet will be selected by a client. It must be either "round_robin" or "least_connections".

- *forwarding_rules* - list - Forwarding Role data structures

- *health_check* - list - Health check data structures

- *sticky_sessions* - list - Sticky Session data structures

- *region* - object - The region where the Load Balancer instance is located. When setting a region, the value should be the slug identifier for the region. When you query a Load Balancer, an entire region object will be returned.

- *tag* - string - The name of a Droplet tag corresponding to Droplets assigned to the Load Balancer.

- *droplet_ids* - array of integers - An array containing the IDs of the Droplets assigned to the Load Balancer.

- *redirect_http_to_https* - bool - A boolean value indicating whether HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.


Returns:

- A Load Balancer data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#update-a-load-balancer>`_



Delete a Load Balancer
----------------------------------------------------------------------------------------------------

.. method:: do.load_balancer.destroy(id)

- *id* - number - The id of the LoadBalancer to destroy


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-load_balancers>`_



Add Droplets to a Load Balancer
----------------------------------------------------------------------------------------------------


Individual Droplets can not be added to a Load Balancer configured with a Droplet tag. Attempting to do so will result in an DOBOTOException.


.. method:: do.load_balancer.droplet_add(id, droplet_ids)

- *id* - number - The id of the Load Balancer to change

- *droplet_ids* - list - A list the IDs of the Droplets to be assigned to the Load Balancer instance.


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#add-droplets-to-a-load-balancer>`_



Remove Droplets to a Load Balancer
----------------------------------------------------------------------------------------------------

.. method:: do.load_balancer.droplet_remove(id, droplet_ids)

- *id* - number - The id of the Load Balancer to change

- *droplet_ids* - list - A list the IDs of the Droplets to be removed from the Load Balancer instance.


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#remove-droplets-from-a-load-balancer>`_



Add forwarding rules to a Load Balancer
----------------------------------------------------------------------------------------------------


Individual Droplets can not be added to a Load Balancer configured with a Droplet tag. Attempting to do so will result in an DOBOTOException.


.. method:: do.load_balancer.forwarding_rule_add(id, forwarding_rules)

- *id* - number - The id of the Load Balancer to change

- *forwarding_rules* - list - Forwarding Roles data structures


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#add-forwarding-rules-to-a-load-balancer>`_



Remove forwarding rules to a Load Balancer
----------------------------------------------------------------------------------------------------

.. method:: do.load_balancer.forwarding_rule_remove(id, forwarding_rules)

- *id* - number - The id of the Load Balancer to change

- *forwarding_rules* - list - Forwarding Roles data structures


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#remove-forwarding-rules-from-a-load-balancer>`_

