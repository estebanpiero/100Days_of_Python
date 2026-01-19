# Day 10: Functions with Outputs

## Project: Calculator

### Description
A fully functional calculator program with support for basic arithmetic operations (addition, subtraction, multiplication, division). The calculator features chained calculations, allowing users to continue calculating with previous results or start fresh.

### What I Learned
- Functions with return statements
- Return values and using them in expressions
- Storing functions in dictionaries
- Higher-order functions
- Recursive function calls
- Chained operations
- Docstrings for documentation

### How to Run
```bash
cd "Day10Project_Calculator"
python3 app.py
```

### Features
- Four basic operations: +, -, *, /
- Continuous calculation mode
- Chain calculations with previous results
- Start new calculations at any time
- Quit option
- ASCII art logo
- Clean, modular code design

### How It Works
1. User enters the first number
2. Selects an operation (+, -, *, /)
3. Enters the second number
4. Result is calculated and displayed
5. User can continue with the result, start new, or quit

### Key Concepts
- **Return Values**: Functions returning calculated results
- **Functions as Values**: Storing functions in a dictionary
- **Dictionary Lookup**: Accessing functions via operator symbols
- **Recursion**: Calculator function calling itself for new calculations
- **Chaining**: Using previous results in new calculations

### Files
- `app.py`: Main calculator program
- `art.py`: ASCII art logo
- `DockString.py`: Documentation string examples
- `year_leap.py`: Leap year calculator (practice)
- `Day10.py`: Additional exercises

### Example Usage
```
What's the first number?: 10
+
-
*
/
Pick an operation: +
What's the next number?: 5
10.0 + 5.0 = 15.0

Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation, or 'q' to quit: y
Pick an operation: *
What's the next number?: 2
15.0 * 2.0 = 30.0
```

### Programming Pattern
This project demonstrates storing functions as dictionary values, enabling dynamic function calls based on user input.
