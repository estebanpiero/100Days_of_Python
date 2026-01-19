# Day 3: Control Flow and Logical Operators

## Project: Treasure Island

### Description
An interactive text-based adventure game where players make choices to navigate through different scenarios in search of hidden treasure. The game uses ASCII art and branching logic to create an engaging Choose Your Own Adventure experience.

### What I Learned
- Conditional statements (`if`, `elif`, `else`)
- Logical operators (`and`, `or`, `not`)
- Nested conditionals
- Input validation with while loops
- String methods (`.lower()` for case-insensitive input)
- Multi-line strings and ASCII art

### How to Run
```bash
python3 Day3_Project_Treasure_Island.py
```

### Game Flow
1. Player chooses between "left" or "right" at a crossroad
2. If they go left, they encounter a lake and must choose to "wait" or "swim"
3. If they wait, they reach an island with three colored doors (red, yellow, blue)
4. Only the yellow door leads to the treasure and victory

### Key Concepts
- **Control Flow**: Using if/elif/else to create branching logic
- **Input Validation**: Ensuring user enters valid choices
- **Nested Conditionals**: Decision trees for complex game logic
- **String Manipulation**: Using `.lower()` for case-insensitive comparisons

### Additional Files
The folder also includes practice exercises:
- `bmi_calculator.py`: BMI calculation with conditional feedback
- `even_or_odd.py`: Number parity checker
- `nested_if.py`: Examples of nested conditional statements
- `pizza_order.py`: Order calculator with multiple conditions

### Win Condition
Choose: Left → Wait → Yellow Door = Victory!
