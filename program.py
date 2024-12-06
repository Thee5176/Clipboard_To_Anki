class Deck:
    def __init__(self):
        self.font_list = list()
        self.back_list = list()
        
    def add_card(self,font, back):
        self.font_list.append(font)
        self.back_list.append(back)

import time
import re
import pyperclip
            
class ClipboardListener:
    def __init__(self):
        self.lang_engine = LanguageEngine()
        
        self.current_item = str()
        self.last_item = str()
        self.tags = str()
        self.saving_item = str()
    
    #TODO Ignore first item
    #TODO detect Japanese Character
    
    def detect_new_item(self):
        '''check if current_item is not the same as last_item'''
        return self.current_item != self.last_item      
   
    def clean_item(self):
        '''remove whitespace and special characters'''
        process_string = self.current_item
        process_string = re.sub(r'[\'\'\[\-\+\.\^\:\,\]\s\?\!\#\*\&\(\)]', '', process_string)
        self.saving_item = process_string
    
    def update_item(self):
        self.last_item = self.current_item
     

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
            result = f'{self.find_furigana(word)}　{self.find_translation(word)}'
        else:
            result = f'{self.find_translation(word)}'
            
        return result
    
import csv

class FileHandler(Deck):
    def __init__(self, deck):
        super().__init__()
        self.deck = deck
    
    def export_csv(self, filename='Anki.csv', deli='/', *tag):
        #TODO Check consistency len(font) = len(back)??
        deck_rows = []
        for i in range(len(self.deck.font_list)):
            deck_rows.append([self.deck.font_list[i],self.deck.back_list[i], tag])
            
        print(f'rows_created: {deck_rows}')
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            deckwriter = csv.writer(csvfile, delimiter=deli)
            
            deckwriter.writerow(['FRONT','BACK','TAGS'])
            
            for card in deck_rows:
                deckwriter.writerow(card)
        
        print(f'Deck exported to {filename}')


def listen():
    myAnkiDeck = Deck()
    myListener = ClipboardListener()
    myEngine = LanguageEngine()
    myHandler = FileHandler(myAnkiDeck)
    try:
        while True:
            myListener.current_item = pyperclip.paste()
            
            if myListener.detect_new_item():
                print(f'Detected new clipboard item: {myListener.current_item}')
                myListener.update_item()
                myListener.clean_item()
                
                font = myListener.saving_item
                
                back = myEngine.combine_result(font)
                
                myAnkiDeck.add_card(font,back) #not appending
                print(f'Saved new item: {myListener.saving_item}')

            time.sleep(0.5)
        
    except KeyboardInterrupt:
        print(f'Stop listen to clipboard')
        myHandler.export_csv(tag='test_vocab')
        
if __name__ == '__main__':
    listen()