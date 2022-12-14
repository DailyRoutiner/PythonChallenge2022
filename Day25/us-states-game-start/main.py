import turtle
from turtle import Turtle, Screen
import pandas

FONT = ("Ariel", 14, "normal")
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guess_list = []


# Convert the guess to Title case
# screen.textinput(title=f"{count}/50 States Correct",  prompt="What's another state's name?")

# Check if the guess is among the 50 states
# Write correct guesses onto the map
# country = data[data.state == answer_state.capitalize()]
#
# if country.empty:
#     answer_text = Turtle()
#     answer_text.penup()
#     answer_text.hideturtle()
#     answer_text.goto(int(country.x), int(country.y))
#     answer_text.write(answer_state.capitalize(), font=FONT)

while len(guess_list) < 50:
    answer_state = screen.textinput(title=f"{len(guess_list)}/50 States Correct", prompt="What's another state's name?").title()

    # if answer_state == "Exit":
    #     missing_states = []
    #     for state in all_states:
    #         if state not in guess_list:
    #             missing_states.append(state)
    #     # states_to_learn.csv
    #     df = pandas.DataFrame(missing_states, columns=["states"])
    #     df.to_csv("states_to_learn.csv")
    #     break

    # List comprehension
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_list]
        df = pandas.DataFrame(missing_states, columns=["states"])
        df.to_csv("states_to_learn.csv")
        break

    # Check if the guess is among the 50 states
    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=FONT)
        guess_list.append(answer_state)

