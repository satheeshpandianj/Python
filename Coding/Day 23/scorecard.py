from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scorecard(Turtle):

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_score()

    def increase_level(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

