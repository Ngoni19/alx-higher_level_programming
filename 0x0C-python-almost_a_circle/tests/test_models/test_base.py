#!/usr/bin/python3
"""
Unittest for Base Class
# run -> python3 -m unittest discover tests
# run -> python3 -m unittest tests/test_models/test_base.py
"""

import unittest
import pep8
import json
import os
from models import base
from models import rectangle
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
        except Exception as e:
            pass

    """Test for attributes"""
    def test_id_given(self):
        """Test-> given ids match"""
        self.assertTrue(Base(300), self.id == 300)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(3), self.id == 3)
        self.assertTrue(Base(-50), self.id == -50)
 
