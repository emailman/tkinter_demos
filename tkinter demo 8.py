from tkinter import *

# Use three sliders to create a color mixer


class ColorMixer:
    def __init__(self):
        window = Tk()
        window.title("Color Mixer")

        self.sldr_red = Scale(window, to="255", orient=HORIZONTAL, troughcolor="RED", fg="RED",
                              length=175, command=self.slider_moved)
        self.sldr_red.grid(row=1, column=1)

        self.sldr_green = Scale(window, to="255", orient=HORIZONTAL, troughcolor="GREEN", fg="GREEN",
                                length=175, command=self.slider_moved)
        self.sldr_green.grid(row=2, column=1)

        self.sldr_blue = Scale(window, to="255", orient=HORIZONTAL, troughcolor="BLUE", fg="BLUE",
                               length=175, command=self.slider_moved)
        self.sldr_blue.grid(row=3, column=1)

        # Create a canvas on which to draw a circle
        self.canvas = Canvas(window, width=200, height=200, bg="grey")
        self.canvas.grid(row=4, column=1, padx=10, pady=10)  # Important: this must not be included in the line above!

        # Create a circle on the canvas: corner = (50, 50), diameter = 150
        self.circle = self.canvas.create_oval(50, 50, 150, 150)

        window.mainloop()

    def slider_moved(self, value):
        red = format(self.sldr_red.get(), '02x')
        print("red =", red)

        green = format(self.sldr_green.get(), '02x')
        print("green =", green)

        blue = format(self.sldr_blue.get(), '02x')
        print("blue =", blue)

        # Convert the three hex values to a valid hex string
        mix = "#" + red + green + blue
        print("mix =", mix)

        # Configure the fill property of the circle on the canvas
        self.canvas.itemconfig(self.circle, fill=mix)


ColorMixer()
