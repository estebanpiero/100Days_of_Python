# Day 12: Scope & Number Guessing Game

## Project: Number Guessing Game

### Description
An interactive number guessing game where players try to guess a randomly generated number between 1 and 100. The game includes difficulty levels that determine the number of attempts allowed, providing feedback after each guess to help players narrow down their guesses.

### What I Learned
- Variable scope (local vs global)
- Global and local variables
- Modifying global variables
- Constants and naming conventions
- Difficulty-based gameplay
- Input validation
- Attempt tracking

### How to Run
```bash
cd "Day12Project_NumberGuessing"
python3 [main_file].py
```

### Features
- Random number generation (1-100)
- Two difficulty levels:
  - Easy: More attempts
  - Hard: Fewer attempts
- Feedback system (Too high/Too low)
- Attempt counter
- Win/Loss conditions
- Replay functionality

### Key Concepts
- **Local Scope**: Variables defined within functions
- **Global Scope**: Variables accessible throughout the program
- **Global Keyword**: Modifying global variables from within functions
- **Constants**: Uppercase naming for values that don't change
- **Game Logic**: Managing attempts and providing player feedback

### Files
- `day12.py`: Scope examples and exercises
- Project folder with main game implementation

### How It Works
1. Player selects difficulty (easy/hard)
2. Computer generates random number 1-100
3. Player makes guesses
4. Game provides "too high" or "too low" feedback
5. Player wins by guessing correctly before running out of attempts
6. Game tracks remaining attempts

### Example Gameplay
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy

You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low.

You have 9 attempts remaining.
Make a guess: 75
Too high.
```

### Learning Focus
This project emphasizes understanding Python scope rules and how variables behave in different contexts.
