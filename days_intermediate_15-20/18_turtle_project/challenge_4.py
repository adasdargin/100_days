import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()
timmy.width(10)
timmy.speed(10)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, b, g


angles = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(25)
    timmy.setheading(random.choice(angles))


screen = t.Screen()
screen.exitonclick()
