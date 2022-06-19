from turtle import Turtle

SCORE_XCOR = -250
LIFE_XCOR = 250
SCORE_YCOR = 260
ALIGNMENT = "center"
FONT = ('Arial', 15, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 3
        self.penup()
        self.color("white")
        self.ht()
        self.update_score()

    def game_over(self):
        self.home()
        self.write(self.write(f"GAME OVER", align=ALIGNMENT, font=FONT))

    def update_score(self):
        self.clear()
        self.goto(x=SCORE_XCOR, y=SCORE_YCOR)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(x=LIFE_XCOR, y=SCORE_YCOR)
        self.write(f"LIFE: {self.life}", align=ALIGNMENT, font=FONT)