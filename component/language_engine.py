import pykakasi
from deep_translator import GoogleTranslator

class LanguageEngine:
    def __init__(self, lang='en'):
        self.furigana_mode = pykakasi.kakasi()
        self.translation_mode = GoogleTranslator(source='ja', target=lang)
    
    def find_furigana(self, kanji_word):
        result = self.furigana_mode.convert(kanji_word)
        if result[0]['kana'] != result[0]['orig'] and result[0]['hira'] != result[0]['orig']: #check if all character is not hiragana,katakana
            furigana = ''.join(item['hira'] for item in result)
            return furigana
        else:
            return False
    
    def find_translation(self, kanji_word):
        translation = self.translation_mode.translate(text=kanji_word)
        return translation
    
    def combine_result(self, word):
        if self.find_furigana((word)):
            result = f'{self.find_furigana(word)} {self.find_translation(word)}'
        else:
            result = f'{self.find_translation(word)}'
            
        return result