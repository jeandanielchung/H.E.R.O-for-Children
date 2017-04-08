from Tkinter import *

class ProfilePage:
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()

        self.back = Button(self.frame, text="Back").grid(row=0, column=0)
        # Child's first and last name will appear here
        self.delete = Button(self.frame, text="Delete").grid(row=0, column=10)
        # Child's first and last name will appear here
        self.name = Label(self.frame, text="First Name").grid(row=1, column=3)
        self.name = Label(self.frame, text="Last Name").grid(row=1, column=4)

        self.programs = Label(self.frame, text="PROGRAMS").grid(row=3, column=3)
        self.years = Label(self.frame, text="YEARS").grid(row=3, column=4)

        # As many detail buttons as needed
        self.details = Button(self.frame, text="See Details").grid(row=4, column=5)
        self.details = Button(self.frame, text="See Details").grid(row=5, column=5)
        self.details = Button(self.frame, text="See Details").grid(row=6, column=5)

master = Tk()
addUserPage = ProfilePage(master)
master.mainloop()
