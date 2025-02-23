# Assignment: write a program that deals / print out 5 cards
# first shuffle the cards using:  https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1
# get the deck_id form this shuffle and with the deck_id get the cards using: https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2


import requests
import json

# this will shuffle the cards
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
data = response.json()

#need to get deck_id and save it as new_deck_id for 5 cards deal
new_deck_id = data["deck_id"]

# deal 5 cards
new_url = f"https://deckofcardsapi.com/api/deck/{new_deck_id}/draw/?count=5"
new_response = requests.get(new_url)
new_data = new_response.json()

##print(new_data)


with open ("card.json", "w") as fp: #creating a card.json file where the data of 5 deal cards will be saved
    json.dump(new_data, fp)

    for card in new_data ["cards"]:
        print(f"Value of the card is: {card['value']}")
        print(f"Suit of the card is: {card['suit']}")
        print('\t')

#reference: https://www.geeksforgeeks.org/response-json-python-requests/