# Day 7: Hangman

## Project: Hangman Game

### Description
A complete implementation of the classic Hangman word-guessing game with ASCII art graphics, random word selection, and game state tracking. Players try to guess a hidden word letter by letter before running out of attempts.

### What I Learned
- Working with imported modules
- Managing game state
- String manipulation and validation
- List operations and indexing
- While loops for game logic
- Screen clearing for better UX
- Modular code organization

### How to Run
```bash
cd "Day7_Hang_Man_Project"
python3 hangman.py
```

### Features
- Random word selection from a word list
- ASCII art hangman stages showing progress
- Visual display of guessed letters
- Attempt tracking (6 total attempts)
- Win/loss conditions
- Screen clearing between guesses for clean display
- Modular design with separate files for words and art

### Files
- `hangman.py`: Main game logic
- `hangman_v2.py`: Enhanced version of the game
- `words.py`: Word list for random selection
- `hangman_art.py`: ASCII art for logo and stages

### How It Works
1. Random word is selected from the word list
2. Display shows blanks for each letter
3. Player guesses one letter at a time
4. Correct guesses reveal letters in the word
5. Wrong guesses decrease remaining attempts and update hangman art
6. Game ends when word is complete (win) or attempts reach 0 (loss)

### Key Concepts
- **Modular Programming**: Separating concerns (words, art, logic)
- **Game State Management**: Tracking attempts, guessed letters, and word progress
- **List Comprehension**: Building the underscore display
- **Import Statements**: Using code from other files
- **User Experience**: Clear screen for cleaner gameplay

### Example Gameplay
```
_ _ _ _ _ _

Guess a letter: e
_ e _ _ _ _

Guess a letter: a
_ e a _ _ _
```
