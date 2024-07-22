# import colorgram
#
# colors = colorgram.extract('image.jpeg', 30)
#
# colors_list = []
#
# # first_color = colors[0]
# # rgb = first_color.rgb
# # print(rgb)
# # red = rgb.r
# # print(red)
#
# for i in colors:
#
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, g, b)
#     colors_list.append(rgb)
# print(colors_list)
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

turtle.colormode(255)

color_list = [(5, 13, 37), (38, 21, 16), (130, 89, 57), (201, 140, 118), (234, 210, 85), (187, 138, 162), (213, 86, 69),
              (79, 8, 20), (38, 137, 63), (194, 80, 100), (145, 85, 104), (31, 87, 29), (74, 107, 139), (220, 177, 212),
              (25, 203, 173), (126, 160, 180), (152, 138, 63), (13, 71, 25), (10, 61, 136), (115, 186, 157),
              (123, 12, 31), (86, 133, 174), (21, 208, 218), (230, 175, 166), (240, 208, 6), (133, 223, 206)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

















screen = Screen()

screen.exitonclick()
