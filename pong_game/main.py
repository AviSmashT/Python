from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Initialize:
screen = Screen()
screen.tracer(0)  # Tracer - 0 => freeze the screen, to unfreeze use "screen.update()"
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(height=600, width=800)
right_paddle = Paddle("right")
left_paddle = Paddle("left")
score = Score()
ball = Ball()
SCREEN_Y_LIMIT = 300
# walls = Wall()


# Key mapping:
screen.listen()
# right player
screen.onkeypress(key="w", fun=right_paddle.move_up)
screen.onkeypress(key="s", fun=right_paddle.move_down)
# left player
screen.onkeypress(key="Up", fun=left_paddle.move_up)
screen.onkeypress(key="Down", fun=left_paddle.move_down)

# Game loop:
game_on = True
while game_on:
    screen.update()  # unfreeze screen
    time.sleep(ball.move_speed)  # 0.1 sec delay
    ball.movement()

    # Wall Collision:
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_wall()

    # Paddle collision:
    if ball.distance(left_paddle) < 50 and ball.xcor() > 330 or ball.distance(right_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_paddle()

    # Sides miss:
    if ball.xcor() > 380 or ball.xcor() < -380:
        game_on = score.increase_score(ball)
        ball.restart_position()

screen.exitonclick()

