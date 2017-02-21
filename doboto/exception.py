"""This holds the DOBOTO execeptions classes."""


class DOBOTOException(Exception):
    """
    description:
        Exception thrown if unexpected output is encountered.

    in:
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


class DOBOTONotFoundException(DOBOTOException):
    """
    description:
        Exception thrown if entity is not found

    in:
        - message - string - Standard exception message
    """

    def __init__(self, message="DO API Not Found"):

        super(Exception, self).__init__(message)


class DOBOTOPollingException(DOBOTOException):
    """
    description:
        Exception thrown if a timeout occurs

    in:
        - message - string - Standard exception message
        - polling - json - What was being polled
        - error - exception - If an exception was throw prior to timeout
    """

    def __init__(self, message="DO API Timeout", polling=None, error=None):

        super(Exception, self).__init__(message)

        self.polling = polling
        self.error = error

    def __str__(self):

        if self.error is not None:
            return "%s: %s while polling: %s" % (self.message, self.error, self.polling)
        else:
            return "%s while polling: %s" % (self.message, self.polling)
