from turtle import Turtle


class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.color("white")
        self.pensize(width=3)
        self.penup()
        self.hideturtle()
        self.draw_middle()

    def draw_middle(self):
        self.goto(x=0, y=280)
        self.setheading(270)
        for _ in range(14):
            self.pendown()
            self.forward(22)
            self.penup()
            self.forward(20)