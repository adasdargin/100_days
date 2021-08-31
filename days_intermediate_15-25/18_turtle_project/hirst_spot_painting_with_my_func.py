# import colorgram
#
# # rgb_colors = []
# # colours = colorgram.extract("hirst-spots.jpg", 84)
# # for color in colours:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     rgb_colors.append((r, g, b))
# #
# # print(rgb_colors)
#
from turtle import Turtle, Screen, colormode
from random import choice


def draw_hist_painting(dots_per_line, lines, space_btw_lines):
    for lines in range(lines):
        for dots in range(dots_per_line):
            timmy.dot(20, choice(colors_list))
            timmy.forward(50)
        space_btw_lines += 50
        timmy.goto(x_cor, space_btw_lines)


colors_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
               (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
               (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
               (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
               (174, 94, 97), (176, 192, 209), (227, 173, 177), (68, 63, 58), (111, 140, 142), (255, 194, 0),
               (178, 196, 202)]

x_cor = -200
y_cor = -100

colormode(255)
timmy = Turtle()
timmy.penup()
timmy.speed(0)
timmy.goto(x_cor, y_cor)

draw_hist_painting(dots_per_line=10, lines=10, space_btw_lines=y_cor)

screen = Screen()
screen.exitonclick()
