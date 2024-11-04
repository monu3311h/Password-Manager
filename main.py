import random
from tkinter import *
from tkinter import messagebox
import pyperclip

window = Tk()
window.minsize(300, 300)
window.title('Password Manager')
window.config(padx=50, pady=50)

# Generating Random Password

ALPHABETS= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'O', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ';', ':', '?', '<', '>', '/']


def generate_password():
    letters = [random.choice(ALPHABETS) for _ in range(5)]
    nums = [str(random.choice(NUMBERS)) for _ in range(3)]
    symbol = [random.choice(SYMBOLS) for _ in range(3)]

    random_password = letters + nums + symbol

    random.shuffle(random_password)
    new_password = ''.join(random_password)

    password.insert(0, new_password)

    pyperclip.copy(new_password) # to copy the password into the clipboard

# Search the data 
def search_password():
    website_name = website.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Error!', message='No Data File Found')
    else:
        if website_name in data:
            website_email = data[website_name]['Email']
            website_password = data[website_name]['Password']
            messagebox.showinfo(title='Here is Your Information', message=f'Email: {website_email}\n Password: {website_password}')
            website.delete(0, END)
        else:
            messagebox.showerror(title='Error!', message=f"The Website {website_name} doesn't exist in file")

# Save data
def save_data():
    website_name = website.get()
    email_data = email.get()
    password_data = password.get()

    if len(website_name) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='Oops', message="Please Don't leave any field empty")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)

canvas = Canvas(width=200, height=190)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 95, image=image)
canvas.grid(column=2, row=1)
label1 = Label(text='Website:')
label1.grid(column=1, row=2)
website = Entry(width=35)
website.focus()
website.grid(column=2, row=2, columnspan=2)
search = Button(text='Search', command=search_password)
search.grid(column = 3, row=2)

label2 = Label(text='Email/Username:')
label2.grid(column=1, row=3)
email = Entry(width=35)
email.insert(0, 'tanwarmonu07@gmail.com')
email.grid(column=2, row=3, pady=10, columnspan=2)

label3 = Label(text='Password:')
label3.grid(column=1, row=4)
password = Entry(width=21)
password.grid(row=4, column=2)

password_btn = Button(text='Generate Password', command=generate_password)
password_btn.grid(row=4, column=3)

add_btn = Button(text='Add', width=36, command=save_data)
add_btn.grid(row=5, column=2, columnspan=2, pady=10)

window.mainloop()
