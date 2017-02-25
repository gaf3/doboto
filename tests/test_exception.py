"""
This module contains tests for the main DO class
"""

from unittest import TestCase
from doboto.exception import DOBOTOException, DOBOTONotFoundException, DOBOTOPollingException


class TestDOBOTOException(TestCase):
    """
    This class checks on the DOBOTOException Class
    """

    def test_can_instantiate(self):
        """
        DOBOTOException class can be instantiated
        """

        exception = DOBOTOException("boo", "hiss")
        self.assertEqual(exception.message, "boo")
        self.assertEqual(exception.result, "hiss")

        exception = DOBOTOException(result="hiss")
        self.assertEqual(exception.message, "DO API Error")
        self.assertEqual(exception.result, "hiss")

    def test_str(self):
        """
        DOBOTOException class can be instantiated
        """

        exception = DOBOTOException("boo", {"hiss": "fire"})
        self.assertEqual(str(exception), "boo: {'hiss': 'fire'}")

        exception = DOBOTOException()
        self.assertEqual(str(exception), "DO API Error")

class TestDOBOTONotFoundException(TestCase):
    """
    This class checks on the DOBOTONotFoundException Class
    """

    def test_can_instantiate(self):
        """
        DOBOTONotFoundException class can be instantiated
        """

        exception = DOBOTONotFoundException()
        self.assertEqual(exception.message, "DO API Not Found")

        exception = DOBOTONotFoundException("boo")
        self.assertEqual(exception.message, "boo")

class TestDOBOTOPolling(TestCase):
    """
    This class checks on the DOBOTOPollingException Class
    """

    def test_can_instantiate(self):
        """
        DOBOTOPollingException class can be instantiated
        """

        exception = DOBOTOPollingException("boo", "hiss", "curse")
        self.assertEqual(exception.message, "boo")
        self.assertEqual(exception.polling, "hiss")
        self.assertEqual(exception.error, "curse")

        exception = DOBOTOPollingException(polling="hiss")
        self.assertEqual(exception.message, "DO API Timeout")
        self.assertEqual(exception.polling, "hiss")

    def test_str(self):
        """
        DOBOTOException class can be instantiated
        """

        exception = DOBOTOPollingException("boo", "hiss", "curse")
        self.assertEqual(str(exception), "boo: curse while polling: hiss")

        exception = DOBOTOPollingException(polling="hiss")
        self.assertEqual(str(exception), "DO API Timeout while polling: hiss")
