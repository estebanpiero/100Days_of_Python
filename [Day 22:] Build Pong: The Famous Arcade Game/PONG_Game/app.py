# PONG Game using Turtle Graphics

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball   
from scoreboard import Scoreboard

import time

# Set up the screen
screen = Screen()
screen.title("PONG Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

'''---------------'''
#Screen Listens to Key Presses
screen.listen()

# Key Bindings for Left Paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Key Bindings for Right Paddle
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
'''---------------'''

# Game Loop
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move()

    # No allow paddle to go out of bounds
    if left_paddle.ycor() > 250:
        left_paddle.goto(left_paddle.xcor(), 250)
    if left_paddle.ycor() < -250:
        left_paddle.goto(left_paddle.xcor(), -250)
    if right_paddle.ycor() > 250:
        right_paddle.goto(right_paddle.xcor(), 250)
    if right_paddle.ycor() < -250:
        right_paddle.goto(right_paddle.xcor(), -250)
 

    # Detect collision with Walls

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with right Paddles
    elif (ball.xcor() > 320 and ball.xcor() < 340) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.bounce_x()
        ball.increase_speed()
        
        

    # Detect collision with left Paddles
    elif (ball.xcor() < -320 and ball.xcor() > -340) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.bounce_x() 
        ball.increase_speed()
    
    else:
        # Detect when Right Paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.left_point()
        
        # Detect when Left Paddle misses
        elif ball.xcor() < -380:
            ball.reset_position()
            scoreboard.right_point()



    screen.update()

screen.exitonclick()