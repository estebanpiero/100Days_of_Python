# Capstone Project Flash Cards

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

FILE_PATH = '/home/argento/Documents/Education/100Days_of_Python/[Day 31:] Flash Card App Capstone Project/Capstone Project Flash Cards/'

# ---------------------------- Reading CSV File with Pandas ------------------------------- #

try:
    card_data = pandas.read_csv(f'{FILE_PATH}' + 'data/italian_words.csv')
except FileNotFoundError as e:
    print({e})
else:
    to_learn = card_data.to_dict(orient="records")
 
# ---------------------------- Functions ------------------------------- #

def flip_card():
    global current_card
    canvas.itemconfig(canvas_iamge, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_iamge, image=card_front_img)
    canvas.itemconfig(card_title, text="Italian", fill="black")
    canvas.itemconfig(card_word, text=current_card["Italian"], fill="black")

    window.after(3000, flip_card)

def learned_word():
    global current_card
    to_learn.remove(current_card)
    next_card()
    
# ---------------------------- GUI ------------------------------- #

window = Tk()
window.title("Italian Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# ---------------------------- Images ------------------------------- #
card_front_img = PhotoImage(file=f"{FILE_PATH}images/card_front.png")
card_back_img = PhotoImage(file=f"{FILE_PATH}images/card_back.png")
right_image = PhotoImage(file=f"{FILE_PATH}images/right.png")
wrong_image = PhotoImage(file=f"{FILE_PATH}images/wrong.png")

# ---------------------------- Canvas ------------------------------- # 

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_iamge = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- Buttons ------------------------------- #

right_button = Button(image=right_image, highlightthickness=0 , command=learned_word)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)      
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()