from turtle import Turtle

STARTING_POSITION = (0, -170)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 170


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.character = []
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.character.append(self)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
    
