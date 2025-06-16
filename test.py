import unittest
import pyperclip, pykakasi
from component.clipboard_listener import ClipboardListener;
from component.deck import Deck;
from component.language_engine import LanguageEngine;
from unittest.mock import patch

'''Test Name Guide:
class Test[class_name]
    def test_[method under test]_[expected behaviour]_when_[precondition]'''


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_correct_add_new_card(self):
        self.deck.add_card('日本語', 'にほんご　japanese')
        self.assertIn('日本語', self.deck.font_list)
        self.assertIn('にほんご　japanese', self.deck.back_list)


class TestClipboardListener(unittest.TestCase):
    def setUp(self):
        self.listener = ClipboardListener()
        self.listener.current_item = 'New Item' 
        self.listener.last_item = 'Old Item'
    
    #TODO: test skip initial item
    #TODO: test non-kanji character
    def test_detect_new_item_initial_case(self):
        self.listener.last_item = ''
        self.assertTrue(self.listener.detect_new_item())
    
    def test_detect_new_item_normal_case(self):
        self.assertTrue(self.listener.detect_new_item())
    
    def test_detect_new_item_repeitive_case(self):
        self.listener.last_item = 'New Item'
        self.assertFalse(self.listener.detect_new_item())
 
    def test_clean_all_special_characters(self):
        self.listener.current_item = 'Item-with.special, characters!' 
        self.listener.clean_item()
        self.assertEqual(self.listener.saving_item,'Itemwithspecialcharacters')
    
    def test_pyperclip_mock(self):
        with patch('pyperclip.paste', return_value='Mocked Item') as mock_paste:
            result = pyperclip.paste()   
            self.assertEqual(result, 'Mocked Item', 'pyperclip.paste mock is not working')
            mock_paste.assert_called_once()
    
    def test_updateitem(self):
        self.listener.update_item()
        self.assertEqual(self.listener.last_item, 'New Item')
    
    
class TestLanguageEngine(unittest.TestCase):
    @patch('pykakasi.kakasi') # Mock the class itself
    def setUp(self, mock_kakasi):
        self.lang_engine = LanguageEngine()
        self.kakasi_instance = mock_kakasi.return_value
    
    def test_furigana_search_when_normal_word(self):
        self.kakasi_instance.convert.return_value = [{'orig': '日本語', 'hira': 'にほんご', 'kana': 'ニホンゴ', 'hepburn': 'nihongo', 'kunrei': 'nihongo', 'passport': 'nihongo'}]
        result = self.lang_engine.find_furigana('日本語')
        self.assertEqual(result, 'にほんご')
    
    def test_furigana_search_when_is_all_kata_word(self):
        self.kakasi_instance.convert.return_value = [{'orig': 'カタカナ', 'hira': 'かたかな', 'kana': 'カタカナ', 'hepburn': 'katakana', 'kunrei': 'katakana', 'passport': 'katakana'}]
        result = self.lang_engine.find_furigana('カタカナ')
        self.assertFalse(result)
    
    @patch('deep_translator.GoogleTranslator') # Mock the class itself
    def test_translation_search(self, mock_translator):
        mock_instance = mock_translator.return_value
        mock_instance.convert.return_value = 'Japanese'
        
        result = self.lang_engine.find_translation('日本語')
        self.assertEqual(result, 'Japanese')
    
class TestFileHandler(unittest.TestCase):
    def test_export_csv(self):
        #Just how to test file??
        pass

if __name__ == '__main__':
    unittest.main()