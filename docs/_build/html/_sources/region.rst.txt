.. DOBOTO documentation sub class file, created bysphinxter.py.

Region (do.region)
============================================

A region in DigitalOcean represents a datacenter where Droplets can be deployed and images can be transferred.

Each region represents a specific datacenter in a geographic location. Some geographical locations may have multiple "regions" available. This means that there are multiple datacenters available within that area.

Data Structures
-----------------------

Region
^^^^^^^^^^^^^^^^^^^^^^^^^

- *slug* - string - A human-readable string that is used as a unique identifier for each region.

- *name* - string - The display name of the region. This will be a full name that is used in the control panel and other interfaces.

- *sizes* - list - This attribute is set to a list which contains the identifying slugs for the sizes available in this region.

- *available* - boolean - This is a boolean value that represents whether new Droplets can be created in this region.

- *features* - list - This attribute is set to a list which contains features available in this region



List all Regions
----------------------------------------------------------------------------------------------------

.. method:: do.region.list()


Returns:

- A list of Region data structures



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-regions>`_

