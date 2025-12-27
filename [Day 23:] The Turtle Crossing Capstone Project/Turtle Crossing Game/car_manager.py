from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

CAR_SIZE = (3, 2, 1)

class CarManager():
    def __init__(self):
        self.all_cars = []
        
        
    def create_car(self, y_cord):
        
        random_chance = random.randint(1, 36)
        if random_chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            
            x_size = random.choice(CAR_SIZE)

            new_car.shapesize(stretch_wid=1, stretch_len=x_size)
            new_car.penup()
            new_car.color(random.choice(COLORS))
        
            new_car.goto(250,y_cord)
            
            self.move_distance = STARTING_MOVE_DISTANCE
            self.all_cars.append(new_car)

    def move(self): 
        for car in self.all_cars:
            car.backward(self.move_distance)

    def increase_speed(self):
            self.move_distance += MOVE_INCREMENT