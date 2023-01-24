from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    # [newitem for item in list if exists]
    # password_list = [random.choice(letters+numbers+symbols) for index in range(nr_letters+nr_symbols+nr_numbers)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = { website: {
        "email": email,
        "password": password
    }}

    # Check empty field
    if len(website) == 0 or len(email) == 0 or not password:
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

Button(text="Generate Password", command=generate_password).grid(column=2, row=3)
Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2)

window.mainloop()