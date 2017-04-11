#import MySQLdb
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

        # Back button will take you to previous page
        self.back = Button(self.frame, text="Back").grid(row=0, column=0)
        # Delete will permanently remove child from database
        self.delete = Button(self.frame, text="Delete", command=self.back).grid(row=0, column=10)

        '''curr.execute("SELECT Name_First From Childs_Information WHERE ID MEDIUMINT = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text=val, font="Arial 12 underline").grid(row=1, column=3)
        else:
            label = Label(self.ChildInfoSectionframe, text="Not found").grid(row=1, column=3)

        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID MEDIUMINT = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text=val, font="Arial 12 underline").grid(row=1, column=4)
        else:
            label = Label(self.ChildInfoSectionframe, text="Not found").grid(row=1, column=4)'''

        self.name = Label(self.frame, text="First Name", font="Arial 12 underline").grid(row=1, column=3)
        self.name = Label(self.frame, text="Last Name", font="Arial 12 underline").grid(row=1, column=4)
        self.programs = Label(self.frame, text="PROGRAMS").grid(row=3, column=3)
        self.years = Label(self.frame, text="YEARS").grid(row=3, column=4)

        # Add as many detail buttons as needed
        # Details button will take you to another page
        self.details = Button(self.frame, text="See Details").grid(row=4, column=5)
        self.details = Button(self.frame, text="See Details").grid(row=5, column=5)
        self.details = Button(self.frame, text="See Details").grid(row=6, column=5)

        #curr.close()
        #db.close()
    def back(self):
        self.destroy();

master = Tk()
addUserPage = ProfilePage(master)
master.mainloop()
