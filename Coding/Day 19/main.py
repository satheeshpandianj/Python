import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "blue", "yellow", "green", "black", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for item in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[item])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[item])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()