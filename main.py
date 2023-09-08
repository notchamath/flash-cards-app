from tkinter import *
from data_manager import DataManager

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

word_manager = DataManager()


# Get next card
def next_card():
    # Cancel already set timers
    global flip_delay
    window.after_cancel(flip_delay)

    canvas.itemconfig(canvas_image, image=front_card_img)
    canvas.itemconfig(title_text, text=word_manager.fr, fill="black")
    canvas.itemconfig(word_text, text=word_manager.fr_word, fill="black")

    # Set new timer
    flip_delay = window.after(3000, flip_card)


# Flip card
def flip_card():
    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(title_text, text=word_manager.en, fill="white")
    canvas.itemconfig(word_text, text=word_manager.en_word, fill="white")


# Handle correct button
def correct_click():
    word_manager.got_correct()
    next_card()


# Handle wrong button
def wrong_click():
    word_manager.got_wrong()
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("FLASH CARDS")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# declare flip_delay as a global variable here so next_card() has an already set timer to cancel
flip_delay = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Canvas image
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_img)

# Canvas texts
title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
correct_img = PhotoImage(file="./images/right.png")
correct_btn = Button(image=correct_img, command=correct_click, highlightthickness=0, border=0)
correct_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, command=wrong_click, highlightthickness=0, border=0)
wrong_btn.grid(column=0, row=1)

# Get first card
next_card()

window.mainloop()
