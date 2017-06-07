from tkinter import *
from tkinter import messagebox

# Provide a function to respond to a button click


def process_click():
    messagebox.showinfo("My Dialog Box", "You Clicked Me")


def demo2():
    window = Tk()
    window.title("Tkinter Demo 2")

    label = Label(window, text="This Is Getting Interesting")

    # Set the action for a button click
    button = Button(window, text="Click Me", command=process_click)

    label.pack()
    button.pack()

    window.mainloop()

demo2()
