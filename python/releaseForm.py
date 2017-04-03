import Tkinter as tk
from Tkinter import *
#import homePage
#import searchResultsPage

class DemographicPage(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title("Demographic Page Search")


        """Entries for criteria"""
        label1 = Label(master, text = "this label1")
        label1.grid(row = 0, column = 0)

        entry1 = Entry(master, bd = 5)
        entry1.grid(row = 0, column = 1)

        label2 = Label(master, text = "this label2")
        label2.grid(row = 1, column = 0)

        entry2 = Entry(master, bd = 5)
        entry2.grid(row = 1, column = 1)

        label3 = Label(master, text = "this label3")
        label3.grid(row = 2, column = 0)

        entry3 = Entry(master, bd = 5)
        entry3.grid(row = 2, column = 1)

        label4 = Label(master, text = "this label4")
        label4.grid(row = 3, column = 0)

        entry4 = Entry(master, bd = 5)
        entry4.grid(row = 3, column = 1)

        label5 = Label(master, text = "this label5")
        label5.grid(row = 4, column = 0)

        entry5 = Entry(master, bd = 5)
        entry5.grid(row = 4, column = 1)

        label6 = Label(master, text = "this label6")
        label6.grid(row = 5, column = 0)

        entry6 = Entry(master, bd = 5)
        entry6.grid(row = 5, column = 1)


        """Buttons for moving pages"""
        self.searchButton = Button(master, text = "Search for these Values", command = lambda: self.search(entry1.get(), entry2.get()))
        self.searchButton.grid(row = 6, column = 0)

        homeButton = Button(master, text = "Back to Home", command = self.backToHome)
        homeButton.grid(row = 6, column = 1)

        closeButton = Button(master, text = "Close", command = self.closeWindow)
        closeButton.grid(row = 6, column = 2)



    def search(self, criteria1, criteria2):
        """Get the criteria passed in and see what needs to be filtered
        will convert this to an SQL command that will retrieve a table and then 
        call the function for searchResultsPage"""

        print "searched"

    def backToHome(self):
        print "homePage"

    def closeWindow(self):
        self.master.destroy()


master = Tk()
my_gui = DemographicPage(master)
master.mainloop()


