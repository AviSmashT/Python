from turtle import Turtle


def check_valid_side(side):
    if side.lower() == "left":
        return 350, 0
    elif side.lower() == "right":
        return -350, 0
    else:
        raise ValueError("False input")


class Paddle(Turtle):
    def __init__(self, side):
        position = check_valid_side(side)
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shapesize(stretch_len=1, stretch_wid=5)  # Stretch is relative to the default size of the turtle
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)
