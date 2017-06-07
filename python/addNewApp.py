import Tkinter as tk
from Tkinter import *
import MySQLdb
import tkMessageBox

    def AddNewAppPage(self):

        self.AddNewAppPageRoot = Toplevel()
        root = self.AddNewAppPageRoot

        if self.PrevPage is 'HomePage':
            self.HomePageRoot.withdraw()
        self.PrevPage = 'AddNewAppPage'

        #get this program list from the DB
        programList = ['none', 'Child Application', 'Camper Application']
        programs = StringVar()
        programs.set(programList[0])
        dropdownProgram = OptionMenu(master, programs, *programList)
        dropdownProgram.grid(row = 0, column = 3)


        labelDate = Label(master, text = "Date Submitted (YYYY-MM-DD)")
        labelDate.grid(row = 1, column = 3)

        entryDate = Entry(master, bd = 3)
        entryDate.grid(row = 1, column = 4)

        returningTxt = Label(master, text = "Returning Child?")
        returningTxt.grid(row = 2, column = 3)

        v = StringVar()
        returningInq = Radiobutton(master, text="Yes", variable=v, value=1)
        returningInq.grid(row = 2,column = 4)

        returningInq = Radiobutton(master, text="No", variable=v, value=2)
        returningInq.grid(row = 2,column = 5)

        v.set(0)

        createButton = Button(master, text = "Create", command = lambda:self.createNewApp(programs, entryDate, v))
        createButton.grid(row = 3, column = 3)

        backButton = Button(master, text = "Back", command = lambda:self.HomePage())
        backButton.grid(row  = 0, column = 0)


    def createNewApp(self, programs, entryDate, v):
        #send to create page
        #add an application form to the DB

       #Database Connection
        db = self.connect()
        curr = db.cursor()

        if v.get() == '2':             # If they are not a returning child, add them and date submitted into Child()
            curr.execute("INSERT INTO Child() VALUES ();") #is this actually auto incrementing
            db.commit()

            #get variables from user input
            curr.execute("SELECT MAX(ID) FROM Child;")
            ID = curr.fetchall()[0][0]
            Date = entryDate.get()
            program =  programs.get()

            #Add the ID and Date_Submitted into the program specified by the user
            #Needs a check for valid date format
            if program == 'Child Application':
                curr.execute("INSERT INTO Child_Application(ID, Date_Submitted) VALUES (%s,%s);",(ID,Date))
                db.commit()
            elif program == "Camper Application":
                curr.execute("INSERT INTO Camp_Application(ID,Date_Submitted) VALUES(%s,%s);",(ID,Date))
                db.commit()
            else:
                tkMessageBox.showinfo("Add a New Applicaiton","Please select a program")


        elif v.get() == '1':       #if they are a returning child, send them to newAppReturning.py
            print '' #place holder... needs to go to newAppReturning.py

        else:         #user failed to select Yes/No for returning Child
            tkMessageBox.showinfo("Add a New Application","Please select Yes or No for 'Returning User?'")

        curr.close()
        db.close()

master = Tk()
my_gui = AddNewAppPage(master)
master.mainloop()
