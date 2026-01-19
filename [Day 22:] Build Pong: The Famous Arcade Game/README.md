# Day 22: Build Pong - The Famous Arcade Game

## Project: Pong Game

### Description
A faithful recreation of the classic Pong arcade game using Python Turtle graphics. Two players control paddles to hit a ball back and forth, with the game tracking scores and implementing realistic ball physics including bouncing and speed variation.

### What I Learned
- Building a complete 2-player game
- Collision detection with paddles and walls
- Ball physics and bouncing
- Score tracking for multiple players
- Separating game logic into multiple classes
- Real-time keyboard input for two players
- Screen boundaries and coordinate system

### How to Run
```bash
python3 [main_file].py
```

### Features
- Two-player gameplay
- Smooth paddle movement
- Realistic ball physics
- Wall bouncing
- Paddle collision detection
- Score tracking for both players
- Ball speed increases after paddle hits
- Automatic ball reset after scoring
- Clean retro aesthetic

### Game Controls
- **Player 1 (Right Paddle)**:
  - Up: ↑ (Up Arrow)
  - Down: ↓ (Down Arrow)

- **Player 2 (Left Paddle)**:
  - Up: W key
  - Down: S key

### Classes Implemented

#### 1. Paddle Class
```python
class Paddle(Turtle):
    - move_up()
    - move_down()
    - go_to_position(x, y)
```

#### 2. Ball Class
```python
class Ball(Turtle):
    - move()
    - bounce_y()  # Wall bounce
    - bounce_x()  # Paddle bounce
    - reset_position()
```

#### 3. Scoreboard Class
```python
class Scoreboard(Turtle):
    - update_scoreboard()
    - l_point()  # Left player scores
    - r_point()  # Right player scores
```

### How It Works
1. Initialize screen, paddles, ball, and scoreboard
2. Set up keyboard listeners for both players
3. Game loop:
   - Move ball continuously
   - Check for wall collisions (bounce)
   - Check for paddle collisions (bounce + speed up)
   - Check if ball goes past paddle (score point, reset)
   - Update scoreboard
4. Continue until players quit

### Key Concepts
- **Collision Detection**: Detecting ball-paddle and ball-wall collisions
- **Multiple Input Handling**: Two players controlling different paddles
- **Object Separation**: Each game element is its own class
- **Game Physics**: Ball bouncing and movement
- **State Management**: Tracking ball position, paddle positions, and scores

### Physics Logic
- Ball moves at constant speed
- Bounces off top/bottom walls (reverse y-direction)
- Bounces off paddles (reverse x-direction)
- Speed increases slightly with each paddle hit
- Resets to center when passing paddle

### Project Structure
- `main.py`: Game loop and setup
- `paddle.py`: Paddle class
- `ball.py`: Ball class with physics
- `scoreboard.py`: Score tracking

### Example Game Flow
```
[Game starts with ball in center]
Player 1 (W/S): [paddle moves up/down]
Player 2 (↑/↓): [paddle moves up/down]
[Ball bounces between paddles]
[Ball passes left paddle]
Right Player Scores! Score: 0 - 1
[Ball resets to center]
[Game continues...]
```

### Learning Focus
Bringing together multiple classes, collision detection, and real-time two-player input to create a complete interactive game.
