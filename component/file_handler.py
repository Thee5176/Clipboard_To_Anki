import csv
from .deck import Deck;

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