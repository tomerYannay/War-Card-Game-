from Card import Card
from Deck import Deck

class JokerDeck(Deck):
    def __init__(self):
        super().__init__()
        joker1 = Card(14,None)
        joker2 = Card(14,None)
        self.card_list.append(joker1)
        self.card_list.append(joker2)
        self.shuffle()


