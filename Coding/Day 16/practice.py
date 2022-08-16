from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.shapesize(5, 5, 12)
timmy.color("red")
# timmy.stamp()


timmy.speed('slowest')
timmy.forward(100)
timmy.circle(100)
timmy.backward(200)
timmy.circle(100)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.circle(100)
timmy.right(90)
timmy.circle(100)
timmy.backward(100)
my_screen.exitonclick()
# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Employee City",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# table.add_column("Salary", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# table.align = "r"

# print(table)