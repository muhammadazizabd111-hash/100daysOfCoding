from turtle import Turtle
from turtle import Screen
import random

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=800,height=600)
user_option = screen.textinput(title='Make ur bet,',prompt='Which turtle is going to win?: ')
y_poss = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-380, y=y_poss[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


if user_option: #checkes if user did not press cancel
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            winner = turtle.pencolor()
            if winner == user_option:
                print(f"You won! The {winner} turtle has won the race!")
            else:
                print(f"You lost:((( The {winner} turtle has won the race!")

            is_race_on = False
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()


