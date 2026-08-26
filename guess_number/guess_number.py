logo = r"""   ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/      
          """



import random
import os

def game():
    print(logo)
    random_number = random.randint(0,4000)

    difficulty = input("Choose either hard or easy mode: ")

    life = 1

    if difficulty == 'easy':
        life = 12
    elif difficulty == 'hard':
        life = 5

    continue_guess = True

    while continue_guess:

        print(f"you have {life} attempts")

        try:
            user_input = int(input("Guess a number 1 and 4000: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_input > random_number:
            print("Too high")
            life -= 1
        elif user_input < random_number:
            print('Too low')
            life -= 1
        elif user_input == random_number:
            print("You got it))")
            continue_guess = False


        if life == 0:
            print("Out of lives!")
            break


while True:
    game()
    cont_g = input("Continue? Yes?: ").lower()
    if cont_g == 'yes':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        game()
    else:
        break

