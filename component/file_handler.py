import csv
import os
from pathlib import Path
from pprint import pprint

class FileHandler():
    """
    Responsibility: parse data from Deck to csv file
    """
    def __init__(self, deck):
        self.deck = deck
    
    def export_csv(self, filename='Anki.csv', deli=';', *tag):
        #TODO Check consistency len(font) = len(back)??
        deck_rows = []
        for i in range(len(self.deck.font_list)):
            deck_rows.append([self.deck.font_list[i],self.deck.back_list[i], tag])
            
        pprint(deck_rows)

        '''if file already exist then append line'''
        isFileExist = Path(os.getcwd() + "/Anki.csv").exists()

        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            deckwriter = csv.writer(csvfile, delimiter=deli)
            
            if not isFileExist:
                deckwriter.writerow(['FRONT','BACK','TAGS'])
            
            for card in deck_rows:
                deckwriter.writerow(card)
        
        print(f'Clipboard list exported to {filename}')