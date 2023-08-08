#!/usr/bin/python3
"""
test_models/base_model.py for testing BaseModel class
"""
import unittest
from models.base_model import BaseModel
import pycodestyle
import os
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Testing for BaseModel Class
    """
    def test_documentation(self):
        """ tests for documentation """
        self.assertTrue(len(BaseModel.__doc__) >= 20, "Short or no doc")
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.save.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        """ tests for pycodestyle """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/base_model.py',
                                     'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ tests for instance """
        base1 = BaseModel()
        self.assertIsInstance(base1, BaseModel, "Not instance of BaseModel")

    def test_id_not_none(self):
        """
        Testing id is not none
        """
        bm = BaseModel()
        self.assertIsNotNone(bm.id)

    def test_id_str(self):
        """
        Testing id is class str
        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_id_unique(self):
        """
        Testing if two id's are unique
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_id_uuid(self):
        """
        Testing if id is uuid
        """
        bm = BaseModel()
        self.assertIsInstance(uuid.UUID(bm.id), uuid.UUID)
