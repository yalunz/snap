class Player(object):
    def __init__(self, name, num_cards=0):
        self.name  = name
        self.num_cards = num_cards

    def add_cards(self, num_won):
        self.num_cards += num_won
        
    def __str__(self):
        return '{name} with {num} cards'.format(name=str(self.name), num=self.num_cards)
