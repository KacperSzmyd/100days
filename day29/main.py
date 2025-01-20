from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    password_input.delete(0, END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []

    [password_list.append(choice(letters)) for x in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for x in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for x in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)

    password_input.insert(0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    username = email_input.get()
    password = password_input.get()

    new_data = {website: {"email": username, "password": password}}

    if website == "" or password == "":
        messagebox.showerror(title="Oops", message="Please do not leave empty fields!")

    else:
        confirmation = messagebox.askokcancel(
            title=website,
            message=f"These are the credentials you entered: \nEmail: {username}\nPassword: {password}",
        )

        if confirmation:
            try:
                with open("data/passwords.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data/passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data/passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_image = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=lock_image)

canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=39)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, string="k.g.szmyd@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(
    text="Add",
    width=36,
    command=save_password,
)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
