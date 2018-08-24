from Deck import Deck

class Player:

    def __init__(self):
        self.name = input("Enter Player Name: ")
        self.hand = []
        self.chips = 0
        self.winner = False

    def draw(self, other, N):
        if isinstance(other, Deck):
            self.hand += [other.cards.pop() for x in range(N)]

    def __repr__(self):
        return self.name + ' ' + str(self.hand)
