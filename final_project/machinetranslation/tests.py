import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french(""), "") # Test for null input 
    def test2(self):    
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # Test for  input Hello

class TestFrenchToEnglish(unittest.TestCase):     
    def test1(self):
        self.assertNotEqual(french_to_english(""), "") # Test for null input
    def test2(self):    
        self.assertEqual(french_to_english("Bonjour"), "Hello") #  Test for nul input Bonjour

unittest.main()