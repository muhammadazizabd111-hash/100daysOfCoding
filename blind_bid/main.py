import os
import art

def clear_screen():
    if os.name == 'nt': #win
        os.system('cls')
    else:
        os.system('clear') #linux



print(art.logo)



bids = {}
bid_end = False

while bid_end != True:
    name = input('What is your name? ')
    bid_value = int(input('What is your bid? $'))
    bids[name] = bid_value

    others = input("Are there others to bid? Type yes or no: ").lower()
    if others == "yes":
        clear_screen()
    elif others == "no":
        bid_end = True
        max_bid = 0
        winner = ''
        for names in bids:
            if bids[names] > max_bid:
                max_bid = bids[names]
                winner = names        
        print(f"winner is {winner}")  
    else:
        print("Error")
        bid_end = True


#no need in recursive function since we have the while loop!
