# Day 28: Tkinter, Dynamic Typing and the Pomodoro GUI Application

## Project: Pomodoro Timer

### Description
A productivity timer application based on the Pomodoro Technique. The app manages work sessions (25 minutes) and breaks (5-15 minutes), helping users maintain focus and productivity. Features include visual timer countdown, session tracking, and checkmarks for completed sessions.

### What I Learned
- Building complex GUI applications
- Timer functionality with `after()` method
- Canvas widget for graphics
- Adding images to GUI
- Color schemes and design
- Managing application state
- Dynamic UI updates
- Countdown mechanics
- Multiple timer modes

### How to Run
```bash
python3 [main_file].py
```

### Features
- 25-minute work sessions
- 5-minute short breaks
- 15-minute long breaks (every 4 sessions)
- Visual countdown timer
- Checkmarks for completed sessions
- Start and Reset buttons
- Color-coded timer states
- Tomato image theme

### The Pomodoro Technique
1. Work for 25 minutes (1 Pomodoro)
2. Take a 5-minute break
3. After 4 Pomodoros, take a 15-minute break
4. Repeat

### Key Tkinter Concepts

#### Canvas Widget
```python
canvas = Canvas(width=200, height=224, bg=YELLOW)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130,
                                 text="00:00",
                                 font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
```

#### Dynamic Updates
```python
canvas.itemconfig(timer_text, text="05:00")
```

#### After Method (Timing)
```python
# Execute function after 1000ms (1 second)
window.after(1000, count_down, count - 1)
```

### Application Structure

```python
import tkinter
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

# Timer mechanism
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()  # Start next session

def start_timer():
    # Determine work or break
    # Update UI
    # Start countdown
```

### How It Works
1. User clicks "Start"
2. Timer begins 25-minute countdown
3. Display updates every second
4. When complete:
   - Checkmark added
   - Break timer starts
5. After 4 work sessions, longer break
6. Reset button clears all and restarts

### Key Concepts
- **Canvas Widget**: Drawing and displaying images
- **After Method**: Scheduling function calls
- **Time Calculations**: Converting seconds to minutes:seconds
- **State Management**: Tracking sessions and break types
- **Dynamic UI**: Updating text and colors
- **Constants**: Using uppercase for fixed values

### UI Components
- **Title Label**: Shows current mode (Work/Break)
- **Canvas**: Displays tomato image and countdown
- **Start Button**: Begins timer
- **Reset Button**: Clears and restarts
- **Checkmarks**: Visual progress tracking

### Countdown Logic
```python
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    # Format with leading zero
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
```

### Session Management
```python
reps = 0

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        # Long break
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # Short break
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        # Work session
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
```

### Design Elements
- Color-coded states (green for work, pink/red for breaks)
- Tomato image theme
- Clean, minimal interface
- Clear visual feedback

### Learning Focus
Building a practical productivity tool with complex state management, timer functionality, and professional UI design using Tkinter.
