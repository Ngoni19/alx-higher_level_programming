#!/usr/bin/python3
"""
Unittest for Base Class
# run -> python3 -m unittest discover tests
# run -> python3 -m unittest tests/test_models/test_base.py
"""

import pep8
import unittest
import os
import json
from models import rectangle
from models import base
Base = base.Base
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """Pep8 models/base.py & tests/test_models/test_base.py"""
    def test_pep8(self):
        """Pep8 testing"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Fix required -> Pep8')


class TestBase(unittest.TestCase):
    """Test for models/base.py"""

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

    """Test for attributes"""
    def test_id_given(self):
        """Test-> given ids match"""
        self.assertTrue(Base(300), self.id == 300)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(3), self.id == 3)
        self.assertTrue(Base(-50), self.id == -50)

    def test_id_not_given(self):
        """Test -> not given ids match; ++nb_objects"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attr_access(self):
        """Test -> not accessible private attr"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    """Test- for args given"""
    def test_invalid_args(self):
        """Test-> excess args given; give error"""
        with self.assertRaises(TypeError):
            Base(30, 30)

    """Test for class"""
    def test_class(self):
        """Test -> class created is Base(true)"""
        self.assertTrue(Base(300), self.__class__ == Base)

    """Test- Python obj to JSON"""
    def test_empty_to_json_string(self):
        """Test -> empty dict given translates into JSON str of {}"""
        d03 = dict()
        strd3 = Base.to_json_string([d03])
        self.assertTrue(len(d03) == 0)
        self.assertTrue(type(strd3) == str)
        self.assertTrue(strd3, "[]")

    def test_from_empty_json_string(self):
        """Test -> no JSON str translates into {} python"""
        s3 = ""
        strs3 = Base.from_json_string(s3)
        self.assertTrue(type(strs3) == list)
        self.assertTrue(strs3 == [])

    def test_to_json_string(self):
        """Test-> dict given translates into JSON str"""
        dict0 = {"id": 4, "width": 5, "height": 6, "x": 7, "y": 8}
        dict1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        strd01 = Base.to_json_string([dict0, dict1])
        self.assertTrue(type(dict0) == dict)
        self.assertTrue(type(strd01) == str)
        self.assertTrue(strd01,
                        [{"id": 4, "width": 5, "height": 6, "x": 7, "y": 8},
                         {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}])

    def test_none_to_json_string(self):
        """Test-> no dict given ;translates into JSON str of {}"""
        d02 = None
        strd2 = Base.to_json_string([d02])
        self.assertTrue(type(strd2) == str)
        self.assertTrue(strd2, "[]")

    """Test- JSON to Python obj"""
    def test_from_json_string(self):
        """Test-> JSON str translates into Python dict"""
        s1 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        strs1 = Base.from_json_string(s1)
        self.assertTrue(type(s1) == str)
        self.assertTrue(type(strs1) == list)
        self.assertTrue(type(strs1[0]) == dict)
        self.assertTrue(strs1,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(strs1[1],
                        {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10})

    def test_from_none_json_string(self):
        """Test -> no JSON str translates into {} python"""
        s2 = None
        strs2 = Base.from_json_string(s2)
        self.assertTrue(type(strs2) == list)
        self.assertTrue(strs2 == [])

    """Test- creating instance from dict"""
    def test_create(self):
        """Test-> transferring attr dict to another instance"""
        r01 = Rectangle(3, 5, 1, 7, 80)
        rdic = r01.to_dictionary()
        r02 = Rectangle.create(**rdic)
        self.assertEqual(str(r01), '[Rectangle] (80) 1/7 - 3/5')
        self.assertEqual(str(r02), '[Rectangle] (99) 1/7 - 3/5')
        self.assertIsNot(r01, r02)

    """Test-save JSON str repr of dict to class specific file"""
    def test_save_to_file(self):
        """Test save to file"""
        r01 = Rectangle(10, 7, 2, 8, 99)
        r02 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r01, r02])
        with open("Rectangle.json", "r01") as file:
            self.assertEqual(
                json.dumps([r01.to_dictionary(), r02.to_dictionary()]),
                file.read())

    def test_save_none_to_file(self):
        """Test save None to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r01") as file:
            self.assertEqual('[]', file.read())

    def test_empty_none_to_file(self):
        """Test save empty list to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r01") as file:
            self.assertEqual('[]', file.read())

    """Test- loading list from JSON str repr of dict in file"""
    def test_load_from_file(self):
        """Test-> load from file"""
        r01 = Rectangle(11, 6, 3, 8, 99)
        r02 = Rectangle(4, 6, 1, 1, 98)
        Rectangle.save_to_file([r01, r02])
        rect = Rectangle.load_from_file()
        self.assertEqual(len(rect), 2)
        for j, k in enumerate(rect):
            if j == 0:
                self.assertEqual(str(k), '[Rectangle] (99) 3/8 - 11/6')
            if j == 1:
                self.assertEqual(str(k), '[Rectangle] (98) 1/1 - 4/6')

    def test_load_from_empty_file(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        rect = Rectangle.load_from_file()
        self.assertEqual(type(rect), list)
        self.assertEqual(len(rect), 0)

    def test_load_from_none_file(self):
        """Test -> load from None file"""
        Rectangle.save_to_file(None)
        rect = Rectangle.load_from_file()
        self.assertEqual(type(rect), list)
        self.assertEqual(len(rect), 0)
