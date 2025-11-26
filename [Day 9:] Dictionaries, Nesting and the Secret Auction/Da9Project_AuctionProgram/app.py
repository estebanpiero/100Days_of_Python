# Auction Program

from art import logo
import os
from time import sleep

bidders = {}
end_program = False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0 
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not end_program:
    print(logo)
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    
    # Store the bid in the dictionary
    bidders[name] = bid_amount
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if more_bidders == 'no':
        end_program = True
        clear_console()
        for key in bidders:
            print(f"{key}: ${bidders[key]}")
        sleep(3)       
    else:
        clear_console()

find_highest_bidder(bidders)    