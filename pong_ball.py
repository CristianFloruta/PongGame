from turtle import Turtle

BALL_SPEED = "fast"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.speed(BALL_SPEED)
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.goto(0, 0)

    def move(self):
        x_coord = self.xcor() + self.x_move
        y_coord = self.ycor() + self.y_move
        self.goto(x_coord, y_coord)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1