from tkinter import *
from tkinter import messagebox
from math import pi

# A form to calculate the area of a circle given the radius


class Form1:
    def __init__(self):

        window = Tk()
        window.title("Tkinter Demo 6")
        window.geometry("300x200")

        # Create the fields
        Label(window, text="Enter the radius: ", font=("Arial", 14),
              foreground="Blue").grid(row=1, column=1, padx=5, pady=10)

        # Declare a DoubleVar and textvariable to read the user entry
        # from an Entry field as a decimal value
        self.radius = DoubleVar()
        Entry(window, font=("Arial", 14), foreground="Blue", width=10,
              textvariable=self.radius).grid(row=1, column=2, pady=10)

        btn_calculate_area =\
            Button(window, text="Calculate Area", font=("Arial", 14),
                   foreground="Green", command=self.process_click)
        btn_calculate_area.grid(row=2, column=1, columnspan=2, pady=10)

        Label(window, text="Area =", font=("Arial", 14),
              foreground="Blue").grid(row=3, column=1, pady=10, sticky=E)

        self.lbl_area = Label(window, text="", font=("Arial", 14),
                              foreground="Blue")
        self.lbl_area.grid(row=3, column=2, pady=10, sticky=W)

        window.mainloop()

    # Handle the button click
    def process_click(self):
        # Try to calculate the area of a circle given the radius
        try:
            if self.radius.get() >= 0:
                area = pi * self.radius.get() ** 2
                area_formatted = "{:.2f}".format(area)
                self.lbl_area.config(text=area_formatted)
            else:
                messagebox.showerror("My Area Calculator",
                                     "Negative radius is not allowed")
        except TclError:
            messagebox.showerror("My Area Calculator",
                                 "Missing or non-numeric entry")


# Create a GUI object
Form1()
