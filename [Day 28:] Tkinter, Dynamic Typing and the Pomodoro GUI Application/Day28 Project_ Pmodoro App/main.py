from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
text_timer = ''
count = 0
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global text_timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(text_timer,text = '00:00')
    label_times.config(text="Timer")
    label_checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1 
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label_times.config(text="Relax",fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        label_times.config(text="Work",fg=GREEN)
    elif reps % 2 == 0 :
        count_down(SHORT_BREAK_MIN * 60)
        label_times.config(text="Relax",fg=PINK)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps, timer

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(text_timer,text = f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1,count_down,count-1)
    else:
        start_timer()
        marks = ""
        worked_session = math.floor(reps/2)
        for _ in range(worked_session):
            marks = '✓'
        label_checkmark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)
#background_image = PhotoImage(file='./Day28_Tkinter-Dynamic-PomodoroGUI/Pomodoro App Project/tomato.png')
background_image = PhotoImage(file='tomato.png')

#tomato bg and timer label
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=background_image)
text_timer = canvas.create_text(103,130,text='00:00',fill='white',font=(FONT_NAME,25,'bold'))
canvas.grid(column=1,row=1)

#label
label_times = Label(text='Timer',fg=GREEN,font=(FONT_NAME,30,'bold'),bg=YELLOW)
label_times.grid(column=1,row=0)

label_checkmark = Label(fg=GREEN,font=(FONT_NAME,20,'bold'),bg=YELLOW)
label_checkmark.grid(column=1,row=2)

#buttons
start_button = Button(text='Start',command=start_timer)
start_button.grid(column=0,row=3)

reset_button = Button(text='Reset',command=reset_timer)
reset_button.grid(column=2,row=3)

window.mainloop()