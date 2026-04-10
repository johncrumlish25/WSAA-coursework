# assignment02-carddraw.py
# API that simulates dealing a deck of cards
# Author: John Crumlish

import requests

# Request a new shuffled deck from the Deck of Cards API
shuffle = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
deck_id = shuffle["deck_id"]

# Draw 5 cards from the shuffled deck using the deck ID
draw = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5").json()
cards = draw["cards"]

print("Your cards:\n")

# Print each cards suit and value
for card in cards:
    print(card["value"], "of", card["suit"])