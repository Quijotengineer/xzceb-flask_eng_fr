import unittest

class TestEnglishToFrench(unittest.TestCase):
    
    def test_NotNull(self):
        self.assertIsNotNone(self)

    def test_Hello(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):

    def test_NotNull(self):
        self.assertIsNotNone(self)

    def test_Bonjour(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__'
    unittest.main()