from tkinter import *
import math

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
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_time():
    window.after_cancel(my_timer)
    # 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title label
    timer.config(text="Timer", fg=GREEN)
    # reset check_marks
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 8th
    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        # if it's the 2nd/4th/6th
        count_down(short_break_sec)
    else:
        timer.config(text="Work", fg=GREEN)
        # if it's the 1st/3rd/5th/7th
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        session = math.floor(reps/2)
        for _ in range(session):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)


# tkinter canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) # position x, y,  image
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# User Interface
# use fg and grid() instead of pack()
timer = Label(text="Timer", font=(FONT_NAME, 45, "normal"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)
start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_time)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

# copy-paste checkmark
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)






window.mainloop()