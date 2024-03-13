from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.move_y *= -1

    def x_bounce(self):
        self.move_x *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_x *= -1
        self.move_speed = 0.1
