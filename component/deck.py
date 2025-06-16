class Deck:
    def __init__(self):
        self.font_list = list()
        self.back_list = list()
        
    def add_card(self,font, back):
        self.font_list.append(font)
        self.back_list.append(back)