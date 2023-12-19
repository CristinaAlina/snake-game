from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 13, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.pencolor("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}      High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
