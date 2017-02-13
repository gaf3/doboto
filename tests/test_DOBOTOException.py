"""
This module contains tests for the main DO class
"""

from unittest import TestCase
from doboto.DOBOTOException import DOBOTOException


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

    def test_str(self):
        """
        DOBOTOException class can be instantiated
        """

        exception = DOBOTOException("boo", {"hiss": "fire"})
        self.assertEqual(str(exception), "boo: {'hiss': 'fire'}")

        exception = DOBOTOException()
        self.assertEqual(str(exception), "DO API Error")
