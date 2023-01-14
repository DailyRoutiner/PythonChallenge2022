from tkinter import *

# Creating a new window and configuration
window = Tk()
window.title("Widget Exmaples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

# Buttons
def action():
    print("Do something")

# calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(END, "Examples of multi-line text entry.")
text.pack()

# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Check button
def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


window.mainloop()

