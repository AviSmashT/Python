from turtle import Turtle
import random
right_restart_position = [30, 330]
left_restart_position = [160, 200]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.setheading(random.choice(right_restart_position))
        self.move_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.speed("normal")
        self.color("white")
        self.penup()

    def movement(self):
        self.forward(20)

    def bounce_paddle(self):
        if 0 <= self.heading() <= 90 or 180 <= self.heading() <= 270:
            self.setheading(self.heading() + 120)
        elif 90 <= self.heading() <= 180 or 270 <= self.heading() <= 360:
            self.setheading(self.heading() - 120)
        self.move_speed *= 0.9

    def bounce_wall(self):
        self.setheading(abs(360-self.heading()))

    def restart_position(self):
        if self.xcor() > 380:
            self.setheading(random.choice(left_restart_position))
        else:
            self.setheading(random.choice(right_restart_position))
        self.move_speed = 0.1
        self.goto(0, 0)
