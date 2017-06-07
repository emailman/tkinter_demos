from tkinter import *

# Show a button and a label, but no action


def demo1():
    window = Tk()
    window.title("Tkinter Demo 1")

    label = Label(window, text="This Is Getting Interesting")
    button = Button(window, text="Click Me")

    label.pack()
    button.pack()

    window.mainloop()

demo1()
