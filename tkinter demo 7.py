from tkinter import *

# Use radio buttons and check buttons to build an ordering menu


class OrderUp:

    def __init__(self):
        window = Tk()
        window.title("Welcome to Jimmy John's")

        Label(text="Order Menu").grid(row=0, column=1, columnspan=3)

        Label(text="Choose Your Meat  ").grid(row=1, column=1)

        self.meat = IntVar()  # variable for all meat choices

        rbtn_ham = Radiobutton(window, text="ham", variable=self.meat, command=self.choose_meat, value=1)
        rbtn_ham.grid(row=2, column=1, sticky=W)

        rbtn_turkey = Radiobutton(window, text="turkey", variable=self.meat, command=self.choose_meat, value=2)
        rbtn_turkey.grid(row=3, column=1, sticky=W)

        rbtn_roast_beef = Radiobutton(window, text="roast beef", variable=self.meat, command=self.choose_meat, value=3)
        rbtn_roast_beef.grid(row=4, column=1, sticky=W)

        Label(text="Choose Your Bread  ").grid(row=1, column=2)

        self.bread = IntVar()  # variable for all bread choices

        rbtn_ham = Radiobutton(window, text="white", variable=self.bread, command=self.choose_bread, value=1)
        rbtn_ham.grid(row=2, column=2, sticky=W)

        rbtn_turkey = Radiobutton(window, text="wheat", variable=self.bread, command=self.choose_bread, value=2)
        rbtn_turkey.grid(row=3, column=2, sticky=W)

        rbtn_roast_beef = Radiobutton(window, text="rye", variable=self.bread, command=self.choose_bread, value=3)
        rbtn_roast_beef.grid(row=4, column=2, sticky=W)

        Label(text="Choose Your Condiments  ").grid(row=1, column=3)

        self.mayo = IntVar()
        cbtn_mayo = Checkbutton(window, text="mayo", variable=self.mayo, command=self.choose_mayo)
        cbtn_mayo.grid(row=2, column=3, sticky=W)

        self.ketchup = IntVar()
        cbtn_ketchup = Checkbutton(window, text="ketchup", variable=self.ketchup, command=self.choose_ketchup)
        cbtn_ketchup.grid(row=3, column=3, sticky=W)

        self.mustard = IntVar()
        cbtn_mustard = Checkbutton(window, text="mustard", variable=self.mustard, command=self.choose_mustard)
        cbtn_mustard.grid(row=4, column=3, sticky=W)

        btn_order = Button(window, text="ORDER", command=self.place_order)
        btn_order.grid(row=5, column=1, columnspan=3)

        self.show_order = StringVar()
        self.lblOrder = Label(window, textvariable=self.show_order)
        self.lblOrder.grid(row=6, column=1, columnspan=3)
        self.show_order.set("Your order will appear here")

        window.mainloop()

    def choose_meat(self):
        print("meat =", self.meat.get())

    def choose_bread(self):
        print("bread =", self.bread.get())

    def choose_mayo(self):
        print("mayo =", self.mayo.get())

    def choose_ketchup(self):
        print("ketchup =", self.ketchup.get())

    def choose_mustard(self):
        print("mustard =", self.mustard.get())

    def place_order(self):

        if self.meat.get() == 1:
            choice1 = "ham"
        elif self.meat.get() == 2:
            choice1 = "turkey"
        elif self.meat.get() == 3:
            choice1 = "roast beef"
        else:
            choice1 = "no meat chosen"
        print("meat =", choice1)

        if self.bread.get() == 1:
            choice2 = "white"
        elif self.bread.get() == 2:
            choice2 = "wheat"
        elif self.bread.get() == 3:
            choice2 = "rye"
        else:
            choice2 = "no bread chosen"
        print("bread =", choice2)

        choice3 = ""
        if self.mayo.get() == 1:
            choice3 += " mayo,"

        if self.ketchup.get() == 1:
            choice3 += " ketchup,"

        if self.mustard.get() == 1:
            choice3 += " mustard,"

        if choice3 == "":
            order = "Ordering " + choice1 + " on " + choice2
        else:
            order = "Ordering " + choice1 + " on " + choice2 + " with" + choice3[:-1]

        print(order)

        self.show_order.set(order)


OrderUp()
