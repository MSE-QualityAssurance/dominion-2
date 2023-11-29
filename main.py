import random
import tkinter as tk
from tkinter import messagebox

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

    def show_discard(self):
        return ', '.join([str(card) for card in self.discard])

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

import tkinter as tk
from tkinter import simpledialog, messagebox

class DominionGUI:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.supply = create_supply()
        self.root = tk.Tk()
        self.root.title("Dominion")
        self.setup_ui()
        self.start_turn()

    def setup_ui(self):
        self.player_hand_label = tk.Label(self.root, text="")
        self.player_hand_label.pack()

        self.supply_label = tk.Label(self.root, text="")
        self.supply_label.pack()

        self.buy_button = tk.Button(self.root, text="Buy Card", command=self.buy_card)
        self.buy_button.pack()

        self.end_turn_button = tk.Button(self.root, text="End Turn", command=self.end_turn)
        self.end_turn_button.pack()

    def update_ui(self):
        player = self.players[self.current_player_index]
        hand_text = f"{player.name}'s hand: " + player.show_hand()
        self.player_hand_label.config(text=hand_text)

        supply_text = "Supply: " + ', '.join(f"{name}: {len(stack)}" for name, stack in self.supply.items())
        self.supply_label.config(text=supply_text)

    def start_turn(self):
        self.update_ui()

    def buy_card(self):
        player = self.players[self.current_player_index]
        # Implement card buying logic and update UI
        # ...

    def end_turn(self):
        # Handle end of turn logic
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.start_turn()

    def run(self):
        self.root.mainloop()

# Example usage
players = [Player("Alice"), Player("Bob")]
app = DominionGUI(players)
app.run()

# players = [Player("Alice"), Player("Bob")]
# play_game(players)