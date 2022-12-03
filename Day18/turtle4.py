from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["medium blue", "chartreuse", "gold", "sienna", "medium violet red", "magenta","spring green", "yellow", "red", "indigo"]


def random_direct():
    flag = random.choice([1, 2])
    if flag == 1:
        tim.right(90)
        tim.fd(20)
    else:
        tim.left(90)
        tim.fd(20)


for num in range(3, 11):
    random_direct()
    tim.color(random.choice(colors))


screen = Screen()
screen.exitonclick()
