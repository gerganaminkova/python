from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-200,200)
        self.write(f"SCORE: {self.score}", align='center', font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-200,200)
        self.write(f"SCORE: {self.score}", align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)