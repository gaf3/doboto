.. DOBOTO documentation sub class file, created bysphinxter.py.

SSHKey (do.ssh_key)
============================================

DigitalOcean allows you to add SSH public keys to the interface so that you can embed your public key into a Droplet at the time of creation. Only the public key is required to take advantage of this functionality.


List all Keys
----------------------------------------------------------------------------------------------------

.. method:: do.ssh_key.list()


Returns:

- A list of SSH Key dict's

  - *id* - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.

  - *fingerprint* - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.

  - *public_key* - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.

  - *name* - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-keys>`_



Create a new Key
----------------------------------------------------------------------------------------------------

.. method:: do.ssh_key.create(name, public_key)

- *name* - string - The name to give the new SSH key in your account.

- *public_key* - string - A string containing the entire public key.


Returns:

- An SSH Key dict

  - *id* - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.

  - *fingerprint* - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.

  - *public_key* - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.

  - *name* - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-key>`_



Retrieve an existing Key
----------------------------------------------------------------------------------------------------

.. method:: do.ssh_key.info(id_fingerprint)

- *id_fingerprint* - number / string - id or fingerprint of the key


Returns:

- An SSH Key dict

  - *id* - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.

  - *fingerprint* - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.

  - *public_key* - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.

  - *name* - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-key>`_



Update a Key
----------------------------------------------------------------------------------------------------

.. method:: do.ssh_key.update(id_fingerprint, name)

- *id_fingerprint* - number / string - id or fingerprint of the key

- *name* - string - The name to give the new SSH key in your account.


Returns:

- An SSH Key dict

  - *id* - number - This is a unique identification number for the key. This can be used to reference a specific SSH key when you wish to embed a key into a Droplet.

  - *fingerprint* - string - This attribute contains the fingerprint value that is generated from the public key. This is a unique identifier that will differentiate it from other keys using a format that SSH recognizes.

  - *public_key* - string - This attribute contains the entire public key string that was uploaded. This is what is embedded into the root user's authorized_keys file if you choose to include this SSH key during Droplet creation.

  - *name* - string - This is the human-readable display name for the given SSH key. This is used to easily identify the SSH keys when they are displayed.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#update-a-key>`_



Destroy a Key
----------------------------------------------------------------------------------------------------

.. method:: do.ssh_key.destroy(id_fingerprint)

- *id_fingerprint* - number / string - id or fingerprint of the key


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#destroy-a-key>`_

