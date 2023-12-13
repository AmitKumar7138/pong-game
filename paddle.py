from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, stretch_width, stretch_height, x_pos, y_pos):
        super().__init__()
        self.color('white')
        self.pu()
        self.goto(x_pos, y_pos)
        self.shape('square')
        self.shapesize(stretch_width, stretch_height, 1)

    def paddle_move_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def paddle_move_down(self):
        self.goto(self.xcor(), self.ycor()-20)
