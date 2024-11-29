import unittest
from program import find_furigana, find_translation

class TestFuriganaFunction(unittest.TestCase):
    def test_correct_furigana_search(self):
       self.assertEqual(find_furigana(["日本語"]), ["にほんご"])
       
class TestTranslationFunction(unittest.TestCase):
    def test_correct_tranlation_search(self):
       self.assertEqual(find_translation(["日本語"]), ["Japanese"])
       
if __name__ == '__main__':
    unittest.main()