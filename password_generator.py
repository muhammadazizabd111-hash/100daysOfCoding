import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword gen!")

while True:
    try:
        length = int(input("Input the length of your password: "))
        break #stops the while loop immideately
    except ValueError:
        print("Invalid input! Please enter a number.")

list_groups = [lowercase, numbers_str, symbols]

password_list = []
for number in range(length):
    rand_group = random.choice(list_groups)
    rand_char = random.choice(rand_group)
    password_list.append(rand_char)

password = ""

for char in password_list:
    password += char

print(f"Your {length} long password is {password}")