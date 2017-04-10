import MySQLdb
from Tkinter import *

class AddUser:
    def __init__(self, master):

        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="yourMySQLPassword",
            db="HERO")

        curr = db.cursor()

        self.frame = Frame(master)
        self.frame.pack()

        self.name = Label(self.frame, text="Name").grid(row=1)
        self.entry1 = Entry(self.frame).grid(row=1, column=1)

        self.username = Label(self.frame, text="Username").grid(row=2)
        self.entry2 = Entry(self.frame).grid(row=2, column=1)

        self.password = Label(self.frame, text="Password").grid(row=3)
        self.entry3 = Entry(self.frame).grid(row=3, column=1)

        self.level = Label(self.frame, text="Type").grid(row=4)
        self.variable = StringVar(master)
        self.variable.set("Regular")
        self.menu = OptionMenu(self.frame, self.variable, "Regular", "Manager", "Admin").grid(row=4, column=1)

        self.add = Button(self.frame, text="Add User").grid(row=6, column=3)
        self.back = Button(self.frame, text="Go Back").grid(row=6, column=0)

        curr.close()
        db.close()

master = Tk()
addUserPage = AddUser(master)
master.mainloop()

