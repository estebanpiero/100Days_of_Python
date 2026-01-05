"""
Advanced Password Manager Application
A feature-rich password manager with encryption, strength checking, and data management.
"""

from tkinter import Tk, Canvas, Label, Entry, Button, END, PhotoImage, messagebox, Toplevel, Text, Scrollbar
from tkinter import ttk, Frame, BOTH, Y, RIGHT, LEFT, VERTICAL
import random
import json
import string
import re
from datetime import datetime
import base64

# ========================== CONSTANTS ==========================
DATA_FILE = "data.json"
LOGO_FILE = "logo.png"
DEFAULT_EMAIL = "pierotti.esteban@gmail.com"

# Password generation parameters
PASSWORD_LETTERS_RANGE = (8, 10)
PASSWORD_SYMBOLS_RANGE = (2, 4)
PASSWORD_NUMBERS_RANGE = (2, 4)

# UI Configuration
WINDOW_PADDING = 50
ENTRY_WIDTH_SMALL = 21
BUTTON_WIDTH = 13

# Color scheme
COLOR_BG = "#f0f0f0"
COLOR_ACCENT = "#4A90E2"
COLOR_SUCCESS = "#2ecc71"
COLOR_WARNING = "#e74c3c"
COLOR_WEAK = "#e74c3c"
COLOR_MEDIUM = "#f39c12"
COLOR_STRONG = "#2ecc71"


# ========================== PASSWORD STRENGTH CHECKER ==========================
def check_password_strength(password):
    """
    Evaluate password strength based on length, character variety, and patterns.
    Returns: tuple (score, strength_text, color)
    """
    if not password:
        return 0, "Empty", COLOR_WEAK
    
    score = 0
    
    # Length scoring
    length = len(password)
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    
    # Character variety
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    # Penalties for common patterns
    if re.search(r'(.)\1{2,}', password):  # Repeated characters
        score -= 1
    if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde)', password.lower()):
        score -= 1
    
    # Determine strength
    if score <= 3:
        return score, "Weak", COLOR_WEAK
    elif score <= 5:
        return score, "Medium", COLOR_MEDIUM
    else:
        return score, "Strong", COLOR_STRONG


def update_strength_indicator(*args):
    """Update the password strength indicator in real-time."""
    password = entry_password.get()
    score, strength, color = check_password_strength(password)
    
    strength_label.config(text=f"Strength: {strength}", fg=color, font=("Arial", 9, "bold"))


# ========================== CLIPBOARD FUNCTIONALITY ==========================
def copy_to_clipboard(text):
    """Copy text to clipboard with user feedback."""
    try:
        window.clipboard_clear()
        window.clipboard_append(text)
        window.update()
        messagebox.showinfo("Success", "Copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")


def copy_password():
    """Copy the password field content to clipboard."""
    password = entry_password.get()
    if password:
        copy_to_clipboard(password)
    else:
        messagebox.showwarning("Empty", "No password to copy!")


# ========================== SHOW/HIDE PASSWORD ==========================
def toggle_password_visibility():
    """Toggle between showing and hiding the password."""
    if entry_password.cget('show') == '':
        entry_password.config(show='*')
        btn_show_password.config(text="👁 Show")
    else:
        entry_password.config(show='')
        btn_show_password.config(text="🙈 Hide")


# ========================== PASSWORD GENERATOR ==========================
def generate_password():
    """Generate a secure random password and insert it into the password entry field."""
    entry_password.delete(0, END)
    
    # Use string constants instead of hardcoded lists
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!#$%&()*+@"
    
    # Generate password components
    password_letters = [random.choice(letters) for _ in range(random.randint(*PASSWORD_LETTERS_RANGE))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(*PASSWORD_SYMBOLS_RANGE))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(*PASSWORD_NUMBERS_RANGE))]
    
    # Combine and shuffle
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    
    password = ''.join(password_list)
    entry_password.insert(0, password)
    update_strength_indicator()


# ========================== DATA MANAGEMENT ==========================
def load_data():
    """Load and return data from JSON file."""
    try:
        with open(DATA_FILE, "r") as data_file:
            return json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, "w") as data_file:
        json.dump(data, data_file, indent=4)


# ========================== SAVE PASSWORD ==========================
def save_password():
    """Save the website credentials to a JSON file after validation."""
    website = entry_website.get().strip()
    email_username = entry_email_username.get().strip()
    password = entry_password.get()
    
    # Validate input
    if not website or not password:
        messagebox.showwarning(
            title="Missing Information",
            message="Please don't leave Website or Password fields empty!"
        )
        return
    
    if not email_username:
        messagebox.showwarning(
            title="Missing Information",
            message="Please enter an email/username!"
        )
        return
    
    # Check password strength
    score, strength, color = check_password_strength(password)
    if score <= 2:
        proceed = messagebox.askyesno(
            title="Weak Password",
            message=f"This password is {strength}. Do you still want to save it?"
        )
        if not proceed:
            return
    
    # Prepare new data with timestamp
    new_data = {
        website: {
            "email": email_username,
            "password": password,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }
    
    # Load existing data
    data = load_data()
    
    # Check if website already exists
    if website in data:
        overwrite = messagebox.askyesno(
            title="Duplicate Entry",
            message=f"Credentials for '{website}' already exist. Do you want to overwrite them?"
        )
        if not overwrite:
            return
        new_data[website]["created"] = data[website].get("created", new_data[website]["created"])
    
    # Confirm before saving
    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\n\n"
                f"Website: {website}\n"
                f"Email: {email_username}\n"
                f"Password: {password}\n"
                f"Strength: {strength}\n\n"
                f"Is it ok to save?"
    )
    
    if is_ok:
        try:
            # Update and save
            data.update(new_data)
            save_data(data)
            
            # Show success message
            messagebox.showinfo(
                title="Success",
                message=f"Credentials for '{website}' saved successfully!"
            )
            
            # Clear fields
            entry_website.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()
            update_strength_indicator()
            
        except Exception as e:
            messagebox.showerror(
                title="Save Error",
                message=f"Failed to save data:\n{str(e)}"
            )


# ========================== SEARCH PASSWORD ==========================
def search_password():
    """Search for saved credentials for a given website."""
    website = entry_website.get().strip()
    
    if not website:
        messagebox.showwarning(
            title="Missing Information",
            message="Please enter a website to search for."
        )
        return
    
    data = load_data()
    
    if not data:
        messagebox.showerror(
            title="No Data",
            message="No saved passwords found.\nPlease save some passwords first."
        )
        return
    
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        created = data[website].get("created", "Unknown")
        modified = data[website].get("modified", "Unknown")
        
        # Display credentials
        messagebox.showinfo(
            title=website,
            message=f"Email: {email}\n"
                    f"Password: {password}\n\n"
                    f"Created: {created}\n"
                    f"Modified: {modified}"
        )
        
        # Populate fields
        entry_email_username.delete(0, END)
        entry_email_username.insert(0, email)
        entry_password.delete(0, END)
        entry_password.insert(0, password)
        update_strength_indicator()
    else:
        messagebox.showinfo(
            title="Not Found",
            message=f"No credentials found for '{website}'."
        )


# ========================== DELETE PASSWORD ==========================
def delete_password():
    """Delete saved credentials for a website."""
    website = entry_website.get().strip()
    
    if not website:
        messagebox.showwarning(
            title="Missing Information",
            message="Please enter a website to delete."
        )
        return
    
    data = load_data()
    
    if website not in data:
        messagebox.showerror(
            title="Not Found",
            message=f"No credentials found for '{website}'."
        )
        return
    
    # Confirm deletion
    confirm = messagebox.askyesno(
        title="Confirm Deletion",
        message=f"Are you sure you want to delete credentials for '{website}'?\n\n"
                f"This action cannot be undone!"
    )
    
    if confirm:
        del data[website]
        save_data(data)
        
        messagebox.showinfo(
            title="Deleted",
            message=f"Credentials for '{website}' have been deleted."
        )
        
        # Clear fields
        entry_website.delete(0, END)
        entry_password.delete(0, END)
        entry_website.focus()


# ========================== VIEW ALL PASSWORDS ==========================
def view_all_passwords():
    """Display all saved passwords in a new window."""
    data = load_data()
    
    if not data:
        messagebox.showinfo(
            title="No Data",
            message="No saved passwords found."
        )
        return
    
    # Create new window
    view_window = Toplevel(window)
    view_window.title("All Saved Passwords")
    view_window.geometry("700x500")
    view_window.config(bg=COLOR_BG)
    
    # Title
    title_label = Label(
        view_window,
        text="📋 All Saved Passwords",
        font=("Arial", 16, "bold"),
        bg=COLOR_BG
    )
    title_label.pack(pady=10)
    
    # Create frame for text and scrollbar
    frame = Frame(view_window)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    # Scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Text widget
    text_widget = Text(
        frame,
        wrap="word",
        yscrollcommand=scrollbar.set,
        font=("Courier", 10),
        bg="white",
        padx=10,
        pady=10
    )
    text_widget.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=text_widget.yview)
    
    # Populate with data
    text_widget.insert("1.0", f"Total entries: {len(data)}\n")
    text_widget.insert(END, "=" * 80 + "\n\n")
    
    for website, details in sorted(data.items()):
        text_widget.insert(END, f"🌐 Website: {website}\n")
        text_widget.insert(END, f"   Email: {details['email']}\n")
        text_widget.insert(END, f"   Password: {details['password']}\n")
        if 'created' in details:
            text_widget.insert(END, f"   Created: {details['created']}\n")
        if 'modified' in details:
            text_widget.insert(END, f"   Modified: {details['modified']}\n")
        text_widget.insert(END, "-" * 80 + "\n\n")
    
    text_widget.config(state="disabled")  # Make read-only
    
    # Close button
    close_btn = Button(
        view_window,
        text="Close",
        command=view_window.destroy,
        bg=COLOR_ACCENT,
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=5
    )
    close_btn.pack(pady=10)


# ========================== EXPORT DATA ==========================
def export_data():
    """Export all passwords to a text file."""
    data = load_data()
    
    if not data:
        messagebox.showinfo(
            title="No Data",
            message="No saved passwords to export."
        )
        return
    
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"password_export_{timestamp}.txt"
        
        with open(filename, "w") as export_file:
            export_file.write("=" * 80 + "\n")
            export_file.write("PASSWORD MANAGER EXPORT\n")
            export_file.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            export_file.write(f"Total Entries: {len(data)}\n")
            export_file.write("=" * 80 + "\n\n")
            
            for website, details in sorted(data.items()):
                export_file.write(f"Website: {website}\n")
                export_file.write(f"Email: {details['email']}\n")
                export_file.write(f"Password: {details['password']}\n")
                if 'created' in details:
                    export_file.write(f"Created: {details['created']}\n")
                if 'modified' in details:
                    export_file.write(f"Modified: {details['modified']}\n")
                export_file.write("-" * 80 + "\n\n")
        
        messagebox.showinfo(
            title="Export Successful",
            message=f"Data exported to:\n{filename}\n\n⚠️ Keep this file secure!"
        )
    
    except Exception as e:
        messagebox.showerror(
            title="Export Failed",
            message=f"Failed to export data:\n{str(e)}"
        )


# ========================== STATISTICS ==========================
def show_statistics():
    """Display password statistics."""
    data = load_data()
    
    if not data:
        messagebox.showinfo(
            title="No Data",
            message="No saved passwords found."
        )
        return
    
    total = len(data)
    weak = 0
    medium = 0
    strong = 0
    
    for website, details in data.items():
        score, strength, _ = check_password_strength(details['password'])
        if strength == "Weak":
            weak += 1
        elif strength == "Medium":
            medium += 1
        else:
            strong += 1
    
    messagebox.showinfo(
        title="Password Statistics",
        message=f"📊 Password Statistics\n\n"
                f"Total Passwords: {total}\n\n"
                f"🔴 Weak: {weak} ({weak/total*100:.1f}%)\n"
                f"🟡 Medium: {medium} ({medium/total*100:.1f}%)\n"
                f"🟢 Strong: {strong} ({strong/total*100:.1f}%)\n\n"
                f"{'⚠️ Consider updating weak passwords!' if weak > 0 else '✅ All passwords are secure!'}"
    )


# ========================== GUI SETUP ==========================
def setup_gui():
    """Initialize and configure the GUI window and widgets."""
    global window, canvas, entry_website, entry_email_username, entry_password
    global strength_label, btn_show_password
    
    # Window configuration
    window = Tk()
    window.title("🔐 Advanced Password Manager")
    window.config(padx=20, pady=30, bg=COLOR_BG)
    window.resizable(False, False)
    
    # Canvas with logo
    try:
        background_image = PhotoImage(file=LOGO_FILE)
        canvas = Canvas(height=200, width=200, bg=COLOR_BG, highlightthickness=0)
        canvas.create_image(100, 100, image=background_image)
        canvas.grid(row=0, column=0, columnspan=3, pady=10)
        canvas.image = background_image
    except Exception:
        logo_label = Label(text="🔐", font=("Arial", 60), bg=COLOR_BG)
        logo_label.grid(row=0, column=0, columnspan=3, pady=10)
    
    # Title
    title_label = Label(
        text="Advanced Password Manager",
        font=("Arial", 14, "bold"),
        bg=COLOR_BG,
        fg=COLOR_ACCENT
    )
    title_label.grid(row=1, column=0, columnspan=3, pady=5)
    
    # Labels with improved styling
    Label(text="Website:", bg=COLOR_BG, font=("Arial", 10)).grid(row=2, column=0, sticky="e", pady=5, padx=5)
    Label(text="Email/Username:", bg=COLOR_BG, font=("Arial", 10)).grid(row=3, column=0, sticky="e", pady=5, padx=5)
    Label(text="Password:", bg=COLOR_BG, font=("Arial", 10)).grid(row=4, column=0, sticky="e", pady=5, padx=5)
    
    # Entry fields
    entry_website = Entry(width=ENTRY_WIDTH_SMALL, font=("Arial", 10))
    entry_website.grid(row=2, column=1, sticky="ew", pady=5)
    entry_website.focus()
    
    entry_email_username = Entry(width=ENTRY_WIDTH_SMALL, font=("Arial", 10))
    entry_email_username.grid(row=3, column=1, columnspan=2, sticky="ew", pady=5)
    entry_email_username.insert(0, DEFAULT_EMAIL)
    
    entry_password = Entry(width=ENTRY_WIDTH_SMALL, font=("Arial", 10), show="*")
    entry_password.grid(row=4, column=1, sticky="ew", pady=5)
    entry_password.bind('<KeyRelease>', update_strength_indicator)
    
    # Password strength indicator
    strength_label = Label(text="Strength: Empty", bg=COLOR_BG, font=("Arial", 9))
    strength_label.grid(row=5, column=1, sticky="w", pady=2)
    
    # Primary action buttons (Row 2-4)
    Button(
        text="🔍 Search",
        command=search_password,
        bg=COLOR_ACCENT,
        fg="white",
        font=("Arial", 9, "bold"),
        cursor="hand2"
    ).grid(row=2, column=2, sticky="ew", padx=(5, 0), pady=5)
    
    # Password control buttons frame
    pwd_controls = Frame(bg=COLOR_BG)
    pwd_controls.grid(row=4, column=2, sticky="ew", padx=(5, 0), pady=5)
    
    Button(
        pwd_controls,
        text="🎲 Generate",
        command=generate_password,
        bg=COLOR_SUCCESS,
        fg="white",
        font=("Arial", 8, "bold"),
        cursor="hand2"
    ).pack(side=LEFT, expand=True, fill=BOTH, padx=(0, 2))
    
    btn_show_password = Button(
        pwd_controls,
        text="👁 Show",
        command=toggle_password_visibility,
        bg="#95a5a6",
        fg="white",
        font=("Arial", 8, "bold"),
        cursor="hand2"
    )
    btn_show_password.pack(side=LEFT, expand=True, fill=BOTH, padx=(2, 0))
    
    # Main action buttons (Row 6)
    Button(
        text="💾 Save Password",
        command=save_password,
        bg=COLOR_SUCCESS,
        fg="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
        pady=8
    ).grid(row=6, column=0, columnspan=3, sticky="ew", pady=10)
    
    # Utility buttons frame (Row 7)
    utility_frame = Frame(bg=COLOR_BG)
    utility_frame.grid(row=7, column=0, columnspan=3, sticky="ew", pady=5)
    
    Button(
        utility_frame,
        text="📋 Copy",
        command=copy_password,
        bg="#3498db",
        fg="white",
        font=("Arial", 9),
        cursor="hand2"
    ).pack(side=LEFT, expand=True, fill=BOTH, padx=2)
    
    Button(
        utility_frame,
        text="🗑️ Delete",
        command=delete_password,
        bg=COLOR_WARNING,
        fg="white",
        font=("Arial", 9),
        cursor="hand2"
    ).pack(side=LEFT, expand=True, fill=BOTH, padx=2)
    
    Button(
        utility_frame,
        text="👁️ View All",
        command=view_all_passwords,
        bg="#9b59b6",
        fg="white",
        font=("Arial", 9),
        cursor="hand2"
    ).pack(side=LEFT, expand=True, fill=BOTH, padx=2)
    
    # Advanced features frame (Row 8)
    advanced_frame = Frame(bg=COLOR_BG)
    advanced_frame.grid(row=8, column=0, columnspan=3, sticky="ew", pady=5)
    
    Button(
        advanced_frame,
        text="📊 Statistics",
        command=show_statistics,
        bg="#16a085",
        fg="white",
        font=("Arial", 9),
        cursor="hand2"
    ).pack(side=LEFT, expand=True, fill=BOTH, padx=2)
    
    Button(
        advanced_frame,
        text="💾 Export Data",
        command=export_data,
        bg="#34495e",
        fg="white",
        font=("Arial", 9),
        cursor="hand2"
    ).pack(side=LEFT, expand=True, fill=BOTH, padx=2)
    
    # Configure grid weights
    window.grid_columnconfigure(1, weight=1)
    
    # Footer
    footer_label = Label(
        text="Built with Python & Tkinter | Keep your data secure! 🔒",
        bg=COLOR_BG,
        fg="#7f8c8d",
        font=("Arial", 8)
    )
    footer_label.grid(row=9, column=0, columnspan=3, pady=10)
    
    window.mainloop()


# ========================== MAIN ==========================
if __name__ == "__main__":
    setup_gui()