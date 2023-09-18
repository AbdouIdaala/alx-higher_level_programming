#!/usr/bin/python3
"""import modules"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        """Test if the Base class correctly assigns unique IDs to instances.

        - Create two Base instances, and check if their IDs are 1 and 2.
        - Change the ID of the first instance and verify if it's updated.
        - Create a new Base instance with a specific ID and
        check if it matches.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b1.id = 10
        self.assertEqual(b1.id, 10)
        b3 = Base(42)
        self.assertEqual(b3.id, 42)


if __name__ == "__main__":
    unittest.main()
