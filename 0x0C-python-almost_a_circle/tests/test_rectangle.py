#!/usr/bin/python3
"""import modules"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_id(self):
        """Test if the Rectangle class correctly assigns unique IDs to
        instances.

        - Create three Rectangle instances with different arguments and
        verify their IDs.
        """
        r1 = Rectangle(10, 3)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 4, 2, 1, 10)
        self.assertEqual(r2.id, 10)
        r3 = Rectangle(4, 8, 0, 0)
        self.assertEqual(r3.id, 6)

    def test_width(self):
        """Test width attribute validation and modification.

        - Verify that setting width to a non-integer value raises TypeError.
        - Verify that setting width to a negative value raises ValueError.
        - Create a Rectangle instance with a valid width and modify it.
        """
        with self.assertRaises(TypeError):
            Rectangle("4", 2)
        with self.assertRaises(ValueError):
            Rectangle(-4, 2)
        r4 = Rectangle(4, 2)
        self.assertEqual(r4.width, 4)
        r5 = Rectangle(4, 2)
        r5.width = 1
        self.assertEqual(r5.width, 1)

    def test_height(self):
        """Test height attribute validation and modification.

        - Verify that setting width to a non-integer value raises TypeError.
        - Verify that setting width to a negative value raises ValueError.
        - Create a Rectangle instance with a valid width and modify it.
        """
        with self.assertRaises(TypeError):
            Rectangle(4, "2")
        with self.assertRaises(ValueError):
            Rectangle(4, -2)
        r6 = Rectangle(4, 2)
        self.assertEqual(r6.height, 2)
        r7 = Rectangle(4, 2)
        r7.height = 1
        self.assertEqual(r7.height, 1)

    def test_x(self):
        """Test x attribute validation and modification.

        - Verify that setting width to a non-integer value raises TypeError.
        - Verify that setting width to a negative value raises ValueError.
        - Create a Rectangle instance with a valid width and modify it.
        """
        with self.assertRaises(TypeError):
            r8 = Rectangle(10, 2)
            r8.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3)

    def test_y(self):
        """Test y attribute validation and modification.

        - Verify that setting width to a non-integer value raises TypeError.
        - Verify that setting width to a negative value raises ValueError.
        - Create a Rectangle instance with a valid width and modify it.
        """
        with self.assertRaises(TypeError):
            r9 = Rectangle(10, 2)
            r9.y = []
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test the area calculation for Rectangle instances.

        - Create two Rectangle instances with different dimensions and
        check their areas.
        - Modify the width of an existing Rectangle instance and
        recheck its area.
        """
        r10 = Rectangle(3, 2)
        self.assertEqual(r10.area(), 6)
        r11 = Rectangle(2, 10)
        self.assertEqual(r11.area(), 20)
        r12 = Rectangle(8, 7, 0, 0, 12)
        r12.width = 2
        self.assertEqual(r12.area(), 14)


if __name__ == "__main__":
    unittest.main()
