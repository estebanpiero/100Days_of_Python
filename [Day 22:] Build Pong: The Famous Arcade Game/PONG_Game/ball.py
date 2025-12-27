#PONG BALL

from turtle import Turtle

BALL_MOVE_DISTANCE = 15
BALL_SIZE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = BALL_MOVE_DISTANCE
        self.y_move = BALL_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
    
    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1