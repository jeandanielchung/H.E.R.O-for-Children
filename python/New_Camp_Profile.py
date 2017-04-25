from Tkinter import *
import MySQLdb

class CampProfile:
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()

        # Database Connection
        #db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        #curr = db.cursor()

        backButton = Button(self.frame, text="Back").grid(row=0, column=0)
        label = Label(self.frame, text="First Name:").grid(row=1, column=0)
        label = Label(self.frame, text="Last Name:").grid(row=2, column=0)

master = Tk()
addUserPage = CampProfile(master)
master.mainloop()
