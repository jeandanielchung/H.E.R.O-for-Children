import Tkinter as tk
from Tkinter import *

class AddNewApp(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title = "Add a New Application"


        """Pull in a request from the database 
        about the programs that are offered
        and then add them to a list and pull them into the programList"""

        programList = ['none', 'program1', 'program2']
        programs = StringVar(master)
        programs.set(programList[0])
        dropdownProgram = OptionMenu(master, programs, *programList)
        dropdownProgram.grid(row = 0, column = 3)

        labelDate = Label(master, text = "Date Submitted (YYYY/MM/DD)")
        labelDate.grid(row = 1, column = 3)

        entryDate = Entry(master, bd = 3)
        entryDate.grid(row = 1, column = 4)
        
        returningTxt = Label(master, text = "Returning Child?")
        returningTxt.grid(row = 2, column = 3)

        v = StringVar()
        returningInq = Radiobutton(master, text="Yes", variable=v, value=1)
        returningInq.grid(row = 2,column = 4)

        returningInq = Radiobutton(master, text="No", variable=v, value=1)
        returningInq.grid(row = 2,column = 5)


        createButton = Button(master, text = "Create", command = self.create)
        createButton.grid(row = 3, column = 3)

        closeButton = Button(master, text = "Back", command = self.close)
        closeButton.grid(row  = 0, column = 0)


    def create(self):
        #send to create page
        print "app created"

    def close(self):
        #closes pages
        self.master.destroy()

master = Tk()
my_gui = AddNewApp(master)
master.mainloop()