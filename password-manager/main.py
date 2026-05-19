import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint

#PASSWORD GENERATOR
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letters + password_numbers + password_symbol

    shuffle(password_list)
    password = "".join(password_list)

    third_entry.insert(0, password)

    pyperclip.copy(password)

#SAVE PASSWORD
def save():
    web_entry = first_entry.get()
    email_entry = second_entry.get()
    pass_entry = third_entry.get()


    if len(web_entry) == 0 or len(email_entry) == 0 or len(pass_entry) == 0:
        messagebox.showerror("Error", "Please make sure you don't let any fields empty")
    else:
        is_okay = messagebox.askokcancel(title=web_entry, message=f"These are the details entered: "
                                                                  f"\nEmail: {email_entry}"
                                                                  f"\nPassword: {pass_entry} "
                                                                  f"\n Is it ok to save?")

        if is_okay:
            with open("data.txt", "a") as file:
                formatted_data = f"{web_entry} | {email_entry} | {pass_entry}\n"
                file.write(formatted_data)

            first_entry.delete(0, END)
            third_entry.delete(0, END)



#UI SETUP

window = Tk()
window.title("Password Manager")
window.config(pady=40,padx=40)

canvas = Canvas(width=200, height=200)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_image)
canvas.grid(column=1, row=0,columnspan=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_email = Label(text="Email/Username::")
website_email.grid(column=0, row=2)

website_password = Label(text="Password:")
website_password.grid(column=0, row=3)

first_entry = Entry(width=35)
first_entry.grid(column=1, row=1, columnspan=2,sticky="EW")
first_entry.focus()

second_entry = Entry(width=35)
second_entry.grid(column=1, row=2, columnspan=2,sticky="EW")
second_entry.insert(0,"example04gmail.com")
second_entry.focus()

third_entry = Entry(width=21)
third_entry.grid(column=1, row=3,sticky="W")
third_entry.focus()

generatePass_button = Button(text="Generate password",command=generatePassword)
generatePass_button.grid(column=2, row=3,sticky="E")

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1, row=4, columnspan=2,sticky="EW")


window.mainloop()