from turtle import Turtle, Screen
import random

tim = Turtle()

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#colors = ["medium blue", "chartreuse", "gold", "sienna", "medium violet red", "magenta","spring green", "yellow", "red", "indigo"]
directions = [0, 90, 180, 270]

# for num in range(3, 11):
#     angle = 360 / num
#     for _ in range(num):
#         tim.fd(100)
#         tim.right(angle)
#     tim.color(random.choice(colors))

# tim.pensize(10)
# tim.speed("fastest")
#
# for num in range(201):
#     tim.fd(20)
#     tim.setheading(random.choice(directions))
#     tim.color(random.choice(colors))
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)

tim.pensize(10)
tim.speed("fastest")

for num in range(201):
    tim.fd(20)
    tim.setheading(random.choice(directions))
    random_color()

screen.exitonclick()
