# from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print("Welcome to the silent auction App!")
print(art.logo)

bids = {}
further_bidder_exists = True

while further_bidder_exists:
    name = input("Who is bidding?\n")
    bid = int(input("What is your bid?\n$"))

    bids[name] = bid

    answer = input("Anyone else, who would like to bid? Type 'yes' or 'no':\n").lower()
    if answer == "no":
        further_bidder_exists = False

highest_bid = 0
winner = 0

for bid in bids:
    if bids[bid] > highest_bid:
        highest_bid = bids[bid]
        winner = bid

print(f"The highest bid was {highest_bid}, {winner} has won the auction!")

