# Day 14: Higher Lower Game Project

## Project: Higher Lower Game

### Description
An interactive game based on the popular "Higher or Lower" concept where players guess which of two options has more followers, fans, or a higher metric. Players accumulate points for correct guesses and the game continues until they make a wrong guess.

### What I Learned
- Working with data structures (lists of dictionaries)
- Random selection from datasets
- Comparison logic
- Score tracking across rounds
- Screen clearing for better UX
- Game flow control
- Data formatting and presentation

### How to Run
```bash
cd "Day14Project_HigherLower"
python3 [main_file].py
```

### Features
- Random selection of comparison items
- Score tracking
- Continuous gameplay until wrong answer
- Screen clearing between rounds
- ASCII art and visual formatting
- Data-driven gameplay

### How It Works
1. Display two random items (celebrities, brands, etc.)
2. Player guesses which has higher value (followers, etc.)
3. Correct guess: score increases, continue playing
4. Wrong guess: game over, final score displayed
5. Previous winner becomes next comparison item

### Key Concepts
- **Data Structures**: Lists of dictionaries for game data
- **Random Selection**: Using `random.choice()` for variety
- **Comparison Logic**: Evaluating player guesses
- **Game State**: Tracking score and current vs next item
- **User Experience**: Clear screen and formatted output

### Files
- Project folder with game implementation
- Data file with comparison items
- ASCII art for visual appeal

### Example Gameplay
```
Compare A: Instagram, a social media platform
Against B: Cristiano Ronaldo, a footballer

Who has more followers? Type 'A' or 'B': B
You're right! Current score: 1

Compare A: Cristiano Ronaldo, a footballer
Against B: Ariana Grande, a musician

Who has more followers? Type 'A' or 'B': A
You're right! Current score: 2
```

### Learning Focus
Working with structured data and creating engaging game loops with proper state management.
