import random
from turtle import Turtle, Screen
import turtle as t


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


tim = t.Turtle()
# tim.shape("turtle")
# tim.color("gold2")
tim.speed("fastest")
t.colormode(255)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(75)
        tim.seth(tim.heading() + size_of_gap)

draw_spirograph(10)
# for number in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# number_of_sides = 5

# colors = ["blue", "green", "black", "red", "gray", "khaki", "cyan"]
# angles = [0, 90, 180, 270]
# def draw_shape(number_of_sides, line_colors):
#     angle = 360 / number_of_sides
#     for number in range(number_of_sides):
#         tim.color(line_colors)
#         tim.pensize(10)
#         tim.forward(100)
#         tim.right(angle)
#
# for _ in range(3,11):
#     draw_shape(_, random.choice(colors))
#
# t.colormode(255)
#

#
# number = random.randint(1,100)
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(number):
#     tim.setheading(random.choice(angles))
#     tim.color(random_color())
#     tim.forward(30)

#
screen = Screen()
screen.exitonclick()
