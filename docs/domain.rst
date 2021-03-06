.. DOBOTO documentation sub class file, created bysphinxter.py.

Domain (do.domain)
============================================

Domain resources are domain names that you have purchased from a domain name registrar that you are managing through the DigitalOcean DNS interface.

This resource establishes top-level control over each domain. Actions that affect individual domain records should be taken on the [Domain Records] resource.

Data Structures
-----------------------

Domain
^^^^^^^^^^^^^^^^^^^^^^^^^

- *name* - string - The name of the domain itself. This should follow the standard domain format of domain.TLD. For instance, example.com is a valid domain name.

- *ttl* - number - This value is the time to live for the records on this domain, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested.

- *zone_file* - string - This attribute contains the complete contents of the zone file for the selected domain. Individual domain record resources should be used to get more granular control over records. However, this attribute can also be used to get information about the SOA record, which is created automatically and is not accessible as an individual record resource.

Domain Record
^^^^^^^^^^^^^^^^^^^^^^^^^

- *id* - number - A unique identifier for each domain record.

- *type* - string - The type of the DNS record (A, CNAME, TXT, ...).

- *name* - string - The name to use for the DNS record.

- *data* - string - The value to use for the DNS record.

- *priority* - nullable number - The priority for SRV and MX records.

- *port* - nullable number - The port for SRV records.

- *weight* - nullable number - The weight for SRV records.



List all Domains
----------------------------------------------------------------------------------------------------

.. method:: do.domain.list()


Returns:

- A list of Domain data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-domains>`_



Create a new Domain
----------------------------------------------------------------------------------------------------

.. method:: do.domain.create(name, ip_address)

- *name* - string - The domain name to add to the DigitalOcean DNS management interface. The name must be unique in DigitalOcean's DNS system. The request will fail if the name has already been taken.

- *ip_address* - string - This attribute contains the IP address you want the domain to point to.


Returns:

- A Domain data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-domain>`_



Create a new Domain if name doesn't already exist
----------------------------------------------------------------------------------------------------

.. method:: do.domain.present(name, ip_address)

- *name* - string - The domain name to add to the DigitalOcean DNS management interface. The name must be unique in DigitalOcean's DNS system. The request will fail if the name has already been taken.

- *ip_address* - string - This attribute contains the IP address you want the domain to


Returns:

- A tuple of Domain data structures, the intended, and created (None if already exists)



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-domain>`_



Retrieve an existing Domain
----------------------------------------------------------------------------------------------------

.. method:: do.domain.info(name)

- *name* - string - The name of the domain to retrieve


Returns:

- A Domain data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-domain>`_



Delete a Domain
----------------------------------------------------------------------------------------------------

.. method:: do.domain.destroy(name)

- *name* - string - The name of the domain to destroy


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-domain>`_



List all Domain Records
----------------------------------------------------------------------------------------------------

.. method:: do.domain.record_list(name)

- *name* - string - The name of the domain, the Domain Records of which to retrieve


Returns:

- A list of Domain Record data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-domain-records>`_



Create a new Domain Record
----------------------------------------------------------------------------------------------------

.. method:: do.domain.record_create(name, attribs)

- *name* - string - The name of the domain

- *attribs* - dict - Domain Record data structure without an id


Returns:

- A Domain Record data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-domain-record>`_



Retrieve an existing Domain Record
----------------------------------------------------------------------------------------------------

.. method:: do.domain.record_info(name, record_id)

- *name* - string - The name of the domain

- *record_id* - number - The id of the domain record to retrieve


Returns:

- A Domain Record data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-domain-record>`_



Update a Domain Record
----------------------------------------------------------------------------------------------------

.. method:: do.domain.record_update(name, record_id, attribs)

- *name* - string - The name of the domain

- *record_id* - number - The id of the domain record to update

- *attribs* - dict - Domain Record data structure without an id


Returns:

- A Domain Record data structure



Related:

* `<https://developers.digitalocean.com/documentation/v2/#update-a-domain-record>`_



Delete a Domain Record
----------------------------------------------------------------------------------------------------

.. method:: do.domain.record_destroy(name, record_id)

- *name* - string - The name of the domain

- *record_id* - number - The id of the domain record to destroy


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-domain-record>`_

