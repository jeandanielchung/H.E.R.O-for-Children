import Tkinter as tk
from Tkinter import *

import searchResultsPage

class ViewProfile(tk.Tk):
    def __init__(self, master, profileName, searchQuery):
        self.master = master
        master.title("Profile")

        """implement a my sql query here with the profile profileName
        this should return the data for the child in totality"""



        self.previousButton = Button(master, text = "Back to Results", command = lambda: self.previous(searchQuery))
        #how to format this with the results display???

        self.closeButton = Button(master, text = "Close", self.closeWindow)
        #how to format

    def previous(self, searchQuery):
        self.newWindow = searchResultsPage.SearchResultsPage(self, searchQuery)
        self.master.destroy()
        #we want to call back the previous query that we made and delete this window

    def closeWindow(self):
        self.master.destroy()