"""This holds the Region class."""

from .Endpoint import Endpoint


class Region(Endpoint):
    """
    description:
        A region in DigitalOcean represents a datacenter where Droplets can be deployed and images
        can be transferred.

        Each region represents a specific datacenter in a geographic location. Some geographical
        locations may have multiple "regions" available. This means that there are multiple
        datacenters available within that area.

    related: https://developers.digitalocean.com/documentation/v2/#regions
    """

    def __init__(self, do, token, url, agent):
        """
        Takes token and agent and sets its DO for reference and URI for floating ip interaction.
        """
        super(Region, self).__init__(token, agent)
        self.do = do
        self.uri = "%s/regions" % url

    def list(self):
        """
        description: List all Regions

        out:
            A list of Region dict's:
                - slug - string - A human-readable string that is used as a unique identifier for each region.
                - name - string - The display name of the region. This will be a full name that is used in the control panel and other interfaces.
                - sizes - list - This attribute is set to a list which contains the identifying slugs for the sizes available in this region.
                - available - boolean - This is a boolean value that represents whether new Droplets can be created in this region.
                - features - list - This attribute is set to a list which contains features available in this region

        related: https://developers.digitalocean.com/documentation/v2/#list-all-regions
        """  # nopep8

        return self.pages(self.uri, "regions")
