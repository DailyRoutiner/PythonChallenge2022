def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if right_is_clear():
        jump()
    elif wall_in_front() == True:
        turn_left()
    elif wall_on_right():
        move()
    else:
        move()
    
