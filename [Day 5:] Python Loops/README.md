# Day 5: Python Loops

## Project: Password Generator

### Description
A secure password generator that creates randomized passwords based on user specifications. Users can specify the number of letters, symbols, and numbers they want, and the program generates a strong, shuffled password.

### What I Learned
- For loops and iteration
- The `range()` function
- List methods (`.append()`)
- `random.choice()` for selecting random elements
- `random.shuffle()` for randomizing list order
- String concatenation in loops
- Building strings from lists

### How to Run
```bash
python3 Day5_Project_PassWordGen.py
```

### Features
- Customizable password length
- Mix of uppercase and lowercase letters
- Inclusion of numbers and symbols
- Random character shuffling for security
- User-defined composition

### How It Works
1. User specifies how many letters, symbols, and numbers they want
2. Program randomly selects characters from predefined lists
3. All selected characters are shuffled randomly
4. Final password is assembled and displayed

### Key Concepts
- **For Loops**: Iterating a specific number of times with `range()`
- **Lists**: Building collections of password characters
- **Random Module**: Using `choice()` and `shuffle()` for randomization
- **String Building**: Concatenating characters to form the final password

### Security Note
The password is shuffled to prevent predictable patterns (e.g., all letters first, then symbols, then numbers).

### Additional Files
- `for_loops.py`: Practice exercises with for loops
- `FizzBuzz.py`: Classic FizzBuzz programming challenge

### Example Usage
```
Welcome to the Password Generator!
How many letters would you like in your password?
> 8
How many symbols would you like?
> 2
How many numbers would you like?
> 2

Your password is: aB7#dE9fG!hK
```
