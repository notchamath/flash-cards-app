from tkinter import *
from data_manager import DataManager

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
TITLE = "French"

word_manager = DataManager()


# ---------------------------- UI SETUP ------------------------------- #

# Update Word
def update_word():
    canvas.itemconfig(word_text, text=word_manager.fr_word)


# Handle correct button
def correct_click():
    word_manager.got_correct()
    update_word()


# Handle wrong button
def wrong_click():
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
canvas.create_image(400, 263, image=front_card_img)
# Canvas texts
title_text = canvas.create_text(400, 150, text=TITLE, font=(FONT_NAME, 40, "italic"))
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
