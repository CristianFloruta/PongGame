from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"


class Paddle(Turtle):

    def __init__(self, x_coord=0, y_coord=0):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.goto(self.x_coord, self.y_coord)

    def move_up(self):
        self.y_coord = self.ycor() + 20
        self.goto(self.xcor(), self.y_coord)

    def move_down(self):
        self.y_coord = self.ycor() - 20
        self.goto(self.xcor(), self.y_coord)
