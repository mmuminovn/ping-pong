from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 700)

    def update_score(self):
        self.clear()
        self.write(f'{self.l_score}', font=('Courier', 24, 'normal'))
        self.goto(-150, 260)
        self.write(f'{self.r_score}', font=('Courier', 24, 'normal'))
        self.goto(150, 260)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
