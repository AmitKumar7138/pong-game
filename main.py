from turtle import Turtle, Screen
import turtle
from paddle import Paddle
from pong_class import PONG
from score_board import ScoreBoard
import time

WINNING_SCORE = 10

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)


r_paddle = Paddle(stretch_width=5, stretch_height=1, x_pos=350, y_pos=0)
l_paddle = Paddle(stretch_width=5, stretch_height=1, x_pos=-350, y_pos=0)
ball = PONG()
score_board_r = ScoreBoard('r', 200)
score_board_l = ScoreBoard('l', -200)


screen.listen()
screen.onkey(r_paddle.paddle_move_up, 'Up')
screen.onkey(r_paddle.paddle_move_down, 'Down')
screen.onkey(l_paddle.paddle_move_up, 'w')
screen.onkey(l_paddle.paddle_move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        score_board_l.inc_score()
        ball.restart()
        score_board_l.updarte_scoreboard()

    if ball.xcor() < -380:
        score_board_r.inc_score()
        ball.restart()
        score_board_r.updarte_scoreboard()

    if int(score_board_l.score) == WINNING_SCORE or int(score_board_r.score) == WINNING_SCORE:
        if int(score_board_l.score) > int(score_board_r.score):
            winner = 'Player on the left paddle'
        else:
            winner = 'Player on the right paddle'

        game_over = Turtle()
        game_over.pu()
        game_over.color('white')
        game_over.home()
        game_over.write(f"GAME OVER",
                        align='center', font=("Courier", 24, "normal"))
        game_over.goto(0, -30)
        game_over.write(f"{winner} won!",
                        align='center', font=("Courier", 24, "normal"))
        game_is_on = False


screen.exitonclick()
