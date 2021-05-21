# import turtle
# timmy = turtle.Turtle()     # new turtle object

# or

# aliasing modules
# import turtle as t
#timmy = t.Turtle()

# or

# keyword / Module name/ keyword/ Module thing
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkOrange")
timmy.forward(100)

# object  # Class
my_screen = Screen()

# object .#attribute = 300
print(my_screen.canvheight)

# object .#method
my_screen.exitonclick()

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/labs/lab01/colors