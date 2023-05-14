import random
from Card import Card

class Deck:
    def __init__(self):
        card_list = []
        self.card_list = card_list
        suits = ['heart', 'diamond', 'club', 'spade']
        ranks = [1,2, 3, 4, 5, 6, 7, 8,9, 10, 11,12,13]
        for suit in suits:
            for rank in ranks:
                card = Card(rank,suit)
                card_list.append(card)
        self.shuffle()

    def draw_card(self):
        if(len(self.card_list) == 0):
            return None
        self.first_card = self.card_list.pop(0)
        return self.first_card

    def draw_multiple(self,num):
        if(len(self.card_list) == 0):
            return None
        self.trash_list = []
        if(num > len(self.card_list)):
            num = len(self.card_list)
        for card in self.card_list[:num]:
            self.trash_list.append(self.card_list.pop())
        return self.trash_list

    def shuffle(self):
        random.shuffle(self.card_list)

    def reset(self):
        for card in self.trash_list:
            self.card_list.append(card)
        self.card_list.append(self.first_card)
        self.shuffle()

    def __repr__(self):
        return f'A Deck Containing {len(self.card_list)} Cards'


    def __lt__(self,other):
        return len(self.card_list) < len(other.card_list)