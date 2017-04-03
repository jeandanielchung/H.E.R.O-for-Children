import Tkinter as tk
from Tkinter import *

class SearchPage:
    def __init__(self, master):
        self.master = master
        master.title("Search Page")

        labelWelcome = Label(master, text = "Pick Criteria to Search For")
        labelWelcome.grid(row = 0, column = 0) #might want to reformat

        allergiesButton = Button(master, text = "Allergies", command = self.allergies)
        allergiesButton.grid(row = 1, column = 0)

        closeButton = Button(master, text = "Close", command = self.quit)
        closeButton.grid(row = 2, column = 0)

    def quit(self):
        #deletes the page
        self.master.destroy()

    def allergies(self):
        print "trying to find allergies"