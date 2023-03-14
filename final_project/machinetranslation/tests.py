import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        
unittest.main()        
