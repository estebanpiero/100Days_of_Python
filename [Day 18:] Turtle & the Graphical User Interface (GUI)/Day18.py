from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)  # Set the color mode to 255 for RGB colors

# Import the Turtle and Screen classes from the turtle module
timmy = Turtle()
screen = Screen()

timmy.shape("turtle")



colors = ['red', 'green', 'blue', 'purple', 'orange', 'hot pink', 'navy', 'teal']
directions = [0, 90, 180, 270]  # Possible directions: right, up, left, down

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b) # Return a tuple representing an RGB color

def draw_circle():
    timmy.circle(100)  # Draw a circle with a radius of 100 units
    
'''
# Draw a square using the turtle
for i in range(4):
    timmy.forward(100)  # Move the turtle forward by 100 units
    timmy.right(90)    # Turn the turtle right by 90 degrees
'''
'''
# Drawing a dashed line

for i in range(15):
    timmy.forward(10)  # Move forward by 10 units
    timmy.penup()      # Lift the pen to not draw
    print("Pen is up, moving forward without drawing")
    timmy.forward(10)  # Move forward by another 10 units
    timmy.pendown()    # Put the pen down to draw
    print("Pen is down, drawing forward")


# Drawing a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon

for i in range (8):
    shape = 3 + i  # Number of sides for the polygon
    angle = 360 / shape  # Calculate the angle for the polygon
    timmy.pencolor(random.choice(colors))  # Choose a random color from the list
    for _ in range(shape):
        timmy.forward(100)  # Move forward by 100 units
        timmy.right(angle)  # Turn right by the calculated angle


# Random walk with the turtle

timmy.pensize(10)  # Set the pen size to 10
timmy.speed("fastest")  # Set the turtle speed to the fastest   

def random_walk(steps):
    for _ in range(steps):
        timmy.pencolor(random_color())  # Choose a random color
        timmy.setheading(random.choice(directions))  # Set a random direction
        timmy.forward(30)  # Move forward by 30 units

random_walk(100)  # Call the random_walk function with 100 steps



#Draw a Spirograph


timmy.speed("fastest")  # Set the turtle speed to the fastest

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.pencolor(random_color())  # Choose a random color
        timmy.circle(100)  # Draw a circle with a radius of 100 units
        timmy.setheading(timmy.heading() + size_of_gap)  # Change the heading by the size_of_gap angle

draw_spirograph(5)  # Draw a spirograph with a gap of 5 degrees

'''

screen.exitonclick()  # This will keep the window open until clicked