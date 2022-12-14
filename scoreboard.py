from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.goto(0, 270)
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"Score: {self.user_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
