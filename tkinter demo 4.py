from tkinter import *

# Respond to a button click by changing the text in a label

# All code and variables are contained in functions
# All functions are contained in a class


class ButtonAndLabel:
    # Constructor
    def __init__(self):

        window = Tk()
        # Set the window title and size
        window.title("Tkinter Demo 4")
        window.geometry("300x100")

        # Create a label and a button with a font and a color
        self.label = Label(window, text="This Is Getting Interesting",
                           font=("Arial", 14), foreground="Blue")

        self.button = Button(window, text="Click Me", font=("Arial", 14),
                        foreground="Green", command=self.process_click)

        self.label.pack()
        self.button.pack()

        window.mainloop()

    def process_click(self):
        # Change the label in response to the button click
        self.label.config(text="Thanks for clicking")


# Create a GUI object
ButtonAndLabel()
