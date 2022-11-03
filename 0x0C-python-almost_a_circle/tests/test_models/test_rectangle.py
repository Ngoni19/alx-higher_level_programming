#!/usr/bin/python3
"""
Unittest for Rectangle Class
# run -> python3 -m unittest discover tests
# run -> python3 -m unittest tests/test_models/test_rectangle.py
"""


import os
import pep8
import unittest
from contextlib import redirect_stdout
from io import StringIO
from models import rectangle
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """Pep8 models/rectangle.py & tests/test_models/test_rectangle.py"""
    def test_pep8(self):
        """Pep8 testing"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Fix-> Pep8')


class TestBase(unittest.TestCase):
    """Tests -> models/rectangle.py"""

    """Test for attributes"""
    def test_all_attr_given(self):
        """Test -> all attributes; match given args"""
        r01 = Rectangle(11, 30, 4, 5, 99)
        self.assertTrue(r01.width == 11)
        self.assertTrue(r01.height == 30)
        self.assertTrue(r01.x == 4)
        self.assertTrue(r01.y == 5)
        self.assertTrue(r01.id == 99)

    def test_deflt_attr(self):
        """Test-> default attr are set when not given"""
        r02 = Rectangle(5, 6)
        self.assertTrue(r02.width == 5)
        self.assertTrue(r02.height == 6)
        self.assertTrue(r02.x == 0)
        self.assertTrue(r02.y == 0)
        self.assertTrue(r02.id is not None)

    def test_private_attr_acs(self):
        """Test private attributes are not accessible"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_attr_validated(self):
        """Test-> attr validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("15", 2, 2, 2, 2)
            Rectangle([11, 8], 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {50, }, 1, 1, 1)
            Rectangle(1, {"r": 20}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (60, 10), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -10, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -50, 1)

    """Test for args given"""
    def test_invalid_args(self):
        """Test -> many args given; indicate error"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        """Test very little args; indicate error"""
        with self.assertRaises(TypeError):
            Rectangle(2)
            Rectangle()
            Rectangle(None)

    """Test for class"""
    def test_class(self):
        """Test-> class created is Rectangle(true)"""
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)

    """Test methods"""
    def test_area(self):
        """Test method: area"""
        self.assertEqual(Rectangle(4, 5).area(), 20)
        self.assertEqual(Rectangle(7, 8, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Test method: display"""
        with StringIO() as buff, redirect_stdout(buff):
            Rectangle(4, 3).display()
            buf = buff.getvalue()
        self.assertEqual(buf, '####\n####\n####\n')
        with StringIO() as buff, redirect_stdout(buff):
            Rectangle(4, 3, 1, 2).display()
            buf = buff.getvalue()
        self.assertEqual(buf, '\n\n ####\n ####\n ####\n')

    def test_print(self):
        """Test method: __str__"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    def test_update(self):
        """Test method: update(*args)"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(98)
        self.assertEqual(str(r), '[Rectangle] (98) 10/10 - 10/10')
        r.update(98, 2)
        self.assertEqual(str(r), '[Rectangle] (98) 10/10 - 2/10')
        r.update(98, 2, 3)
        self.assertEqual(str(r), '[Rectangle] (98) 10/10 - 2/3')
        r.update(98, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (98) 4/5 - 2/3')
        """Test for invalid *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(55, 1, 2, 3, "alx")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(45, 1, 2, 3, -88)
        """Test method: update(*kwargs)"""
        r.update(id=45)
        self.assertEqual(str(r), '[Rectangle] (45) 4/5 - 2/3')
        r.update(id=44, x=760, y=870, width=980)
        self.assertEqual(str(r), '[Rectangle] (44) 760/870 - 980/2')
        """Test for valid & invalid *kwargs"""
        r.update(nokey=6000, invalid=7000, testing=8000, id=5000)
        self.assertEqual(str(r), '[Rectangle] (5000) 760/870 - 980/2')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        rd = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(rd), dict)
        r02 = Rectangle(10, 10)
        r02.update(**rd)
        self.assertEqual(str(r02), '[Rectangle] (5) 3/4 - 1/2')
