#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-20, -30, -10]), -10)
        self.assertEqual(max_integer([99, 2, 3, 4]), 99)
        self.assertEqual(max_integer([1, 2, 100, 4, 4]), 100)