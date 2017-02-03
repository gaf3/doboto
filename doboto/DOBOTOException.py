"""This holds the DOBOTOException class."""


class DOBOTOException(Exception):

    def __init__(self, message="DO API Error", result=None):

        super(Exception, self).__init__(message)

        self.result = result
