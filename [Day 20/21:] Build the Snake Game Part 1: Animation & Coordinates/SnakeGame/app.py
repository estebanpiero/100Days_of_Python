#Snake Game

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

#Creating Objects

snake = Snake()
screen = Screen()
food = Food()
scoreboard = ScoreBoard()

#Coonfiguring Screen

screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


#Screen Listens to Key Presses
screen.listen()

# Key Bindings

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Moving Snake

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #Detecting Collision with Food
    #Using distance method from turtle module

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    '''
    #Detecting Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()        
        game_is_on = False
    '''
    # Move head and tail to between walls
    if snake.head.xcor() > 280:
        snake.head.goto(-280, snake.head.ycor())
    elif snake.head.xcor() < -280:
        snake.head.goto(280, snake.head.ycor())
    elif snake.head.ycor() > 280:
        snake.head.goto(snake.head.xcor(), -280)
    elif snake.head.ycor() < -280:
        snake.head.goto(snake.head.xcor(), 280)


    #Detecting Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

#Closing Screen on Click
screen.exitonclick()