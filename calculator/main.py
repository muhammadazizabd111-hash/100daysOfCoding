import art
import os


def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add, #now + is ref to add function without ()
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    to_continue = True
    print(art.logo)

    input1=float(input('What is the first number?: ')) #because we will call it recursively we need to ask for input outside of while loop; only if started over will we ask for first number


    while to_continue:
        for key in operations:
                print(key)
        operation = input("Pick an operation: ")
        input2=float(input('What is the second number?: '))

        if operation in operations:
            result = operations[operation](input1,input2)
            print(f"{input1} {operation} {input2} = {result}")
        else:
            print("Error")
            return

        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if cont == 'y':
            input1 = result
        elif cont == 'n':
            to_continue = False
            os.system('cls')
            calculator()
        else:
            return

calculator()
