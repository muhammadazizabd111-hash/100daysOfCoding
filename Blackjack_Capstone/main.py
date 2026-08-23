import random
import os
import art 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_blackjack(hand): # == evaluates boolean #### sum() function
    return len(hand)==2 and sum(hand)==21 #if len =2 and sum=21 returns True

def check_ace(hand):
    while 11 in hand and sum(hand) > 21: # element in list and while for continious work
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def check_continue(player, dealer):
    while True:
        cont = input('Do you want to draw another card? "y" for yes, "n" for no: ').lower()
        
        if cont == 'y':
            player.append(random.choice(cards))
            p_score = check_ace(player)
            print(f"Your cards: {player}, current score: {p_score}")
            
            if p_score > 21:
                print(f"Your total is {p_score}. You went over 21. You lose!😮‍💨")
                return
                
        elif cont == 'n':
            while check_ace(dealer) <= 16:
                dealer.append(random.choice(cards))
            
            p_score = check_ace(player)
            d_score = check_ace(dealer)
            
            print(f"\nYour final hand: {player}, final score: {p_score}")
            print(f"Dealer's final hand: {dealer}, final score: {d_score}")
            
            if d_score > 21:
                print("Dealer went over 21! You win! 🎉✨")
            elif p_score > d_score:
                print("You win! 🎉✨")
            elif d_score > p_score:
                print("Dealer wins! You lose.😮‍💨")
            else:
                print("It's a draw!😮‍💨")
            
            return

def play_game():
    print(art.logo)
    player = []
    dealer = []

    for time in range(2):
        player.append(random.choice(cards))
        dealer.append(random.choice(cards))

    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Dealer's first card: {dealer[0]}")

    if check_blackjack(dealer):
        print(f"Dealer's hand: {dealer}")
        print("Dealer got blackjack! You lost.😮‍💨") 
        return
    elif check_blackjack(player):
        print(f"Player's hand: {player}")
        print("Player got blackjack, yahoooww! Congratulations man! 🎉✨")
        return
    else:
        print("No initial blackjacks, moving to player turn...")


    check_continue(player, dealer)#only loop line fo game function


while True:
    play_game()

    again = input("\nWould you like to play again? Type 'y' for yes, 'n' for no: ").lower()
    if again == "y":
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("Thanks for playing!")
        break

