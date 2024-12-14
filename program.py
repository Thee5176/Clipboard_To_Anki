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
    
    def export_csv(self, filename='Anki.csv', deli=';', *tag):
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

    def bypass_export_csv(self, deck_rows):
        #In case program fail it continue from the last saved data    
        print(f'rows_created: {deck_rows}')
        with open('Anki.csv', 'w', newline='', encoding='utf-8') as csvfile:
            deckwriter = csv.writer(csvfile, delimiter=';')
            
            deckwriter.writerow(['FRONT','BACK','TAGS'])
            
            for card in deck_rows:
                deckwriter.writerow(card)
        
        print(f'Deck exported to Anki.csv')

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
        myHandler.export_csv()
        
if __name__ == '__main__':
    listen()
    
    # deck = Deck()
    # fhand = FileHandler(deck)
    # deck_rows = [['要望', 'ようぼう\u3000request', ()], ['要する', 'ようする\u3000Required', ()], [' 引き継ぐ', 'ひきつぐ\u3000take over', ()], ['ベルスタッフ', 'Belstaff', ()], ['自家用車', 'じかようしゃ\u3000Private car', ()], ['ハイヤー', 'Hire car', ()], ['館内外', 'かんないそと\u3000Inside and outside the building', ()], ['体調管理', 'たいちょうかんり\u3000Health Management', ()], ['優等', 'ゆうとう\u3000Honors', ()], ['情報', 'じょうほう\u3000information', ()], ['返答', 'へんとう\u3000reply', ()], ['負担をかける', 'ふたんをかける\u3000Put a burden on', ()], ['同様', 'どうよう\u3000Similar', ()], ['回避', 'かいひ\u3000Avoid', ()], ['~うえで', '~And', ()], ['用途', 'ようと\u3000Applications', ()], ['車寄せ', 'くるまよせせ\u3000Port', ()], ['出迎え', 'でむかえ\u3000Meet and greet', ()], ['接遇', 'せつぐう\u3000Hospitality', ()], ['見送り', 'みおくり\u3000Seeing off', ()], ['ト ーン', 'tone', ()], ['曖昧', 'あいまい\u3000ambiguous', ()], ['車種', 'しゃしゅ\u3000Car model', ()], ['連携をとる', 'れんけいをとる\u3000Collaborate', ()], ['トラブル', 'trouble', ()], ['回避', 'かいひ\u3000Avoid', ()], ['複数', 'ふくすう\u3000multiple', ()], ['同様', 'どうよう\u3000Similar', ()], ['負担をかける', 'ふたんをかける\u3000Put a burden on', ()], ['クッション言葉', 'Cushion Words', ()], ['聞き返し', 'ききかえし\u3000Ask again', ()], ['情報交換', 'じょうほうこうかん\u3000Information Exchange', ()], ['ロビー', 'lobby', ()], ['ドアマン', 'doorman', ()], ['玄関', 'げんかん\u3000entrance', ()], ['ベルスタッフ', 'Belstaff', ()], ['ベルデスク', 'Bell Desk', ()], ['シャトルバス', 'Shuttle bus', ()], ['リムジンバス', 'Limousine bus', ()], ['コンシェルジュ', 'Concierge', ()], [' コンシェルジュデスク', 'Concierge Desk', ()], ['フロント', 'front', ()], ['自家用車', 'じかようしゃ\u3000Private car', ()], ['荷物の積み降ろし', 'にもつのつみふろし\u3000Loading and unloading luggage', ()], ['周辺の警備', 'しゅうへんのけいび\u3000Periphery Security', ()], ['菅内外の案内', 'かんないがいのあんない\u3000Guide to Suga Inside and Outside', ()], ['手配', 'てはい\u3000Arrangements', ()], ['お辞儀', 'bow', ()], ['会釈', 'えしゃく\u3000nod', ()], ['敬礼', 'けいれい\u3000salute', ()], ['最敬礼', 'さいけいれい\u3000Deepest bow', ()], ['業務の流れ', 'ぎょうむのながれ\u3000Workflow', ()]]
    # fhand.bypass_export_csv(deck_rows)

