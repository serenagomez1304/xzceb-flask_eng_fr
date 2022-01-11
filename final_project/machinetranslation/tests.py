import unittest

from translator import french_to_english, english_to_french

class EnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class FrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()