#Miles to KM convertor using Tkinter GUI
import tkinter
from tkinter import *

# Create a Window

window = tkinter.Tk()   
window.title("Miles to KM Converter")
window.minsize(width=400, height=300)

# User Input Entry

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

# Labels

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

km_unit_label = Label(text="KM")
km_unit_label.grid(column=2, row=1)

# Convert Button Functionality

def convert_miles_to_km():
    miles = float(miles_entry.get())
    km = miles * 1.60934
    km_label.config(text=f"{km:.2f}")

# Convert Button
convert_button = Button(text="Convert", command=convert_miles_to_km)
convert_button.grid(column=1, row=2)    


window.mainloop()