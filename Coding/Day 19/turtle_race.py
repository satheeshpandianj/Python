from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)

colors = ["red", "blue", "green", "violet", "yellow", "brown", "cyan", "purple", "black"]
turtle_start_position = [0, 50, 100, 150, 200, -50, -100, -150, -200]
turtle_count = screen.numinput(title="Turtle Race", prompt="How many turtle will be in the race? Enter the number: ",
                               default=8, minval=2, maxval=8)
# print(turtle_count)
all_turtles = []

for turtle in range(int(turtle_count)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=random.choice(turtle_start_position))
    all_turtles.append(new_turtle)

new_color_list = []
for number_of_turtles in range(int(turtle_count)):
    new_color_list.append(colors[number_of_turtles])

# print(new_color_list)


def ask_input_color():
    user_input = screen.textinput(title="Turtle Race", prompt="which turtle will will the race? Enter the color: ")
    return user_input


user_bet = ask_input_color()
# print(user_bet)

while user_bet not in new_color_list:
    user_bet = ask_input_color()

is_race_on = True

# while is_race_on:
#     for item in all_turtles:
#         if item.xcor() > 230:
#             is_race_on = False
#             winning_color = item.pencolor()
#             if user_bet == winning_color:
#                 print(f'You have won! The winner is {winning_color} turtle')
#             else:
#                 print(f'You have lost! The winner is {winning_color} turtle')
#         random_distance = random.randint(1, 10)
#         item.forward(random_distance)

while is_race_on:
    for item in all_turtles:
        random_distance = random.randint(1, 10)
        item.forward(random_distance)
        if item.xcor() > 230:
            item.setheading(180)
        if item.xcor() <= -230:
            is_race_on = False
            winning_color = item.pencolor()
            if user_bet == winning_color:
                print(f'You have won! The winner is {winning_color} turtle')
            else:
                print(f'You have lost! The winner is {winning_color} turtle')

screen.exitonclick()
