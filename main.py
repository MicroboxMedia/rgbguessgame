import random
import tkinter as tk
from turtle import color

window = tk.Tk()
font_tuple_large = ("Fugaz One Regular", 20, "bold")
font_tuple_small = ("Fugaz One Regular", 14, "bold")


color_guess = f'#{hex(random.randint(0,16777215))[2:]}'
red_value = int(color_guess[1] + color_guess[2], 16)
green_value = int(color_guess[3] + color_guess[4], 16)
blue_value = int(color_guess[5] + color_guess[6], 16)

title = tk.Label(text="Guess the RGB Value")
colorbackground = tk.Label(
    text = "",
    background=color_guess,
    width=25,
    height=10
)

label_red = tk.Label(text="R")
entry_red = tk.Entry()

label_green = tk.Label(text="G")
entry_green = tk.Entry()

label_blue = tk.Label(text="B")
entry_blue = tk.Entry()

title.configure(font=font_tuple_large)
label_red.configure(font=font_tuple_small)
label_green.configure(font=font_tuple_small)
label_blue.configure(font=font_tuple_small)

title.pack()
colorbackground.pack()
label_red.pack()
entry_red.pack()
label_green.pack()
entry_green.pack()
label_blue.pack()
entry_blue.pack()
window.mainloop()
