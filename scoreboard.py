from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 13, "bold")
HIGHSCORE_TXT_FILE = "highscore.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.pencolor("white")
        with open(HIGHSCORE_TXT_FILE) as highscore_file:
            self.high_score = int(highscore_file.read())
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}      High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as highscore_file:
                highscore_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
