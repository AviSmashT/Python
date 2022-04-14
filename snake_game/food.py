from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()  # when initializing an object from this class - use refresh function

    def refresh(self):
        """ Plase food item in a random location on the screen range """
        x_pos = random.randint(-280, 280)  # random x
        y_pos = random.randint(-280, 280)  # random y
        self.goto(x_pos, y_pos)  # place item