from Tkinter import *

class HomePage:
    def __init__(self, master):
        self.master = master
        master.title = "Home Page"

        labelSearch = Label(master, text = "Search by Name")
        labelSearch.grid(row = 0, column = 0) #probably want to reformat this

        entrySearch = Entry(master, bd =  3)
        entrySearch.grid(row = 0, column = 1)

        searchButton = Button(master, text = "Search by Criteria", command = self.search)
        searchButton.grid(row = 1, column = 0)

        closeButton = Button(master, text = "Close", command = self.quit)
        closeButton.grid(row = 1, column = 1)

    def search(self):
        self.newWindow = Tk()
        self.app = SearchPage(self.newWindow)
        self.master.destroy() #should destroy the home page on search call


    def quit(self):
        #deletes the page
        self.master.destroy()

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


master = Tk()
my_gui = HomePage(master)
master.mainloop()