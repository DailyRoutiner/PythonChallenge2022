from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)


def draw_spirograph(num):
    for _ in range(int(360/num)):
        random_color()
        tim.circle(120)
        tim.left(num)     # tim.setheading(5)


draw_spirograph(5) # 1~ 360

screen.exitonclick()

