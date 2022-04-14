from turtle import Turtle

# Constants:
ALIGNMENT = "center"
FONT = ("Terminal", 15, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)  # message in the top of screen
        self.write(f"SCORE: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ Display game over message """
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ Increase the score when function is called, cleaning the previous score """
        self.current_score += 1
        self.clear()
        self.write(f"SCORE: {self.current_score}", align=ALIGNMENT, font=FONT)
