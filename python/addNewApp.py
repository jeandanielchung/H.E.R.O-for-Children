import Tkinter as tk
from Tkinter import *
import MySQLdb
import tkMessageBox

class AddNewApp(tk.Tk):
    def __init__(self, master):
        self.master = master
        master.title = "Add a New Application"


        """Pull in a request from the database 
        about the programs that are offered
        and then add them to a list and pull them into the programList"""


        #get this program list from the DB
        programList = ['none', 'Child Application', 'Camper Application']
        global programs
        programs = StringVar()
        programs.set(programList[0])
        dropdownProgram = OptionMenu(master, programs, *programList)
        dropdownProgram.grid(row = 0, column = 3)


        labelDate = Label(master, text = "Date Submitted (YYYY-MM-DD)")
        labelDate.grid(row = 1, column = 3)

        global entryDate
        entryDate = Entry(master, bd = 3)
        entryDate.grid(row = 1, column = 4)
        
        returningTxt = Label(master, text = "Returning Child?")
        returningTxt.grid(row = 2, column = 3)

        global v
        v = StringVar()
        returningInq = Radiobutton(master, text="Yes", variable=v, value=1)
        returningInq.grid(row = 2,column = 4)

        returningInq = Radiobutton(master, text="No", variable=v, value=2)
        returningInq.grid(row = 2,column = 5)

        v.set(0)

        createButton = Button(master, text = "Create", command = self.create)
        createButton.grid(row = 3, column = 3)

        closeButton = Button(master, text = "Back", command = self.close)
        closeButton.grid(row  = 0, column = 0)


    def create(self):
        #send to create page
        #add an application form to the DB
        
        db = MySQLdb.connect(
            host = "localhost", 
            user="root", 
            passwd="Darling", 
            db="HERO" )
        curr = db.cursor()

        
        if v.get() == '2':             # If they are not a returning child, add them and date submitted into Child()
            curr.execute("INSERT INTO Child() VALUES ();") #is this actually auto incrementing
            db.commit()

            #get variables from user input
            ID = curr.execute("SELECT MAX(ID) FROM Child;")
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

        print "app created"

        curr.close()
        db.close()

    def close(self):
        #closes pages
        self.master.destroy()

master = Tk()
my_gui = AddNewApp(master)
master.mainloop()
