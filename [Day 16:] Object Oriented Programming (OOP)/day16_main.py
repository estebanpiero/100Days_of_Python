#Object Oriented Programming (OOP) 
'''
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

print(timmy)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()
'''
# Classes are blueprints for creating objects.
# An object is an instance of a class.
# Attributes are characteristics of an object.
# Methods are functions that belong to an object.

#Pretty Table

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
print(table)

