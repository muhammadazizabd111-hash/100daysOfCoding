from art import logo
from art import vs
from game_data import data
import random
import os

A = random.choice(data)
score = 0
to_continue = True


while to_continue:
    print(logo)
    print('King of the Hill, if you are confident enough!\n\n Spoiler, you gotta fail, cuz game is designed this way:)\n\n')


    if score > 0:
        print('You got it right!')
        print(f"Your score is {score}.")
    B = random.choice(data)

    while A == B:
        B = random.choice(data)

    print(f" A is {A['name']}, a {A['description']} from {A['country']}") 
    print(vs)
    print(f"B is {B['name']}, a {B['description']} from {B['country']}") 


    user_choice = input('Who has more followers? A or B?: ').upper()
    while user_choice not in ['A', 'B']:
        user_choice = input('Please choose A or B: ').upper()

    if user_choice=='A':
        user_choice = A
    elif user_choice == 'B':
        user_choice = B

    if user_choice['follower_count'] == max(A['follower_count'], B['follower_count']):
        score += 1
        A = user_choice
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('You lost')
        to_continue = False


