from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
LANG = "French"
word = "Word"

# UI SETUP

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
title_text = canvas.create_text(400, 150, text=LANG, font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text=word, font=(FONT_NAME, 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
correct_img = PhotoImage(file="./images/right.png")
correct_btn = Button(image=correct_img, highlightthickness=0, border=0)
correct_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, border=0)
wrong_btn.grid(column=0, row=1)

window.mainloop()
