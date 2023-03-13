import unittest
import machinetranslation.translator as trans # pylint: disable=import-error

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(trans.french_to_english(None), None)
        self.assertEqual(trans.french_to_english("Bonjour"), "Hello")

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(trans.english_to_french(None), None)
        self.assertEqual(trans.english_to_french("Hello"), "Bonjour")        

        unittest.main()        
