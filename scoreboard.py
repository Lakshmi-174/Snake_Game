from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.forward(280)
        with open("../../Desktop/day20-data.txt") as file:
            self.highscore = int(file.read())
        self.score_update()


    def score_update(self):
        self.clear()
        self.write(f'Score={self.score} High-Score={self.highscore}', False, font=("Arial", 14, "bold"),
                   align="center")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write ( f'GAME OVER', False, font=("Arial", 14, "bold"), align="center" )
    def score_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("../../Desktop/day20-data.txt", mode="w") as file:
                file.write(f'{self.highscore}')
        self.score = 0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.score_update()

