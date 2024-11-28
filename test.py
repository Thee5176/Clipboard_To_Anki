import unittest
from program import find_furigana

class TestFuriganaFunction(unittest.TestCase):
    def test_correct_furigana_search(self):
       self.assertEqual(find_furigana("漢字"), "かんじ")
       
if __name__ == '__main__':
    unittest.main()