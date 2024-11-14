from unittest import TestCase

from functions.functions import *

class TestFunctions(TestCase):
    def test_get_date_of_birth(self):
        self.assertEqual(get_date_of_birth('0004185035083'), '18/04/00')
        self.assertEqual(get_date_of_birth('0111224903088'), '22/11/01')
        self.assertEqual(get_date_of_birth('9809126723080'), '12/09/98')

    def test_get_gender(self):
        self.assertEqual(get_gender('9106236034082'), 'Male')
        self.assertEqual(get_gender('9402030894089'), 'Female')
        self.assertEqual(get_gender('0312264983083'), 'Female')

    def test_get_citizenship(self):
        self.assertEqual(get_citizenship('9407076583088'), 'South African')
        self.assertEqual(get_citizenship('9210304503182'), 'Non-South African')
        self.assertEqual(get_citizenship('0312264983083'), 'South African')
