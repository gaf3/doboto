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
