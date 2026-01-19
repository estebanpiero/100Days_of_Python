# Day 27: Tkinter, *args, **kwargs and Creating GUI Programs

## Project: Mile to Kilometers Converter

### Description
A graphical user interface (GUI) application that converts miles to kilometers. This is the first GUI project using Python's Tkinter library, introducing widgets, layout management, and event handling in desktop applications.

### What I Learned
- Tkinter GUI library basics
- Creating windows and widgets
- Layout managers (pack, grid, place)
- Event handling and button clicks
- Entry widgets and user input
- Labels and displaying text
- *args (unlimited positional arguments)
- **kwargs (unlimited keyword arguments)
- Creating functional desktop applications

### How to Run
```bash
python3 [main_file].py
```

### Features
- Clean GUI interface
- Real-time conversion
- Input validation
- Button-triggered calculation
- Professional layout

### Tkinter Basics

#### Creating a Window
```python
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

window.mainloop()
```

#### Common Widgets
```python
# Label
label = Label(text="I Am a Label", font=("Arial", 24))

# Button
button = Button(text="Click Me", command=button_clicked)

# Entry (input field)
entry = Entry(width=10)
text = entry.get()  # Get user input
```

### Layout Managers

#### Grid Layout (Recommended)
```python
label.grid(column=0, row=0)
button.grid(column=1, row=1)
```

#### Pack Layout
```python
label.pack()
button.pack()
```

### *args and **kwargs

#### *args - Unlimited Positional Arguments
```python
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(1, 2, 3, 4, 5))  # 15
```

#### **kwargs - Unlimited Keyword Arguments
```python
def calculate(**kwargs):
    print(kwargs)  # Dictionary of arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

calculate(add=3, multiply=5)
```

### Project Implementation

```python
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
```

### Key Concepts
- **Tkinter**: Python's standard GUI library
- **Widgets**: GUI components (buttons, labels, entries)
- **Layout Management**: Organizing widgets with grid
- **Event Handling**: Responding to button clicks
- **Config Method**: Modifying widget properties
- **Variable Arguments**: Flexible function parameters

### Common Tkinter Widgets
- `Label`: Display text
- `Button`: Clickable button
- `Entry`: Text input field
- `Text`: Multi-line text
- `Spinbox`: Number selector
- `Scale`: Slider
- `Checkbutton`: Checkbox
- `Radiobutton`: Radio button
- `Listbox`: Scrollable list

### Widget Configuration
```python
# During creation
label = Label(text="Hello", font=("Arial", 12), fg="blue")

# After creation
label.config(text="New Text", bg="yellow")
```

### Learning Focus
Introduction to GUI programming, understanding how to create interactive desktop applications with Tkinter, and using advanced function arguments.
