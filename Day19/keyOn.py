from turtle import Turtle, Screen
screen = Screen()
tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
def turn_left():
    header = tim.heading() + 10
    tim.setheading(header)
def turn_right():
    header = tim.heading() - 10
    tim.setheading(header)

# listen key on
screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
