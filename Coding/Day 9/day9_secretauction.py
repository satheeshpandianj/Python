from art import logo
import os

print(logo)

def highest_bidder(bidding_record): 
    maximum = 0
    name = ""   
    for dict in bidding_record:
        if int(bidding_record[dict]) >= maximum:
            maximum = int(bidding_record[dict])
            name = dict
    os.system('clear') 
    print(f"The winner is {name} with a bid of ${maximum}.")    
    
bids = {}

should_continue = True

while should_continue:
    name = input("What is your name?\n")
    price = input("What is your bid?\n$")
    bids[name] = price
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if new_bidder == 'no':
        should_continue = False    
        highest_bidder(bids)  
    else:
        os.system('clear') 
 

