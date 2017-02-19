"""This holds the Account class."""

from .Endpoint import Endpoint


class Account(Endpoint):
    """
    description: Class for obtaining account information

    related: https://developers.digitalocean.com/documentation/v2/#account
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for account interaction.
        """
        super(Account, self).__init__(token, agent)
        self.do = do
        self.uri = "%s/account" % url

    def info(self):
        """
        description: Get User Information

        out:
            An Account dict:
                - droplet_limit - number - The total number of droplets the user may have
                - floating_ip_limit - number - The total number of floating IPs the user may have
                - email - string - The email the user has registered for Digital Ocean with
                - uuid - string (alphanumeric) - The universal identifier for this user
                - email_verified - boolean - If true, the user has verified their account via email. False otherwise.
                - status - string - This value is one of "active", "warning" or "locked".
                - status_message - string - A human-readable message giving more details about the status of the account.

        related: https://developers.digitalocean.com/documentation/v2/#get-user-information
        """  # nopep8

        return self.request(self.uri, "account")
