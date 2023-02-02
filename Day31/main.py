import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")# very important to get records
current_card = {}

def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    # shuffle word
    current_card = random.choice(to_learn)
    board_canvas.itemconfig(card_title, text="French", fill="black")
    board_canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    board_canvas.itemconfig(board, image=card_front)
    flip_time = window.after(3000, flip_card)

def flip_card():
    board_canvas.itemconfig(board, image=card_back)
    board_canvas.itemconfig(card_title, text="English", fill="white")
    board_canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)


# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_time = window.after(3000, flip_card)
# card board
board_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
board = board_canvas.create_image(400, 263, image=card_front)
# card text
card_title = board_canvas.create_text(400, 150, text="", fill="black", font=("Courier", 40, "italic"))
card_word = board_canvas.create_text(400, 263, text="", fill="black", font=("Courier", 60, "bold"))
board_canvas.grid(column=0, row=0, columnspan=2)

known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()



