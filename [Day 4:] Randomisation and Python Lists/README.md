# Day 4: Randomisation and Python Lists

## Project: Rock Paper Scissors

### Description
A feature-rich Rock Paper Scissors game with ASCII art graphics, score tracking, and replay functionality. Players compete against the computer in the classic hand game with a complete game loop and statistics tracking.

### What I Learned
- Working with Python lists
- The `random` module for generating random choices
- List indexing and accessing elements
- Global variables for score tracking
- Functions for code organization
- While loops for game replay
- ASCII art for visual enhancement

### How to Run
```bash
python3 Day4_Project_rock_paper_scissor.py
```

### Features
- ASCII art representation of rock, paper, and scissors
- Input validation with error handling
- Score tracking across multiple games
- Replay functionality
- Statistics display (total games played and score)
- Option to quit during invalid input

### Game Rules
- Rock (0) beats Scissors (2)
- Paper (1) beats Rock (0)
- Scissors (2) beats Paper (1)

### Key Concepts
- **Lists**: Storing multiple related items (game images)
- **Random Module**: Using `random.randint()` for computer choices
- **Functions**: Organizing code into reusable blocks
- **Global Variables**: Tracking state across function calls
- **Input Validation**: Handling invalid user input gracefully

### Additional Files
The folder includes practice exercises:
- `lists.py`: List basics and operations
- `head_or_tails.py`: Simple coin flip using randomization
- `dirty_dozen.py`: Working with lists of data
- `splitting_bill.py`: Random bill payer selector
- `my_module.py`: Creating custom modules

### Example Gameplay
```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
> 0
[Rock ASCII art displayed]
Computer chose: [Scissors ASCII art]
You win!

Do you want to play again? Type 'Y' for Yes or 'N' for No:
```
