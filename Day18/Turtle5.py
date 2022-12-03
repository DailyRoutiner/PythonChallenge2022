from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)       # rgb 쓰려면 필요함

#colors = ["medium blue", "chartreuse", "gold", "sienna", "medium violet red", "magenta","spring green", "yellow", "red", "indigo"]
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)

tim.pensize(10)
tim.speed("fastest")

for num in range(21):
    tim.fd(20)
    tim.setheading(random.choice(directions))
    random_color()


screen.exitonclick()