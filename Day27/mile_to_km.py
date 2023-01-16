from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=15, pady=15)

# Entry
mile_field = Entry()
mile_field.config(width=10)
mile_field.grid(column=1, row=0)

# Miles Label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# equal Label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# km Label
converted_km = Label(text="0")
converted_km.grid(column=1, row=1)

# km Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate
def calculate():
    # mile to km
    mile = mile_field.get()
    km = round(float(mile) * 1.60934, 2)
    converted_km.config(text=f"{km}")

# the way we do that is by tying it as a command.
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)




window.mainloop()