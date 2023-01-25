from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# function save, generate passowrd
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = { website: {
        "email": email,
        "password": password
    }}

    # check empty field
    if not website or not email or not password:
        messagebox.showwarning(title="Found Empty field", message="You haven't left any field empty!")
    else:
        # save data
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \n Email: {email} \n Password: {password}")
        if is_ok:
            try:
                with open(file="data.json", mode="r") as file:
                    # Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open(file="data.json", mode="w") as file:
                    # insert data
                    json.dump(new_data, file, indent=4)

            else:
                # update json format with new data
                data.update(new_data)

                with open(file="data.json", mode="w") as file:
                    # insert data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def generate_password():

    # [newitem for item in list if exists]
    # password_list = [random.choice(letters+numbers+symbols) for index in range(nr_letter+nr_number+nr_symbol)]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)


def search_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showwarning(title="Empty field", message="Not allowed empty field.")
    else:
        try:
            with open(file="data.json", mode="r") as file_data:
                json_data = json.load(file_data)
                data = json_data[website]
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File found")
        except KeyError:
            messagebox.showwarning(title="Not exist", message="Not found data")
        else:
            messagebox.showinfo(title=data, message=f"Email: {data['email']} \n Password: {data['password']}")


# UI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

Label(text="Website:").grid(column=0, row=1)
Label(text="Email:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abc@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

Button(text="Search", width=13,  command=search_password).grid(column=2, row=1)
Button(text="Generate Password", command=generate_password).grid(column=2, row=3)
Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2)


window.mainloop()
