from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [random.choice(letters) for _ in range(random.randint(6, 8))]
    password_list2 = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list3 = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_list3 + password_list2 + password_list1

    random.shuffle(password_list)

    password = "".join(password_list)
    entry3.delete(0, "end")
    entry3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data = {website: {
        "email": email,
        "password": password
    }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave a field empty")

    else:
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            entry1.delete(0, "end")
            entry3.delete(0, "end")


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = entry1.get()
    try:
        with open(file="data.json", mode="r")as file:
            data_read = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")

    else:

        if website in data_read:
            email = data_read[website]["email"]
            password = data_read[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
# window.minsize(width=400, height=400)
window.config(padx=50, pady=50)
window.title("Password manager")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

label_website = Label(text="Website/App:", font=(15,))
label_website.grid(row=2, column=1)

# website entry
entry1 = Entry(width=25)
entry1.grid(row=2, column=2, columnspan=1)
entry1.focus()

label_username = Label(text="Email/Username:", font=(15,))
label_username.grid(row=3, column=1)

# username entry
entry2 = Entry(width=44)
entry2.grid(row=3, column=2, columnspan=2)
entry2.insert(0, "example_id@gmail.com")

label_password = Label(text="Password:", font=15)
label_password.grid(row=4, column=1)

# password entry
entry3 = Entry(width=25)
entry3.grid(row=4, column=2)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=4, column=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=2, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=2, column=3)

window.mainloop()
