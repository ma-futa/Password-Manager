import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(numbers) for _ in range(randint(2, 4))] + [choice(symbols) for _ in
                                                                       range(randint(2, 4))] + [
                        choice(letters) for _ in range(randint(8, 10))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(END,password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data =  {
        website:{
            'email':email,
            'password':password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title='Warning', message='please fill in all fields')
        return

    if messagebox.askokcancel(title=website,
                              message=f"These are the details entered \nEmail/UserName: {email}\nPassword: {password}\nIs it okay to save?"):
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open('data.json', mode='w') as file:
                json.dump(data,file,indent=4)
        finally:
            # file.write(f'{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n ')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.gif', )
canvas.create_image(100, 100, image=logo_img, )
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', font=('Arial'))
website_label.grid(column=0, row=1)
username_label = Label(text='Email/Username:', font=('Arial'))
username_label.grid(column=0, row=2)
password_label = Label(text='Password', font=('Arial'))
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.config(width=35)
website_entry.grid(column=1, row=1, columnspan=2, )
website_entry.focus()
username_entry = Entry()
username_entry.config(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, 'rhealmohammedfuta2000@gmail.com')
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
