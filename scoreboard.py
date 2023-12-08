from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 13, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.pencolor("white")

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def end_of_game(self):
        self.home()
        self.write("Game over!", move=False, align=ALIGNMENT, font=FONT)
