import os
from art import logo
print(logo)

def highest_bidder(auction_dict):
    #{"name" : bid_value}
    max_bid = 0
    win = {}
    for bidder in auction_dict:
        bid = auction_dict[bidder]
        if bid > max_bid:
            max_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")

auction_dict = {}
flag = True
while flag:
    name = input("What is your name ? ")
    bid = int(input("What is your bid ? $"))
    auction_dict[name] = bid
    ans = input("Are there any other bidders ? yes/no \n").lower()
    if ans == "no":
        flag = False
    else:
        os.system('cls')

highest_bidder(auction_dict)


