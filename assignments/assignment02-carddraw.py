# assignment2-carddraw.py
# API that simulates dealing a deck of cards
# Author: John Crumlish

import requests

# Shuffle Deck
shuffle = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
deck_id = shuffle["deck_id"]

# Draw 5 Cards
draw = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5").json()
cards = draw["cards"]

print("Your cards:\n")

# Print Each Card
for card in cards:
    print(card["value"], "of", card["suit"])