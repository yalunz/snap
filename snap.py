from player import Player
from card import Card, Deck
import random

class Game(object):
    def __init__(self, number_decks):
        self.number_decks = number_decks
        self.player1 = Player(name='Player 1')
        self.player2 = Player(name='Player 2')
        self.main_pile = Deck(number_decks)
        self.round_pile = 0

    # simlation style?
    def simulate(self):
        self.main_pile.shuffle()
        last_card = None

        while (not self.main_pile.is_empty()):
            top_card = self.main_pile.draw()
            print(top_card)
            self.round_pile+=1
            is_match = top_card.compare(last_card)

            if (is_match):
                round_winner = random.choice([self.player1,self.player2])
                print('-' * 10)
                print(round_winner.name + " says SNAP! They collect " + str(self.round_pile) + " cards.")
                print('-' * 10)

                round_winner.add_cards(self.round_pile)
                self.round_pile = 0

            last_card = top_card
        
        print('ALL CARDS PLAYED')

    def show_winner(self):
        print('-' * 10)
        print('Game result:')
        total_cards = str(self.number_decks * 52)

        if self.player1.num_cards == self.player2.num_cards:
            print("It's a draw!")
        else:
            if self.player1.num_cards > self.player2.num_cards:
                print('The winner is {player} (out of a possible {total})'.format(player=self.player1, total=total_cards))
            else:
                print('The winner is {player} (out of a possible {total})'.format(player=self.player2, total=total_cards))
        
        print('-' * 10)

if __name__ == '__main__':
    print('Welcome to SNAP!')
    print('-' * 10)
    while True:
        user_input = input('How many packs of cards do you want to play with? ')
        try:
            num_packs = int(user_input)
            if (num_packs <= 0):
                print("You've got to play with at least one pack!")
            else:
                break
        except ValueError:
            print('Please enter a number!')
    
    print('Simulating a game of snap...')
    print('-' * 10)

    game = Game(num_packs)
    game.simulate()
    winner = game.show_winner()

        
    
    

