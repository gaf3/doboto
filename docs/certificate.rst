.. DOBOTO documentation sub class file, created bysphinxter.py.

Certificate (do.certificate)
============================================

SSL certificates may be uploaded to DigitalOcean where they will be placed in a fully encrypted and isolated storage system. They may then be used to perform SSL termination on Load Balancers.


List all Certificates
----------------------------------------------------------------------------------------------------

.. method:: do.certificate.list(tag_name=None)


Returns:

- A list of Certificate dict's

  - *id* - string - A unique ID that can be used to identify and reference a certificate.

  - *name* - string - A unique human-readable name referring to a certificate.

  - *not_after* - string - A time value given in ISO8601 combined date and time format that represents the certificate's expiration date.

  - *sha1_fingerprint* - string - A unique identifier generated from the SHA-1 fingerprint of the certificate.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the certificate was created.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#list-all-certificates>`_



Create a new Certificate or multiple Certificates
----------------------------------------------------------------------------------------------------

.. method:: do.certificate.create(name, private_key, leaf_certificate, certificate_chain)

- *name* - string - A unique human-readable name referring to a certificate. - true

- *private_key* - string - The contents of a PEM-formatted private-key corresponding to the SSL certificate. - true

- *leaf_certificate* - string - The contents of a PEM-formatted public SSL certificate. - true

- *certificate_chain* - string - The full PEM-formatted trust chain between the certificate authority's certificate and your domain's SSL certificate. - true


Returns:

- A Certificate dict

  - *id* - string - A unique ID that can be used to identify and reference a certificate.

  - *name* - string - A unique human-readable name referring to a certificate.

  - *not_after* - string - A time value given in ISO8601 combined date and time format that represents the certificate's expiration date.

  - *sha1_fingerprint* - string - A unique identifier generated from the SHA-1 fingerprint of the certificate.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the certificate was created.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#create-a-new-certificates>`_



Create a new Certificate if not already existing
----------------------------------------------------------------------------------------------------

.. method:: do.certificate.present(name, private_key, leaf_certificate, certificate_chain)

- *name* - string - A unique human-readable name referring to a certificate. - true

- *private_key* - string - The contents of a PEM-formatted private-key corresponding to the SSL certificate. - true

- *leaf_certificate* - string - The contents of a PEM-formatted public SSL certificate. - true

- *certificate_chain* - string - The full PEM-formatted trust chain between the certificate authority's certificate and your domain's SSL certificate. - true


Returns:

- A tuple of two Certificate dict's (second is None if already present)

  - *id* - string - A unique ID that can be used to identify and reference a certificate.

  - *name* - string - A unique human-readable name referring to a certificate.

  - *not_after* - string - A time value given in ISO8601 combined date and time format that represents the certificate's expiration date.

  - *sha1_fingerprint* - string - A unique identifier generated from the SHA-1 fingerprint of the certificate.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the certificate was created.



Retrieve an existing Certificate by id
----------------------------------------------------------------------------------------------------

.. method:: do.certificate.info(id)

- *id* - number - The id of the Certificate to retrieve


Returns:

- A Certificate dict

  - *id* - string - A unique ID that can be used to identify and reference a certificate.

  - *name* - string - A unique human-readable name referring to a certificate.

  - *not_after* - string - A time value given in ISO8601 combined date and time format that represents the certificate's expiration date.

  - *sha1_fingerprint* - string - A unique identifier generated from the SHA-1 fingerprint of the certificate.

  - *created_at* - string - A time value given in ISO8601 combined date and time format that represents when the certificate was created.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#retrieve-an-existing-certificates>`_



Delete a Certificate
----------------------------------------------------------------------------------------------------

.. method:: do.certificate.destroy(id=None, tag_name=None)

- *id* - number - The id of the Certificate to destroy


Returns:

- None. A DOBOTOException is thrown if an issue is encountered.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#delete-a-certificates>`_

