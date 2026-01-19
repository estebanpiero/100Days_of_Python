# Day 25: Working with CSV Data and the Pandas Library

## Project: U.S. States Game

### Description
An interactive geography game where players try to name all 50 U.S. states. As players guess correctly, state names appear on a map at their correct locations. The game uses Pandas for data manipulation and Turtle graphics for visualization.

### What I Learned
- Reading CSV files with Pandas
- DataFrame operations
- Working with tabular data
- Pandas Series and DataFrame methods
- Data filtering and querying
- Exporting data to CSV
- Combining Pandas with Turtle graphics
- Data-driven applications

### How to Run
```bash
python3 [main_file].py
```

### Features
- Interactive U.S. map
- 50 states to guess
- Case-insensitive input
- Track remaining states
- Export missed states to CSV
- Real-time visual feedback
- Score tracking

### Pandas Basics

#### Reading CSV
```python
import pandas

data = pandas.read_csv("file.csv")
```

#### DataFrame Operations
```python
# Access column
data["column_name"]

# Access row
data[data.column == "value"]

# Convert to list
data["column"].to_list()

# Get specific value
state_data = data[data.state == "Texas"]
x = int(state_data.x)
y = int(state_data.y)
```

### CSV File Structure
```
state,x,y
Alabama,100,50
Alaska,-150,-200
Arizona,-50,30
...
```

### How It Works
1. Load blank U.S. map image
2. Read state data from CSV (names and coordinates)
3. Player enters state name
4. Check if guess is correct:
   - If yes: Display state name on map at correct position
   - Add to guessed list
5. Continue until all states guessed or player exits
6. Export missed states to CSV for learning

### Key Concepts
- **Pandas Library**: Powerful data manipulation tool
- **CSV Files**: Comma-Separated Values for data storage
- **DataFrames**: 2D labeled data structure
- **Data Filtering**: Finding specific rows
- **Data Export**: Saving results to file

### Game Loop
```python
import pandas
import turtle

# Load data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer in all_states:
        # Display state on map
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        guessed_states.append(answer)
```

### Project Structure
- Main game file
- `50_states.csv`: State names and coordinates
- `blank_states_img.gif`: U.S. map image
- `states_to_learn.csv`: Exported missed states

### Data Export Feature
```python
# States user didn't guess
missing_states = [state for state in all_states
                  if state not in guessed_states]

# Create DataFrame and export
missed_data = pandas.DataFrame(missing_states)
missed_data.to_csv("states_to_learn.csv")
```

### Additional Exercises
The folder may include:
- CSV reading practice
- DataFrame manipulation
- Data analysis exercises
- Working with different datasets

### Pandas Methods Used
- `read_csv()` - Load CSV file
- `to_list()` - Convert column to list
- `to_csv()` - Export to CSV
- Boolean indexing - Filter data
- Column access - Get specific data

### Learning Focus
Introduction to data analysis with Pandas, one of Python's most important libraries for data science and data manipulation.
