# Tkinter GUI Application with *args and **kwargs

import tkinter
from tkinter import Button, Entry

window = tkinter.Tk()   
window.title("Tkinter GUI with *args and **kwargs")
window.minsize(width=400, height=300)

# Label

my_label = tkinter.Label(text="Hello, Tkinter!", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)



# *args and **kwargs explanation:
# *args allows you to pass a variable number of non-keyword arguments to a function.
# Example:
#def example_args(*args):
#    for arg in args:
#        print(arg)
# **kwargs allows you to pass a variable number of keyword arguments to a function.
# Example:
#def example_kwargs(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")

# Creating a Button

def on_button_click():
    print("Button Clicked!")
    new_text = input.get()
    print(new_text)
    my_label.config(text=new_text)
    # my_label.config(text="Button was clicked!")

button = Button(text="Click Me", command=on_button_click)
button.grid(column=1, row=1)

new_button = Button(text="Click Me", command=on_button_click)
new_button.grid(column=2, row=0)

# Entry component

input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())



window.mainloop()