# Day 30: Errors, Exceptions and JSON Data - Improving the Password Manager

## Project: Password Manager v2.0 (with Exception Handling & JSON)

### Description
An enhanced version of the Password Manager with exception handling, JSON data storage, and search functionality. This version is more robust, with better error handling and structured data storage that allows searching for saved passwords.

### What I Learned
- Exception handling (try, except, else, finally)
- Working with JSON data
- JSON read/write operations
- Updating JSON data
- Search functionality in stored data
- Error handling in GUI applications
- FileNotFoundError and KeyError handling

### How to Run
```bash
python3 [main_file].py
```

### New Features (v2.0)
- **Search Function**: Find saved passwords by website
- **JSON Storage**: Structured data format
- **Exception Handling**: Graceful error management
- **Better Data Structure**: Nested dictionaries
- **Error Messages**: User-friendly error feedback

### Exception Handling

#### Try-Except-Else-Finally
```python
try:
    # Code that might raise an exception
    file = open("file.txt")
except FileNotFoundError:
    # Handle file not found
    file = open("file.txt", "w")
    file.write("Something")
except KeyError:
    # Handle missing key
    print("Key doesn't exist")
else:
    # Runs if try succeeds
    content = file.read()
    print(content)
finally:
    # Always runs (cleanup)
    file.close()
```

#### Raising Exceptions
```python
if height > 3:
    raise ValueError("Human height should not be over 3 meters")
```

### Working with JSON

#### Writing JSON
```python
import json

data = {
    "website": {
        "email": "user@email.com",
        "password": "abc123"
    }
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

#### Reading JSON
```python
with open("data.json", "r") as file:
    data = json.load(file)
    print(data["website"]["email"])
```

#### Updating JSON
```python
# Read existing data
with open("data.json", "r") as file:
    data = json.load(file)

# Update data
data["new_website"] = {
    "email": "user@email.com",
    "password": "xyz789"
}

# Write back
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

### Enhanced Save Function

```python
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                           message="Please don't leave fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Read existing data
                data = json.load(file)
        except FileNotFoundError:
            # Create new file if doesn't exist
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update existing data
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            # Clear entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)
```

### Search Functionality

```python
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                           message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error",
                message=f"No details for {website} exists."
            )
```

### JSON Data Structure

```json
{
    "amazon.com": {
        "email": "user@email.com",
        "password": "aB7#dE9fG!hK"
    },
    "facebook.com": {
        "email": "user@email.com",
        "password": "xY3$mN8pQ@wR"
    }
}
```

### Key Concepts
- **Exception Handling**: Gracefully handling errors
- **JSON Format**: Structured, readable data storage
- **Try-Except-Else-Finally**: Complete error handling flow
- **FileNotFoundError**: Handling missing files
- **KeyError**: Handling missing dictionary keys
- **Data Persistence**: Maintaining and updating stored data

### Error Types
- `FileNotFoundError`: File doesn't exist
- `KeyError`: Dictionary key doesn't exist
- `IndexError`: List index out of range
- `TypeError`: Wrong type of data
- `ValueError`: Correct type, incorrect value

### UI Updates
Added "Search" button:
```
┌─────────────────────────────┐
│         [Logo Image]        │
├─────────────────────────────┤
│ Website: [_______] Search   │
│ Email/Username: [_______]   │
│ Password: [_____] Generate  │
│           [  Add  ]         │
└─────────────────────────────┘
```

### Benefits of JSON over Text
1. Structured data format
2. Easy to search and update
3. Nested data support
4. Standard format across languages
5. Human-readable

### Learning Focus
Professional error handling and working with JSON for data storage - essential skills for real-world applications and data management.
