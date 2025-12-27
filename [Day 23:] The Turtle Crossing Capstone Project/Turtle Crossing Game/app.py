# Turtle Crossing Game

from turtle import Turtle, Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from background import BackGround

import time
import random

# Set up the screen
screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=400, height=400)
screen.tracer(0)    

# Create player
player = Player()

# Create car manager
car_manager = CarManager()

# Create background
background = BackGround()

# Create scoreboard
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(player.move_up, "Up")

car_locations = [-100,-80,40,60,120,140,160]

# Gameplay
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
     
    # Create Random Cars and Move them
    car_manager.create_car(random.choice(car_locations))

    #car_manager.create_car(random.randrange(-120,-60,20))
    # car_manager.create_car(random.randrange(20,80,20))
    # car_manager.create_car(random.randrange(120,180,20))
    car_manager.move()

    # Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(player.character[0]) < 20:
            is_game_on = False
            scoreboard.game_over()
            

    # Detect successful crossing
    if player.ycor() > 170:
        player.reset_position()
        scoreboard.increase_score()
        car_manager.increase_speed()

    # Delete cars that are out of screen
    for car in car_manager.all_cars:
        if car.xcor() < -220:
            car_manager.all_cars.remove(car)
            car.hideturtle()    

screen.exitonclick()