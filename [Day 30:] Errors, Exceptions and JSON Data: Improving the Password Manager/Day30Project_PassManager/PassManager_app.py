# Password Generator Using Tkinter GUI and Canvas

from tkinter import *
from tkinter import messagebox 
import pyperclip

import random 
import json

file_path = '/home/argento/Documents/Education/100Days_of_Python/[Day 29:] Building a Password Manager GUI App with Tkinter/Day29Project_PassManager/'
data = {}

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)


    password = ''.join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE GENERATOR ------------------------------- #

def save_password():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }
    
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return
    
    '''
    Save password

    with open('data.txt', 'a') as data_file:
        data_file.write(f"{website} | {email_username} | {password}\n")

    '''

    if messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} "f"\nPassword: {password} \nIs it ok to save?"): 

        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except (FileNotFoundError,json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ----------------------------  Search Password ------------------------------- # 

def search_password():
    global entry_password
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            
            # Show the password in the password entry field
            entry_password.delete(0, END)
            entry_password.insert(0, password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ----------------------------  GUI Setup ------------------------------- # 
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)
background_image = PhotoImage(file='logo.png')

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=background_image)
canvas.grid(row=0, column=1)

# Labels

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entries

entry_website = Entry(width=21)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email_username = Entry(width=35)

entry_email_username.grid(row=2, column=1, columnspan=2)
entry_email_username.insert(0, 'pierotti.esteban@gmail.com')
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)    

# Buttons

button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)  

search_button = Button(text="Search", width=13, command=search_password)
search_button.grid(row=1, column=2)





window.mainloop()