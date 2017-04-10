import MySQLdb
from Tkinter import *

class ProfilePage:
    def __init__(self, master):
        # Connect to database
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="HERO")
        curr = db.cursor()

        # id and date
        id = 1
        date = '2016-11-24'

        self.frame = Frame(master)
        self.frame.pack()

        self.back = Button(self.frame, text="Back").grid(row=0, column=0)
        self.delete = Button(self.frame, text="Delete").grid(row=0, column=10)

        curr.execute("SELECT Name_First From Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text=val, font="Arial 12 underline").grid(row=1, column=3)
        else:
            label = Label(self.ChildInfoSectionframe, text="Not found").grid(row=1, column=3)

        #self.name = Label(self.frame, text="First Name", font="Arial 12 underline").grid(row=1, column=3)

        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text=val, font="Arial 12 underline").grid(row=1, column=4)
         else:
            label = Label(self.ChildInfoSectionframe, text="Not found").grid(row=1, column=4)

        #self.name = Label(self.frame, text="Last Name", font="Arial 12 underline").grid(row=1, column=4)

        self.programs = Label(self.frame, text="PROGRAMS").grid(row=3, column=3)
        self.years = Label(self.frame, text="YEARS").grid(row=3, column=4)

        # As many detail buttons as needed
        self.details = Button(self.frame, text="See Details").grid(row=4, column=5)
        self.details = Button(self.frame, text="See Details").grid(row=5, column=5)
        self.details = Button(self.frame, text="See Details").grid(row=6, column=5)

master = Tk()
addUserPage = ProfilePage(master)
master.mainloop()
