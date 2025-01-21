from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Fiszki polsko francuskie")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# --------------------------- DATA ---------------------------#
df = pd.read_csv("data/fiszki_fr-pl.csv")
all_words = df.to_dict(orient="records")


def new_word():
    global current_word
    global swap_timer
    window.after_cancel(swap_timer)
    current_word = random.choice(all_words)
    canvas.itemconfig(canvas_card, image=card_front_image)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(
        word_label, text=f"{current_word['French']}".lower(), fill="black"
    )
    all_words.remove(current_word)
    swap_timer = window.after(3000, answer)


def answer():
    global current_word
    canvas.itemconfig(canvas_card, image=card_back_image)
    canvas.itemconfig(language_label, text="Polish", fill="white")
    canvas.itemconfig(word_label, text=f"{current_word['Polish']}", fill="white")


# --------------------------- CANVAS ---------------------------#
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=card_front_image)
language_label = canvas.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic")
)
word_label = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

swap_timer = window.after(3000, answer)

# --------------------------- BUTTONS ---------------------------#
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=wrong_button_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=new_word,
)
wrong_button.grid(column=0, row=1)

correct_button_image = PhotoImage(file="images/right.png")
correct_button = Button(
    image=correct_button_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=new_word,
)
correct_button.grid(column=1, row=1)

new_word()
window.mainloop()
