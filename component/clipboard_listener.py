import re
import pyperclip
from .language_engine import LanguageEngine;
            
class ClipboardListener:
    def __init__(self):
        self.lang_engine = LanguageEngine()
        self.current_item = str()
        self.last_item = str()
        self.tags = str()
        self.saving_item = str()
        self.first_item_flag = True;
    
    #TODO detect Japanese Character
    
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
        self.saving_item = process_string