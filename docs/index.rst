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

Installation
---------------

**Via pip**::

  pip install doboto

Ubuntu
^^^^^^

**If installation issues, try this before pip install**::

    apt-get install python-dev libffi-dev

Fedora
^^^^^^

**If installation issues, try this before pip install**::

    dnf install redhat-rpm-config
    yum install libffi-devel python-devel openssl-devel

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
   volume
   certificate
   domain
   droplet
   floating_ip
   image
   region
   size
   snapshot
   ssh_key
   tag

Present
-----------

Many classes have a a preset method, which will check to see if intended resource exists,
creating only if not.  Only the name is checked, none of the other data is verified.

See the documentation for each class to see if there's a present feature.

Waiting
-----------

Many methods have a wait option, complete with a polling interval and timeout value.

For Droplets, DOBOTO waits for the status to no longer be 'new', whether all request
networking interfaces are up, a that all requested tags have been applied.

For Volumes, DOBOTO waits for the volume to be accessible by id.

For Actions, (those that return an Action dict or dict's), DOBOTO waits for the Action to no
longer be 'in-progress'.

Expectations and Exceptions
---------------------------

The DigitalOcean API sends back JSON objects with expected formats. Rather than have you check
that format with every call, DOBOTO checks it for you, raising an exception when its
expectations aren't met:

DOBOTOException
^^^^^^^^^^^^^^^

DOBOTOException is the main exception and the parent of the others.  Raised when general
expectations aren't met.

**Bad token**::

    from doboto.DO import DO

    do = DO(token="incorrect")

    account = do.account.info()

**Result**::

    Traceback (most recent call last):
      File "doboto/Account.py", line 38, in info
        return self.request(self.uri, "account")
      File "doboto/Endpoint.py", line 50, in request
        raise DOBOTOException(result=response.json())
    doboto.exception.DOBOTOException: DO API Error: {u'message': u'Unable to authenticate you.', u'id': u'unauthorized'}

The JSON result (second part of the string output) is accessible via the result property.

DOBOTONotFoundException
^^^^^^^^^^^^^^^^^^^^^^^

DOBOTONotFoundException is raised when a response from the API contains an "id" field with a value of "not_found"

**Missing droplet**::

    from doboto.DO import DO

    do = DO(token="secret")

    droplet = do.droplet.info(-1)

**Result**::

    Traceback (most recent call last):
      File "doboto/Droplet.py", line 417, in info
        return self.request(uri, "droplet")
      File "doboto/Endpoint.py", line 47, in request
        raise DOBOTONotFoundException()
    doboto.exception.DOBOTONotFoundException


DOBOTOPollingException
^^^^^^^^^^^^^^^^^^^^^^^

DOBOTOPollingException is raised when the timeout is exceeded while waiting for a resource to
become ready.

**Impatient droplet**::

    from doboto.DO import DO

    do = DO(token="secret")

    droplet = do.droplet.create({
        "name": "notyet",
        "region": "nyc2",
        "size": 2,
        "image": "debian-7-0-x64"
    }, wait=True, timeout=10)

**Result**::

    Traceback (most recent call last):
      File "doboto/Droplet.py", line 238, in create
        raise DOBOTOPollingException(polling=droplet)
        doboto.exception.DOBOTOPollingException: DO API Timeout while polling: {"name": "notyet" ... }

Whatever was being polled (a droplet in this case) is accessible via the polling attribute on the
exception.  If an exception was throw prior to the timeout, that is accessible via the error
attribute.
