def movment ():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
while not at_goal():
    while wall_in_front():
        if is_facing_north():
            move()
        else : turn_left()
    while wall_on_right() and is_facing_north():
            move()
            if right_is_clear() :
                movment ()
    while front_is_clear():
        move()
    while right_is_clear():
        move()
            

        