#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max integer
    """

    def test_max(self):
        """Basic tests for max_integer
        """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 4, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1.2, 4.7, 3.3]), 4.7)
        self.assertEqual(max_integer([1.2, 4.7, 3.3, 4]), 4.7)
        self.assertEqual(max_integer([1.2, 4.7, 3.3, 5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(""), None)

        with self.assertRaises(TypeError):
            max_integer([1, 'j'])

        with self.assertRaises(TypeError):
            max_integer([1.0, 'j'])
