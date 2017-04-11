from Tkinter import *
import MySQLdb


class NewAppReturningPage:
        def __init__(self, master):
                self.master = master
                master.title("Returning Child")
                #5 columns at least 3 rows
                idLabel = Label(master, text = "ID")
                idLabel.grid(row = 2, column = 0)

                global idEntry
                idEntry = Entry(master, bd =3)
                idEntry.grid(row = 2, column = 1)

                divider = Label(master, text = "Or", font= "Verdana 10 underline")
                divider.grid(row = 3, column = 1)

                programLabel = Label(master, text = "Program")
                programLabel.grid(row = 0, column = 3)

                programList = ['none', 'Child Application', 'Camper Application']
                global programs
                programs = StringVar()
                programs.set(programList[0])
                dropdownProgram = OptionMenu(master, programs, *programList)
                dropdownProgram.grid(row = 0, column = 4)
               
                nameLabel = Label(master, text = "First Name")
                nameLabel.grid(row = 4, column = 0)

                
                global nameEntry
                nameEntry = Entry(master,bd = 3)
                nameEntry.grid(row = 4, column = 1)

                name2Label = Label(master, text = "Last Name")
                name2Label.grid(row = 5, column = 0)

                global name2Entry
                name2Entry = Entry(master,bd = 3)
                name2Entry.grid(row = 5, column = 1)

                bdLabel = Label(master, text = "Birthday (YYYY-MM-DD)")
                bdLabel.grid(row = 6, column = 0)

                global bdEntry
                bdEntry = Entry(master, bd = 3)
                bdEntry.grid(row = 6, column = 1)

                continueButton = Button(master, text = "Continue", command = self.Continue)
                continueButton.grid(row = 7, column = 3)

                self.back = Button(master, text = "Back", command = self.closeWindow)
                self.back.grid(row = 0, column = 0)

        def Continue(self):
                db = MySQLdb.connect(
                        host = "localhost",
                        user="root",
                        passwd="Mr10371!",
                        db="HERO" )
                curr = db.cursor()
                program = programs.get()
                ID = idEntry.get()
                firstName = nameEntry.get()
                lastName = name2Entry.get()
                bd = bdEntry.get()
                print(program,ID,firstName,lastName,bd)

                if firstName != '' and lastName != '' and ID == '' and bd != '': # checks if the filled name and bd fields and left ID blank
                        #select data if from child
                        if program == 'Child Application':
                                curr.execute("SELECT * FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND Birthday = %s;",(firstName,lastName,bd))
                                data = curr.fetchall()[0][0]
                                print data #how to print the data selected
                        #select data if from camper
                        elif program == 'Camper Application':
                                curr.execute("SELECT * FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s;",(firstName,lastName,bd))
                                data = curr.fetchall()[0][0]
                                print data #how to print the data selected
        def closeWindow(self):
                self.master.destroy()

master = Tk()
my_gui = NewAppReturningPage(master)
master.mainloop()
