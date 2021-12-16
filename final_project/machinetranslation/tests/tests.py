import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):

    ## Test for Null inputs:    
    # def test_NotNull(self):
    #     self.assertIsNotNone(englishToFrench.locals().get("english_text"))
    
    def test_e2f_NullInput(self):
        self.assertNotEqual(englishToFrench('None'), '')
    
    def test_e2f_ZeroInput(self):
        self.assertNotEqual(englishToFrench(0), 0)

    def test_Hello(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):

    ## Test for Null inputs:    
    # def test_NotNull(self):
    #     self.assertIsNotNone(frenchToEnglish.locals().get("french_text"))

    def test_f2e_NullInput(self):
        self.assertNotEqual(englishToFrench('None'), '')
    
    def test_f2e_ZeroInput(self):
        self.assertNotEqual(englishToFrench(0), 0)

    def test_Bonjour(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()