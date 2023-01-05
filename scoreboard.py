from turtle import Turtle

TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self, x_coord=0, y_coord=0):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.color(TEXT_COLOR)
        self.goto(x_coord, y_coord)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score()
