from turtle import Turtle

FONT = ('Arial', 24, 'normal')

CENTER = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align=CENTER, font=FONT)

    def show_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=CENTER, font=FONT)

