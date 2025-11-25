def turn_right():
    turn_left()
    turn_left()
    turn_left()
 

while at_goal() == False:
    if wall_in_front():
        turn_left()
    if right_is_clear():
        turn_right()
    if front_is_clear():
        move()

#Final Project:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while front_is_clear():
    move()
    
turn_left()

while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
       