import random
import time
import tkinter as tk

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

title.configure(font=font_tuple_large)

title.pack()
colorbackground.pack()

print("What is the RGB Value (R,G,B)")
rgb_string = str(input())

rgb_list = rgb_string.split(",")
red_score = 255 - abs(red_value - int(rgb_list[0]))
blue_score = 255 - abs(blue_value - int(rgb_list[1]))
green_score = 255 - abs(red_value - int(rgb_list[2]))

total_score = red_score + green_score + blue_score

print("Your score is ", total_score, "Highest Possible Score 765")
time.sleep(6000)

exit()


window.mainloop()
