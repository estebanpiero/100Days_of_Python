# Day 29: Building a Password Manager GUI App with Tkinter

## Project: Password Manager

### Description
A desktop password manager application with GUI that generates strong random passwords and securely stores login credentials. Users can save website, email, and password combinations, with automatic password generation and clipboard functionality.

### What I Learned
- Building practical applications with Tkinter
- Working with multiple entry fields
- Messagebox for user feedback
- Clipboard functionality
- Writing data to files
- Password generation algorithms
- Grid layout with spanning columns
- Exception handling in GUI apps

### How to Run
```bash
python3 [main_file].py
```

### Features
- Generate strong random passwords
- Copy passwords to clipboard automatically
- Save credentials to file
- Clean, user-friendly interface
- Input validation
- Confirmation dialogs
- Logo/branding
- Email/username autofill

### Application Layout

```
┌─────────────────────────────┐
│         [Logo Image]        │
├─────────────────────────────┤
│ Website: [______________]   │
│ Email/Username: [_______]   │
│ Password: [_____] Generate  │
│           [  Add  ]         │
└─────────────────────────────┘
```

### Key Features Implementation

#### Password Generation
```python
import random

letters = ['a', 'b', 'c', ..., 'Z']
numbers = ['0', '1', '2', ..., '9']
symbols = ['!', '#', '$', '%', '&']

password_list = []
password_list += [random.choice(letters) for _ in range(8)]
password_list += [random.choice(symbols) for _ in range(2)]
password_list += [random.choice(numbers) for _ in range(2)]

random.shuffle(password_list)
password = "".join(password_list)
```

#### Clipboard Functionality
```python
import pyperclip

password = generate_password()
pyperclip.copy(password)  # Copy to clipboard
```

#### Save to File
```python
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                           message="Please don't leave fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Email: {email}\nPassword: {password}\nSave?"
        )

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            # Clear entries
```

### Tkinter Widgets Used

#### Entry with Grid Spanning
```python
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Cursor starts here
```

#### Button with Function
```python
generate_button = Button(text="Generate Password",
                        command=generate_password)
generate_button.grid(row=3, column=2)
```

#### Messagebox
```python
from tkinter import messagebox

# Info message
messagebox.showinfo(title="Title", message="Message")

# Confirmation dialog
is_ok = messagebox.askokcancel(title="Confirm", message="Save?")
```

### How It Works
1. User enters website name
2. Email is pre-filled (can be edited)
3. Click "Generate Password":
   - Random password created
   - Displayed in entry field
   - Copied to clipboard
4. Click "Add":
   - Validate inputs
   - Confirmation dialog
   - Save to data.txt
   - Clear entries
5. Ready for next entry

### Key Concepts
- **Dialog Boxes**: User feedback and confirmation
- **File I/O**: Append mode for storing data
- **Clipboard**: System clipboard access
- **Input Validation**: Checking for empty fields
- **Grid Layout**: Spanning columns for wider widgets
- **Focus**: Setting cursor position
- **Widget Methods**: insert(), get(), delete()

### Entry Widget Methods
```python
# Set cursor focus
entry.focus()

# Insert default text
entry.insert(0, "default@email.com")

# Get user input
text = entry.get()

# Clear entry
entry.delete(0, END)
```

### Data Storage Format
```
amazon.com | user@email.com | aB7#dE9fG!hK
facebook.com | user@email.com | xY3$mN8pQ@wR
github.com | user@email.com | kL2%fT6vZ#nB
```

### Security Note
This basic version stores passwords in plain text. In a production app, passwords should be encrypted!

### Project Files
- Main application file
- `logo.png`: Application logo
- `data.txt`: Stored passwords (created on first save)

### Learning Focus
Building a complete, practical desktop application with file persistence, user interaction, and real-world utility using Tkinter.
