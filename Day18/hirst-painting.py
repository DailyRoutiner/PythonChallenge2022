import random
from turtle import Turtle, Screen
import colorgram

colors = colorgram.extract('Ellipticine.png', 30)
color_arr = []
for i in range(len(colors)):
    tuple = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
    color_arr.append(tuple)

#print(color_arr)
color_list = [(34, 108, 167), (223, 229, 235), (227, 233, 230), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46), (99, 93, 2)]

# circle =20,  space=50 , dot = 10 X 10
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.hideturtle()

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()

