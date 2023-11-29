import random

class Card:
    def __init__(self, name, cost, action):
        self.name = name
        self.cost = cost
        self.action = action

    def play(self, player, game):
        self.action(player, game)

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.hand = []
        self.discard_pile = []
        self.play_area = []
        self.actions = 0  # Number of actions the player can perform

    def draw(self, n=1):
        for _ in range(n):
            if not self.deck:
                self.deck, self.discard_pile = self.discard_pile, []
                random.shuffle(self.deck)
            if self.deck:
                self.hand.append(self.deck.pop())

    # Example method to show a player's hand
    def show_hand(self):
        return [card.name for card in self.hand]

class Game:
    def __init__(self, players):
        self.players = players
        self.supply = {}  # Add cards to the supply
        self.trash = []

    def play_game(self):
        # Game loop goes here
        pass

# Define some basic cards
village = Card("Village", 3, lambda player, game: (player.draw(1), setattr(player, 'actions', player.actions + 2)))
smithy = Card("Smithy", 4, lambda player, game: player.draw(3))

# Example of setting up a game
players = [Player("Alice"), Player("Bob")]
game = Game(players)

# Adding some cards to a player's deck and testing draw
alice = players[0]
alice.deck = [village, smithy, village, smithy, village]
alice.draw(5)  # Draw 5 cards

# Show Alice's hand after drawing
alice.show_hand()
