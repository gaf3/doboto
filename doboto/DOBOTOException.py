"""This holds the DOBOTOException class."""


class DOBOTOException(Exception):
    """
    description:
        Exception thrown if unexpected output is encountered.

    out:
        - message - string - Standard exception message
        - result - json - The JSON dict from the response
    """

    def __init__(self, message="DO API Error", result=None):

        super(Exception, self).__init__(message)

        self.result = result

    def __str__(self):

        if self.result is not None:
            return "%s: %s" % (self.message, self.result)
        else:
            return super(Exception, self).__str__()
