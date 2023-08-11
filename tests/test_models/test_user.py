#!/usr/bin/python3
"""
test_models/base_model.py for testing BaseModel class
"""
import unittest
from models.base_model import BaseModel
from models.user import User
import pycodestyle
import os
import uuid
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    Testing for BaseModel Class
    """
    @classmethod
    def setUpClass(cls):
        """setting up class instances"""
        cls.u1 = User()
        cls.u1.email = "user1@email.com"
        cls.u1.password = "#12G3n4Q5"
        cls.u1.first_name = "Myfname"
        cls.u1.last_name = "Mylname"

        cls.u2 = User()
        cls.u2.email = "user2@email.com"
        cls.u2.password = "#12G3n4Q6"
        cls.u2.first_name = "Myfname2"
        cls.u2.last_name = "Mylname2"

        cls.d = cls.u2.to_dict()

        cls.u3 = User(**cls.d)

    @classmethod
    def tearDownClass(cls):
        """tearing down created instances"""
        del cls.u1
        del cls.u2
        del cls.u3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ tests for documentation """
        self.assertTrue(len(User.__doc__) >= 20, "Short or no doc")

    def test_pycodestyle(self):
        """ tests for pycodestyle """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/user.py',
                                     'tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ tests for instance """
        self.assertIsInstance(self.u1, User, "Not instance of User")
        self.assertIsInstance(self.u2, User, "Not instance of User")
        self.assertIsInstance(self.u3, User, "Not instance of User")

    def test_subclass(self):
        """ tests for subclass """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """
        Testing attributes is not none
        """
        self.assertIsNotNone(self.u1.id)
        self.assertIsNotNone(self.u1.created_at)
        self.assertIsNotNone(self.u1.updated_at)
        self.assertIsNotNone(self.u1.email)
        self.assertIsNotNone(self.u1.password)
        self.assertIsNotNone(self.u1.first_name)
        self.assertIsNotNone(self.u1.last_name)

    def test_attributes2(self):
        """
        Testing attributes
        """
        self.assertTrue(hasattr(self.u2, 'id'))
        self.assertTrue(hasattr(self.u2, 'created_at'))
        self.assertTrue(hasattr(self.u2, 'updated_at'))
        self.assertTrue(hasattr(self.u2, 'email'))
        self.assertTrue(hasattr(self.u2, 'password'))
        self.assertTrue(hasattr(self.u2, 'first_name'))
        self.assertTrue(hasattr(self.u2, 'last_name'))

    def test_attribute_type(self):
        """
        Testing attribute types
        """
        self.assertIsInstance(self.u2.email, str)
        self.assertIsInstance(self.u2.password, str)
        self.assertIsInstance(self.u2.last_name, str)
        self.assertIsInstance(self.u2.first_name, str)
        self.assertIsInstance(self.u1.created_at, datetime)
        self.assertIsInstance(self.u1.updated_at, datetime)
        self.assertIsInstance(uuid.UUID(self.u1.id), uuid.UUID)

    def test_id_unique(self):
        """
        Testing if two id's are unique
        """
        self.assertNotEqual(self.u1.id, self.u2.id)

    def test_str(self):
        """
        Testing __str__ return
        """
        s1 = f"[User] ({self.u1.id}) {self.u1.__dict__}"
        s3 = f"[User] ({self.u3.id}) {self.u3.__dict__}"
        self.assertEqual(str(self.u1), s1)
        self.assertEqual(str(self.u3), s3)

    def test_save(self):
        """
        Testing save updated_time
        """
        self.u1.save()
        self.assertNotEqual(self.u1.updated_at, self.u1.created_at)

    def test_to_dict_class(self):
        """
        Testing if __class__ added to to_dict
        """
        self.assertIsNotNone(self.d['__class__'])
        self.assertEqual(self.d['__class__'], 'User')

    def test_to_dict_created_at(self):
        """
        Testing if created_at is converted to isoformat
        """
        self.assertEqual(self.d['created_at'], self.u2.created_at.isoformat())
        self.assertIsInstance(self.d['created_at'], str)

    def test_to_dict_updated_at(self):
        """
        Testing if updated_at is converted to isoformat
        """
        self.assertEqual(self.d['updated_at'], self.u2.updated_at.isoformat())
        self.assertIsInstance(self.d['updated_at'], str)

    def test_to_dict_id(self):
        """
        Testing if id is the same
        """
        self.assertEqual(self.d['id'], self.u2.id)

    def test_to_dict_added_attributes(self):
        """
        Testing if added attributes are the same
        """
        self.assertEqual(self.d['email'], 'user2@email.com')
        self.assertEqual(self.d['password'], "#12G3n4Q6")
        self.assertEqual(self.d['first_name'], "Myfname2")
        self.assertEqual(self.d['last_name'], "Mylname2")

    def test_to_dict_type(self):
        """
        Testing if to_dict returns a dictionary
        """
        self.assertIsInstance(self.d, dict)

    def test_kwargs_attributes(self):
        """
        Testing if attributes of created instance by kwargs in equal
        """
        self.assertEqual(self.u3.id, self.u2.id)
        self.assertEqual(self.u3.created_at, self.u2.created_at)
        self.assertEqual(self.u3.updated_at, self.u2.updated_at)
        self.assertEqual(self.u3.email, self.u2.email)
        self.assertEqual(self.u3.password, self.u2.password)

    def test_kwargs_classname_notadded(self):
        """
        Testing if __class__ name not addded as attribute
        """
        self.assertEqual(self.u3.__dict__, self.u2.__dict__)

    def test_kwargs_false(self):
        """
        Testing if object created by kwargs different
        """
        self.assertFalse(self.u3 is self.u2)


if __name__ == "__main__":
    unittest.main()
