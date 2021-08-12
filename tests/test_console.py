#!/usr/bin/python3
""" Unittest for console. """
import os
import pep8
import sys
from io import StringIO
import unittest
import console
HBNBCommand = console.HBNBCommand


class test_console(unittest.TestCase):
    """ Unittests for console. """
    def test_pep8_conformance_console(self):
        """ pep8 for console """
        pep8s = pep8.StyleGuide(quiet=True)
        errors = pep8s.check_files(['console.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_pep8_conformance_test_console(self):
        """ pep8 for test_console """
        pep8s = pep8.StyleGuide(quiet=True)
        errors = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_console_module_docstring(self):
        """ docstring test for console """
        self.assertIsNot(console.__doc__, None,
                         "docstring err in console.py")
        self.assertTrue(len(console.__doc__) >= 1,
                        "docstring err in console.py")

    def test_HBNBCommand_class_docstring(self):
        """ docstring test for HBNBCommand """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "docstring err in HBNBCommand class")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "docstring err in HBNBCommand class")
