import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

# colors = ['red', 'green', 'blue', 'indianred', 'firebrick', 'ForestGreen']
#
#
# tim. setheading(180)
#
# def rand_colors():
#     color = random.choice(colors)
#     return color
#
#
# color = rand_colors()
# for _ in range(3):
#     tim.color(color)
#     tim.left(120)
#     tim.forward(100)
#
# color = rand_colors()
# for _ in range(4):
#     tim.color(color)
#     tim.left(90)
#     tim.forward(100)
#
# color = rand_colors()
# for _ in range(5):
#     tim.color(color)
#     tim.left(72)
#     tim.forward(100)
#
# color = rand_colors()
# for _ in range(6):
#     tim.color(color)
#     tim.left(60)
#     tim.forward(100)
#
# color = rand_colors()
# for _ in range(7):
#     tim.color(color)
#     tim.left(51.4)
#     tim.forward(100)
#
# color = rand_colors()
# for _ in range(8):
#     tim.color(color)
#     tim.left(45)
#     tim.forward(100)
#
# color = rand_colors()
# for _ in range(9):
#     tim.color(color)
#     tim.left(40)
#     tim.forward(100)
#
# color = rand_colors()
# for _ in range(10):
#     tim.color(color)
#     tim.left(36)
#     tim.forward(100)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


#
directions = [0, 90, 180, 270]

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


#
# for i in range(100):
#     tim.color(random_color())
#
#     tim.speed('fast')
#     tim.pensize(5)
#
#     tim.fd(25)
#     tim.setheading(random.choice(directions))

# steps = int(random() * 50)
# angle = int(random() * 90)

# tim.fd(steps)
# tim.left(angle)

tim.speed('fastest')


########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()

screen.exitonclick()
