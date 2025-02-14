import os

from art import logo

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {}

print(logo)

bidding = "yes"

while bidding == "yes":
    user = input("What is your name? ")
    bid = int(input("What is you bid? $"))

    bids[user] = bid

    bidding = input("Is there another user who wants to bid? \"Yes\" or \"No\" ").lower()
    if bidding == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')

highest_bidder = ""
highest_bid = 0

for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bidder = bidder
        highest_bid = bid_amount

print(f"The winner is {highest_bidder} who bid ${highest_bid}!")