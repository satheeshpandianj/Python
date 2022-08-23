import random
import colorgram
import turtle as t
from turtle import Turtle, Screen

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 20)
new_color = []
for each_color in colors:
    r = each_color.rgb.r
    g = each_color.rgb.g
    b = each_color.rgb.b
    final_color = (r, g, b)
    new_color.append(final_color)

# print(new_color)  # [(232, 172, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
# (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (96, 246, 252), (243, 33, 165),
# (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]

new_color = [(232, 172, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
(229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (96, 246, 252), (243, 33, 165),
(229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]

t.colormode(255)
tim = Turtle()
screen = Screen()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(223)
tim.forward(500)
tim.left(137)


def draw_shape():
    for dot in range(0, 10):
        tim.dot(20, random.choice(new_color))
        tim.forward(80)

    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(800)
    tim.left(180)


for _ in range(15):
    draw_shape()

screen.exitonclick()
