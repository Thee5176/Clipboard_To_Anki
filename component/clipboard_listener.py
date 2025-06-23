from .deck import Deck
from .file_handler import FileHandler
from .language_engine import LanguageEngine
from .regex_engine import RegexEngine

import time
import pyperclip # type: ignore
            
class ClipboardListener:
    '''
    Responsibility: keep track of update in clipboard item  
    '''
    deck = Deck()
    fileHandler = FileHandler(deck)
    languageEngine = LanguageEngine()

    def __init__(self):
        self.current_item = str()
        self.last_item = str()
        self.tags = str()
        self.saving_item = str()
        self.first_item_flag = True
    
    def detect_new_item(self):
        '''ignore first item that already in the clipboard'''
        if self.first_item_flag:
            self.last_item = self.current_item
            self.first_item_flag = False
            print('Listening to clipboard...')
            pass
        
        '''check if current_item is not the same as last_item'''
        return self.current_item != self.last_item      

    def update_item(self):
        print(f'Detected new clipboard item: {self.current_item}')
        self.last_item = self.current_item

    def clean_item(self):
        try:
            self.saving_item = RegexEngine.clean(self.current_item)

        except ValueError as e:
            print(f'Error : {e}')

    def save_item(self):
        kanji = self.saving_item
                    
        furi_trans_result = self.languageEngine.parse_kanji(kanji)
        
        self.deck.add_card(kanji,furi_trans_result)
        print(f'Saved new item: {self.saving_item}')

    def listen(self):
        try:
            while True:
                self.current_item = pyperclip.paste()
                
                if self.detect_new_item(): # Check the clipboard item against last record
                    
                    self.update_item()

                    self.clean_item()

                    self.save_item()
                
                    print('listening...')
                time.sleep(0.5)
            
        except KeyboardInterrupt:
            print(f'\nStop listen to clipboard')
            self.fileHandler.export_csv()
