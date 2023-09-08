from tkinter import *
from data_manager import DataManager

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

word_manager = DataManager()
flip_delay = ""
disable_btns = False


# ---------------------------- UI SETUP ------------------------------- #

# Update Word
def update_word():
    canvas.itemconfig(word_text, text=word_manager.fr_word)


# Flip card
def flip_card():
    global flip_delay
    window.after_cancel(flip_delay)

    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(title_text, text=word_manager.en, fill="white")
    canvas.itemconfig(word_text, text=word_manager.en_word, fill="white")

    word_manager.got_correct()
    flip_delay = window.after(3000, flip_back)


# Flip the card back and load next word
def flip_back():
    global flip_delay, disable_btns
    window.after_cancel(flip_delay)

    update_word()
    canvas.itemconfig(canvas_image, image=front_card_img)
    canvas.itemconfig(title_text, text=word_manager.fr, fill="black")
    canvas.itemconfig(word_text, text=word_manager.fr_word, fill="black")

    disable_btns = False


# Handle correct button
def correct_click():

    global flip_delay, disable_btns
    if not disable_btns:
        disable_btns = True

        flip_delay = window.after(2000, flip_card)


# Handle wrong button
def wrong_click():
    global disable_btns
    if not disable_btns:
        word_manager.got_wrong()
        update_word()


# Window
window = Tk()
window.title("FLASH CARDS")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Canvas image
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_img)

# Canvas texts
title_text = canvas.create_text(400, 150, text=word_manager.fr, font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text=word_manager.fr_word, font=(FONT_NAME, 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
correct_img = PhotoImage(file="./images/right.png")
correct_btn = Button(image=correct_img, command=correct_click, highlightthickness=0, border=0)
correct_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, command=wrong_click, highlightthickness=0, border=0)
wrong_btn.grid(column=0, row=1)

window.mainloop()
