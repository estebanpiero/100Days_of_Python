# Day 11: The Blackjack Capstone Project

## Project: Blackjack Game

### Description
A complete implementation of the classic casino card game Blackjack (21). Players compete against the computer dealer, trying to get as close to 21 as possible without going over. The game includes proper Blackjack rules, including Ace handling, dealer behavior, and win/loss conditions.

### What I Learned
- Complex game logic implementation
- Managing multiple lists and game state
- Conditional logic and nested if statements
- Card value calculation and Ace handling (11 or 1)
- Dealer AI (must hit until 17)
- Win/loss condition checking
- List manipulation and clearing

### How to Run
```bash
cd "Day11Project_BlackJack"
python3 app.py
```

### Features
- Full Blackjack rules implementation
- Unlimited deck (cards are not removed)
- Automatic Ace value adjustment (11 → 1 when busting)
- Dealer follows standard casino rules (must hit until 17)
- ASCII art logo
- Multiple rounds support
- Clear score tracking
- Win/Loss/Draw detection

### Game Rules
- Jack, Queen, King all count as 10
- Ace can count as 11 or 1 (automatically adjusted)
- Player gets 2 initial cards
- Dealer gets 2 cards (one hidden)
- Goal: Get closer to 21 than dealer without going over
- Dealer must hit until reaching 17 or higher
- Blackjack (21 with first 2 cards) is instant win

### How It Works
1. Player and dealer each receive 2 cards
2. Player sees both their cards and one dealer card
3. Player chooses to hit (get another card) or stand
4. If player goes over 21, they lose (Aces auto-convert)
5. Dealer reveals cards and plays by house rules
6. Winner is determined based on final scores

### Key Concepts
- **Game State Management**: Tracking player/dealer hands and scores
- **Conditional Logic**: Complex win/loss conditions
- **List Operations**: Adding cards, clearing hands between rounds
- **Automatic Ace Handling**: Converting 11 to 1 when necessary
- **AI Behavior**: Dealer following fixed strategy

### Files
- `app.py`: Main game implementation
- `blackjack_v2.py`: Alternative version
- `art.py`: ASCII art logo

### Example Gameplay
```
Your cards: [10, 9], current score: 19
Computer's first card: [7] [ ]

Type 'y' to get another card, type 'n' to pass: n

You win!
Your final cards: [10, 9], final score: 19
Computer's final cards: [7, 10], final score: 17
```
