import Tkinter as tk
from Tkinter import *
import searchPage

class HomePage(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title = "Home Page"

        labelSearch = Label(master, text = "Search by Name")
        labelSearch.grid(row = 0, column = 0) #probably want to reformat this

        entrySearch = Entry(master, bd =  3)
        entrySearch.grid(row = 0, column = 1)


        """Lists that can be used in dropdowns"""
        programList = ['none', 'program1', 'program2']
        yearList = ['none', "2017", "2016", "2015"]
        categoriesList = ['none', 'Demographic', 'Emergency Contact Info', 'Insurance', 'Medical Provider',
         'Medical Info', 'Allergies', 'Diet Needs', 'General Physical Health', 'Psych/Behavioral Info', 'Medications']




        labelProgram = Label(master, text = "Program")
        labelProgram.grid(row = 1, column = 0)

        programs = StringVar(master)
        programs.set(programList[0])
        dropdownProgram = OptionMenu(master, programs, *programList)
        dropdownProgram.grid(row = 1, column = 1)  #want to have a dropdowm of the potential programs that they can select from

        labelYear = Label(master, text = "Year")
        labelYear.grid(row = 2, column = 0) 

        years = StringVar(master)
        years.set(yearList[0])
        dropdownYear = OptionMenu(master, years, *yearList) 
        dropdownYear.grid(row = 2, column = 1) # want to have a dropdown for the years that they can search from

        labelCategory = Label(master, text = "Category")
        labelCategory.grid(row = 3, column = 0) 

        categories = StringVar(master)
        categories.set(categoriesList[0])
        dropdownCategory = OptionMenu(master, categories, *categoriesList)
        dropdownCategory.grid(row = 3, column = 1) # want to have a dropdown of the categories that they can choose to select from
        # also need to figure out what exactly all the categories are
        # that should be present in the dropdown

        searchButton = Button(master, text = "Search by Criteria", command = lambda: self.search(entrySearch.get(), programs.get(), years.get(), categories.get()))
        searchButton.grid(row = 4, column = 0)

        closeButton = Button(master, text = "Close", command = self.quit)
        closeButton.grid(row = 4, column = 1)

        newProfileButton = Button(master, text = "New Profile", command = self.newProfile)
        newProfileButton.grid(row = 4, column = 2)

    def newProfile(self):
        self.newWindow = createProfile.CreateProfile(self)
        #self.app = newProfile(self.newWindow)
        self.master.destroy()

    def search(self, name, program, year, category):
        if name == "":
            name = "Jeremy"
        print name
        print program
        print year
        print category

        #self.newWindow = searchPage.SearchPage(self)
        #self.app = SearchPage(self.newWindow)
        #self.master.destroy() #should destroy the home page on search call


    def quit(self):
        #deletes the page
        self.master.destroy()


master = Tk()
my_gui = HomePage(master)
master.mainloop()



