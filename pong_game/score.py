from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Terminal", 15, "bold")
GAME_OVER_FONT = ("Terminal", 30, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 270)
        self.write(f"{self.left_score} SCORE {self.right_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self, location):
        if location.xcor() > 380:
            self.left_score += 1
        elif location.xcor() < -380:
            self.right_score += 1
        self.clear()
        self.write(f"{self.left_score} SCORE {self.right_score}", align=ALIGNMENT, font=FONT)
        if self.left_score == 10 or self.right_score == 10:
            self.game_over()
            return False
        return True

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -50)
        if self.left_score > self.right_score:
            self.write(f"Left Player Won", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Right Player Won", align=ALIGNMENT, font=FONT)


