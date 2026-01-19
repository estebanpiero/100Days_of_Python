# Day 20 & 21: Build the Snake Game - Animation & Coordinates

## Project: Snake Game

### Description
A complete implementation of the classic Snake game using Python's Turtle graphics. The player controls a snake that grows longer as it eats food, with the game ending if the snake hits the wall or its own tail. This two-day project covers animation, coordinates, inheritance, and file I/O.

### What I Learned

#### Day 20 - Part 1: Animation & Coordinates
- Class inheritance
- Breaking programs into multiple files
- Screen refresh and animation
- Coordinate systems
- Snake movement logic
- Keyboard event listeners

#### Day 21 - Part 2: Inheritance & List Slicing
- Class inheritance (`super()`)
- List slicing
- Collision detection
- Scorekeeping
- File handling for high scores

### How to Run
```bash
python3 [main_file].py
```

### Features
- Smooth snake animation
- Keyboard controls (arrow keys)
- Food generation at random positions
- Snake growth when eating food
- Wall collision detection
- Self-collision detection
- Score tracking
- High score persistence
- Game over screen

### Game Mechanics

#### Snake Movement
- Snake made of multiple turtle segments
- Segments follow the head
- Continuous forward movement
- Direction changes via arrow keys

#### Collision Detection
- **Food**: Snake head reaches food position
- **Wall**: Snake head goes beyond screen boundaries
- **Tail**: Snake head collides with its body

#### Scoring
- Each food eaten increases score
- High score saved to file
- Persists between game sessions

### Key Concepts

#### Object-Oriented Design
```python
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def move(self):
        # Move snake forward

    def up/down/left/right(self):
        # Change direction
```

#### Inheritance
```python
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Inherits from Turtle class
```

### Project Structure
- `snake.py`: Snake class implementation
- `food.py`: Food class
- `scoreboard.py`: Score display and tracking
- `main.py`: Game loop and setup
- `data.txt`: High score storage

### Controls
- **↑** (Up Arrow): Move up
- **↓** (Down Arrow): Move down
- **←** (Left Arrow): Move left
- **→** (Right Arrow): Move right

### How It Works
1. Initialize game screen and objects
2. Create snake with 3 segments
3. Place food at random position
4. Game loop:
   - Update screen
   - Move snake forward
   - Check for food collision (grow snake, move food)
   - Check for wall collision (game over)
   - Check for tail collision (game over)
5. Save high score on exit

### Key Programming Concepts
- **Class Inheritance**: Extending existing classes
- **List Slicing**: Managing snake segments
- **File I/O**: Reading and writing high scores
- **Event Handling**: Keyboard input
- **Collision Detection**: Checking for overlapping positions
- **Game Loop**: Continuous update cycle

### Example Code Pattern
```python
# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
```

### Learning Focus
Building a complete game with multiple classes, inheritance, collision detection, and data persistence. Demonstrates professional game development practices.
