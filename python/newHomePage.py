import Tkinter as tk
from Tkinter import *

class HomePage(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title = "Home Page"

        newAppButton = Button(master, text = "Add New Application", command = self.newApp)
        newAppButton.grid(row = 1, column = 1)

        searchButton = Button(master, text = "Search", command = self.search)
        searchButton.grid(row = 2, column = 1)

        adminButton = Button(master, text = "Admin Users", command = self.admin)
        #probably want to change the text on this button....
        adminButton.grid(row = 3, column = 1)

        closeButton = Button(master, text = "Close", command = self.close)
        closeButton.grid(row = 5, column = 1)

    def newApp(self):
        #goes to new Application Page
        self.newWindow = Tk()
        self.app = AddNewApp(self.newWindow)
        self.master.destroy()

        print "make a new app"

    def search(self):
        #goes to the search Page

        db = MySQLdb.connect(
            host = "localhost", 
            user="root", 
            passwd="yourMySqlPassword", 
            db="HERO" )
        curr = db.cursor()

        credentials = curr.execute("SELECT User_Type FROM User WHERE ID = %s AND Date_Submitted = %s;", (ID, Date,))

        #need to be able to get the user credentials
        if (credentials == 'Administrator' or credentials == 'Manager'):
            self.newWindow = Tk()
            self.app = searchPage(self.newWindow)
            self.master.destroy()
        else:
            "Sorry, you do not have the needed credentials for this command."

        curr.close()
        db.close()

    def admin(self):
        #goes to admin the Users

        db = MySQLdb.connect(
            host = "localhost", 
            user="root", 
            passwd="yourMySqlPassword", 
            db="HERO" )
        curr = db.cursor()

        credentials = curr.execute("SELECT User_Type FROM User WHERE ID = %s AND Date_Submitted = %s;", (ID, Date,))

        if (credentials == 'Administrator'):
            self.newWindow = Tk()
            self.app = adminPage(self.newWindow)
            self.master.destroy()
        else:
            "Sorry, you do not have the needed credentials for this command."

        curr.close()
        db.close()

    def close(self):
        #deletes the Page
        self.master.destroy()

master = Tk()
my_gui = HomePage(master)
master.mainloop()