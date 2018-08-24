import random
from Card import Card

class Deck:

    ranks = [str(x) for x in range(2,11)] + ["Jack", "Queen", "King", "Ace"]
    suits = ["Hearts","Diamonds", "Clubs", "Spades"]
    
    def __init__(self):
        self.cards = [Card(x,y) for x in self.ranks for y in self.suits]

    def __repr__(self):
        return str(["{} of {}".format(self.cards[x].rank,self.cards[x].suit)\
               for x in range(len(self.cards))])

    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self, N):
        hand = [self.cards.pop() for x in range(N)]
        return hand
