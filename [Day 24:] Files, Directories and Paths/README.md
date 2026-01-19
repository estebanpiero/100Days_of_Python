# Day 24: Files, Directories and Paths

## Project: Mail Merge

### Description
An automated mail merge program that reads names from a file and generates personalized invitation letters for each person. This project demonstrates file I/O operations, working with directories, and automating repetitive tasks.

### What I Learned
- Reading from files (`open()`, `read()`, `readlines()`)
- Writing to files (`write()`, `close()`)
- File paths (relative and absolute)
- Working with directories
- File modes (r, w, a)
- Context managers (`with` statement)
- String replacement and formatting
- Automating document generation

### How to Run
```bash
cd "Day24Project_MailMerger"
python3 [main_file].py
```

### Features
- Reads names from input file
- Uses letter template
- Generates personalized letters
- Saves each letter to separate file
- Automatic directory creation
- Bulk document generation

### File Operations

#### Reading Files
```python
# Method 1: Manual close
file = open("file.txt")
contents = file.read()
file.close()

# Method 2: Context manager (better)
with open("file.txt") as file:
    contents = file.read()
```

#### Writing Files
```python
with open("output.txt", mode="w") as file:
    file.write("New content")
```

### File Modes
- `"r"` - Read (default)
- `"w"` - Write (overwrites)
- `"a"` - Append (adds to end)

### Project Structure
```
Day24Project_MailMerger/
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   └── Letters/
│       └── starting_letter.txt
└── Output/
    └── ReadyToSend/
        ├── letter_for_name1.txt
        ├── letter_for_name2.txt
        └── ...
```

### How It Works
1. Read template letter from file
2. Read list of names from file
3. For each name:
   - Replace placeholder in template
   - Create new personalized letter
   - Save to output directory
4. All letters ready to send!

### Key Concepts
- **File I/O**: Reading and writing files
- **Path Management**: Working with directories
- **String Replacement**: Using `replace()` or `.format()`
- **Context Managers**: `with` statement for safe file handling
- **Automation**: Batch processing multiple items
- **Template Processing**: Placeholder replacement

### Example Template
```
Dear [name],

You are invited to my birthday party!

Sincerely,
Angela
```

### Example Output
```
Dear John,

You are invited to my birthday party!

Sincerely,
Angela
```

### Additional Files
- `Day24.py`: File I/O exercises
- `my_file.txt`: Practice file

### Common File Operations
```python
# Read all content
with open("file.txt") as file:
    content = file.read()

# Read lines as list
with open("file.txt") as file:
    lines = file.readlines()

# Write to file
with open("output.txt", "w") as file:
    file.write("Hello World")

# Append to file
with open("output.txt", "a") as file:
    file.write("\nNew line")
```

### Best Practices
- Always use `with` statement (auto-closes files)
- Use relative paths for portability
- Check if files exist before reading
- Handle file exceptions
- Close files properly (or use context manager)

### Learning Focus
Understanding file operations is essential for data processing, automation, and working with external data sources.
