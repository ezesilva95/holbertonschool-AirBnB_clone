#!/usr/bin/python3
""" Testing for Place """
import unittest
import pep8
from models.place import Place

class Place_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle for Place """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/place.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
