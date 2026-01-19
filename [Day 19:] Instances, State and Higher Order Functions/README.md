# Day 19: Instances, State and Higher Order Functions

## Project: Turtle Racing Game

### Description
An interactive turtle racing game where multiple colorful turtles race across the screen. Players bet on which turtle will win, and the race outcome is determined randomly. This project demonstrates working with multiple object instances, event listeners, and higher-order functions.

### What I Learned
- Creating multiple instances of the same class
- Managing object state independently
- Higher-order functions (functions as arguments)
- Event listeners and user input
- Random movement and animation
- Coordinate systems
- Working with multiple turtles simultaneously

### How to Run
```bash
python3 [main_file].py
```

### Features
- Multiple racing turtles (different colors)
- User betting system
- Random race outcomes
- Event-driven programming
- Animated race
- Win/loss determination
- Screen setup and configuration

### Key Concepts

#### 1. Multiple Instances
```python
# Creating multiple turtle objects
red_turtle = Turtle()
blue_turtle = Turtle()
green_turtle = Turtle()
```

#### 2. Higher-Order Functions
- Functions that take other functions as arguments
- Event listeners: `screen.listen()`, `screen.onkey()`
- Callback functions

#### 3. State Management
- Each turtle maintains its own position
- Independent movement for each racer
- Tracking which turtle crosses finish line

### How It Works
1. Set up screen with appropriate dimensions
2. Create multiple turtle instances (racers)
3. Position turtles at starting line
4. User places bet on a color
5. Race begins - turtles move randomly
6. First turtle to reach finish line wins
7. Compare winner with user's bet

### Event Handling
```python
screen = Screen()
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
```

### Files
- Main racing game implementation
- Possibly separate turtle configuration
- Screen setup and event handling

### Example Gameplay
```
Welcome to the Turtle Racing Game!
Which turtle do you want to bet on?
Enter a color (red/blue/green/yellow/purple): blue

Ready... Set... GO!

[Turtles race across screen with random movements]

The green turtle wins!
You lost! Better luck next time.
```

### Key Programming Concepts
- **Object Instances**: Multiple objects from same class
- **State Independence**: Each object has its own attributes
- **Event Listeners**: Responding to user input
- **Higher-Order Functions**: Functions as parameters
- **Randomization**: Creating unpredictable outcomes

### Advanced Features
- Multiple turtle colors and starting positions
- Random distance for each move
- Finish line detection
- User input handling
- Winner announcement

### Learning Focus
Understanding how to work with multiple instances of objects, manage their independent states, and use higher-order functions for event-driven programming.
