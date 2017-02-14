.. DOBOTO documentation master file, created by
   sphinx-quickstart on Sun Feb 12 22:48:09 2017.

DOBOTO: BOTO like interface for DigitalOcean
============================================

DOBOTO was created to be a feature complete Python API to the DigitalOcean RESTful API.

While there are several existing projects along these lines, we at DigitalOcean felt they weren't
feature complete and weren't being updated as the DigitalOcean API grew.

With DOBOTO, we aim to fix that. 

**Simple straight forward API**::

    from doboto.DO import DO

    do = DO(token="secret")

    ssh_keys = do.ssh_key.list()
    droplet = do.droplet.create({
        "name": "example.com",
        "region": "nyc3",
        "size": "512mb",
        "image": "ubuntu-14-04-x64",
        "ssh_keys": [ssh_key["id"] for ssh_key in ssh_keys]
    })

    do.droplet.destroy(droplet['id'])

Classes
-----------

DOBOTO has an interesting design, made for decent code organization and collaboration.  Rather than
have a single giant class, there's a central class, DO, which has attribute instantiations of
sub classes.  The Account example below shows this with do.account.

**Accessing account information**::

    from doboto.DO import DO

    do = DO(token="secret")

    account = do.account.info()

For more information, see the documentation for each class:

.. toctree::
   :maxdepth: 1

   do
   account
   action
   domain
   droplet
   floating_ip
   image
   region
   size
   snapshot
   ssh_key
   tag
   volume

Expectations and Exceptions
---------------------------

The DigitalOcean API sends back JSON objects with expected formats. Rather than have you check
that format with every call, DOBOTO checks it for you, raising an DOBOTOException when its
expectations aren't met:

**Bad token**::

    from doboto.DO import DO

    do = DO(token="incorrect")

    account = do.account.info()

**Result**::

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "doboto/Account.py", line 36, in info
        return self.request(self.uri, "account")
      File "doboto/Endpoint.py", line 45, in request
        raise DOBOTOException(result=response.json())
    doboto.DOBOTOException.DOBOTOException: DO API Error: {u'message': u'Unable to authenticate you.', u'id': u'unauthorized'}

The JSON result (second part of the string output) is accessible via the result`\ property.
