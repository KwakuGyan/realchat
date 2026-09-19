import tkinter as tk
import random

root = tk.Tk()
root.title("Color Changing Window")
root.geometry("400x400")

colors = ["red", "green", "blue", "yellow", "purple", "orange"]

def change_color():
    root.config(bg=random.choice(colors))

button = tk.Button(
    root,
    text="Change Color",
    command=change_color
)

button.pack(pady=170)

root.mainloop()