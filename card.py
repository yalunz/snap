import random
class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    SUITS = ('Hearts','Diamonds','Clubs','Spades')
    VALUES = ('2', '3', '4', '5', '6','7', '8', '9', '10',
              'Jack', 'Queen', 'King', 'Ace')

    def compare(self,other_card):
        if other_card != None:
            return self.value == other_card.value
        else:
            return False

    def __str__(self):
        return '{value} of {suit}'.format(suit=self.suit, value=self.value)


class Deck(object):
    def __init__(self, num_packs,cards=[]):
        self.num_packs = num_packs
        for _ in range(num_packs):
            pack = [ Card(value,suit) for suit in Card.SUITS for value in Card.VALUES ]
            cards = cards + pack
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def is_empty(self):
        return len(self.cards) == 0
    
    def size(self):
        return len(self.cards)



              
