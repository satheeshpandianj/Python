from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVING_DISTANCE = 10
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)


    def move_up(self):
        new_y = self.ycor() + MOVING_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_to_start_position(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

