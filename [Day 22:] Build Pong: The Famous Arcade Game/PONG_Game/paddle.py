#Creating PONG Paddle

from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self,X_position, Y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_HEIGHT / 20, stretch_len=PADDLE_WIDTH / 20)
        self.penup()
        self.goto(X_position, Y_position)
        

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)