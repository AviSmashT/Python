from turtle import Turtle

# Constants:
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
SNAKE_HEAD = 0
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []  # Snake "squares"/length
        self.create_snake()
        self.head = self.segments[0]  # point (kinda) to head
        self.snake_size = len(self.segments)-1

    def create_snake(self):
        """ creates new snake with 3 segments, every segment is stored in a list.
            each segment will be position on the STARTING_POSITIONS one after the other"""
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """ Using this function to make snake move by looping trough the segments of the snake.
            The loop will go in reverse order to make sure the direction of all segments are correct
            Every segment will move to the position of segment -1 to him."""
        for i in range((len(self.segments) - 1), SNAKE_HEAD, -1):  # start = len(segments), end = 0, step = -1, movement is last seg to first
            position_x = self.segments[i - 1].position()[0]
            position_y = self.segments[i - 1].position()[1]
            self.segments[i].goto(position_x, position_y)  # position current segment of sanke
        self.head.forward(STEP)

    def increase_size(self):
        """ This function will increase the snake size by adding new segment to the end of the snake (the segment list) """
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[self.snake_size].position())
        self.snake_size += 1
        self.segments.append(new_segment)


    # Basic snake movements:
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
