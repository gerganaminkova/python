import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG_GAME")
screen.bgcolor("black")
screen.tracer(0)

paddle_right = Paddle((350,0))
paddle_left = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect wall collision only the top and the bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with right paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()

