from tkinter import *

# Respond to a button click by changing the text in a label

# These need to defined globally

window = Tk()
label = Label()


def process_click():
    # Change the label in response to the button click
    label.config(text="Thanks for clicking")


def demo3():

    # Set the window title and size

    window.title("Tkinter Demo 3")
    window.geometry("200x100")

    global label
    label = Label(window, text="This Is Getting Interesting")
    button = Button(window, text="Click Me", command=process_click)

    label.pack()
    button.pack()

    window.mainloop()

demo3()
