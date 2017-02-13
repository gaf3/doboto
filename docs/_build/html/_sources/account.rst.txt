.. DOBOTO documentation sub class file, created bysphinxter.py.

Account (do.account)
============================================

Class for obtaining account information


Get User Information
----------------------------------------------------------------------------------------------------

.. method:: do.account.info()


Returns:

- An Account dict

  - *droplet_limit* - number - The total number of droplets the user may have

  - *floating_ip_limit* - number - The total number of floating IPs the user may have

  - *email* - string - The email the user has registered for Digital Ocean with

  - *uuid* - string (alphanumeric) - The universal identifier for this user

  - *email_verified* - boolean - If true, the user has verified their account via email. False otherwise.

  - *status* - string - This value is one of "active", "warning" or "locked".

  - *status_message* - string - A human-readable message giving more details about the status of the account.



Related:

* `<https://developers.digitalocean.com/documentation/v2/#get-user-information>`_

