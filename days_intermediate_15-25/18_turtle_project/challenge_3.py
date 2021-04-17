from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkOrange2")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "PowderBlue", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(150)
        timmy.right(angle)


for shape_side_num in range(3, 10):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_num)


screen = Screen()
screen.exitonclick()
