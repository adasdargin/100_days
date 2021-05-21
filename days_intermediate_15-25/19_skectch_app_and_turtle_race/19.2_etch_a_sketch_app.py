from turtle import Turtle, Screen

timmy = Turtle()


def move_forwards():
    timmy.forward(20)


def move_backwards():
    timmy.backward(20)


def turn_left():
    timmy.left(5)


def turn_right():
    timmy.right(5)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


my_screen = Screen()
my_screen.listen()
my_screen.onkey(move_forwards, "w")
my_screen.onkey(move_backwards, "s")
my_screen.onkey(turn_left, "a")
my_screen.onkey(turn_right, "d")
my_screen.onkey(clear_screen, "c")

my_screen.exitonclick()

