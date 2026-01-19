# Day 31: Flash Card App Capstone Project

## Project: Flash Card Language Learning App

### Description
An interactive language learning flashcard application using Tkinter. The app displays French words and reveals English translations, helping users learn vocabulary. Features include automatic card flipping, progress tracking, and removal of learned words from the deck.

### What I Learned
- Capstone project combining Tkinter and Pandas
- Timer-based card flipping
- Reading CSV data with Pandas
- Dynamic image updates on canvas
- Tracking learning progress
- Creating/updating CSV files
- Building complete learning applications

### How to Run
```bash
python3 [main_file].py
```

### Features
- French to English flashcards
- Automatic card flip after 3 seconds
- Right/Wrong buttons for tracking progress
- Removes known words from deck
- Saves progress to CSV
- Random word selection
- Visual card flip effect
- Progress persistence between sessions

### How It Works
1. Load French words from CSV
2. Display random French word (front of card)
3. After 3 seconds, flip to show English translation
4. User clicks:
   - ✓ (Right): Remove from learning deck, next card
   - ✗ (Wrong): Keep in deck, next card
5. Save remaining words to learn
6. Continue until all words learned

### Application Layout

```
┌─────────────────────────────┐
│                             │
│         French              │
│                             │
│         [Word]              │
│                             │
│                             │
├─────────────────────────────┤
│    [✗]           [✓]        │
└─────────────────────────────┘
```

### Key Implementation

#### Card Flip Timer
```python
flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,
                     text=current_card["English"],
                     fill="white")
    canvas.itemconfig(card_background,
                     image=card_back_img)
```

#### Next Card Function
```python
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,
                     text="French",
                     fill="black")
    canvas.itemconfig(card_word,
                     text=current_card["French"],
                     fill="black")
    canvas.itemconfig(card_background,
                     image=card_front_img)

    flip_timer = window.after(3000, flip_card)
```

#### Save Progress
```python
def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()
```

### Data Files

#### Original Word List (french_words.csv)
```csv
French,English
partie,part
histoire,history
chercher,search
...
```

#### Progress File (words_to_learn.csv)
```csv
French,English
chercher,search
seulement,only
...
```
(Contains only words not yet learned)

### Key Concepts
- **Canvas Images**: Displaying and updating images
- **Timers**: Using `after()` for delayed actions
- **Timer Cancellation**: `after_cancel()` to prevent overlap
- **Pandas**: Reading and writing CSV data
- **Data Filtering**: Removing learned items
- **State Management**: Tracking current card
- **Progress Persistence**: Saving learning state

### Pandas Operations
```python
import pandas

# Read data
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# Create list of dictionaries
# [{"French": "partie", "English": "part"}, ...]

# Save progress
df = pandas.DataFrame(to_learn)
df.to_csv("data/words_to_learn.csv", index=False)
```

### Images Required
- `card_front.png`: Front of flashcard (white)
- `card_back.png`: Back of flashcard (colored)
- `right.png`: Checkmark button
- `wrong.png`: X button

### Project Structure
```
Day31_FlashCard/
├── main.py
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv (created)
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    └── wrong.png
```

### Learning Focus
Capstone project demonstrating mastery of Tkinter GUI, Pandas data manipulation, timer functionality, and building practical educational applications with progress tracking.
