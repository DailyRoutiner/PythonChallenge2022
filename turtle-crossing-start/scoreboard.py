from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)