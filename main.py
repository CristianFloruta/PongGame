from turtle import Screen
from time import sleep
from paddle import Paddle
from pong_ball import Ball
from gameBoard import GameBoard
from scoreboard import Scoreboard

NIGHT_MODE = "black"
DAY_MODE = "white"
LEFT_KEY_UP = "q".lower()
LEFT_KEY_DOWN = "a".lower()

# screen game creation
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor(NIGHT_MODE)
screen.title("Python Pong Game")
screen.tracer(0)

# paddle creation and board game set-up
left_paddle = Paddle(-370, 0)
right_paddle = Paddle(370, 0)
ball = Ball()
game_net = GameBoard()
score_left = Scoreboard(-40, 270)
score_right = Scoreboard(40, 270)

# setting paddles movement
screen.listen()
screen.onkeypress(key=LEFT_KEY_UP, fun=left_paddle.move_up)
screen.onkeypress(key=LEFT_KEY_DOWN, fun=left_paddle.move_down)
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

# setting game logic
game_on = True

while game_on:
    sleep(ball.ball_speed)
    screen.update()
    # set up ball movement
    ball.move()
    # detect collision (top and bottom of screen)
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # detect collision with left and right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect when right paddle missed and update score and reset position
    if ball.xcor() > 380:
        score_left.plus_count()
        score_left.update()
        ball.reset_position()
        ball.increase_speed()
    # detect when left paddle missed and update score and reset position
    if ball.xcor() < -380:
        score_right.plus_count()
        score_right.update()
        ball.reset_position()
        ball.increase_speed()

screen.exitonclick()
