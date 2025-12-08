# The Hirst Painting Project

from extracting_color import extract_colors
from turtle import Turtle, Screen
import turtle as t
import random, os

# Converting EPS as PNG

from PIL import Image

# Extrac the colors from Image using Cologram
colors = extract_colors("/home/argento/Documents/Education/100Days_of_Python/[Day 18:] Turtle & the Graphical User Interface (GUI)/Day18Project_HirstPainting/hirst_paint.jpg")

# Set up the Turtle Screen
screen = Screen()

# Timmy the Turtle
t. colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.pensize(10)

# Function to draw a dot painting

def draw_dot_painting():
    timmy.hideturtle()
    for i in range(0,500,50):
        timmy.penup()
        timmy.sety(-200+i)
        timmy.setx(-200)
        for _ in range(10):
            timmy.dot(20, random.choice(colors))
            timmy.forward(50)

draw_dot_painting()

# Save the drawing as EPS and convert to PNG

canvas = screen.getcanvas()

filename = f'hirst_paiting_{random.randint(0,1000)}.eps'
canvas.postscript(file=filename)


img = Image.open(filename)
img.save(filename.replace(".eps", ".png"), "png")

os.remove(filename)

screen.exitonclick()