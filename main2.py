from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

scrn = Screen()
scrn.tracer(0)
scrn.setup(width=900, height=600)
scrn.bgcolor('black')
scrn.tracer(0)

r_paddle = Paddle((400, 0))
l_paddle = Paddle((-400, 0))
ball = Ball()
scrn.listen()
scrn.onkey(key="Up", fun=r_paddle.go_up)
scrn.onkey(key="Down", fun=r_paddle.go_down)
scrn.onkey(key="w", fun=l_paddle.go_up)
scrn.onkey(key="s", fun=l_paddle.go_down)
scoreboard = Score()
while True:
    time.sleep(ball.move_speed)
    scrn.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if r_paddle.distance(ball) < 50 and ball.xcor() > 380:
        ball.x_bounce()

    if l_paddle.distance(ball) < 50 and ball.xcor() < -380:
        ball.x_bounce()
        ball.move_speed *= 0.8
    if ball.xcor() > 440:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() < -440:
        ball.reset()
        scoreboard.r_point()

    ball.move()

    # scoreboard.l_player()
    # scoreboard.r_player()
    scoreboard.update_score()

scrn.exitonclick()
