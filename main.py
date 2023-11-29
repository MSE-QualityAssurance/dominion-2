import random

# Basic card definitions
class Card:
    def __init__(self, name, cost, value=0, victory_points=0):
        self.name = name
        self.cost = cost
        self.value = value
        self.victory_points = victory_points

    def __str__(self):
        return self.name

# Game setup
def create_supply():
    # Basic supply of cards for this simple implementation
    supply = {
        'Copper': [Card('Copper', 0, 1) for _ in range(60)],
        'Silver': [Card('Silver', 3, 2) for _ in range(40)],
        'Gold': [Card('Gold', 6, 3) for _ in range(30)],
        'Estate': [Card('Estate', 2, victory_points=1) for _ in range(24)],
        'Duchy': [Card('Duchy', 5, victory_points=3) for _ in range(12)],
        'Province': [Card('Province', 8, victory_points=6) for _ in range(12)]
    }
    return supply

# Player setup
class Player:
    def __init__(self, name):
        self.name = name
        self.deck = [Card('Copper', 0, 1) for _ in range(7)] + [Card('Estate', 2, victory_points=1) for _ in range(3)]
        random.shuffle(self.deck)
        self.hand = []
        self.discard = []
        self.draw(5)

    def draw(self, num_cards):
        for _ in range(num_cards):
            if len(self.deck) == 0:
                self.deck, self.discard = self.discard, []
                random.shuffle(self.deck)
            if len(self.deck) > 0:
                self.hand.append(self.deck.pop())

    def show_hand(self):
        return ', '.join([str(card) for card in self.hand])

    def play_turn(self, supply):
        print(f"\n{self.name}'s turn. Hand: {self.show_hand()}")
        # Play all treasures in hand (simplified for this example)
        treasure = sum(card.value for card in self.hand)
        print(f"Available coins: {treasure}")

        # Display available cards to buy
        affordable_cards = {card.name for stack in supply.values() for card in stack if card.cost <= treasure}
        print("Cards you can afford to buy: " + ", ".join(affordable_cards))

        # Player chooses a card to buy
        while True:
            choice = input("Choose a card to buy (or type 'pass' to skip): ").capitalize()
            if choice == 'Pass':
                print("Skipping buy phase.")
                break
            elif choice in affordable_cards:
                bought_card = supply[choice].pop()
                self.discard.append(bought_card)
                print(f"Bought {bought_card}")
                break
            else:
                print("Invalid choice or can't afford the card. Please choose again.")

        # Cleanup
        self.discard.extend(self.hand)
        self.hand = []
        self.draw(5)

# Main game loop
def play_game(players):
    supply = create_supply()
    while len(supply['Province']) > 0:
        for player in players:
            player.play_turn(supply)
            if len(supply['Province']) == 0:
                break

    # Calculate scores
    print("\nGame Over! Final Scores:")
    for player in players:
        score = sum(card.victory_points for card in player.deck + player.hand + player.discard)
        print(f"{player.name}: {score} points")

# Example game
players = [Player("Alice"), Player("Bob")]
play_game(players)