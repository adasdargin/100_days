from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


screen.listen()
screen.onkey(move_forwards, "space")
screen.exitonclick()

