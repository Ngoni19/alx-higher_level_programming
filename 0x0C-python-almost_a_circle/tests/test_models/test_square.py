#!/usr/bin/python3
"""
Unittest for Square Class
# run -> python3 -m unittest discover tests
# run -> python3 -m unittest tests/test_models/test_square.py
"""


import unittest
import pep8
from io import StringIO
from contextlib import redirect_stdout
from models import square
Square = square.Square


class TestPep8(unittest.TestCase):
    """Pep8 models/square.py & tests/test_models/test_square.py"""
    def test_pep8(self):
        """Pep8 square testing"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Fix -> Pep8')


class TestBase(unittest.TestCase):
    """Tests for models/square.py"""

    """Test for attributes"""
    def test_all_attr_given(self):
        """Test-> all attributes match what's given"""
        s01 = Square(5, 55, 555, 1000)
        self.assertTrue(s01.width == 5)
        self.assertTrue(s01.height == 5)
        self.assertTrue(s01.size == 5)
        self.assertTrue(s01.x == 55)
        self.assertTrue(s01.y == 555)
        self.assertTrue(s01.id == 1000)

    def test_default_attr(self):
        """Test-> default attr are set when not given"""
        s2 = Square(55)
        self.assertTrue(s2.width == 55)
        self.assertTrue(s2.height == 55)
        self.assertTrue(s2.size == 55)
        self.assertTrue(s2.x == 0)
        self.assertTrue(s2.y == 0)
        self.assertTrue(s2.id is not None)

    def test_attr_validated(self):
        """Test attributes are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("18")
            Square([15, 3])
            Square({50, })
            Square({"s": 20})
            Square(None)
            Square((30, 20), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)
            Square(5).size(-5)

    """Test given args """
    def test_invalid_args(self):
        """Test-> more args given;indicate error"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)
        """Test-> less args given; indicate error"""
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    """Test for class"""
    def test_class(self):
        """Test -> class created is Rectangle(true)"""
        s = Square(10)
        self.assertEqual(type(s), Square)

    """Test methods"""
    def test_print(self):
        """Test method: __str__"""
        s = Square(3, 6, 9, 55)
        s.size = 500
        self.assertEqual(str(s), '[Square] (55) 6/9 - 500')

    def test_area(self):
        """Test method: area"""
        self.assertEqual(Square(6).area(), 36)
        self.assertEqual(Square(4, 0, 0).area(), 16)

    def test_display(self):
        """Test method: display"""
        with StringIO() as Buf, redirect_stdout(Buf):
            Square(4).display()
            b = Buf.getvalue()
        self.assertEqual(b, '####\n####\n####\n####\n')
        with StringIO() as Buf, redirect_stdout(Buf):
            Square(3, 1, 2).display()
            b = Buf.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')

    def test_update(self):
        """Test method: update(*args)"""
        s = Square(1, 2, 3, 4)
        s.update(11, 11, 11, 11)
        self.assertEqual(str(s), '[Square] (11) 11/11 - 11')
        s.update()
        self.assertEqual(str(s), '[Square] (11) 11/11 - 11')
        s.update(55)
        self.assertEqual(str(s), '[Square] (55) 11/11 - 11')
        s.update(55, 5)
        self.assertEqual(str(s), '[Square] (55) 11/11 - 5')
        s.update(44, 55, 1, 2)
        self.assertEqual(str(s), '[Square] (44) 1/2 - 55')
        """Test method: update(*kwargs)"""
        s.update(id=88, size=77, nokey=55)
        self.assertEqual(str(s), '[Square] (88) 1/2 - 77')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        sd = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sd), dict)
        s2 = Square(10, 10)
        s2.update(**sd)
        self.assertEqual(str(s2), '[Square] (4) 2/3 - 1')
