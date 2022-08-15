# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
#
# timmy.shape("turtle")
# timmy.color("red")
# print(timmy.position())
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Employee City",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Salary", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.align = "r"

print(table)