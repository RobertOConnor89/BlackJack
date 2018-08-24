class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.faceup = False

    def __lt__(self, other):
        if self.rank  < other.rank:
            return True
        else:
            return False
        
    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank
        else:
            return False
        
    def __repr__(self):
        if self.faceup == True:
            return "{} of {}".format(self.rank,self.suit)
        else:
            return "?"
