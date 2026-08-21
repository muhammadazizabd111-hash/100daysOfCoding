import random
import hangman_words
import hangman_art 

word = random.choice(hangman_words.word_list).lower()
length = len(word)
print(hangman_art.logo)
print(word)

blank = ""
for lf in range(length):
    blank += "_"


game_over = False

correct_letter = []
life = 6


while not game_over:
    guess = input("Guess: ")

    display = ""

    if guess in correct_letter:
        print("You already have guessed that letter!")


    for letter in word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    if guess not in word:
        life -= 1
        print(f"****************************<6>/{life} LIVES LEFT****************************")

    print(hangman_art.stages[life])

    print(display)

    if display == word:
        game_over = True
        print(f"***********************YOU WIN**********************")
    elif life == 0:
        game_over = True
        print(f"***********************YOU LOSE**********************")
        print("Shame on you, you have killed an innocent human being!")
