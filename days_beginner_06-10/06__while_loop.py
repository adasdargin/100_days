def jump():
    move()
    turn_left()
    move()
    turn_right()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)