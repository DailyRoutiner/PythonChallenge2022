import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# shuffle word
df = pandas.read_csv("./data/french_words.csv")
to_learn = df.to_dict(orient="records")# very important to get records


def next_card():
    current_card = random.choice(to_learn)
    board_canvas.itemconfig(card_title, text="French")
    board_canvas.itemconfig(card_word, text=current_card["French"])

# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


board_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
board_image = PhotoImage(file="./images/card_front.png")
board_canvas.create_image(400, 263, image=board_image)

card_title = board_canvas.create_text(400, 150, text="", fill="black", font=("Courier", 40, "italic"))
card_word = board_canvas.create_text(400, 263, text="", fill="black", font=("Courier", 60, "bold"))
board_canvas.grid(column=0, row=0, columnspan=2)

known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)
unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()



