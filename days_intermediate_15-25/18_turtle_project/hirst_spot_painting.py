# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst-spots.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module

import random

color_list = [
    (246, 244, 243), (233, 239, 246), (240, 246, 243), (247, 239, 243), (129, 165, 205), (223, 151, 109), (31, 40, 60), (202, 133, 146),
    (139, 185, 163), (236, 214, 92), (167, 60, 47), (143, 64, 72), (34, 100, 151), (171, 28, 33), (237, 165, 156), (216, 84, 76), (49, 114, 91),
    (233, 159, 163), (169, 188, 222), (155, 34, 31), (17, 96, 71), (30, 64, 59), (57, 51, 48), (50, 44, 48), (28, 60, 115), (103, 128, 163), (213, 88, 93),
    (174, 200, 188), (32, 152, 210), (65, 66, 57)
]

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for num_of_dots in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if num_of_dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_screen = turtle_module.Screen()
my_screen.exitonclick()