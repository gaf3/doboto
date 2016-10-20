"""
This module contains tests for the main DO class
"""

from unittest import TestCase
from doboto import DO


class TestDO(TestCase):
    """
    This class implements unittests for the main DO class
    """

    def setUp(self):
        """
        Define resources usable by all unit tests
        """

        self.test_url = "http://abc.example.com/"
        self.test_token = "abc123"
        self.instantiate_args = (self.test_url, self.test_token)

        self.klass_name = "DO"
        self.klass = getattr(DO, self.klass_name)
        self.klass_attrs = ('droplet', 'ssh_key')

    def test_class_exists(self):
        """
        DO class is defined
        """

        self.assertTrue(hasattr(DO, self.klass_name))

    def test_can_instantiate(self):
        """
        DO class can be instantiated
        """

        exc_thrown = False

        try:
            self.klass(*self.instantiate_args)
        except Exception:
            exc_thrown = True

        self.assertFalse(exc_thrown)
