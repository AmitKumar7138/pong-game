from turtle import Turtle


class PONG(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        newx = self.xcor()+self.xmove
        newy = self.ycor()+self.ymove
        self.goto(newx, newy)

    def bounce(self):
        self.ymove *= -1

    def bounce_paddle(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.move_speed = 0.1
