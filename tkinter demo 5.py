from tkinter import *

# Layout a simple form using the Grid Manager


class Form1:
    def __init__(self):

        window = Tk()
        window.title("Tkinter Demo 5")
        window.geometry("400x200")

        # Create the fields
        Label(window, text="Enter your name: ", font=("Arial", 14),
              foreground="Blue").grid(row=1, column=1, pady=10)

        # Declare a StringVar and textvariable
        # to read the user entry from an Entry field
        self.name = StringVar()
        Entry(window, font=("Arial", 14), foreground="Blue",
              textvariable=self.name).grid(row=1, column=2, pady=10)

        btn_greeting =\
            Button(window, text="Announce Guest", font=("Arial", 14),
                   foreground="Green", command=self.process_click)
        btn_greeting.grid(row=2, column=1, columnspan=2, pady=10)

        self.lbl_message = Label(window, text="Welcome", font=("Arial", 14),
                                 foreground="Blue")
        self.lbl_message.grid(row=3, column=1, columnspan=2, pady=10)

        window.mainloop()

    # Handle the button click
    def process_click(self):
        # Show a welcome message for the guest
        self.lbl_message.config(text="Welcome " + self.name.get())


# Create a GUI object
Form1()
