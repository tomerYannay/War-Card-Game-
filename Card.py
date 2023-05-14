class Card:
    def __init__(self,val,suit):
        self.suit = suit
        self.val = val
        if(val < 0 or val > 14):
            raise ValueError('Invalid value')
        list = ['diamond', 'club', 'heart', 'spade',None]
        if(suit not in list ):
            raise ValueError('Invalid suit')
        if((suit is None and val != 14) or(suit is not None and val == 14)):
            raise ValueError('Something went wrong')
        if(suit is not None):
            self.suit = suit.lower()

        name = self.convert_num_to_name(self.val)
        # return self.__repr__(name,suit)

    def convert_num_to_name(self,val):
        dict = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four' ,5 : 'five',6 :'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'jack',12:'queen',13:'king',14:'joker'}
        return dict.get(val)

    def __repr__(self):
        name = self.convert_num_to_name(self.val)
        suit = self.suit
        if(suit is not None):
            upper_name = name[0].upper() + name[1:]
            upper_suit = suit[0].upper() + suit[1:]
        if(name == 'joker'):
            str = f'{name[0].upper() + name[1:]}!'
            return str
        str = f'{upper_name} of {upper_suit}s'
        return str

    def __lt__(self, other):
        return self.val < other.val
