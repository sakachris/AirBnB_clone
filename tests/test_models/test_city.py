#!/usr/bin/python3
"""
test_models/base_model.py for testing BaseModel class
"""
import unittest
from models.base_model import BaseModel
from models.city import City
import pycodestyle
import os
import uuid
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Testing for City Class
    """
    @classmethod
    def setUpClass(cls):
        """setting up class instances"""
        cls.c1 = City()
        cls.c1.name = "City1"
        cls.c1.state_id = "1234"

        cls.c2 = City()

        cls.d = cls.c2.to_dict()

        cls.c3 = City(**cls.d)

    @classmethod
    def tearDownClass(cls):
        """tearing down created instances"""
        del cls.c1
        del cls.c2
        del cls.c3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ tests for documentation """
        self.assertTrue(len(City.__doc__) >= 20, "Short or no doc")

    def test_pycodestyle(self):
        """ tests for pycodestyle """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/city.py',
                                     'tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ tests for instance """
        self.assertIsInstance(self.c1, City, "Not instance of City")
        self.assertIsInstance(self.c2, City, "Not instance of City")
        self.assertIsInstance(self.c3, City, "Not instance of City")

    def test_subclass(self):
        """ tests for subclass """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """
        Testing attributes is not none
        """
        self.assertIsNotNone(self.c1.id)
        self.assertIsNotNone(self.c1.created_at)
        self.assertIsNotNone(self.c1.updated_at)
        self.assertIsNotNone(self.c1.name)

    def test_attributes2(self):
        """
        Testing attributes
        """
        self.assertTrue(hasattr(self.c2, 'id'))
        self.assertTrue(hasattr(self.c2, 'created_at'))
        self.assertTrue(hasattr(self.c2, 'updated_at'))
        self.assertTrue(hasattr(self.c2, 'name'))
        self.assertTrue(hasattr(self.c2, 'state_id'))

    def test_attribute_type(self):
        """
        Testing attribute types
        """
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.state_id, str)
        self.assertIsInstance(self.c1.created_at, datetime)
        self.assertIsInstance(self.c1.updated_at, datetime)
        self.assertIsInstance(uuid.UUID(self.c1.id), uuid.UUID)

    def test_id_unique(self):
        """
        Testing if two id's are unique
        """
        self.assertNotEqual(self.c1.id, self.c2.id)

    def test_str(self):
        """
        Testing __str__ return
        """
        s1 = f"[City] ({self.c1.id}) {self.c1.__dict__}"
        s3 = f"[City] ({self.c3.id}) {self.c3.__dict__}"
        self.assertEqual(str(self.c1), s1)
        self.assertEqual(str(self.c3), s3)

    def test_save(self):
        """
        Testing save updated_time
        """
        self.c1.save()
        self.assertNotEqual(self.c1.updated_at, self.c1.created_at)

    def test_to_dict_class(self):
        """
        Testing if __class__ added to to_dict
        """
        self.assertIsNotNone(self.d['__class__'])
        self.assertEqual(self.d['__class__'], 'City')

    def test_kwargs_false(self):
        """
        Testing if object created by kwargs different
        """
        self.assertFalse(self.c3 is self.c2)


if __name__ == "__main__":
    unittest.main()
