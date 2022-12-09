# day 19
from turtle import Turtle, Screen
import random

# Set Screen
screen = Screen()
screen.setup(width= 500, height=400)    # Screen size
user_guess = screen.textinput(title= "Race Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["yellow", "red", "purple", "green", "blue", "black", "orange", "pink"]
all_turtle =[]

y = -100
def initialize_turtle(color , y):
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y)
    return new_turtle

# Set position using goto()
for color in colors:
    all_turtle.append(initialize_turtle(color, y))
    y = y + 30

# Start a race
is_race_on = True
if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230: # xcor is turtle x position
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_guess == winning_color:
                print(f"You win!, Winner is {user_guess}")
            else:
                print(f"You Lose, Winner is {winning_color}")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()