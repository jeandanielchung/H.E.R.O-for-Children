from Tkinter import *

class addUser:
    def __init__(self, master):

        self.name = Label(master, text="Name").grid(row=0)
        self.entry1 = Entry(master).grid(row=0, column=1)

        self.username = Label(master, text="Username").grid(row=1)
        self.entry2 = Entry(master).grid(row=1, column=1)

        self.password = Label(master, text="Password").grid(row=2)
        self.entry3 = Entry(master).grid(row=2, column=1)

        self.level = Label(master, text="Label").grid(row=3)
        self.variable = StringVar(master)
        self.variable.set("Options")
        self.menu = OptionMenu(master, self.variable, "Manager", "Admin").grid(row=3, column=1)

        self.add = Button(master, text="ADD").grid(row=5, column=3)

master = Tk()
addUserPage = addUser(master)
master.mainloop()

