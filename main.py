from turtle import Turtle, Screen

trl = Turtle()
trl2 = Turtle()
trl.color('white')
trl.shape('square')
trl.shapesize(stretch_wid=5, stretch_len=1)
trl.penup()
trl.goto(400, 0)

scrn = Screen()
scrn.tracer(0)
scrn.setup(width=900, height=500)
scrn.bgcolor('black')

trl2.color('white')
trl2.shape('square')
trl2.shapesize(stretch_wid=5, stretch_len=1)
trl2.penup()
trl2.goto(-400, 0)

ball = Turtle()
# ball.speed(0.005)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

l_player = 0
r_player = 0

score = Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("score_player_1 : 0    score_player_2 : 0",
            align="center", font=("Ariel", 24, "normal"))

scrn.listen()


def go_up():
    new_y = trl.ycor() + 20
    new_x = trl.xcor()
    trl.goto(new_x, new_y)


def go_down():
    new_y = trl.ycor() - 20
    new_x = trl.xcor()
    trl.goto(new_x, new_y)


scrn.onkey(key="Up", fun=go_up)
scrn.onkey(key="Down", fun=go_down)


def go_up2():
    new_y = trl2.ycor() + 20
    new_x = trl2.xcor()
    trl2.goto(new_x, new_y)


def go_down2():
    new_y = trl2.ycor() - 20
    new_x = trl2.xcor()
    trl2.goto(new_x, new_y)


scrn.onkey(key="w", fun=go_up2)
scrn.onkey(key="s", fun=go_down2)
while True:
    scrn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        l_player += 1
        score.clear()
        score.write("l_player : {}    r_player: {}".format(
            l_player, r_player), align="center",
            font=("Courier", 24, "normal"))

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        r_player += 1
        score.clear()
        score.write("l_player : {}    r_player: {}".format(
            l_player, r_player), align="center",
            font=("Courier", 24, "normal"))

    if (360 < ball.xcor() < 370) and (trl2.ycor() + 40 > ball.ycor() > trl2.ycor() - 40):
        ball.setx(360)
        ball.dx *= -1

    if (-360 > ball.xcor() > -370) and (trl.ycor() + 40 > trl.ycor() > trl.ycor() - 40):
        ball.setx(-360)
        ball.dx *= -1
