from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-180, -180)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)  
