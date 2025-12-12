# Turtle Race Game

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

all_turtles = []
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

def user_bet_input():
    return screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

def create_turtles():
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=colors.index(color) * 30 - 90)
        all_turtles.append(new_turtle)

create_turtles()
user_bet = user_bet_input()

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:   
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance) 






screen.exitonclick()




