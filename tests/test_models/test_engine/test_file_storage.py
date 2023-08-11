#!/usr/bin/python3
"""
test_models/test_engine/test_file_storage.py for testing FileStorage class
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pycodestyle
import os
import uuid
from datetime import datetime
from json import load


class TestFileStorage(unittest.TestCase):
    """
    Testing for FileStorage Class
    """
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        """setting up class instances"""
        cls.bm1 = BaseModel()
        cls.bm1.color = "pink"
        cls.bm1.size = 10

        cls.bm2 = BaseModel()
        cls.bm2.color = 'blue'
        cls.bm2.size = 8.45

        cls.store = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """tearing down created instances"""
        del cls.bm1
        del cls.bm2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ tests for documentation """
        self.assertTrue(len(FileStorage.__doc__) >= 20, "Short or no doc")
        self.assertTrue(len(FileStorage.new.__doc__) >= 20, "Short doc")
        self.assertTrue(len(FileStorage.save.__doc__) >= 20, "Short doc")
        self.assertTrue(len(FileStorage.reload.__doc__) >= 20, "Short doc")
        # self.assertTrue(len(BaseModel.__str__.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        """ tests for pycodestyle """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        p = 'tests/test_models/test_engine/test_file_storage.py'
        result = pystyle.check_files(['models/engine/file_storage.py', p])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ tests for instance """
        self.assertIsInstance(self.store, FileStorage)

    def test_all(self):
        """
        Testing if all returns dictionary of __objects
        """
        k1 = f"BaseModel.{self.bm1.id}"
        k2 = f"BaseModel.{self.bm2.id}"
        all = {k: v for k, v in self.store.all().items() if k in [k1, k2]}
        d = {k1: self.bm1, k2: self.bm2}
        self.assertEqual(all, d)

    def test_all_type(self):
        """
        Testing if all returns dictionary
        """
        dt = self.store.all()
        self.assertIsInstance(dt, dict)

    def test_new(self):
        """
        Testing if new adds to __object dictionary
        """
        new_obj = BaseModel()
        self.store.new(new_obj)
        new_key = f"BaseModel.{new_obj.id}"
        keys = [k for k in self.store.all().keys()]
        values = [v for v in self.store.all().values()]
        self.assertIn(new_key, keys)
        self.assertIn(new_obj, values)

    def test_save_file(self):
        """
        Testing if save saves to json file
        """
        self.store.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_retrieve_object(self):
        """
        Testing if objected saved is in file
        """
        sav_obj = BaseModel()
        sav_key = f"BaseModel.{sav_obj.id}"
        self.store.save()
        with open("file.json", encoding='UTF-8') as file:
            from_json = load(file)
            keys = [k for k in from_json.keys()]
            values = [v for v in from_json.values()]
            self.assertIn(sav_key, keys)
            self.assertIn(sav_obj.to_dict(), values)

    def test_reload(self):
        """
        Testing if reload saves to __object
        """
        self.store.save()
        self.store.reload()
        keys_obj = [i for i in self.store.all().keys()]
        with open("file.json", encoding='UTF-8') as file:
            from_json = load(file)
            keys = [k for k in from_json.keys()]
            # values = [v for v in from_json.values()]
            # self.assertIn(sav_key, keys)
            self.assertEqual(keys, keys_obj)

    def test_reload_no_file(self):
        """
        Testing reload if no file
        """
        self.store.save()
        os.remove("file.json")
        self.store.reload()
        keys_obj = [i for i in self.store.all().keys()]
        self.assertIsNotNone(self.store.all())
