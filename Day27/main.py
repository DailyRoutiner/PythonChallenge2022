from tkinter import *

window = Tk()
window.title("My First GUI Progress")
window.minsize(width=500, height=300)
window.config(padx=15, pady=15)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack() # place view in the center and **kw
my_label.grid(column=0, row=0)
my_label.config(padx=15, pady=15)

my_label["text"] = "New Text1"
my_label.config(text="New Text2")


# Button
def button_clicked():
    # print("I got clicked!")
    text = input1.get()
    my_label["text"] = text


button = Button(text="Click Me!", command=button_clicked )
# button.pack()
button.grid(column=1, row=1)

# Entry
input1 = Entry(width=10)
# input1.pack()
input1.grid(column=3, row=2)


# New button
button1 = Button(text="New button")
button1.grid(column=2, row=0)





window.mainloop()
