from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check empty field
    if not website or not email or not password:
        messagebox.showwarning(title="Error", message="You haven't left any fields empty!")
    else:
        # message box here
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \n Email: {email}\n Password: {password}")

        if is_ok:
            with open(file="data.txt", mode="a+") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abc@dummy.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

Button(text="Generate Password").grid(column=2, row=3)
Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2)

window.mainloop()