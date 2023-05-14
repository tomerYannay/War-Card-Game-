from JokerDeck import JokerDeck
from Card import Card
from Deck import Deck


class WarGame:
    def __init__(self, has_jokers):
        self.card_pile = []
        if type(has_jokers) != bool:
            raise ValueError('Invalid boolean type')
        if (has_jokers):
            self.d1 = JokerDeck()
            self.d2 = JokerDeck()
        else:
            self.d1 = Deck()
            self.d2 = Deck()

    def give_pile(self,player):
        if(player == 1):
            for card in self.card_pile:
                self.d1.card_list.append(card)
        else:
            for card in self.card_pile:
                self.d2.card_list.append(card)
        self.card_pile = []

    def round(self,i):

        card_p1 = self.d1.draw_card()
        card_p2 = self.d2.draw_card()
        print(f'Round {i}: {card_p1} vs {card_p2}')
        self.card_pile.append(card_p1)
        self.card_pile.append(card_p2)
        if(card_p1 < card_p2):
            print('Player 2 Won\n')
            self.give_pile(2)
        elif(card_p2 < card_p1):
            print('Player 1 Won\n')
            self.give_pile(1)
        else:
            print(len(self.d1.card_list),len(self.d2.card_list),len(self.card_pile))
            print('War!\n.\n.\n.\n')

            if(len(self.d1.card_list) < 3):
                len_cards1 = len(self.d1.card_list)
            else:
                len_cards1 = 2
            if (len(self.d2.card_list) < 3):
                len_cards2 = len(self.d2.card_list)
            else:
                len_cards2 = 2

                for card in self.d1.card_list[0:len_cards1]:
                    self.d1.card_list.pop(0)
                    self.card_pile.append(card)

                for card in self.d2.card_list[0:len_cards2]:
                    self.d2.card_list.pop(0)
                    self.card_pile.append(card)

    def run_game(self):
        round_number = 0
        print('STRATING WAR...')
        while(len(self.d1.card_list) != 0 and len(self.d2.card_list) != 0):
            self.round(round_number)
            round_number = round_number + 1
        if(len(self.d2.card_list)==0):
            print('PLAYER 1 IS THE VICTOR!')
        elif(len(self.d1.card_list) == 0):
            print('PLAYER 2 IS THE VICTOR!')
        else:
            print("IT'S A TIE!")
