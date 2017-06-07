from Tkinter import *
import MySQLdb
import tkMessageBox


    def NewAppReturningPage(self, newProgram, entryDate):

        #TODO: adjust
        self.master = master
        master.title("Returning Child")


        #5 columns at least 3 rows
        idLabel = Label(master, text = "ID")
        idLabel.grid(row = 2, column = 0)

        idEntry = Entry(master, bd =3)
        idEntry.grid(row = 2, column = 1)

        divider = Label(master, text = "Or", font= "Verdana 10 underline")
        divider.grid(row = 3, column = 1)

        programLabel = Label(master, text = "Program Previously Enrolled In: ")
        programLabel.grid(row = 0, column = 3)

        programList = ['none', 'Child Application', 'Camper Application']
        programs = StringVar()
        programs.set(programList[0])
        dropdownProgram = OptionMenu(master, programs, *programList)
        dropdownProgram.grid(row = 0, column = 4)

        nameLabel = Label(master, text = "First Name")
        nameLabel.grid(row = 4, column = 0)

        nameEntry = Entry(master,bd = 3)
        nameEntry.grid(row = 4, column = 1)

        name2Label = Label(master, text = "Last Name")
        name2Label.grid(row = 5, column = 0)

        name2Entry = Entry(master,bd = 3)
        name2Entry.grid(row = 5, column = 1)

        bdLabel = Label(master, text = "Birthday (YYYY-MM-DD)")
        bdLabel.grid(row = 6, column = 0)

        bdEntry = Entry(master, bd = 3)
        bdEntry.grid(row = 6, column = 1)

        continueButton = Button(master, text = "Continue", command = lambda:self.Continue(idEntry, programs, nameEntry, name2Entry, bdEntry, newProgram, entryDate))
        continueButton.grid(row = 7, column = 3)

        back = Button(master, text = "Back")
            #, command = self.closeWindow)
        back.grid(row = 0, column = 0)

    def Continue(self, idEntry, programs, nameEntry, name2Entry, bdEntry, newProgram, entryDate):

        program = programs.get()
        ID = idEntry.get()
        firstName = nameEntry.get()
        lastName = name2Entry.get()
        bd = bdEntry.get()

       #Database Connection
        db = self.connect()
        curr = db.cursor()

        if program == 'Child Application':

            #FN LN  BD  ID
            if firstName is not '' and lastName is not '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND Birthday = %s AND ID = %s;",(firstName,lastName,bd,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)
            
            #FN! LN  BD  ID
            elif firstName is '' and lastName is not '' and bd is not '' and ID is not '':
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND Birthday = %s AND ID = %s;",(firstName,lastName,bd,ID,))                
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)

            #FN LN! BD  ID
            elif firstName is not '' and lastName is '' and bd is not '' and ID is not '':
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Birthday = %s AND ID = %s;",(firstName,bd,ID,))                
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)

            #FN! LN! BD  ID
            elif firstName is '' and lastName is '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Birthday = %s AND ID = %s;",(bd,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)

            #FN LN  BD! ID
            elif firstName is not '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND ID = %s;",(firstName,lastName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)

            #FN! LN  BD! ID
            elif firstName is '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND ID = %s;",(lastName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)

            #FN LN! BD! ID
            elif firstName is not '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND ID = %s;",(firstName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)

            #FN! LN! BD! ID
            elif firstName is '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE ID = %s;",(ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)

            #FN LN  BD  ID!
            elif firstName is not '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND Birthday = %s;",(firstName,lastName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)
    
            #FN! LN  BD  ID!
            if firstName is '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND Birthday = %s;",(lastName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)

            #FN LN! BD  ID!
            elif firstName is not '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Birthday = %s;",(firstName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)
    
            #FN! LN! BD  ID!
            elif firstName is '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Birthday = %s;",(bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)
    
            #FN LN  BD! ID!
            elif firstName is not '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s;",(firstName,lastName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)
    
            #FN! LN  BD! ID!
            elif firstName is '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s;",(lastName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)
    
            #FN LN! BD! ID!
            elif firstName is not '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s;",(firstName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)
    
            #FN! LN! BD! ID!
            elif firstName is '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information;")
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data, None, newProgram, entryDate)
    
        #select data if from camper
        elif program == 'Camper Application':

           #FN LN  BD  ID
            if firstName is not '' and lastName is not '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,lastName,bd,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)
            
            #FN! LN  BD  ID
            elif firstName is '' and lastName is not '' and bd is not '' and ID is not '':
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,lastName,bd,ID,))                
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)

            
            #FN LN! BD  ID
            elif firstName is not '' and lastName is '' and bd is not '' and ID is not '':
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,bd,ID,))                
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)


            #FN! LN! BD  ID
            elif firstName is '' and lastName is '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Date_Of_Birth = %s AND ID = %s;",(bd,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)

            #FN LN  BD! ID
            elif firstName is not '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND ID = %s;",(firstName,lastName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)

            #FN! LN  BD! ID
            elif firstName is '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND ID = %s;",(lastName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)

            #FN LN! BD! ID
            elif firstName is not '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND ID = %s;",(firstName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)

            #FN! LN! BD! ID
            elif firstName is '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE ID = %s;",(ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)

            #FN LN  BD  ID!
            elif firstName is not '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s;",(firstName,lastName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)
    
            #FN! LN  BD  ID!
            if firstName is '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND Date_Of_Birth = %s;",(lastName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)

            #FN LN! BD  ID!
            elif firstName is not '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Date_Of_Birth = %s;",(firstName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)
    
            #FN! LN! BD  ID!
            elif firstName is '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Date_Of_Birth = %s;",(bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)
    
            #FN LN  BD! ID!
            elif firstName is not '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s;",(firstName,lastName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)
    
            #FN! LN  BD! ID!
            elif firstName is '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s;",(lastName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)
    
            #FN LN! BD! ID!
            elif firstName is not '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s;",(firstName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)
    
            #FN! LN! BD! ID!
            elif firstName is '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information;")
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(None, data, newProgram, entryDate)

        #No program selected
        else:

            #FN LN  BD  ID
            if firstName is not '' and lastName is not '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND Birthday = %s AND ID = %s;",(firstName,lastName,bd,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,lastName,bd,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN! LN  BD  ID
            elif firstName is '' and lastName is not '' and bd is not '' and ID is not '':
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND Birthday = %s AND ID = %s;",(firstName,lastName,bd,ID,))                
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,lastName,bd,ID,))                
                data2 = curr.fetchall()

                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            
            #FN LN! BD  ID
            elif firstName is not '' and lastName is '' and bd is not '' and ID is not '':
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Birthday = %s AND ID = %s;",(firstName,bd,ID,))                
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,bd,ID,))                
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            

            #FN! LN! BD  ID
            elif firstName is '' and lastName is '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Birthday = %s AND ID = %s;",(bd,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Date_Of_Birth = %s AND ID = %s;",(bd,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN LN  BD! ID
            elif firstName is not '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND ID = %s;",(firstName,lastName,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND ID = %s;",(firstName,lastName,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN! LN  BD! ID
            elif firstName is '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND ID = %s;",(lastName,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND ID = %s;",(lastName,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN LN! BD! ID
            elif firstName is not '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND ID = %s;",(firstName,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND ID = %s;",(firstName,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN! LN! BD! ID
            elif firstName is '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE ID = %s;",(ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE ID = %s;",(ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN LN  BD  ID!
            elif firstName is not '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND Birthday = %s;",(firstName,lastName,bd,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s;",(firstName,lastName,bd,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN! LN  BD  ID!
            if firstName is '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND Birthday = %s;",(lastName,bd,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND Date_Of_Birth = %s;",(lastName,bd,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN LN! BD  ID!
            elif firstName is not '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Birthday = %s;",(firstName,bd,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Date_Of_Birth = %s;",(firstName,bd,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN! LN! BD  ID!
            elif firstName is '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Birthday = %s;",(bd,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Date_Of_Birth = %s;",(bd,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN LN  BD! ID!
            elif firstName is not '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s;",(firstName,lastName,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s;",(firstName,lastName,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN! LN  BD! ID!
            elif firstName is '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s;",(lastName,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s;",(lastName,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN LN! BD! ID!
            elif firstName is not '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s;",(firstName,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s;",(firstName,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)
            
            #FN! LN! BD! ID!
            elif firstName is '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information;")
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information;")
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntry(data1, data2, newProgram, entryDate)




master = Tk()
my_gui = NewAppReturningPage(master)
master.mainloop()
