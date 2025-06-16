import re
import time
import pyperclip # type: ignore

from .deck import Deck;
from .file_handler import FileHandler;
from .language_engine import LanguageEngine;

            
class ClipboardListener:
    myDeck = Deck()
    myEngine = LanguageEngine()
    myHandler = FileHandler(myDeck)


    def __init__(self):
        self.current_item = str()
        self.last_item = str()
        self.tags = str()
        self.saving_item = str()
        self.first_item_flag = True;
    
    def detect_new_item(self):
        '''ignore first item'''
        if self.first_item_flag:
            self.last_item = self.current_item
            self.first_item_flag = False;
            print("Listening to clipboard...")
            pass
        
        '''check if current_item is not the same as last_item'''
        return self.current_item != self.last_item      

    def update_item(self):
        self.last_item = self.current_item

    def clean_item(self):
        '''remove whitespace and special characters'''
        process_string = self.current_item
        process_string = re.sub(r'[\'\'\[\-\+\.\^\:\,\]\s\?\!\#\*\&\(\)]', '', process_string)
        
        '''check if all character is kanji'''
        kanji_pattern = re.compile(r'[\u3041-\u3096\u30A0-\u30FF\u4E00-\u9FAF]')
        if len(kanji_pattern.findall(process_string)) == len(process_string):
            self.saving_item = process_string
        else:
            raise ValueError(f"text concist non-kanji character: {process_string}")
    
    def listen(self):
        try:
            while True:
                self.current_item = pyperclip.paste()
                
                if self.detect_new_item():
                    print(f'Detected new clipboard item: {self.current_item}')
                    self.update_item()
                    
                    try:
                        self.clean_item()
                    except ValueError as e:
                        print(f"Error : {e}")
                    else:
                        font = self.saving_item
                        
                        back = self.myEngine.combine_result(font)
                        
                        self.myDeck.add_card(font,back) #not appending
                        print(f'Saved new item: {self.saving_item}')
                    finally:
                        print("listening...")
                
                time.sleep(0.5)
            
        except KeyboardInterrupt:
            print(f'Stop listen to clipboard')
            self.myHandler.export_csv()
