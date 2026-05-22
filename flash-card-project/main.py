import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}



#CREATE NEW FLASK CARD

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(title, text="French",fill="black")
    canvas.itemconfig(word, text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image, image=front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English",fill = "white")
    canvas.itemconfig(word, text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_image, image=back_img)

#CREATING A FILE WITH THE NEW UNKNOWN
def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

#UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50 ,bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg = BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

flip_timer = window.after(3000, func=flip_card)

#Buttons
wrong_button = PhotoImage(file="./images/wrong.png")
w_button = Button(image = wrong_button, highlightthickness = 0,command=next_card)
w_button.grid(column = 0, row = 1)

right_button = PhotoImage(file="./images/right.png")
r_button = Button(image = right_button, highlightthickness = 0,command=is_known)
r_button.grid(column = 1, row = 1)


next_card()
window.mainloop()