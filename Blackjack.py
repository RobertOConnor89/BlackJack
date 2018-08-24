"""this is a text-based blackjack game"""
from Deck import Deck
from Player import Player

'''issues to fix:
show dealers second card at the right time
automatically declare players as winner if dealer loses
write debugging script
SET UP A GITHUB REPO!!!!!!!!!!!!!!!!!'''


class BlackJack:
    # a dictionary that assigns points to ranks
    scores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        self.dealer = Player()
        self.deck = Deck()
        self.players = [self.dealer]

    def add_player(self):  # adds a player to the game
        self.players.append(Player())

    def deal_hand(self):  # deals cards to all players and sets faceup/down
        for x in self.players:
            x.draw(self.deck, 2)
            if x == self.dealer:
                x.hand[0].faceup = True
            else:
                x.hand[0].faceup = True
                x.hand[1].faceup = True

    def show_cards(self):  # prints players hands to screen
        for x in self.players:
            print(x)

    def players_play(self, player):
        total = sum([self.scores[card.rank] for card in player.hand])
        while True:
            if input("{}: hit or stand?".format(player.name)) == "hit":
                player.draw(self.deck, 1)
                player.hand[-1].faceup = True
                total += self.scores[player.hand[-1].rank]
                print(player)
                print(total)
                if total > 21: break
            else:
                print(player)
                print(total)
                break
        if total > 21:
            print("{} has busted!".format(player.name))
            return 0
        else:
            print("{} stands at {}.".format(player.name, total))
            return total

    def dealers_play(self):
        self.dealer.hand[1].faceup = True
        print(self.dealer)
        total = sum([self.scores[card.rank] for card in self.dealer.hand])
        while total < 17:
            self.dealer.draw(self.deck, 1)
            self.dealer.hand[-1].faceup = True
            total += self.scores[self.dealer.hand[-1].rank]
            print(self.dealer)
            if total > 21:
                print("The dealer has busted")
                return 0
        return total

    def play_round(self):  # plays a round of blackjack
        totals = []
        for x in range(len(self.players) - 1):
            totals.append(self.players_play(self.players[x+1]))
        totals.insert(0,self.dealers_play())
        if totals[self.players.index(self.dealer)] >= max(totals):
            self.dealer.winner = True
        else:
            for x in self.players:
                if totals[self.players.index(x)] == max(totals):
                    x.winner = True

    def declare_winners(self):  # prints the winners of a round to screen
        print("Winners:")
        for x in self.players:
            if x.winner == True:
                print(x.name)

    def discard(self):  # clears players hands between rounds
        for x in self.players:
            x.winner = False
            x.hand = []

    def face_up(self):  # turns all cards faceup
        for x in self.players:
            for y in x.hand:
                y.faceup = True

    def start_game(self):  # main game loops
        self.deck.shuffle()
        print("Welcome to Blackjack!")
        while True:
            self.add_player()
            if input("Would you like to add another player?(y/n)") != "y":
                break
        while True:
            self.deal_hand()
            self.show_cards()
            self.face_up()
            self.play_round()
            self.face_up()
            self.show_cards()
            self.declare_winners()
            self.discard()
            if input("would you like to play another round?(y/n)") == "n":
                break
        print("Goodbye!")


if __name__ == "__main__":
    new_game = BlackJack()
    new_game.start_game()
