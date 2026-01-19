# Day 23: The Turtle Crossing Capstone Project

## Project: Turtle Crossing Game

### Description
An arcade-style game where a turtle attempts to cross a busy road filled with moving cars. Players must time their movements carefully to avoid collisions while progressing through increasingly difficult levels. This capstone project combines all OOP concepts learned so far.

### What I Learned
- Capstone project bringing together OOP concepts
- Creating multiple object instances dynamically
- Increasing game difficulty progressively
- Collision detection between moving objects
- Level management and progression
- Random object generation
- Managing multiple moving objects simultaneously

### How to Run
```bash
python3 [main_file].py
```

### Features
- Player-controlled turtle
- Randomly generated cars
- Multiple car lanes
- Increasing difficulty (faster cars each level)
- Level progression
- Collision detection
- Game over screen
- Score/level tracking

### Game Controls
- **Up Arrow (↑)**: Move turtle forward
- Turtle moves one step at a time
- No backward movement (like real traffic!)

### Classes Implemented

#### 1. Player Class
```python
class Player(Turtle):
    - move_up()
    - go_to_start()
    - is_at_finish_line()
```

#### 2. CarManager Class
```python
class CarManager:
    - create_car()  # Random car generation
    - move_cars()   # Move all cars
    - level_up()    # Increase speed
```

#### 3. Scoreboard Class
```python
class Scoreboard(Turtle):
    - update_level()
    - game_over()
```

### How It Works
1. Player starts at bottom of screen
2. Cars spawn randomly and move left across screen
3. Player moves up using arrow key
4. If player reaches top:
   - Level up
   - Cars move faster
   - Player returns to start
5. If player collides with car:
   - Game over
6. Repeat until collision

### Game Mechanics

#### Car Generation
- Cars created at random intervals
- Random y-positions (different lanes)
- Random colors for variety
- Move from right to left

#### Difficulty Progression
- Each level increases car speed
- More challenging to find gaps
- Requires better timing

#### Collision Detection
```python
for car in cars:
    if player.distance(car) < 20:
        game_over()
```

### Project Structure
- `main.py`: Game loop and coordination
- `player.py`: Player turtle class
- `car_manager.py`: Car creation and movement
- `scoreboard.py`: Level display and game over

### Key Concepts
- **Dynamic Object Creation**: Creating cars on-the-fly
- **List Management**: Managing multiple car objects
- **Difficulty Scaling**: Increasing challenge over time
- **Collision Detection**: Player-car intersection
- **Level System**: Tracking and displaying progress
- **Game Loop**: Coordinating all game elements

### Example Gameplay
```
[Level 1]
Turtle at bottom
Cars moving slowly across screen
Player moves up between cars
Reaches top!

[Level 2]
Cars moving faster
More challenging gaps
Player must time movements carefully
Collision! Game Over

Final Level: 2
```

### Learning Focus
Capstone project demonstrating mastery of OOP concepts: multiple classes, object management, game state, and progressive difficulty.
