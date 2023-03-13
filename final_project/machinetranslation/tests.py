import unittest
from translator import frenchToEnglish
from translator import englishToFrench

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(None), None)
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(None), None)
        self.assertEqual(englishToFrench("Hello"), "Bonjour")        

unittest.main()        