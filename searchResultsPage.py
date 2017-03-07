import Tkinter as tk
from Tkinter import *

import searchPage
import viewProfile


class SearchResultsPage(tk.Tk):
    def __init__(self, master, searchQuery):
        self.master = master 
        master.title("Results") 
        #might want the title of the page to be changed based on query

        labelName = Label(master, text = "Name")
        labelName.grid(row = 0, column = 0)

        labelQuery = Label(master, text = "Criteria") 
        labelQuery.grid(row = 0, column = 1)
        # this might be inherent to the table, might take out
        # want to be able to modify the name of the column based on query
        # FIX ME 




        """want to have SQL command here to get the 
        table of info for the query that will get 
        passed in from the search page"""








        self.profileButton = Button(master, text = "View Selected Profile", command = lambda: self.profile("childName", searchQuery))
        #need to figure out how to get the actual value that is being search for
        #want to have a table eith a selection button for a profile to the side

        self.previousButton = Button(master, text = "Back to Search", command = self.previous)
        self.closeButton = Button(master, text = "Close", command = self.closeWindow)
        #we want to format this to the very bottom, after the grid is displayed
        # FIX ME


    def profile(self, profileName):
        self.newWindow = viewProfile.ViewProfile(self, profileName)
        #want to pass in a specific kid 
        self.master.destroy()



    def previous(self):
        self.newWindow = searchPage.SearchPage(self)
        self.master.destroy()
        #want to point back to the search page and delete this window

    def closeWindow(self):
        self.master.destroy()






