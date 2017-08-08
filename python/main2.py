import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import tkMessageBox
import MySQLdb

#TODO: add in camp pages
#TODO: add exit buttons
#TODO: Fix edit so that none are global and it is passing params instead (see childInfo0)
#TODO: pass in proper params for id in adding to database
#TODO: edit child checkboxes make it "if var is not None" and then create UI (see edit camper app)
#TODO: figure out fixing if they use a contraction ex: doesn't
#TODO: add lables for "PARENT SECTION", "MEDICAL PROVIDOR SECTION", "HIV PROVIDOR SECTION"
#TODO: Handle feedback for data errors that's too long!! in edit child. ex: VARCHAR(30)

class Main():

    session = {}
    PrevPage = ''
    searchCriteria = {}
    prevSection = -1
    
    def __init__(self,root):
        self.root = root
        self.LoginPage()
        self.username = ""
        self.session['login'] = False

    def connect(self):
        try:
            db = MySQLdb.connect(
                host = "localhost",
                user="root",
                passwd = "Darling",
                db="HERO")
            return db
        except:
            tkMessageBox.showinfo("Error!","Check your internet connection.")

#******************************************************************************************************************************************************

    def LoginPage(self):

        self.root.withdraw()

        self.LoginPageRoot = Toplevel()
        root = self.LoginPageRoot

        if self.PrevPage is 'HomePage':
            self.HomePageRoot.withdraw()
        self.PrevPage = 'LoginPage'

        master = Frame(root)
        master.grid(row=0,column=0, columnspan=4)

        root.title("Login Page")

        self.session['login'] = False
        self.session['username'] = None
        self.session['credentials'] = None

        labelUsername = Label(master, text = "Username")
        labelUsername.grid(row = 1, column = 1)

        entryUsername = Entry(master, bd = 5)
        entryUsername.grid(row = 1, column = 2)

        labelPassword = Label(master, text = "Password")
        labelPassword.grid(row = 2, column = 1)

        entryPassword = Entry(master, bd = 5, show = "*")
        entryPassword.grid(row = 2, column = 2)

        loginButton = Button(master, text = "login", command = lambda: self.login(entryUsername.get(), entryPassword.get(),))
        loginButton.grid(row = 3, column = 2)

    def login(self, username, password):

       #Database Connection
        db = self.connect()
        curr = db.cursor()

        curr.execute("SELECT * FROM User WHERE Username = %s AND Password = SHA1(%s)", (username, password,))
        result = curr.fetchone()

        if result is not None: # if the result isn't None then there is a user/password combination match
            self.session['login'] = True
            self.session['username'] = username
            self.session['credentials'] = result[3]            
            
            curr.close()
            db.close()
            
            self.HomePage()
        else:
            tkMessageBox.showinfo("Login Page", "Either password or username was incorrect, try again")
            curr.close()
            db.close()

#******************************************************************************************************************************************************

    def HomePage(self):

        self.HomePageRoot = Toplevel()
        root = self.HomePageRoot
        if self.PrevPage is 'LoginPage':
            self.LoginPageRoot.withdraw()
        elif self.PrevPage is 'AdminUserPage':
            self.AdminUserPageRoot.withdraw()
        elif self.PrevPage is 'SearchPage':
            self.SearchPageRoot.withdraw()
        elif self.PrevPage is 'AddNewAppPage':
            self.AddNewAppPageRoot.withdraw()
        self.PrevPage = 'HomePage'

        root.title("Home Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        username = self.session['username']
        credentials = self.session['credentials']
        
        logoutButton = Button(master, text = "Log Out", command=lambda: self.LoginPage())
        logoutButton.grid(row = 0, column = 0)

        newAppButton = Button(master, text = "Add New Application", command=lambda: self.AddNewAppPage())
        newAppButton.grid(row = 1, column = 3, padx = 185, pady = 10)

        if (credentials == 'Administrator' or credentials == 'Manager'):
            searchButton = Button(master, text = "Search",  command=lambda: self.SearchPage())
            searchButton.grid(row = 2, column = 3, padx = 185, pady = 10)

        if (credentials == 'Administrator'):
            adminButton = Button(master, text = "Administrate Users", command=lambda: self.AdminUserPage())
            adminButton.grid(row = 3, column = 3, padx = 185, pady = 10)

#******************************************************************************************************************************************************

    def AddNewAppPage(self):

        self.AddNewAppPageRoot = Toplevel()
        root = self.AddNewAppPageRoot

        if self.PrevPage is 'HomePage':
            self.HomePageRoot.withdraw()
        if self.PrevPage is 'NewAppReturningPage':
            self.NewAppReturningPageRoot.withdraw()
        if self.PrevPage is 'NewChildProfilePage':
            self.NewChildProfilePageRoot.withdraw()
        self.PrevPage = 'AddNewAppPage'

        root.title("New App Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        #get this program list from the DB
        programLabel = Label(master, text = "Program: ")
        programLabel.grid(row = 0, column = 3, sticky = 'e')
        programList = ['none', 'Child Application', 'Camper Application']
        programs = StringVar()
        programs.set(programList[0])
        dropdownProgram = OptionMenu(master, programs, *programList)
        dropdownProgram.grid(row = 0, column = 4, sticky = 'w')


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
        createButton.grid(row = 4, column = 4, sticky = 'w')

        backButton = Button(master, text = "Back", command = lambda:self.HomePage())
        backButton.grid(row  = 0, column = 0)

    def createNewApp(self, programs, entryDate, v):
        #send to create page
        #add an application form to the DB

        Date = entryDate.get()
        program =  programs.get()
        
        if Date is '' or program is '':
            tkMessageBox.showinfo("Add a New Applicaiton","Please fill in program and date")

        elif v.get() == '2':             # If they are not a returning child, add them and date submitted into Child()
            #Database Connection
            db = self.connect()
            curr = db.cursor()

            curr.execute("INSERT INTO Child() VALUES ();") #is this actually auto incrementing
            db.commit()

            #get variables from user input
            curr.execute("SELECT MAX(ID) FROM Child;")
            ID = curr.fetchall()[0][0]

            #Add the ID and Date_Submitted into the program specified by the user
            #Needs a check for valid date format
            if program == 'Child Application':
                curr.execute("INSERT INTO Child_Application(ID, Date_Submitted) VALUES (%s,%s);",(ID,Date,))
                db.commit()
                curr.close()
                db.close()

                self.NewChildProfilePage(ID, Date)

            elif program == "Camper Application":
                curr.execute("INSERT INTO Camp_Application(ID,Date_Submitted) VALUES(%s,%s);",(ID,Date,))
                db.commit()
                curr.close()
                db.close()

                #TODO: link to NewCampApp(ID, Date)

        elif v.get() == '1':       #if they are a returning child, send them to newAppReturning.py
            self.NewAppReturningPage(program, Date)

        else:         #user failed to select Yes/No for returning Child
            tkMessageBox.showinfo("Add a New Application","Please select Yes or No for 'Returning User?'")

#******************************************************************************************************************************************************

    def NewAppReturningPage(self, newProgram, entryDate):

        self.NewAppReturningPageRoot = Toplevel()
        root = self.NewAppReturningPageRoot

        if self.PrevPage is 'AddNewAppPage':
            self.AddNewAppPageRoot.withdraw()
        if self.PrevPage is 'nameBirthEntryPage':
            self.nameBirthEntryPageRoot.withdraw()
        self.PrevPage = 'NewAppReturningPage'

        root.title("New App Returning Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

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

        back = Button(master, text = "Back", command = lambda:self.AddNewAppPage())
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
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)
            
            #FN! LN  BD  ID
            elif firstName is '' and lastName is not '' and bd is not '' and ID is not '':
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND Birthday = %s AND ID = %s;",(firstName,lastName,bd,ID,))                
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)

            #FN LN! BD  ID
            elif firstName is not '' and lastName is '' and bd is not '' and ID is not '':
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Birthday = %s AND ID = %s;",(firstName,bd,ID,))                
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)

            #FN! LN! BD  ID
            elif firstName is '' and lastName is '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Birthday = %s AND ID = %s;",(bd,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)

            #FN LN  BD! ID
            elif firstName is not '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND ID = %s;",(firstName,lastName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)

            #FN! LN  BD! ID
            elif firstName is '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND ID = %s;",(lastName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)

            #FN LN! BD! ID
            elif firstName is not '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND ID = %s;",(firstName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)

            #FN! LN! BD! ID
            elif firstName is '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE ID = %s;",(ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)

            #FN LN  BD  ID!
            elif firstName is not '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND Birthday = %s;",(firstName,lastName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)
    
            #FN! LN  BD  ID!
            if firstName is '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND Birthday = %s;",(lastName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)

            #FN LN! BD  ID!
            elif firstName is not '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Birthday = %s;",(firstName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)
    
            #FN! LN! BD  ID!
            elif firstName is '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Birthday = %s;",(bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)
    
            #FN LN  BD! ID!
            elif firstName is not '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s;",(firstName,lastName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)
    
            #FN! LN  BD! ID!
            elif firstName is '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s;",(lastName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)
    
            #FN LN! BD! ID!
            elif firstName is not '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s;",(firstName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)
    
            #FN! LN! BD! ID!
            elif firstName is '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information;")
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data, None, newProgram, entryDate)
    
        #select data if from camper
        elif program == 'Camper Application':

           #FN LN  BD  ID
            if firstName is not '' and lastName is not '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,lastName,bd,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)
            
            #FN! LN  BD  ID
            elif firstName is '' and lastName is not '' and bd is not '' and ID is not '':
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,lastName,bd,ID,))                
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)

            
            #FN LN! BD  ID
            elif firstName is not '' and lastName is '' and bd is not '' and ID is not '':
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,bd,ID,))                
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)


            #FN! LN! BD  ID
            elif firstName is '' and lastName is '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Date_Of_Birth = %s AND ID = %s;",(bd,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)

            #FN LN  BD! ID
            elif firstName is not '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND ID = %s;",(firstName,lastName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)

            #FN! LN  BD! ID
            elif firstName is '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND ID = %s;",(lastName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)

            #FN LN! BD! ID
            elif firstName is not '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND ID = %s;",(firstName,ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)

            #FN! LN! BD! ID
            elif firstName is '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE ID = %s;",(ID,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)

            #FN LN  BD  ID!
            elif firstName is not '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s;",(firstName,lastName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)
    
            #FN! LN  BD  ID!
            if firstName is '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND Date_Of_Birth = %s;",(lastName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)

            #FN LN! BD  ID!
            elif firstName is not '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Date_Of_Birth = %s;",(firstName,bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)
    
            #FN! LN! BD  ID!
            elif firstName is '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Date_Of_Birth = %s;",(bd,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)
    
            #FN LN  BD! ID!
            elif firstName is not '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s;",(firstName,lastName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)
    
            #FN! LN  BD! ID!
            elif firstName is '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s;",(lastName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)
    
            #FN LN! BD! ID!
            elif firstName is not '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s;",(firstName,))
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)
    
            #FN! LN! BD! ID!
            elif firstName is '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information;")
                data = curr.fetchall()
                if data == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(None, data, newProgram, entryDate)

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
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN! LN  BD  ID
            elif firstName is '' and lastName is not '' and bd is not '' and ID is not '':
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND Birthday = %s AND ID = %s;",(firstName,lastName,bd,ID,))                
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,lastName,bd,ID,))                
                data2 = curr.fetchall()

                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            
            #FN LN! BD  ID
            elif firstName is not '' and lastName is '' and bd is not '' and ID is not '':
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Birthday = %s AND ID = %s;",(firstName,bd,ID,))                
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Date_Of_Birth = %s AND ID = %s;",(firstName,bd,ID,))                
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            

            #FN! LN! BD  ID
            elif firstName is '' and lastName is '' and bd is not '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Birthday = %s AND ID = %s;",(bd,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Date_Of_Birth = %s AND ID = %s;",(bd,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN LN  BD! ID
            elif firstName is not '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND ID = %s;",(firstName,lastName,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND ID = %s;",(firstName,lastName,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN! LN  BD! ID
            elif firstName is '' and lastName is not '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND ID = %s;",(lastName,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND ID = %s;",(lastName,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN LN! BD! ID
            elif firstName is not '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND ID = %s;",(firstName,ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND ID = %s;",(firstName,ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN! LN! BD! ID
            elif firstName is '' and lastName is '' and bd is '' and ID is not '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE ID = %s;",(ID,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE ID = %s;",(ID,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN LN  BD  ID!
            elif firstName is not '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND Birthday = %s;",(firstName,lastName,bd,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s;",(firstName,lastName,bd,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN! LN  BD  ID!
            if firstName is '' and lastName is not '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s AND Birthday = %s;",(lastName,bd,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s AND Date_Of_Birth = %s;",(lastName,bd,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN LN! BD  ID!
            elif firstName is not '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Birthday = %s;",(firstName,bd,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Date_Of_Birth = %s;",(firstName,bd,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN! LN! BD  ID!
            elif firstName is '' and lastName is '' and bd is not '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Birthday = %s;",(bd,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Date_Of_Birth = %s;",(bd,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN LN  BD! ID!
            elif firstName is not '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s;",(firstName,lastName,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s;",(firstName,lastName,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN! LN  BD! ID!
            elif firstName is '' and lastName is not '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_Last = %s;",(lastName,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE Last_Name = %s;",(lastName,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN LN! BD! ID!
            elif firstName is not '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information WHERE Name_First = %s;",(firstName,))
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information WHERE First_Name = %s;",(firstName,))
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)
            
            #FN! LN! BD! ID!
            elif firstName is '' and lastName is '' and bd is '' and ID is '': # checks if the filled name and bd fields and left ID blank
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted),ID FROM Childs_Information;")
                data1 = curr.fetchall()

                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted),ID FROM Demographic_Information;")
                data2 = curr.fetchall()
                
                if data1 == () and data2 == ():
                    tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                else:
                    self.nameBirthEntryPage(data1, data2, newProgram, entryDate)

#******************************************************************************************************************************************************

    def nameBirthEntryPage(self, childNameDate, camperNameDate, newProgram, entryDate):
        
        self.nameBirthEntryPageRoot = Toplevel()
        root = self.nameBirthEntryPageRoot
        if self.PrevPage is 'NewAppReturningPage':
            self.NewAppReturningPageRoot.withdraw()
        self.PrevPage = 'nameBirthEntryPage'

        root.title("Find New Applicant Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)
        
        #5 columns at least 3 rows
        nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = 1, column = 0)

        progHead = Label(master, text = "Program", font= "Verdana 10 underline")
        progHead.grid(row = 1, column = 1)

        yearHead = Label(master, text = "Year", font= "Verdana 10 underline")
        yearHead.grid(row = 1, column = 2)

        backButton = Button(master, text = "Back", command = lambda:self.NewAppReturningPage(newProgram, entryDate))
        backButton.grid(row = 0, column = 0)


        for num in range(len(childNameDate)):
                name = Label(master, text = childNameDate[num][0]+' '+childNameDate[num][1])
                name.grid(row = 2 + num, column = 0)

                prog = Label(master, text = "Child Application")
                prog.grid(row = 2 + num, column = 1)

                year = Label(master, text = childNameDate[num][2])
                year.grid(row = 2 + num, column = 2)

                profBut = Button(master, text = "Select", command = lambda: self.NewChildProfilePage(childNameDate[num][3], entryDate))
                profBut.grid(row = 2 + num, column = 3)

        for num in range(len(camperNameDate)):
                name = Label(master, text = camperNameDate[num][0]+' '+camperNameDate[num][1])
                name.grid(row = 2 + num +len(childNameDate), column = 0)

                prog = Label(master, text = "Camper Application")
                prog.grid(row = 2 + num +len(childNameDate), column = 1)

                year = Label(master, text = camperNameDate[num][2])
                year.grid(row = 2 + num +len(childNameDate), column = 2)

                profBut = Button(master, text = "Select")
                #TODO: go to NewCampApp(id, entryDate), command = self.closeWindow), command = self.closeWindow)
                profBut.grid(row = 2 + num +len(childNameDate), column = 3)

        total = len(childNameDate)+len(camperNameDate)
                
 
        #print total number of matches
        count = Label(master, text = "Total Matches: " + str(total))
        count.grid(row = 0, column = 3)

#******************************************************************************************************************************************************

    def NewChildProfilePage(self, id, date):

        #setup
        self.NewChildProfilePageRoot = Toplevel()
        root = self.NewChildProfilePageRoot
        if self.PrevPage is 'nameBirthEntryPage':
            self.nameBirthEntryPageRoot.withdraw()
        elif self.PrevPage is 'AddNewAppPage':
            self.AddNewAppPageRoot.withdraw()
        root.title("New Child Profile Page")

        self.canvas = Canvas(root)
        master = Frame(self.canvas)

        scrollbarY = Scrollbar(root, orient = "vertical", command = self.canvas.yview)
        scrollbarY.pack(side = RIGHT, fill = Y)
        scrollbarX = Scrollbar(root, orient = "horizontal", command = self.canvas.xview)
        scrollbarX.pack(side = BOTTOM, fill = X)

        self.canvas.configure(xscrollcommand = scrollbarX.set, yscrollcommand = scrollbarY.set)
        self.canvas.pack(side = "left", fill = "both", expand = True)
        self.canvas.create_window((4,4), window = master, anchor="nw", 
                                  tags="master")

        master.bind("<Configure>", self.onFrameConfigure)
        root.geometry("740x1000")

#Buttons
        #frame
        buttonframe = Frame(master)
        buttonframe.pack(side = "top", fill = "x")

        #back
        backButton = Button(buttonframe, text = "Back", command = lambda:self.backNewChildProfilePage(id, date))
        backButton.pack(side = "left")

#Database dump frame
        ChildInfoSectionframe = Frame(master)
        ChildInfoSectionframe.pack(fill = 'y', side = 'left') 
        r = 0

#Child info section

        #header
        labelChildInfoSection = Label(ChildInfoSectionframe, text = "\nCHILD'S INFORMATION")
        labelChildInfoSection.grid(row = r, column = 0)
        labelChildInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        childInfo0 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        childInfo1 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #nickname
        label = Label(ChildInfoSectionframe, text = "\nNickname .............................................................................................. ")
        childInfo2 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        childInfo3 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        label = Label(ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        childInfo4 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        label = Label(ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        childInfo5 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        childInfo6 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #home phone
        label = Label(ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... ")
        childInfo7 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian phone
        label = Label(ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ ")
        childInfo8 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian email
        label = Label(ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... ")
        childInfo9 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        label = Label(ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        childInfo10 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #birthday
        label = Label(ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ ")
        childInfo11 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        label = Label(ChildInfoSectionframe, text = "\nGender .................................................................................................. ")
        childInfo12 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(ChildInfoSectionframe, childInfo12, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #HIV status
        label = Label(ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")
        childInfo13 = StringVar()
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(ChildInfoSectionframe, childInfo13, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #aware  
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... ')
        childInfo14 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo14, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo14, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #why
        label = Label(ChildInfoSectionframe, text = "If no, please provide a reason why child is not aware .............................. ")
        childInfo15 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Referral source
        label = Label(ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... ")
        childInfo16 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #school attending
        label = Label(ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. ")
        childInfo17 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Grade Level
        label = Label(ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... ")
        childInfo18 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo18.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Ethnicity
        label = Label(ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... ")
        childInfo19 = StringVar()
        choices = ['White/Caucasian','Black/African-American','Hispanic/Latino',
        'Native American','Asian/Pacific Islander/Indian Sub-Continent','Multi-racial','Other']
        option = tk.OptionMenu(ChildInfoSectionframe, childInfo19, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Ethnicity Other
        label = Label(ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        childInfo20 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Even been...
        label = Label(ChildInfoSectionframe, text = "\nHas your child ever been...")       
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #ADD_ADHD
        label = Label(ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. ')
        childInfo21 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo21, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo21, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Learning_Disability
        label = Label(ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')
        childInfo22 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo22, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo22, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Developmental_Disability
        label = Label(ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... ')
        childInfo23 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo23, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo23, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Mental_Health_Issues
        label = Label(ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. ')
        childInfo24 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo24, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo24, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Other_Medical_Condition
        label = Label(ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... ')
        childInfo25 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo25, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo25, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Victim_of_Abuse
        label = Label(ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... ')
        childInfo26 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo26, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo26, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Criminal_Justice_System
        label = Label(ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... ')
        childInfo27 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo27, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo27, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Custody
        label = Label(ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... ")
        childInfo28 = StringVar()
        choices = ['Mother','Father','Both Parents','Aunt/Uncle','Grandparent','Pending Court Action','Other']
        option = tk.OptionMenu(ChildInfoSectionframe, childInfo28, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Custody Other
        label = Label(ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        childInfo29 = Entry(ChildInfoSectionframe)
        r = r+1
        childInfo29.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Section
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        parentInfo0 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        parentInfo1 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        label = Label(ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        parentInfo2 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Age
        label = Label(ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        parentInfo3 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)       
        
        #HIV Status
        label = Label(ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ ")
        parentInfo4 =  StringVar()
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo4, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Adoptive Parent
        label = Label(ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... ")
        parentInfo5 = StringVar()
        choices = ['Yes','No','Not Applicable']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo5, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Marital Status
        label = Label(ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... ")
        parentInfo6 = StringVar()
        choices = ['Married','Single','Separated','Divorced','Widowed']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo6, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Highest Level of Education Completed
        label = Label(ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. ")
        parentInfo7 = StringVar()
        choices = ['HS','GED','Some College','Associates Degree','Bachelor Degree','Master Degree','Doctorate']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo7, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Status
        label = Label(ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... ")
        parentInfo8 = StringVar()
        choices = ['Full-Time','Part-Time','Unemployed','Disability']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo8, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Company
        r = r+1
        label = Label(ChildInfoSectionframe, text = "\nIf employed,")
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(ChildInfoSectionframe, text = "please provide Company Name ............................................................. ")
        parentInfo9 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Address
        label = Label(ChildInfoSectionframe, text = "\nAddress ................................................................................................ ")
        parentInfo10 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        parentInfo11 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        label = Label(ChildInfoSectionframe, text = "\nState .................................................................................................... ")
        parentInfo12 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        parentInfo13 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Work Phone
        label = Label(ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... ")
        parentInfo14 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #E-mail
        label = Label(ChildInfoSectionframe, text = "\nE-mail ................................................................................................... ")
        parentInfo15 = Entry(ChildInfoSectionframe)
        r = r+1
        parentInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Absent Parent Info
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        absParentInfo0 = Entry(ChildInfoSectionframe)
        r = r+1
        absParentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        absParentInfo1 = Entry(ChildInfoSectionframe)
        r = r+1
        absParentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Telephone
        label = Label(ChildInfoSectionframe, text = "\nTelephone .............................................................................................. ")
        absParentInfo2 = Entry(ChildInfoSectionframe)
        r = r+1
        absParentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        absParentInfo3 = Entry(ChildInfoSectionframe)
        r = r+1
        absParentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        absParentInfo4 = Entry(ChildInfoSectionframe)
        r = r+1
        absParentInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #County
        label = Label(ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        absParentInfo5 = Entry(ChildInfoSectionframe)
        r = r+1
        absParentInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(ChildInfoSectionframe, text = "\nZip ......................................................................................................... ")
        absParentInfo6 = Entry(ChildInfoSectionframe)
        r = r+1
        absParentInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status
        label = Label(ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ ")
        absParentInfo7 =  StringVar()
        choices = ['HIV Positive','HIV Negative', 'Unkown']
        option = tk.OptionMenu(ChildInfoSectionframe, absParentInfo7, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

#Household Info
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nHOUSEHOLD INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #list all individuals living in the household
        label = Label(ChildInfoSectionframe, text = "\nAll Individuals Living in the Household")
        r = r+1
        label.grid(row = r, column = 0)

    #person1        
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 1')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name1
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")
        houseInfo10 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child1
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        houseInfo11 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex1
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        houseInfo12 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo12, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age1
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        houseInfo13 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status1
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        houseInfo14 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo14, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person2        
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 2')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name2
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")
        houseInfo20 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child2
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        houseInfo21 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex2
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        houseInfo22 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo22, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age2
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        houseInfo23 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status2
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        houseInfo24 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo24, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person3        
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 3')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name3
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")
        houseInfo30 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child3
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        houseInfo31 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex3
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        houseInfo32 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo32, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age3
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        houseInfo33 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo33.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status3
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        houseInfo34 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo34, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person4
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 4')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name4
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")
        houseInfo40 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo40.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child4
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        houseInfo41 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex4
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        houseInfo42 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo42, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age4
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        houseInfo43 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo43.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status4
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        houseInfo44 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo44, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0) 

    #person5        
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 5')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name5
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")
        houseInfo50 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo50.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child5
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        houseInfo51 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex5
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        houseInfo52 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo52, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age5
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        houseInfo53 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo53.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status5
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        houseInfo54 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo54, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person6        
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 6')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name6
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")
        houseInfo60 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo60.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child6
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        houseInfo61 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex6
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        houseInfo62 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo62, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age6
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        houseInfo63 = Entry(ChildInfoSectionframe)
        r = r+1
        houseInfo63.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status6
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        houseInfo64 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo64, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #Family Annual Income Info
        label = Label(ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... ")
        famIncome0 = StringVar()
        choices = ['$0-10,000','$10,001-15,000','$15,001-20,000','$20,000-25,000','$25,001-30,000','$30,001-35,000','$35,001-40,000','$40,001-45,000','$50,000+']
        option = tk.OptionMenu(ChildInfoSectionframe, famIncome0, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income
        label = Label(ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        famIncome1 = IntVar()
        Checkbutton(ChildInfoSectionframe, text = 'Employment', variable = famIncome1).grid(row = r,  column = 1, sticky = W)

        famIncome2 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text = 'Government Support', variable = famIncome2).grid(row = r,  column = 1, sticky = W)

        famIncome3 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text = 'Public Assistance', variable = famIncome3).grid(row = r,  column = 1, sticky = W)

        famIncome4 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text = 'Unemployment Benefits', variable = famIncome4).grid(row = r,  column = 1, sticky = W)

        famIncome5 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text = 'Medicaid', variable = famIncome5).grid(row = r,  column = 1, sticky = W)

        famIncome6 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text = 'Social Security', variable = famIncome6).grid(row = r,  column = 1, sticky = W)

        famIncome7 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text = 'Veterans Benefits', variable = famIncome7).grid(row = r,  column = 1, sticky = W)

        #Other
        famIncome8 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text = 'Other', variable = famIncome8).grid(row = r,  column = 1, sticky = W)

        #If other
        famIncome9 = Entry(ChildInfoSectionframe, width = 19)
        famIncome9.grid(row = r, column = 1, sticky = E)

#In Case of Emergency Contact
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        emergencyInfo0 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        emergencyInfo1 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        label = Label(ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        emergencyInfo2 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        emergencyInfo3 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        emergencyInfo4 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        label = Label(ChildInfoSectionframe, text = "\nState ..................................................................................................... ")
        emergencyInfo5 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        emergencyInfo6 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Phone Number
        label = Label(ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. ")
        emergencyInfo7 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Cell Phone Number
        label = Label(ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... ")
        emergencyInfo8 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Alternate Phone Number
        label = Label(ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... ")
        emergencyInfo9 = Entry(ChildInfoSectionframe)
        r = r+1
        emergencyInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#H.E.R.O. Programs
        #header               
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS\n")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Program(s) you wish your child to participate in
        label = Label(ChildInfoSectionframe, text = "Program(s) you wish your child to participate in .................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Super HEROes Program
        programs0 = IntVar()
        Checkbutton(ChildInfoSectionframe, text="Super HEROes Program", variable = programs0).grid(row = r,  column = 1, sticky = W)

        #Bright HEROs Program
        programs1 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Bright HEROs Program", variable = programs1).grid(row = r,  column = 1, sticky = W)

        #Camp High Five
        programs2 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Camp High Five", variable = programs2).grid(row = r,  column = 1, sticky = W)

        #Holiday of HEROs
        programs3 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Holiday of HEROs", variable = programs3).grid(row = r,  column = 1, sticky = W)

        #Transition to Adulthood
        programs4 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Transition to Adulthood", variable = programs4).grid(row = r,  column = 1, sticky = W)

    #Program(s) you would be interested in your child to participating in
        label = Label(ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Healthy HEROs (health curriculum)
        programs5 = IntVar()
        Checkbutton(ChildInfoSectionframe, text="Healthy HEROs", variable = programs5).grid(row = r,  column = 1, sticky = SW)

        #Career Development/Job Readiness
        programs6 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Career Development/Job Readiness", variable = programs6).grid(row = r,  column = 1, sticky = W)

        #Other
        programs7 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Other", variable = programs7).grid(row = r,  column = 1, sticky = W)

        programs8 = Entry(ChildInfoSectionframe, width = 19)
        programs8.grid(row = r, column = 1, sticky = E)

#Referral Needs
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Referral
        label = Label(ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Food
        Referral0 = IntVar()
        Checkbutton(ChildInfoSectionframe, text="Food", variable = Referral0).grid(row = r,  column = 1, sticky = SW)

        #Transitional Housing/Shelter
        Referral1 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Transitional Housing/Shelter", variable = Referral1).grid(row = r,  column = 1, sticky = W)

        #Rent/Utilities Assistance
        Referral2 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Rent/Utilities Assistance", variable = Referral2).grid(row = r,  column = 1, sticky = W)

        #Clothing/Furniture
        Referral3 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Clothing/Furniture", variable = Referral3).grid(row = r,  column = 1, sticky = W)

        #Financial/Public Assistance
        Referral4 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Financial/Public Assistance", variable = Referral4).grid(row = r,  column = 1, sticky = W)

        #Other
        Referral5 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Other", variable = Referral5).grid(row = r,  column = 1, sticky = W)
        
        Referral6 = Entry(ChildInfoSectionframe, width = 19)
        Referral6.grid(row = r, column = 1, sticky = E)

#Statement of Understanding
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #one
        label = Label(ChildInfoSectionframe, text = "Statement 1 ........................................................................................... ")
        statement0 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement0, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement0, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #two
        label = Label(ChildInfoSectionframe, text = "Statement 2 .......................................................................................... ")
        statement1 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement1, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement1, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #three
        label = Label(ChildInfoSectionframe, text = "Statement 3 .......................................................................................... ")
        statement2 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement2, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement2, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #four
        label = Label(ChildInfoSectionframe, text = "Statement 4 .......................................................................................... ")
        statement3 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement3, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement3, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #five
        label = Label(ChildInfoSectionframe, text = "Statement 5 .......................................................................................... ")
        statement4 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement4, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement4, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #six
        label = Label(ChildInfoSectionframe, text = "Statement 6 .......................................................................................... ")
        statement5 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement5, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement5, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #seven
        label = Label(ChildInfoSectionframe, text = "Statement 7 .......................................................................................... ")
        statement6 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement6, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement6, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#Signature
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nSIGNATURE")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        label = Label(ChildInfoSectionframe, text = "\nSignature .............................................................................................. ")
        signature = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = signature, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = signature, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#Submit
        r = r+1
        submitProfileButton = Button(ChildInfoSectionframe, text = "Submit Profile", 
            command = lambda:self.submitProfile(
        programs0, programs1, programs2, programs3, programs4, programs5, programs6, programs7, programs8,
        Referral0, Referral1, Referral2, Referral3, Referral4, Referral5, Referral6,
        childInfo0, childInfo1, childInfo2, childInfo3, childInfo4, childInfo5, childInfo6, childInfo7,
        childInfo8, childInfo9, childInfo10, childInfo11, childInfo12, childInfo13, childInfo14, childInfo15,
        childInfo16, childInfo17, childInfo18, childInfo19, childInfo20, childInfo21, childInfo22, childInfo23,
        childInfo24, childInfo25, childInfo26, childInfo27, childInfo28, childInfo29,
        parentInfo0, parentInfo1, parentInfo2, parentInfo3, parentInfo4, parentInfo5, parentInfo6, parentInfo7,
        parentInfo8, parentInfo9, parentInfo10, parentInfo11, parentInfo12, parentInfo13, parentInfo14, parentInfo15,
        absParentInfo0, absParentInfo1, absParentInfo2, absParentInfo3, absParentInfo4, absParentInfo5, absParentInfo6, absParentInfo7,
        houseInfo10, houseInfo11, houseInfo12, houseInfo13, houseInfo14,
        houseInfo20, houseInfo21, houseInfo22, houseInfo23, houseInfo24,
        houseInfo30, houseInfo31, houseInfo32, houseInfo33, houseInfo34,
        houseInfo40, houseInfo41, houseInfo42, houseInfo43, houseInfo44,
        houseInfo50, houseInfo51, houseInfo52, houseInfo53, houseInfo54,
        houseInfo60, houseInfo61, houseInfo62, houseInfo63, houseInfo64, 
        famIncome0, famIncome1, famIncome2, famIncome3, famIncome4, famIncome5, famIncome6, famIncome7, famIncome8, famIncome9,
        emergencyInfo0, emergencyInfo1, emergencyInfo2, emergencyInfo3, emergencyInfo4, emergencyInfo5, emergencyInfo6,
        emergencyInfo7, emergencyInfo8, emergencyInfo9,
        statement0, statement1, statement2, statement3, statement4, statement5, statement6, signature))
        
        submitProfileButton.grid(sticky = 'w, e', row = r, columnspan = 2)

#Button Definitions
    def backNewChildProfilePage(self, id, date):
        if askyesno('Verify', '\nAre you sure you want to leave this page?\nYour work will not be saved.'):
            #Go back to 1st level profile page (call back if you can)
            self.PrevPage = 'NewChildProfilePage'
            self.AddNewAppPage()

    def submitProfile(self,
        programs0, programs1, programs2, programs3, programs4, programs5, programs6, programs7, programs8,
        Referral0, Referral1, Referral2, Referral3, Referral4, Referral5, Referral6,
        childInfo0, childInfo1, childInfo2, childInfo3, childInfo4, childInfo5, childInfo6, childInfo7,
        childInfo8, childInfo9, childInfo10, childInfo11, childInfo12, childInfo13, childInfo14, childInfo15,
        childInfo16, childInfo17, childInfo18, childInfo19, childInfo20, childInfo21, childInfo22, childInfo23,
        childInfo24, childInfo25, childInfo26, childInfo27, childInfo28, childInfo29,
        parentInfo0, parentInfo1, parentInfo2, parentInfo3, parentInfo4, parentInfo5, parentInfo6, parentInfo7,
        parentInfo8, parentInfo9, parentInfo10, parentInfo11, parentInfo12, parentInfo13, parentInfo14, parentInfo15,
        absParentInfo0, absParentInfo1, absParentInfo2, absParentInfo3, absParentInfo4, absParentInfo5, absParentInfo6, absParentInfo7,
        houseInfo10, houseInfo11, houseInfo12, houseInfo13, houseInfo14,
        houseInfo20, houseInfo21, houseInfo22, houseInfo23, houseInfo24,
        houseInfo30, houseInfo31, houseInfo32, houseInfo33, houseInfo34,
        houseInfo40, houseInfo41, houseInfo42, houseInfo43, houseInfo44,
        houseInfo50, houseInfo51, houseInfo52, houseInfo53, houseInfo54,
        houseInfo60, houseInfo61, houseInfo62, houseInfo63, houseInfo64, 
        famIncome0, famIncome1, famIncome2, famIncome3, famIncome4, famIncome5, famIncome6, famIncome7, famIncome8, famIncome9,
        emergencyInfo0, emergencyInfo1, emergencyInfo2, emergencyInfo3, emergencyInfo4, emergencyInfo5, emergencyInfo6,
        emergencyInfo7, emergencyInfo8, emergencyInfo9,
        statement0, statement1, statement2, statement3, statement4, statement5, statement6, signature):

        success = 1
        goodData = 1

#adapt for database

#Child App
        
        #wish
        programsA = ''

        if programs0.get():
            programsA = programsA + 'Super HEROes Program,'

        if programs1.get():
            programsA = programsA + 'Bright HEROs Program,'

        if programs2.get():
            programsA = programsA + 'Camp High Five,'

        if programs3.get():
            programsA = programsA + 'Holiday of HEROs,'

        if programs4.get():
            programsA = programsA + 'Transition to Adulthood,'

        if programsA == '':
            programsA = None
        else:
            programsA = programsA[:-1]

        #future
        programsB = ''

        if programs5.get():
            programsB = programsB + 'Healthy HEROs,'

        if programs6.get():
            programsB = programsB + 'Career Development/Job Readiness,'

        if programs7.get():
            programsB = programsB + 'Other,'

        if programsB == '':
            programsB = None
        else:
            programsB = programsB[:-1]


        programsOther = programs8.get()
        if programsOther == '':
            programsOther = None

        #Referral 
        programsC = ''

        if Referral0.get():
            programsC = programsC + 'Food,'

        if Referral1.get():
            programsC = programsC + 'Transitional Housing/Shelter,'

        if Referral2.get():
            programsC = programsC + 'Rent/Utilities Assistance,'

        if Referral3.get():
            programsC = programsC + 'Clothing/Furniture,'

        if Referral4.get():
            programsC = programsC + 'Financial/Public Assistance,'

        if Referral5.get():
            programsC = programsC + 'Other,'

        if programsC == '':
            programsC = None
        else:
            programsC = programsC[:-1]

        ReferralOther = Referral6.get()
        if ReferralOther == '':
            ReferralOther = None

        #Signature
        sig = signature.get()
        if sig == 0:
            sig = None
        elif sig == 2:
            sig = 0
   
#Child's Information

        cI0 = childInfo0.get()
        if cI0 == '':
            cI0 = None

        cI1 = childInfo1.get()
        if cI1 == '':
            cI1 = None

        cI2 = childInfo2.get()
        if cI2 == '':
            cI2 = None        

        cI3 = childInfo3.get()
        if cI3 == '':
            cI3 = None

        cI4 = childInfo4.get()
        if cI4 == '':
            cI4 = None

        cI5 = childInfo5.get()
        if cI5 == '':
            cI5 = None

        cI6 = childInfo6.get()
        if cI6 != '':
            if self.is_number(cI6):
                cI6 = int(cI6)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Child's Information\n\nZip code must be only numbers.")
                goodData = 0
        else:
            cI6 = None


        cI7 = childInfo7.get()
        if cI7 == '':
            cI7 = None

        cI8 = childInfo8.get()
        if cI8 == '':
            cI8 = None
            
        cI9 = childInfo9.get()
        if cI9 == '':
            cI9 = None

        cI10 = childInfo10.get()
        if cI10 != '':
            if self.is_number(cI10):
                cI10 = int(cI10)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Child's Information\n\nAge must be only numbers.")
                goodData = 0
        else:
            cI10 = None

        cI11 = childInfo11.get()
        if cI11 != '':
            if not self.is_date(cI11):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Child's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            cI11 = None

        cI12 = childInfo12.get()
        if cI12 == '':
            cI12 = None

        cI13 = childInfo13.get()
        if cI13 == '':
            cI13 = None

        cI14 = childInfo14.get()
        if cI14 == 0:
            cI14 = None
        elif cI14 == 2:
            cI14 = 0

        cI15 = childInfo15.get()
        if cI15 == '':
            cI15 = None

        cI16 = childInfo16.get()
        if cI16 == '':
            cI16 = None

        cI17 = childInfo17.get()
        if cI17 == '':
            cI17 = None

        cI18 = childInfo18.get()
        if cI18 == '':
            cI18 = None

        cI19 = childInfo19.get()
        if cI19 == '':
            cI19 = None

        cI20 = childInfo20.get()
        if cI20 == '':
            cI20 = None

        cI21 = childInfo21.get()
        if cI21 == 0:
            cI21 = None
        elif cI21 == 2:
            cI21 = 0

        cI22 = childInfo22.get()
        if cI22 == 0:
            cI22 = None
        elif cI22 == 2:
            cI22 = 0

        cI23 = childInfo23.get()
        if cI23 == 0:
            cI23 = None
        elif cI23 == 2:
            cI23 = 0

        cI24 = childInfo24.get()
        if cI24 == 0:
            cI24 = None
        elif cI24 == 2:
            cI24 = 0

        cI25 = childInfo25.get()
        if cI25 == 0:
            cI25 = None
        elif cI25 == 2:
            cI25 = 0

        cI26 = childInfo26.get()
        if cI26 == 0:
            cI26 = None
        elif cI26 == 2:
            cI26 = 0

        cI27 = childInfo27.get()
        if cI27 == 0:
            cI27 = None
        elif cI27 == 2:
            cI27 = 0

        cI28 = childInfo28.get()
        if cI28 == '':
            cI28 = None

        cI29 = childInfo29.get()
        if cI29 == '':
            cI29 = None

#Parent/ Guardian's Information
        #adapt for database

        pI0 = parentInfo0.get()
        if pI0 == '':
            pI0 = None

        pI1 = parentInfo1.get()
        if pI1 == '':
            pI1 = None

        pI2 = parentInfo2.get()
        if pI2 == '':
            pI2 = None

        pI3 = parentInfo3.get()
        if pI3 != '':
            if self.is_number(pI3):
                pI3 = int(pI3)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Parent/Guardian Information\n\nAge must be only numbers.")
                goodData = 0
        else:
            pI3 = None

        pI4 = parentInfo4.get()
        if pI4 == '':
            pI4 = None

        pI5 = parentInfo5.get()
        if pI5 == '':
            pI5 = None

        pI6 = parentInfo6.get()
        if pI6 == '':
            pI6 = None

        pI7 = parentInfo7.get()
        if pI7 == '':
            pI7 = None

        pI8 = parentInfo8.get()
        if pI8 == '':
            pI8 = None

        pI9 = parentInfo9.get()
        if pI9 == '':
            pI9 = None

        pI10 = parentInfo10.get()
        if pI10 == '':
            pI10 = None

        pI11 = parentInfo11.get()
        if pI11 == '':
            pI11 = None

        pI12 = parentInfo12.get()
        if pI12 == '':
            pI12 = None

        pI13 = parentInfo13.get()
        if pI13 != '':
            if self.is_number(pI13):
                pI13 = int(pI13)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Parent/Guardian Information\n\nZip must be only numbers.")
                goodData = 0
        else:
            pI13 = None

        pI14 = parentInfo14.get()
        if pI14 == '':
            pI14 = None

        pI15 = parentInfo15.get()
        if pI15 == '':
            pI15 = None
        
#Absent Parent's Information
        #adapt for database

        abs0 = absParentInfo0.get()
        if abs0 == '':
            abs0 = None

        abs1 = absParentInfo1.get()
        if abs1 == '':
            abs1 = None            

        abs2 = absParentInfo2.get()
        if abs2 == '':
            abs2 = None  

        abs3 = absParentInfo3.get()
        if abs3 == '':
            abs3 = None

        abs4 = absParentInfo4.get()
        if abs4 == '':
            abs4 = None  

        abs5 = absParentInfo5.get()
        if abs5 == '':
            abs5 = None  

        abs6 = absParentInfo6.get()
        if abs6 != '':
            if self.is_number(abs6):
                abs6 = int(abs6)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Absent Parent Information\n\nZip must be only numbers.")
                goodData = 0
        else:
            abs6 = None

        abs7 = absParentInfo7.get()
        if abs7 == '':
            abs7 = None  

#Household Information
        #adapt for database
        person1 = 0
        person2 = 0
        person3 = 0
        person4 = 0
        person5 = 0
        person6 = 0

        #person 1
        house10 = houseInfo10.get()
        if house10 != '':
            person1 = 1

            house11 = houseInfo11.get()
            if house11 == '':
                house11 = None  
            
            house12 = houseInfo12.get()
            if house12 == '':
                house12 = None  
            
            house13 = houseInfo13.get()
            if house13 != '':
                if self.is_number(house13):
                    house13 = int(house13)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house13 = None
            
            house14 = houseInfo14.get()
            if house14 == '':
                house14 = None 

        #person 2
        house20 = houseInfo20.get()
        if house20 != '':
            person2 = 1

            house21 = houseInfo21.get()
            if house21 == '':
                house21 = None  
            
            house22 = houseInfo22.get()
            if house22 == '':
                house22 = None  
            
            house23 = houseInfo23.get()
            if house23 != '':
                if self.is_number(house23):
                    house23 = int(house23)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house23 = None
            
            house24 = houseInfo24.get()
            if house24 == '':
                house24 = None 

        #person 3
        house30 = houseInfo30.get()
        if house30 != '':
            person3 = 1

            house31 = houseInfo31.get()
            if house31 == '':
                house31 = None  
            
            house32 = houseInfo32.get()
            if house32 == '':
                house32 = None  
            
            house33 = houseInfo33.get()
            if house33 != '':
                if self.is_number(house33):
                    house33 = int(house33)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house33 = None
            
            house34 = houseInfo34.get()
            if house34 == '':
                house34 = None 

        #person 4
        house40 = houseInfo40.get()
        if house40 != '':
            person4 = 1

            house41 = houseInfo41.get()
            if house41 == '':
                house41 = None  
            
            house42 = houseInfo42.get()
            if house42 == '':
                house42 = None  
            
            house43 = houseInfo43.get()
            if house43 != '':
                if self.is_number(house43):
                    house43 = int(house43)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house43 = None
            
            house44 = houseInfo44.get()
            if house44 == '':
                house44 = None 

        #person 5
        house50 = houseInfo50.get()
        if house50 != '':
            person5 = 1

            house51 = houseInfo51.get()
            if house51 == '':
                house51 = None  
            
            house52 = houseInfo52.get()
            if house52 == '':
                house52 = None  
            
            house53 = houseInfo53.get()
            if house53 != '':
                if self.is_number(house53):
                    house53 = int(house53)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house53 = None
            
            house54 = houseInfo54.get()
            if house54 == '':
                house54 = None 

        #person 6
        house60 = houseInfo60.get()
        if house60 != '':
            person6 = 1

            house61 = houseInfo61.get()
            if house61 == '':
                house61 = None  
            
            house62 = houseInfo62.get()
            if house62 == '':
                house62 = None  
            
            house63 = houseInfo63.get()
            if house63 != '':
                if self.is_number(house63):
                    house63 = int(house63)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house63 = None
            
            house64 = houseInfo64.get()
            if house64 == '':
                house64 = None 

#Family Annual Income Info
        #adapt for database

        income = famIncome0.get()
        if income == '':
            income = None

#Source of Family Income
        #adapt for database
        sourceIncome = ''

        if famIncome1.get():
            sourceIncome = sourceIncome + 'Employment,'

        if famIncome2.get():
            sourceIncome = sourceIncome + 'Government Support,'

        if famIncome3.get():
            sourceIncome = sourceIncome + 'Public Assistance,'
        
        if famIncome4.get():
            sourceIncome = sourceIncome + 'Unemployment Benefits,'
        
        if famIncome5.get():
            sourceIncome = sourceIncome + 'Medicaid,'
        
        if famIncome6.get():
            sourceIncome = sourceIncome + 'Social Security,'
        
        if famIncome7.get():
            sourceIncome = sourceIncome + 'Veterans Benefits,'
        
        if famIncome8.get():
            sourceIncome = sourceIncome + 'Other,'

        if sourceIncome == '':
            sourceIncome = None
        else:
            sourceIncome = sourceIncome[:-1]

        otherSource = famIncome9.get()
        if otherSource == '':
            otherSource = None

#In Case of Emergency Contact
        #adapt for database

        emergency0 = emergencyInfo0.get()
        if emergency0 == '':
            emergency0 = None

        emergency1 = emergencyInfo1.get()
        if emergency1 == '':
            emergency1 = None

        emergency2 = emergencyInfo2.get()
        if emergency2 == '':
            emergency2 = None

        emergency3 = emergencyInfo3.get()
        if emergency3 == '':
            emergency3 = None

        emergency4 = emergencyInfo4.get()
        if emergency4 == '':
            emergency4 = None

        emergency5 = emergencyInfo5.get()
        if emergency5 == '':
            emergency5 = None

        emergency6 = emergencyInfo6.get()
        if emergency6 != '':
            if self.is_number(emergency6):
                emergency6 = int(emergency6)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in In Case of Emergency Contact\n\nZip must be only numbers.")
                goodData = 0
        else:
            emergency6 = None

        emergency7 = emergencyInfo7.get()
        if emergency7 == '':
            emergency7 = None

        emergency8 = emergencyInfo8.get()
        if emergency8 == '':
            emergency8 = None

        emergency9 = emergencyInfo9.get()
        if emergency9 == '':
            emergency9 = None

#statements of understanding
        #adapt for database

        s0 = statement0.get()
        if s0 == 0:
            s0 = None
        elif s0 == 2:
            s0 = 0

        s1 = statement1.get()
        if s1 == 0:
            s1 = None
        elif s1 == 2:
            s1 = 0

        s2 = statement2.get()
        if s2 == 0:
            s2 = None
        elif s2 == 2:
            s2 = 0

        s3 = statement3.get()
        if s3 == 0:
            s3 = None
        elif s3 == 2:
            s3 = 0

        s4 = statement4.get()
        if s4 == 0:
            s4 = None
        elif s4 == 2:
            s4 = 0

        s5 = statement5.get()
        if s5 == 0:
            s5 = None
        elif s5 == 2:
            s5 = 0

        s6 = statement6.get()
        if s6 == 0:
            s6 = None
        elif s6 == 2:
            s6 = 0

#Database Connection
        db = self.connect()
        curr = db.cursor()

#Insert into DB
#TODO: pass in params ID & Date
        id = 2
        date = '2016-12-12'

        if goodData:
            try:
                curr.execute("""DELETE FROM Child_Application WHERE ID = %s;""", (id,))
                db.commit()

                curr.execute("""INSERT INTO Child_Application VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, sig, programsC, ReferralOther, programsB, programsOther, programsA,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM Childs_Information WHERE ID = %s;""", (id,))
                db.commit()

                curr.execute("""INSERT INTO Childs_Information VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                             (id, date, cI0, cI1, cI2, cI3, cI4, cI5, cI6, cI7, cI8, cI9, cI10, cI11, cI12, cI13, cI14, cI15, cI16,
                                 cI17, cI18, cI19, cI20, cI21, cI22, cI23, cI24, cI25, cI26, cI27, cI28, cI29,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM Parent_Guardian_Information WHERE ID = %s;""", (id,))
                db.commit()

                curr.execute("""INSERT INTO Parent_Guardian_Information VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                             (id, date, pI0, pI1, pI2, pI3, pI4, pI5, pI6, pI7, pI8, pI9, pI10, pI11,
                                 pI12, pI13, pI14, pI15,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM Absent_Parent_Information WHERE ID = %s;""", (id,))
                db.commit()

                curr.execute("""INSERT INTO Absent_Parent_Information VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                                 (id, date, abs0, abs1, abs2, abs3, abs4, abs5, abs6, abs7,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            if person1:
                try:
                    count = 1
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 1;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house10, house11, house12, house13, house14,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person2:
                try:
                    count = 2
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 2;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house20, house21, house22, house23, house24,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person3:
                try:
                    count = 3
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 3;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house30, house31, house32, house33, house34,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person4:
                try:
                    count = 4
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 4;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house40, house41, house42, house43, house44,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person5:
                try:
                    count = 5
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 5;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house50, house51, house52, house53, house54,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person6:
                try:
                    count = 6
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 6;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house60, house61, house62, house63, house64,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            try:
                curr.execute("""DELETE FROM Fam_Annual_Income WHERE ID = %s;""", (id,))
                db.commit()

                curr.execute("""INSERT INTO Fam_Annual_Income VALUES
                    (%s, %s, %s);""",
                    (id, date, income,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM Source_Fam_Income WHERE ID = %s;""", (id,))
                db.commit()

                curr.execute("""INSERT INTO Source_Fam_Income VALUES
                    (%s, %s, %s, %s);""",
                    (id, date, sourceIncome, otherSource,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM ChildApp_Emergency_Contact WHERE ID = %s;""", (id,))
                db.commit()

                curr.execute("""INSERT INTO ChildApp_Emergency_Contact VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, emergency0, emergency1, emergency2, emergency3, emergency4, emergency5, emergency6,
                         emergency7, emergency8, emergency9,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""INSERT INTO Statement_Of_Understanding VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, s0, s1, s2, s3, s4, s5, s6,))

            except (MySQLdb.IntegrityError) as e:
                success = 0
            

            db.commit()

            if success:
                tkMessageBox.showinfo("New Profile", "Submission Sucessful!")
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nA Child application \nSubmitted on: " + date + "\nFor ID number: " + str(id) + " \nAlready exists in the system")

#Close Database Connection
        curr.close()
        db.close()

#check string entry is a number
    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

#check string entry is a date (YYYY-MM-DD)
    def is_date(self, s):
        if len(s) != 10:
            return False
        if (s[4] != s[7]) or (s[4] != '-') or (not self.is_number(s[0:4])) or (not self.is_number(s[5:7])) or (not self.is_number(s[-2:])):
            return False
        if (1 > int(s[0:4])) or (1 > int(s[5:7])) or (int(s[5:7]) > 12) or (1 > int(s[-2:])):
            return False
        if int(s[5:7]) == 02:
            if (int(s[-2:]) > 29):
                return False
        elif (int(s[5:7]) == 04) or (int(s[5:7]) == 06) or (int(s[5:7]) == 9) or (int(s[5:7]) == 11):
            if (int(s[-2:]) > 30): 
                return False
        elif int(s[-2:]) > 31:
            return False

        return True

#******************************************************************************************************************************************************

    def AdminUserPage(self):
       
        self.AdminUserPageRoot = Toplevel()
        root = self.AdminUserPageRoot
        if self.PrevPage is 'HomePage':
            self.HomePageRoot.withdraw()
        elif self.PrevPage is 'AddUserPage':
            self.AddUserPageRoot.withdraw()
        elif self.PrevPage is 'DeleteUserPage':
            self.DeleteUserPageRoot.withdraw()
        self.PrevPage = 'AdminUserPage'
        
        root.title("Administrate Users Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        username = self.session['username']
        
        back = Button(master, text = "Back", command = lambda: self.HomePage())
        back.grid(row = 0, column = 0)

        addButton = Button(master, text = "Add", command=lambda: self.AddUserPage())
        addButton.grid(row = 1, column = 1, padx = 225, pady = 10)
        
        deleteButton = Button(master, text = "Delete", command = lambda: self.DeleteUserPage())
        deleteButton.grid(row = 2, column = 1, padx = 225, pady = 10)

#******************************************************************************************************************************************************

    def AddUserPage(self):
 
        self.AddUserPageRoot = Toplevel()
        root = self.AddUserPageRoot
        self.AdminUserPageRoot.withdraw()
        self.PrevPage = 'AddUserPage'
        root.title("Add User Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        name = Label(master, text="Name").grid(row=1)
        nameEntry = Entry(master)
        nameEntry.grid(row=1, column=1)

        username = Label(master, text="Username").grid(row=2)
        usernameEntry = Entry(master)
        usernameEntry.grid(row=2, column=1)

        password = Label(master, text="Password").grid(row=3)
        passwordEntry = Entry(master)
        passwordEntry.grid(row=3, column=1)

        level = Label(master, text="Type").grid(row=4)
        levelEntry = StringVar(master)
        levelEntry.set("Regular")
        menu = OptionMenu(master, levelEntry, 'Administrator', 'Manager', 'Regular').grid(row=4, column=1)

        add = Button(master, text="Add User", command = lambda: self.addUser(nameEntry.get(), usernameEntry.get(), 
            passwordEntry.get(), levelEntry.get())).grid(row=6, column=3)
        back = Button(master, text="Back", command = lambda: self.AdminUserPage()).grid(row=6, column=0)

    def addUser(self, name, username, password, level):

        db = self.connect()
        curr = db.cursor()

        curr.execute("""INSERT INTO User VALUES (%s, %s, SHA1(%s), %s);""", (name, username, password, level,))
        
        db.commit()
        curr.close()
        db.close()

        #TODO: duplicate usernames error handling
        tkMessageBox.showinfo("Add User", "Update Successful!")

#******************************************************************************************************************************************************

    def DeleteUserPage(self):

        self.DeleteUserPageRoot = Toplevel()
        root = self.DeleteUserPageRoot
        self.AdminUserPageRoot.withdraw()
        self.PrevPage = 'DeleteUserPage'
        root.title("Delete User Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        nameHead = Label(master, text = "Nameame", font= "Verdana 10 underline")
        nameHead.grid(row = 1, column = 0)

        usernameHead = Label(master, text = "Username", font= "Verdana 10 underline")
        usernameHead.grid(row = 1, column = 1)

        critHead = Label(master, text = "User Type", font= "Verdana 10 underline")
        critHead.grid(row = 1, column = 2)

        #back button
        self.back = Button(master, text = "Back", command = lambda: self.AdminUserPage())
        self.back.grid(row = 0, column = 0)

        #database fetch
        db = MySQLdb.connect(host = "localhost", user="root", passwd = "Darling", db="HERO")
        curr = db.cursor()
        curr.execute("SELECT * FROM User")
        results = curr.fetchall()
        curr.close()
        db.close()

        count = 0
        deleteButtonArr = [0 for x in range(len(results))]
        for name,username,_,usertype in results:
            nameLabel = Label(master, text = name, font= "Verdana 10")
            nameLabel.grid(row = 2 + count, column = 0)

            usernameLabel = Label(master, text = username, font= "Verdana 10")
            usernameLabel.grid(row = 2 + count, column = 1)

            usertypeLabel = Label(master, text = usertype, font= "Verdana 10")
            usertypeLabel.grid(row = 2 + count, column = 2)

            deleteButtonArr[count] = Button(master, text = "Delete", command = lambda username1 = username: self.deleteUser(username1))
            deleteButtonArr[count].grid(row = 2 + count, column = 3)
            count += 1

    def deleteUser(self, username):        
        db = MySQLdb.connect(host = "localhost", user="root", passwd = "Darling", db="HERO")
        curr = db.cursor()

        curr.execute("DELETE FROM User WHERE Username = %s", (username,))
        db.commit()

        curr.close()
        db.close()

        tkMessageBox.showinfo("Delete User","User "+username+" has been deleted.")
        
        self.DeleteUserPageRoot.withdraw()
        self.DeleteUserPage()

#******************************************************************************************************************************************************

    def SearchPage(self):

        self.SearchPageRoot = Toplevel()
        root = self.SearchPageRoot
        if self.PrevPage is 'HomePage':
            self.HomePageRoot.withdraw()
        elif self.PrevPage is 'SearchCatPage':
            self.SearchCatPageRoot.withdraw()
        elif self.PrevPage is 'SearchNamePage':
            self.SearchNamePageRoot.withdraw()
        elif self.PrevPage is 'FirstProfilePage':
            self.FirstProfilePageRoot.withdraw()
        self.PrevPage = 'SearchPage'
        
        root.title("Search Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        db = MySQLdb.connect(host="localhost", user="root", passwd="Darling", db="HERO")
        curr = db.cursor()

        curr.execute("SELECT COUNT(ID) FROM Child;")
        total = curr.fetchall()[0][0]

        count = Label(master, text = "Total: " + str(total))
        count.grid(row = 0, column = 4)

        catLabel = Label(master, text = "Search by Category", font= "Verdana 10 underline")
        catLabel.grid(row = 2, column = 0)

        nameLabel = Label(master, text = "Search by Name", font= "Verdana 10 underline")
        nameLabel.grid(row = 4, column = 0)

        programList = ['None', "Child Application", "Camp High Five Application"]
        programs = StringVar(root)
        programs.set('Program') 

        dropdownProgram = OptionMenu(master, programs, *programList)
        dropdownProgram.grid(row = 1, column = 1)

        
        #grab all data submitted, remove duplicates, set to yearList
        childDatesSubmitted = curr.execute("SELECT Year(Date_Submitted) FROM Child_Application;")
        childYears = curr.fetchall()
        campDatesSubmitted = curr.execute("SELECT Year(Date_Submitted) FROM Camp_Application;")
        campYears = curr.fetchall()
        yearList = []

        for item in childYears:
            if item not in yearList:
                yearList.append(item)

        for item in campYears:
            if item not in yearList:
                yearList.append(item)
        years = StringVar(root)
        years.set("Year")

        #add back yearlist
        dropdownYear = OptionMenu(master, years, "None", *yearList)
        dropdownYear.grid(row = 1, column = 2)

        categoriesList = ['None', 'Zip Code', 'City', "County", 'Referral Source', "Child's Age",
                    "Child's Gender", "Child's Race/Ethnicity",
                    "Child's HIV Status (infected or affected)", "Child's Other Issues",
                    "Child's HERO Program Participation", "Child's Allergies", "Child's Years with HERO",
                    "Household Composition", "Parent(s) HIV Status (infected or affected)",
                    "Household Income Range", "Household Income Source", "Parent(s) Highest Level of Education",
                    "Parent(s) Employment Status"]
        categories = StringVar(root)
        categories.set("Category")

        dropdownCategories = OptionMenu(master, categories, *categoriesList)
        dropdownCategories.grid(row = 3, column = 1)
        catEntry = Entry(master, width=15)
        catEntry.grid(row = 3, column = 2)

        txt = Label(master, text = "First Name:")
        txt.grid(row = 5, column = 1)

        firstName = Entry(master, width=15)
        firstName.grid(row = 5, column = 2)
        
        txt = Label(master, text = "Last Name:")
        txt.grid(row = 6, column = 1)

        lastName = Entry(master, width=15)
        lastName.grid(row = 6, column = 2)

        searchCatButton = Button(master, text = "Search", command = lambda: self.SearchCatPage(programs.get(), years.get(), categories.get(), catEntry.get()))
        searchCatButton.grid(row = 3, column = 3)

        back = Button(master, text = "Back", command = lambda:self.HomePage())
        back.grid(row = 0, column = 0)

        searchNameButton = Button(master, text = "Search", command = lambda: self.SearchNamePage(programs.get(), years.get(), firstName.get(), lastName.get()))
        searchNameButton.grid(row = 5, column = 3)

        curr.close()
        db.close()
        
#******************************************************************************************************************************************************

    def SearchCatPage(self, selectedProgram, selectedYear, selectedCategory, catEntry):

        self.SearchCatPageRoot = Toplevel()
        root = self.SearchCatPageRoot
        self.SearchPageRoot.withdraw()
        self.PrevPage = 'SearchCatPage'
        root.title("Search Results Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        camp = ''
        child = ''

        db = MySQLdb.connect(host="localhost", user="root", passwd="Darling", db="HERO")
        curr = db.cursor()

        #check for program selection
        programParam = 1
        if (selectedProgram == 'Program') or (selectedProgram == 'None'):
            #no program input
            programParam = 0

        #check for year selection
        yearParam = 1
        if (selectedYear == 'Year') or (selectedYear == 'None'):
            #no year input
            yearParam = 0
        else:
            selectedYear = selectedYear[1:5]

        #no category input
        if (selectedCategory == 'Category') or (selectedCategory == 'None'):

            #no year & no program OR no year & child
            #first, last, year in child
            if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                    curr.execute("SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information;")
                    child = curr.fetchall()

            #no year & no program OR no year & camp
            #first, last, year in camp
            if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                    curr.execute("SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information;")
                    camp = curr.fetchall()

            #year & no program OR year & child
            #first, last in child
            if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                    curr.execute("SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information WHERE YEAR(Date_Submitted) = %s;", (selectedYear,))
                    child = curr.fetchall()

            #year & no program OR year & camp
            #first, last in camp
            if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                    curr.execute("SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information WHERE YEAR(Date_Submitted) = %s;", (selectedYear,))
                    camp = curr.fetchall()

        elif selectedCategory == 'Zip Code':
            
            if (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_Zip FROM Childs_Information 
                            WHERE Address_Zip != '';""")
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_Zip FROM Demographic_Information 
                            WHERE Address_Zip != '';""")
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                check = yearParam and ((not programParam) or (selectedProgram == 'Child Application'))
                if (check):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_Zip FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_Zip != '';""", (selectedYear,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_Zip FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_Zip != '';""", (selectedYear,))
                        camp = curr.fetchall()
            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_Zip FROM Childs_Information 
                            WHERE Address_Zip = %s;""", (int(catEntry),))
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_Zip FROM Demographic_Information 
                            WHERE Address_Zip = %s;""", (int(catEntry),))
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                check = yearParam and ((not programParam) or (selectedProgram == 'Child Application'))
                if (check):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_Zip FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_Zip = %s;""", (selectedYear, int(catEntry),))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_Zip FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_Zip = %s;""", (selectedYear, int(catEntry),))
                        camp = curr.fetchall()

        elif selectedCategory == 'City':
            
            if (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_City FROM Childs_Information 
                            WHERE Address_City != '';""")
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_City FROM Demographic_Information 
                            WHERE Address_City != '';""")
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                check = yearParam and ((not programParam) or (selectedProgram == 'Child Application'))
                if (check):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_City FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_City != '';""", (selectedYear,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_City FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_City != '';""", (selectedYear,))
                        camp = curr.fetchall()
            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_City FROM Childs_Information 
                            WHERE Address_City = %s;""", (catEntry,))
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_City FROM Demographic_Information 
                            WHERE Address_City = %s;""", (catEntry,))
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                check = yearParam and ((not programParam) or (selectedProgram == 'Child Application'))
                if (check):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_City FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_City = %s;""", (selectedYear, catEntry,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_City FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_City = %s;""", (selectedYear, catEntry,))
                        camp = curr.fetchall()

        elif selectedCategory == 'County':

            if (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_County FROM Childs_Information 
                            WHERE Address_County != '';""")
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_County FROM Demographic_Information 
                            WHERE Address_County != '';""")
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_County FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_County != '';""", (selectedYear,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_County FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_County != '';""", (selectedYear,))
                        camp = curr.fetchall()
            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_County FROM Childs_Information 
                            WHERE Address_County = %s;""", (catEntry,))
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_County FROM Demographic_Information 
                            WHERE Address_County = %s;""", (catEntry,))
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_County FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_County = %s;""", (selectedYear, catEntry,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_County FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Address_County = %s;""", (selectedYear, catEntry,))
                        camp = curr.fetchall()

        elif selectedCategory == 'Referral Source':

            if (selectedProgram == 'Camp High Five Application'):
                tkMessageBox.showinfo("Search", "This application does not contain the category Referral Source")

            elif (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Referral_Source FROM Childs_Information 
                            WHERE Referral_Source != '';""")
                        child = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Referral_Source FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Referral_Source != '';""", (selectedYear,))
                        child = curr.fetchall()

            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Referral_Source FROM Childs_Information 
                            WHERE Referral_Source = %s;""", (catEntry,))
                        child = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Referral_Source FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Referral_Source = %s;""", (selectedYear, catEntry,))
                        child = curr.fetchall()

        elif selectedCategory == "Child's Age":

            if (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Age FROM Childs_Information 
                            WHERE Age != '';""")
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Age FROM Demographic_Information 
                            WHERE Age != '';""")
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Age FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Age != '';""", (selectedYear,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Age FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Age != '';""", (selectedYear,))
                        camp = curr.fetchall()

            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Age FROM Childs_Information 
                            WHERE Age = %s;""", (catEntry,))
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Age FROM Demographic_Information 
                            WHERE Age = %s;""", (catEntry,))
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Age FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Age = %s;""", (selectedYear, catEntry,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Age FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Age = %s;""", (selectedYear, catEntry,))
                        camp = curr.fetchall()

        elif selectedCategory == "Child's Gender":

            if (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Gender FROM Childs_Information 
                            WHERE Gender != '';""")
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Gender FROM Demographic_Information 
                            WHERE Gender != '';""")
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Gender FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Gender != '';""", (selectedYear,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Gender FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Gender != '';""", (selectedYear,))
                        camp = curr.fetchall()
            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Gender FROM Childs_Information 
                            WHERE Gender = %s;""", (catEntry,))
                        child = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Gender FROM Demographic_Information 
                            WHERE Gender = %s;""", (catEntry,))
                        camp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Gender FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Gender = %s;""", (selectedYear, catEntry,))
                        child = curr.fetchall()

                #year & no program OR year & camp
                #first, last, cat in camp
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Gender FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Gender = %s;""", (selectedYear, catEntry,))
                        camp = curr.fetchall()

        elif selectedCategory == "Child's Race/Ethnicity":

            if catEntry == '':
                #no year & (no program OR camp)
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Race FROM Demographic_Information 
                            WHERE Race != '';""")
                        camp = curr.fetchall()

                #year & (no program OR camp)
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Race FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Race != '';""", (selectedYear,))
                        camp = curr.fetchall()

                #no year & (no program OR child)
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Ethnicity, Ethnicity_Other FROM Childs_Information 
                            WHERE Ethnicity != '' OR Ethnicity_Other != '';""")
                        child = curr.fetchall()

                #year & (no program OR child)
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Ethnicity, Ethnicity_Other FROM Childs_Information 
                            WHERE Ethnicity != '' OR Ethnicity_Other !- '';""")
                        child = curr.fetchall()         

            else:
                #no year & (no program OR camp)
                #first, last, year, cat in camp
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Race FROM Demographic_Information 
                            WHERE Race = %s;""", (catEntry,))
                        camp = curr.fetchall()

                #year & (no program OR camp)
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Race FROM Demographic_Information 
                            WHERE YEAR(Date_Submitted) = %s AND Race != %s;""", (selectedYear, catEntry,))
                        camp = curr.fetchall()

                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Ethnicity, Ethnicity_Other FROM Childs_Information 
                            WHERE Ethnicity != %s OR Ethnicity_Other != %s;""", (catEntry, catEntry,))
                        child = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Ethnicity, Ethnicity_Other FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND (Ethnicity != %s OR Ethnicity_Other != %s);""", (selectedYear, catEntry, catEntry,))
                        child = curr.fetchall()

        elif selectedCategory == "Child's HIV Status (infected or affected)":

            if (selectedProgram == 'Camp High Five Application'):
                tkMessageBox.showinfo("Search", "This application does not contain the category")

            elif (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, HIV_Status FROM Childs_Information 
                            WHERE HIV_Status != '';""")
                        child = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, HIV_Status FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND HIV_Status != '';""", (selectedYear,))
                        child = curr.fetchall()
            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, HIV_Status FROM Childs_Information 
                            WHERE HIV_Status = %s;""", (catEntry,))
                        child = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, HIV_Status FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s AND HIV_Status = %s;""", (selectedYear, catEntry,))
                        child = curr.fetchall()

        elif selectedCategory == "Child's Other Issues":

            if (selectedProgram == 'Camp High Five Application'):
                tkMessageBox.showinfo("Search", "This application does not contain the category")

            elif (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if not yearParam:
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            ADD_ADHD, Learning_Disability, Developmental_Disability, Mental_Health_Issues, 
                            Other_Medical_Condition, Victim_of_Abuse, Criminal_Justice_System
                            FROM Childs_Information 
                            WHERE ADD_ADHD != '' OR Learning_Disability != '' OR Developmental_Disability != '' OR
                            Mental_Health_Issues != '' OR Other_Medical_Condition != '' OR Victim_of_Abuse != '' OR 
                            Criminal_Justice_System != '';""")
                        temp = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if yearParam:
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, 
                            ADD_ADHD, Learning_Disability, Developmental_Disability, Mental_Health_Issues, 
                            Other_Medical_Condition, Victim_of_Abuse, Criminal_Justice_System 
                            FROM Childs_Information WHERE YEAR(Date_Submitted) = %s 
                            AND (ADD_ADHD != '' OR Learning_Disability != '' OR Developmental_Disability != '' OR
                            Mental_Health_Issues != '' OR Other_Medical_Condition != '' OR Victim_of_Abuse != '' OR 
                            Criminal_Justice_System != '');""", (selectedYear,))
                        temp = curr.fetchall()
            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                    if (catEntry == "ADD" or catEntry == "ADHD" or catEntry == "ADD/ADHD"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            ADD_ADHD
                            FROM Childs_Information 
                            WHERE ADD_ADHD != '1';""")
                        temp = curr.fetchall()
                    
                    if (catEntry == "Learning Disability"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Learning_Disability
                            FROM Childs_Information 
                            WHERE Learning_Disability != '1';""")
                        temp = curr.fetchall()
                    
                    if (catEntry == "Developmental Disability"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Developmental_Disability
                            FROM Childs_Information 
                            WHERE Developmental_Disability != '1';""")
                        temp = curr.fetchall()
                    
                    if (catEntry == "Mental Health Issues"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, 
                            Mental_Health_Issues
                            FROM Childs_Information 
                            WHERE Mental_Health_Issues != '1';""")
                        temp = curr.fetchall()
                    
                    if (catEntry == "Other Medical Condition"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Other_Medical_Condition
                            FROM Childs_Information 
                            WHERE Other_Medical_Condition != '1';""")
                        temp = curr.fetchall()
                    
                    if (catEntry == "Victim of Abuse"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Victim_of_Abuse
                            FROM Childs_Information 
                            WHERE Victim_of_Abuse != '1';""")
                        temp = curr.fetchall()
                    
                    if (catEntry == "Criminal Justice System"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Criminal_Justice_System
                            FROM Childs_Information 
                            WHERE Criminal_Justice_System != '1';""")
                        temp = curr.fetchall()
                    

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
                    if (catEntry == "ADD" or catEntry == "ADHD" or catEntry == "ADD/ADHD"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            ADD_ADHD
                            FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s 
                            AND ADD_ADHD != '1';""", (selectedYear,))
                        temp = curr.fetchall()
                
                    if (catEntry == "Learning Disability"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, 
                            Learning_Disability
                            FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s 
                            AND Learning_Disability != '1';""", (selectedYear,))
                        temp = curr.fetchall()
                    
                    if (catEntry == "Developmental Disability"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Developmental_Disability
                            FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s 
                            AND Developmental_Disability != '1';""", (selectedYear,))
                        temp = curr.fetchall()
                    
                    if (catEntry == "Mental Health Issues"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Mental_Health_Issues
                            FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s 
                            AND Mental_Health_Issues != '1';""", (selectedYear,))
                        temp = curr.fetchall()
                    
                    if (catEntry == "Other Medical Condition"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Other_Medical_Condition
                            FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s 
                            AND Other_Medical_Condition != '1';""", (selectedYear,))
                        temp = curr.fetchall()
                    
                    if (catEntry == "Victim of Abuse"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last,
                            Victim_of_Abuse
                            FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s 
                            AND Victim_of_Abuse != '1';""", (selectedYear,))
                        temp = curr.fetchall()
                    
                    if (catEntry == "Criminal Justice System"):
                        curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, 
                            Criminal_Justice_System
                            FROM Childs_Information 
                            WHERE YEAR(Date_Submitted) = %s 
                            AND Criminal_Justice_System != '1';""", (selectedYear,))
                        temp = curr.fetchall()
            if temp:
                child = ()
                for person in temp:
                    newChild = person[0:4]

                    if person[4]:
                        newChild += ('ADD/ADHD',)
                    if person[5]:
                        newChild += ('Learning Disability',)
                    if person[6]:
                        newChild += ('Developmental Disability',)
                    if person[7]:
                        newChild += ('Mental Health Issues',)
                    if person[8]:
                        newChild += ('Other Medical Condition',)
                    if person[9]:
                        newChild += ('Victim of Abuse',)
                    if person[10]:
                        newChild += ('Criminal Justice System',)

                    child += (newChild,)

        elif selectedCategory == "Child's HERO Program Participation":

            #no year & (no cat OR Child)
            if (not yearParam) and (not programParam or selectedProgram == 'Child Application'):
                curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information;""")
                child = curr.fetchall()

            #no year & (no cat OR Camp)
            if (not yearParam) and (not programParam or selectedProgram == 'Camp High Five Application'):
                curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information;""")
                camp = curr.fetchall()

            #no year & (no cat OR Child)
            if yearParam and (not programParam or selectedProgram == 'Child Application'):
                curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information 
                    WHERE YEAR(Date_Submitted) = %s;""", (selectedYear,))
                child = curr.fetchall()

            #no year & (no cat OR Camp)
            if yearParam and (not programParam or selectedProgram == 'Camp High Five Application'):
                curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information 
                    WHERE YEAR(Date_Submitted) = %s;""", (selectedYear,))
                camp = curr.fetchall()

        elif selectedCategory == "Child's Allergies":
            #child app
            if (selectedProgram == 'Child Application'):
                tkMessageBox.showinfo("Search", "This application does not contain the category")

            #camp app
            else:
                if (catEntry == ''):
                    #no year & (no program OR camp)
                    #first, last, year, cat in camp
                    if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""
                            SELECT Allergies.ID, Allergies.Date_Submitted, Demographic_Information.First_Name, Demographic_Information.Last_Name, Allergies.Med_Reaction, 
                            Allergies.Food_Reaction, Allergies.Env_Reaction, Allergies.Type, Allergies.Allergy, Allergies.Reaction 
                            FROM Demographic_Information 
                            JOIN (
                                SELECT Allergies.ID, Allergies.Date_Submitted, Allergies.Med_Reaction, Allergies.Food_Reaction, Allergies.Env_Reaction, 
                                Med_Hist_Allergies.Type, Med_Hist_Allergies.Allergy, Med_Hist_Allergies.Reaction 
                                FROM Allergies 
                                JOIN Med_Hist_Allergies 
                                ON Allergies.ID = Med_Hist_Allergies.ID AND Allergies.Date_Submitted = Med_Hist_Allergies.Date_Submitted
                                    AND (Allergies.Med_Reaction != '' OR Allergies.Food_Reaction != '' OR Allergies.Env_Reaction != '' 
                                    OR Med_Hist_Allergies.Type != '' OR Med_Hist_Allergies.Allergy != '' OR Med_Hist_Allergies.Reaction != '')
                            ) as Allergies 
                            ON Allergies.ID = Demographic_Information.ID AND Allergies.Date_Submitted = Demographic_Information.Date_Submitted;""")
                        camp = curr.fetchall()


                    #year & (no program OR camp)
                    #first, last, cat in camp
                    if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""
                            SELECT Allergies.ID, Allergies.Date_Submitted, Demographic_Information.First_Name, Demographic_Information.Last_Name, Allergies.Med_Reaction, 
                            Allergies.Food_Reaction, Allergies.Env_Reaction, Allergies.Type, Allergies.Allergy, Allergies.Reaction 
                            FROM Demographic_Information 
                            JOIN (
                                SELECT Allergies.ID, Allergies.Date_Submitted, Allergies.Med_Reaction, Allergies.Food_Reaction, Allergies.Env_Reaction, 
                                Med_Hist_Allergies.Type, Med_Hist_Allergies.Allergy, Med_Hist_Allergies.Reaction 
                                FROM Allergies 
                                JOIN Med_Hist_Allergies 
                                ON Allergies.ID = Med_Hist_Allergies.ID AND Allergies.Date_Submitted = Med_Hist_Allergies.Date_Submitted
                                    AND (Allergies.Med_Reaction != '' OR Allergies.Food_Reaction != '' OR Allergies.Env_Reaction != '' 
                                    OR Med_Hist_Allergies.Type != '' OR Med_Hist_Allergies.Allergy != '' OR Med_Hist_Allergies.Reaction != '')
                                    AND YEAR(Allergies.Date_Submitted) = %s 
                            ) as Allergies 
                            ON Allergies.ID = Demographic_Information.ID AND Allergies.Date_Submitted = Demographic_Information.Date_Submitted;""", (selectedYear,))
                        camp = curr.fetchall()

                else:
                    #no year & (no program OR camp)
                    #first, last, year, cat in camp
                    if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""
                            SELECT Allergies.ID, Allergies.Date_Submitted, Demographic_Information.First_Name, Demographic_Information.Last_Name, Allergies.Med_Reaction, 
                            Allergies.Food_Reaction, Allergies.Env_Reaction, Allergies.Type, Allergies.Allergy, Allergies.Reaction 
                            FROM Demographic_Information 
                            JOIN (
                                SELECT Allergies.ID, Allergies.Date_Submitted, Allergies.Med_Reaction, Allergies.Food_Reaction, Allergies.Env_Reaction, 
                                Med_Hist_Allergies.Type, Med_Hist_Allergies.Allergy, Med_Hist_Allergies.Reaction 
                                FROM Allergies 
                                JOIN Med_Hist_Allergies 
                                ON Allergies.ID = Med_Hist_Allergies.ID AND Allergies.Date_Submitted = Med_Hist_Allergies.Date_Submitted
                                    AND (Allergies.Med_Reaction = %s OR Allergies.Food_Reaction = %s OR Allergies.Env_Reaction = %s 
                                    OR Med_Hist_Allergies.Type = %s OR Med_Hist_Allergies.Allergy = %s OR Med_Hist_Allergies.Reaction = %s)
                            ) as Allergies 
                            ON Allergies.ID = Demographic_Information.ID AND Allergies.Date_Submitted = Demographic_Information.Date_Submitted;""",
                             (catEntry, catEntry, catEntry, catEntry, catEntry, catEntry,))
                        camp = curr.fetchall()

                    #year & (no program OR camp)
                    #first, last, cat in camp
                    if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                        curr.execute("""
                            SELECT Allergies.ID, Allergies.Date_Submitted, Demographic_Information.First_Name, Demographic_Information.Last_Name, Allergies.Med_Reaction, 
                            Allergies.Food_Reaction, Allergies.Env_Reaction, Allergies.Type, Allergies.Allergy, Allergies.Reaction 
                            FROM Demographic_Information 
                            JOIN (
                                SELECT Allergies.ID, Allergies.Date_Submitted, Allergies.Med_Reaction, Allergies.Food_Reaction, Allergies.Env_Reaction, 
                                Med_Hist_Allergies.Type, Med_Hist_Allergies.Allergy, Med_Hist_Allergies.Reaction 
                                FROM Allergies 
                                JOIN Med_Hist_Allergies 
                                ON Allergies.ID = Med_Hist_Allergies.ID AND Allergies.Date_Submitted = Med_Hist_Allergies.Date_Submitted
                                    AND (Allergies.Med_Reaction = %s OR Allergies.Food_Reaction = %s OR Allergies.Env_Reaction = %s 
                                    OR Med_Hist_Allergies.Type = %s OR Med_Hist_Allergies.Allergy = %s OR Med_Hist_Allergies.Reaction = %s)
                                    AND YEAR(Allergies.Date_Submitted) = %s 
                            ) as Allergies 
                            ON Allergies.ID = Demographic_Information.ID AND Allergies.Date_Submitted = Demographic_Information.Date_Submitted;""",
                             (catEntry, catEntry, catEntry, catEntry, catEntry, catEntry, selectedYear,))
                        camp = curr.fetchall()

        elif selectedCategory == "Child's Years with HERO":
            if (yearParam):
                tkMessageBox.showinfo("Search", "This category does not take the year parameter")

            if (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year in child
                if ((not programParam) or (selectedProgram == 'Child Application')):
                    curr.execute("""SELECT ID, Name_First, Name_Last, COUNT(DISTINCT Year(Date_Submitted)) FROM Childs_Information GROUP BY ID, Name_First, Name_Last;""")
                    tempChild = curr.fetchall()

                #no year & no program OR no year & camp
                #first, last, year in camp
                if ((not programParam) or (selectedProgram == 'Camp High Five Application')):
                    curr.execute("""SELECT ID, First_Name, Last_Name, COUNT(DISTINCT Year(Date_Submitted)) FROM Demographic_Information GROUP BY ID, First_Name, Last_Name;""")
                    tempCamp = curr.fetchall()

            else:
                #no year & no program OR no year & child
                #
                #first, last, year in child
                if ((not programParam) or (selectedProgram == 'Child Application')):
                    curr.execute("""SELECT ID, Name_First, Name_Last, COUNT(DISTINCT Year(Date_Submitted)) FROM Childs_Information GROUP BY ID, Name_First, Name_Last;""")
                    temp = curr.fetchall()
                    tempChild = [i for i in temp if i[1] == int(catEntry)]

                #no year & no program OR no year & camp
                #first, last, year in camp
                if ((not programParam) or (selectedProgram == 'Camp High Five Application')):
                    curr.execute("""SELECT ID, First_Name, Last_Name, COUNT(DISTINCT Year(Date_Submitted)) FROM Demographic_Information GROUP BY ID, First_Name, Last_Name;""")
                    temp = curr.fetchall()
                    tempCamp = [i for i in temp if i[1] == int(catEntry)]

            if tempChild:
                child = ()
                for person in tempChild:
                    newChild = (person[0], 'NA', person[1], person[2], person[3])
                    child += (newChild,)
            
            if tempCamp:
                camp = ()
                for person in tempCamp:
                    newCamp = (person[0], 'NA', person[1], person[2], person[3])
                    camp += (newCamp,)

        elif selectedCategory == "Household Composition":
            if (catEntry):
                tkMessageBox.showinfo("Search", "This category does not take specific category parameters")
            else:
                #no year
                #first, last, year, cat in child
                if ((not yearParam)):
                    curr.execute("""
                        SELECT  Childs_Information.ID, Childs_Information.Date_Submitted, Childs_Information.Name_First, Childs_Information.Name_Last,
                        Household_Information.Name, Household_Information.Relationship, Household_Information.Sex, Household_Information.Age, Household_Information.HIV_Status
                        FROM Household_Information
                        JOIN Childs_Information
                        ON Childs_Information.ID = Household_Information.ID AND Childs_Information.Date_Submitted = Household_Information.Date_Submitted
                            AND (Household_Information.Name != '' OR Household_Information.Relationship != '' OR Household_Information.Sex != '' OR Household_Information.Age != '' OR Household_Information.HIV_Status != '');""")
                    child = curr.fetchall()

                else:
                #year
                #first, last, cat in child
                    curr.execute("""
                        SELECT  Childs_Information.ID, Childs_Information.Date_Submitted, Childs_Information.Name_First, Childs_Information.Name_Last,
                        Household_Information.Name, Household_Information.Relationship, Household_Information.Sex, Household_Information.Age, Household_Information.HIV_Status
                        FROM Household_Information
                        JOIN Childs_Information
                        ON Childs_Information.ID = Household_Information.ID AND Childs_Information.Date_Submitted = Household_Information.Date_Submitted
                            AND (Household_Information.Name != '' OR Household_Information.Relationship != '' OR Household_Information.Sex != '' OR Household_Information.Age != '' OR Household_Information.HIV_Status != '')
                            AND YEAR(Date_Submitted) = %s;""", (selectedYear,))
                    child = curr.fetchall()

        elif selectedCategory == "Parent(s) HIV Status (infected or affected)":
            if (catEntry):
                #no year
                #first, last, year, cat in child
                if ((not yearParam)):
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last, 
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.HIV_Status as HIV_Status FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted
                        AND Parent_Guardian_Information.HIV_Status as HIV_Status = %s;""", (catEntry,))
                    child = curr.fetchall()
                else:
                #year
                #first, last, cat in child
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last, 
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.HIV_Status as HIV_Status FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted
                        AND Parent_Guardian_Information.HIV_Status as HIV_Status = %s
                        AND YEAR(Parent_Guardian_Information.Date_Submitted) = %s;""", (catEntry, selectedYear,))
                    child = curr.fetchall()
            else:
                #no year
                #first, last, year, cat in child
                if ((not yearParam)):
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.HIV_Status as HIV_Status FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted;""")
                    child = curr.fetchall()
                else:
                #year
                #first, last, cat in child
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.HIV_Status as HIV_Status FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted 
                        AND YEAR(Parent_Guardian_Information.Date_Submitted) = %s;""", (selectedYear,))
                    child = curr.fetchall()

        elif selectedCategory == "Household Income Range":

            if (catEntry == ''):
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if (not yearParam):
                    curr.execute("""SELECT Fam_Annual_Income.ID as ID, Fam_Annual_Income.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last, 
                        Fam_Annual_Income.Fam_Annual_Income as Fam_Annual_Income
                        FROM Fam_Annual_Income 
                        JOIN Childs_Information ON Fam_Annual_Income.ID = Childs_Information.ID 
                        AND Fam_Annual_Income.Date_Submitted = Childs_Information.Date_Submitted;""")
                    child = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam):
                    curr.execute("""SELECT Fam_Annual_Income.ID as ID, Fam_Annual_Income.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last, 
                        Fam_Annual_Income.Fam_Annual_Income as Fam_Annual_Income
                        FROM Fam_Annual_Income 
                        JOIN Childs_Information ON Fam_Annual_Income.ID = Childs_Information.ID 
                        AND Fam_Annual_Income.Date_Submitted = Childs_Information.Date_Submitted
                        AND YEAR(Fam_Annual_Income.Date_Submitted) = %s;""", (selectedYear,))
                    child = curr.fetchall()

            else:
                #no year & no program OR no year & child
                #first, last, year, cat in child
                if (not yearParam):
                    curr.execute("""SELECT Fam_Annual_Income.ID as ID, Fam_Annual_Income.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Fam_Annual_Income.Fam_Annual_Income as Fam_Annual_Income
                        FROM Fam_Annual_Income 
                        JOIN Childs_Information ON Fam_Annual_Income.ID = Childs_Information.ID 
                        AND Fam_Annual_Income.Date_Submitted = Childs_Information.Date_Submitted AND Fam_Annual_Income.Fam_Annual_Income = %s;""", (catEntry,))
                    child = curr.fetchall()

                #year & no program OR year & child
                #first, last, cat in child
                if (yearParam):
                    curr.execute("""SELECT Fam_Annual_Income.ID as ID, Fam_Annual_Income.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Fam_Annual_Income.Fam_Annual_Income as Fam_Annual_Income
                        FROM Fam_Annual_Income 
                        JOIN Childs_Information ON Fam_Annual_Income.ID = Childs_Information.ID 
                        AND Fam_Annual_Income.Date_Submitted = Childs_Information.Date_Submitted AND Fam_Annual_Income.Fam_Annual_Income = %s
                        AND YEAR(Fam_Annual_Income.Date_Submitted) = %s;""", (catEntry, selectedYear,))
                    child = curr.fetchall()

        elif selectedCategory == "Household Income Source":
            if (catEntry == ''):
                #no year
                #first, last, year, cat in child
                if (not yearParam):
                    curr.execute("""SELECT Source_Fam_Income.ID as ID, Source_Fam_Income.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Source_Fam_Income.Source_Fam_Income as Fam_Annual_Income, Source_Fam_Income.Other as Other
                        FROM Source_Fam_Income 
                        JOIN Childs_Information ON Source_Fam_Income.ID = Source_Fam_Income.ID 
                        AND Source_Fam_Income.Date_Submitted = Childs_Information.Date_Submitted;""")
                    child = curr.fetchall()

                #year
                else:
                    curr.execute("""SELECT Source_Fam_Income.ID as ID, Source_Fam_Income.Date_Submitted as Date_Subbmitted,
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last, 
                        Source_Fam_Income.Source_Fam_Income as Fam_Annual_Income, Source_Fam_Income.Other as Other
                        FROM Source_Fam_Income 
                        JOIN Childs_Information ON Source_Fam_Income.ID = Source_Fam_Income.ID 
                        AND Source_Fam_Income.Date_Submitted = Childs_Information.Date_Submitted
                        AND YEAR(Source_Fam_Income.Date_Submitted) = %s;""", (selectedYear,))
                    child = curr.fetchall()

            else:
                #no year
                #first, last, year, cat in child
                if (not yearParam):
                    curr.execute("""SELECT Source_Fam_Income.ID as ID, Source_Fam_Income.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last, 
                        Source_Fam_Income.Source_Fam_Income as Fam_Annual_Income, Source_Fam_Income.Other as Other
                        JOIN Childs_Information ON Source_Fam_Income.ID = Source_Fam_Income.ID 
                        AND Source_Fam_Income.Date_Submitted = Childs_Information.Date_Submitted
                        AND (Source_Fam_Income.Source_Fam_Income = %s OR Source_Fam_Income.Other = %s);""", (catEntry, catEntry))
                    child = curr.fetchall()

                #year
                else:
                    curr.execute("""SELECT Source_Fam_Income.ID as ID, Source_Fam_Income.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last, 
                        Source_Fam_Income.Source_Fam_Income as Fam_Annual_Income, Source_Fam_Income.Other as Other
                        JOIN Childs_Information ON Source_Fam_Income.ID = Source_Fam_Income.ID 
                        AND Source_Fam_Income.Date_Submitted = Childs_Information.Date_Submitted
                        AND (Source_Fam_Income.Source_Fam_Income = %s OR Source_Fam_Income.Other = %s)
                        AND YEAR(Source_Fam_Income.Date_Submitted) = %s;""", (catEntry, catEntry, selectedYear))
                    child = curr.fetchall()

        elif selectedCategory == "Parent(s) Highest Level of Education":
            if (catEntry):
                #no year
                #first, last, year, cat in child
                if ((not yearParam)):
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted,
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,  
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.Education_Completed as Education_Completed
                        FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted
                        AND Parent_Guardian_Information.Education_Completed = %s;""", (catEntry))
                    child = curr.fetchall()
                else:
                #year
                #first, last, cat in child
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.Education_Completed as Education_Completed
                        FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted 
                        AND Parent_Guardian_Information.Education_Completed = %s
                        AND YEAR(Parent_Guardian_Information.Date_Submitted) = %s;""", (catEntry, selectedYear,))
                    child = curr.fetchall()

            else:
                #no year
                #first, last, year, cat in child
                if ((not yearParam)):
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.Education_Completed as Education_Completed 
                        FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted;""")
                    child = curr.fetchall()
                else:
                #year
                #first, last, cat in child
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.Education_Completed as Education_Completed
                        FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted 
                        AND YEAR(Parent_Guardian_Information.Date_Submitted) = %s;""", (selectedYear,))
                    child = curr.fetchall()

        elif selectedCategory == "Parent(s) Employment Status":
            if (catEntry):
                #no year
                #first, last, year, cat in child
                if ((not yearParam)):
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.Employment_Status as Employment_Status
                        FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted
                        AND Parent_Guardian_Information.Employment_Status = %s;""", (catEntry))
                    child = curr.fetchall()
                else:
                #year
                #first, last, cat in child
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.Employment_Status as Employment_Status
                        FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted 
                        AND Parent_Guardian_Information.Employment_Status = %s
                        AND YEAR(Parent_Guardian_Information.Date_Submitted) = %s;""", (catEntry, selectedYear,))
                    child = curr.fetchall()

            else:
                #no year
                #first, last, year, cat in child
                if ((not yearParam)):
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.Employment_Status as Employment_Status
                        FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted;""")
                    child = curr.fetchall()
                else:
                #year
                #first, last, cat in child
                    curr.execute("""SELECT Parent_Guardian_Information.ID as ID, Parent_Guardian_Information.Date_Submitted as Date_Subbmitted, 
                        Childs_Information.Name_First as Name_First, Childs_Information.Name_Last as Name_Last,
                        Parent_Guardian_Information.Relationship_to_Child as Relationship_to_Child, 
                        Parent_Guardian_Information.Employment_Status as Employment_Status
                        FROM Parent_Guardian_Information 
                        JOIN Childs_Information ON Parent_Guardian_Information.ID = Childs_Information.ID 
                        AND Parent_Guardian_Information.Date_Submitted = Childs_Information.Date_Submitted 
                        AND YEAR(Parent_Guardian_Information.Date_Submitted) = %s;""", (selectedYear,))
                    child = curr.fetchall()
        

        curr.close()
        db.close()
        
        #need to implement dynamic tracking of count
        countText = len(child) + len(camp)
        count = Label(master, text = "Total: " + str(countText))
        count.grid(row = 0, column = 4)

        back = Button(master, text = "Back", command = lambda:self.SearchPage())
        back.grid(row = 0, column = 0)

        r = 2
        idHead = Label(master, text = "ID", font= "Verdana 10 underline")
        idHead.grid(row = r, column = 0)

        dateHead = Label(master, text = "Date Submitted", font= "Verdana 10 underline")
        dateHead.grid(row = r, column = 1)

        nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = r, column = 2)

        critHead = Label(master, text = "Criteria", font= "Verdana 10 underline")
        critHead.grid(row = r, column = 3)

        r = r+1
        childHead = Label(master, text = "Child App", font= "Verdana 10 underline")
        childHead.grid(row = r, column = 0)

        r = r+1
        if (child):
            for num in child:

                ID = Label(master, text = num[0])
                ID.grid(row = r, column = 0)

                Date_Submitted = Label(master, text = num[1])
                Date_Submitted.grid(row = r, column = 1)

                nameText = ''
                if (num[2] is not None):
                    nameText += num[2]
                if (num[3] is not None):
                    if (nameText != ''):
                        nameText += ' '
                    nameText += num[3]
                Name = Label(master, text = nameText
                    )
                Name.grid(row = r, column = 2)

                criteriaText = ''
                if (len(num) > 4):
                    for i in range(len(num) - 4):
                        if num[4+i] is not None:
                            criteriaText += str(num[4+i])
                            criteriaText += ', '

                    criteriaText = criteriaText[:-2]
                
                criteria = Label(master, text = criteriaText)
                criteria.grid(row = r, column = 3)

                profBut = Button(master, text = "See Profile", command = lambda ID = num[0]: self.FirstProfilePage(ID))
                profBut.grid(row = r, column = 4)
                r = r+1

        else:
                childNope = Label(master, text = "None")
                childNope.grid(row = r, column = 0)

        r = r+1
        campHead = Label(master, text = "Camper App", font= "Verdana 10 underline")
        campHead.grid(row = r, column = 0)
        
        r = r+1
        if(camp):
            for num in camp:
                ID = Label(master, text = num[0])
                ID.grid(row = r, column = 0)

                Date_Submitted = Label(master, text = num[1])
                Date_Submitted.grid(row = r, column = 1)

                nameText = ''
                if (num[2] is not None):
                    nameText += num[2]
                if (num[3] is not None):
                    if (nameText != ''):
                        nameText += ' '
                    nameText += num[3]
                Name = Label(master, text = nameText
                    )
                Name.grid(row = r, column = 2)

                criteriaText = ''
                if (len(num) > 4):
                    for i in range(len(num) - 4):
                        if num[4+i] is not None:
                            criteriaText += str(num[4+i])
                            criteriaText += ', '
                            
                    criteriaText = criteriaText[:-2]
                
                criteria = Label(master, text = criteriaText)
                criteria.grid(row = r, column = 3)

                profBut = Button(master, text = "See Profile", command = lambda ID = num[0]: self.FirstProfilePage(ID))
                profBut.grid(row = r, column = 4)
                r = r+1

        else:
                campNope = Label(master, text = "None")
                campNope.grid(row = r, column = 0)

#******************************************************************************************************************************************************

    def SearchNamePage(self, selectedProgram, selectedYear, firstName, lastName):

        self.SearchNamePageRoot = Toplevel()
        root = self.SearchNamePageRoot
        if self.PrevPage is 'SearchPage':
            self.SearchPageRoot.withdraw()
        self.PrevPage = 'SearchNamePage'
        
        root.title("Search Results Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        camp = ''
        child = ''

        db = MySQLdb.connect(host="localhost", user="root", passwd="Darling", db="HERO")
        curr = db.cursor()

        #check for program selection
        programParam = 1
        if (selectedProgram == 'Program') or (selectedProgram == 'None'):
            #no program input
            programParam = 0

        #check for year selection
        yearParam = 1
        if (selectedYear == 'Year') or (selectedYear == 'None'):
            #no year input
            yearParam = 0
        else:
            selectedYear = selectedYear[1:5]

        #no year
        if (not yearParam):

            #no program or child
            if ((not programParam) or (selectedProgram == 'Child Application')):
                


                #no first, no last
                if ((not firstName) and (not lastName)):
                    curr.execute("SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information;")
                    child = curr.fetchall()
                
                #yes first, no last
                elif (not lastName):
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information 
                        WHERE Name_First = %s;""", (firstName,))
                    child = curr.fetchall()

                #no first, yes last
                elif (not firstName):
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information
                        WHERE Name_Last = %s;""", (lastName,))
                    child = curr.fetchall()

                #yes first, yes last
                else:
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information
                        WHERE Name_First = %s AND Name_Last = %s;""", (firstName, lastName,))
                    child = curr.fetchall()

            #no program or camp
            if ((not programParam) or (selectedProgram == 'Camp High Five Application')):
                
                #no first, no last
                if ((not firstName) and (not lastName)):
                    curr.execute("SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information;")
                    camp = curr.fetchall()

                #yes first, no last
                elif (not lastName):
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information 
                        WHERE First_Name = %s;""", (firstName,))
                    camp = curr.fetchall()

                #no first, yes last
                elif (not firstName):
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information
                        WHERE Last_Name = %s;""", (lastName,))
                    camp = curr.fetchall()

                #yes first, yes last
                else:
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information
                        WHERE First_Name = %s AND Last_Name = %s;""", (firstName, lastName,))
                    camp = curr.fetchall()

        #yes year
        else:

            #no program or child
            if ((not programParam) or (selectedProgram == 'Child Application')):
                
                #no first, no last
                if ((not firstName) and (not lastName)):
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information
                        WHERE YEAR(Date_Submitted) = %s;""", (selectedYear,))
                    child = curr.fetchall()

                #yes first, no last
                elif (not lastName):
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information
                        WHERE Name_First = %s AND YEAR(Date_Submitted) = %s;""", (firstName, selectedYear,))
                    child = curr.fetchall()

                #no first, yes last
                elif (not firstName):
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information
                        WHERE Name_Last = %s AND YEAR(Date_Submitted) = %s;""", (lastName, selectedYear,))
                    child = curr.fetchall()

                #yes first, yes last
                else:
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information
                        WHERE Name_First = %s AND Name_Last = %s AND YEAR(Date_Submitted) = %s;""", (firstName, lastName, selectedYear,))
                    child = curr.fetchall()

            #no program or camp
            if ((not programParam) or (selectedProgram == 'Camp High Five Application')):
                
                #no first, no last
                if ((not firstName) and (not lastName)):
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information
                         WHERE YEAR(Date_Submitted) = %s;""", (selectedYear,))
                    camp = curr.fetchall()

                #yes first, no last
                elif (not lastName):
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information
                        WHERE First_Name = %s AND YEAR(Date_Submitted) = %s;""", (firstName, selectedYear,))
                    camp = curr.fetchall()

                #no first, yes last
                elif (not firstName):
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information
                        WHERE Last_Name = %s AND YEAR(Date_Submitted) = %s;""", (lastName, selectedYear,))
                    camp = curr.fetchall()

                #yes first, yes last
                else:
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information
                        WHERE First_Name = %s AND Last_Name = %s AND YEAR(Date_Submitted) = %s;""", (firstName, lastName, selectedYear,))
                    camp = curr.fetchall()

        curr.close()
        db.close()

        #need to implement dynamic tracking of count
        countText = len(child) + len(camp)
        count = Label(master, text = "Total: " + str(countText))
        count.grid(row = 0, column = 4)

        back = Button(master, text = "Back", command = lambda:self.SearchPage())
        back.grid(row = 0, column = 0)

        r = 2
        idHead = Label(master, text = "ID", font= "Verdana 10 underline")
        idHead.grid(row = r, column = 0)

        dateHead = Label(master, text = "Date Submitted", font= "Verdana 10 underline")
        dateHead.grid(row = r, column = 1)


        nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = r, column = 2)

        r = r+1
        childHead = Label(master, text = "Child App", font= "Verdana 10 underline")
        childHead.grid(row = r, column = 0)

        r = r+1
        if (child):
            for num in child:
                ID = Label(master, text = num[0])
                ID.grid(row = r, column = 0)

                Date_Submitted = Label(master, text = num[1])
                Date_Submitted.grid(row = r, column = 1)

                nameText = ''
                if (num[2] is not None):
                    nameText += num[2]
                if (num[3] is not None):
                    if (nameText != ''):
                        nameText += ' '
                    nameText += num[3]
                Name = Label(master, text = nameText
                    )
                Name.grid(row = r, column = 2)

                profBut = Button(master, text = "See Profile", command = lambda ID = num[0]: self.FirstProfilePage(ID))
                profBut.grid(row = r, column = 4)

                r = r+1
        
        else:
                childNope = Label(master, text = "None")
                childNope.grid(row = r, column = 0)

        r = r+1
        campHead = Label(master, text = "Camper App", font= "Verdana 10 underline")
        campHead.grid(row = r, column = 0)
        
        r = r+1
        if(camp):
            for num in camp:
                ID = Label(master, text = num[0])
                ID.grid(row = r, column = 0)

                Date_Submitted = Label(master, text = num[1])
                Date_Submitted.grid(row = r, column = 1)

                nameText = ''
                if (num[2] is not None):
                    nameText += num[2]
                if (num[3] is not None):
                    if (nameText != ''):
                        nameText += ' '
                    nameText += num[3]
                Name = Label(master, text = nameText
                    )
                Name.grid(row = r, column = 2)

                profBut = Button(master, text = "See Profile", command = lambda ID = num[0]: self.FirstProfilePage(ID))
                profBut.grid(row = r, column = 4)
                r = r+1

        else:
                campNope = Label(master, text = "None")
                campNope.grid(row = r, column = 0)

#******************************************************************************************************************************************************

    def FirstProfilePage(self, id):

        self.FirstProfilePageRoot = Toplevel()
        root = self.FirstProfilePageRoot
        if self.PrevPage is 'SearchCatPage':
            self.SearchCatPageRoot.withdraw()
        if self.PrevPage is 'SearchNamePage':
            self.SearchNamePageRoot.withdraw()
        if self.PrevPage is 'SecondChildProfilePage':
            self.SecondChildProfilePageRoot.withdraw()
        root.title("First Level Profile Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        db = self.connect()
        curr = db.cursor()

        #Get the name from the database
        curr.execute("SELECT Name_First, Name_Last FROM Childs_Information WHERE ID = %s;", (id,))
        name = curr.fetchall()
        if name is None:
            curr.execute("SELECT First_Name, Last_Name FROM Demographic_Information WHERE ID = %s;", (id,))
            name = curr.fetchall()        

        if name is not ():
            name_first = name[0][0]
            name_last = name[0][1]
        else:
            name_first = ''
            name_last = ''

        # Back button will take you to previous page
        back = Button(master, text="Back", command = lambda: self.backFirstProfilePage())
        back.grid(row=0, column=0)

        delete = Button(master, text="Delete", command=lambda: self.deleteProfile(id))
        delete.grid(row=0, column=10)

        #name title
        firstNameLabel = Label(master, text= name_first, font="Arial 12 underline").grid(row=1, column=3)
        lastNameLabel = Label(master, text= name_last, font="Arial 12 underline").grid(row=1, column=4)

        #child app
        childAppLabel = Label(master, text= "Child Applications").grid(row=2, column=0)

        curr.execute("SELECT Date_Submitted FROM Child_Application WHERE ID = %s;", (id,))
        childDateArr = curr.fetchall()

        r = 3
        for childDate in childDateArr:
            #date of program attended
            dateLabel = Label(master, text= childDate[0]).grid(row=r, column=1)

            # Details button will take you to another page
            details = Button(master, text="See Details", command=lambda childDate = childDate[0]: self.seeDetails(id, childDate)).grid(row=r, column=5)
            r = r + 1

        #camp app
        campAppLabel = Label(master, text= "Camp Applications").grid(row=r, column=0)

        curr.execute("SELECT Date_Submitted FROM Camp_Application WHERE ID = %s;", (id,))
        campDateArr = curr.fetchall()

        r = r + 1
        for campDate in campDateArr:
            #date of program attended
            dateLabel = Label(master, text= campDate[0]).grid(row=r, column=1)

            # Details button will take you to another page
            details = Button(master, text="See Details", command=lambda campDate = campDate[0]: self.seeDetails(id, campDate)).grid(row=r, column=5)
            r = r + 1

        curr.close()
        db.close()

    def backFirstProfilePage(self):
        self.PrevPage = 'FirstProfilePage'
        self.SearchPage()

    def seeDetails(self, id, date):
        self.PrevPage = 'FirstProfilePage'
        self.SecondChildProfilePage(id, date)

    def deleteProfile(self, id):

        if askyesno('Verify', 'Really delete?'):
            #Delete application from database

            db = self.connect()
            curr = db.cursor()
            curr.execute("DELETE FROM Child WHERE ID = %s;", (id,))
            db.commit()
            curr.close()
            db.close()

            tkMessageBox.showinfo("Delete Profile","Profile deletion was successful.")

            self.backFirstProfilePage()

        else:
            #Delete cancelled
            showinfo('No', 'Delete has been cancelled')

#******************************************************************************************************************************************************

    def SecondChildProfilePage(self, id, date):

        #setup
        self.SecondChildProfilePageRoot = Toplevel()
        root = self.SecondChildProfilePageRoot
        if self.PrevPage is 'FirstProfilePage':
            self.FirstProfilePageRoot.withdraw()
        elif self.PrevPage is 'EditChildProfilePage':
            self.EditChildProfilePageRoot.withdraw()
        
        root.title("Second Level Profile Page")

        self.canvas = Canvas(root)
        master = Frame(self.canvas)

        scrollbarY = Scrollbar(root, orient = "vertical", command = self.canvas.yview)
        scrollbarY.pack(side = RIGHT, fill = Y)
        scrollbarX = Scrollbar(root, orient = "horizontal", command = self.canvas.xview)
        scrollbarX.pack(side = BOTTOM, fill = X)

        self.canvas.configure(xscrollcommand = scrollbarX.set, yscrollcommand = scrollbarY.set)
        self.canvas.pack(side = "left", fill = "both", expand = True)
        self.canvas.create_window((4,4), window = master, anchor="nw", 
                                  tags="master")

        master.bind("<Configure>", self.onFrameConfigure)
        root.geometry("740x1000")


        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Buttons
        #back button frame + back button
        buttonframe = Frame(master)
        buttonframe.pack(side = "top", fill = "x")


        #fix alignment
        backButton = Button(buttonframe, text = "Back", command = lambda: self.backSecondChildProfilePage(id))
        backButton.pack(side = "left")

        #edit
        editButton = Button(buttonframe, text = "Edit Application", command = lambda: self.editProfilePageButton(id, date))
        editButton.pack(side = "right")

        #delete
        deleteButton = Button(buttonframe, text = "Delete Application", command = lambda: self.deleteChildApp(id, date))
        deleteButton.pack(side = "right")

#Database dump frame
        ChildInfoSectionframe = Frame(master)
        ChildInfoSectionframe.pack(fill = 'y', side = 'left') 

#Identifying Info Section
        #header
        labelChildInfoSection = Label(ChildInfoSectionframe, text = "\nIDENTIFYING INFORMATION")
        labelChildInfoSection.pack(fill = "x")
        labelChildInfoSection.config(font=("Helvetica", 20))

        #id
        label = Label(ChildInfoSectionframe, text = "\nChild ID.................................................................................................. " + str(id))
        label.pack(anchor = 'w')

        #date
        label = Label(ChildInfoSectionframe, text = "\nDate Submitted...................................................................................... " + str(date))
        label.pack(anchor = 'w')

        #first name
        curr.execute("SELECT Name_First FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #last name
        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nLast Name  ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #nickname
        curr.execute("SELECT Name_Nickname FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nNickname .............................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nNickname .............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #address street
        curr.execute("SELECT Address_Street FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address city
        curr.execute("SELECT Address_City FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nCity ....................................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nCity ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address county
        curr.execute("SELECT Address_County FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nCounty .................................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nCounty .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                
        #address zip
        curr.execute("SELECT Address_Zip FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #home phone
        curr.execute("SELECT Home_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #guardian phone
        curr.execute("SELECT Guardian_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #guardian email
        curr.execute("SELECT Guardian_Email FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #age
        curr.execute("SELECT Age FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nAge ....................................................................................................... " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nAge ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                
        #birthday
        curr.execute("SELECT Birthday FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #gender
        curr.execute("SELECT Gender FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nGender .................................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nGender .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #HIV status
        curr.execute("SELECT HIV_Status FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHIV status ............................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nHIV status ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #aware
        label = Label(ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.pack(anchor = 'w')
        curr.execute("SELECT Aware FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... Yes')
            else:
                label = Label(ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... No')
        else:
            label = Label(ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... Unanswered')
        label.pack(anchor = 'w')
        
        #why
        label = Label(ChildInfoSectionframe, text = "\nIf no,")
        label.pack(anchor = 'w')
        curr.execute("SELECT Why FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "please provide a reason why child is not aware ...................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "please provide a reason why child is not aware ...................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Referral source
        curr.execute("SELECT Referral_Source FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #school attending
        curr.execute("SELECT School_attending FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Grade Level
        curr.execute("SELECT School_grade_level FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Ethnicity
        curr.execute("SELECT Ethnicity_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        ethnicityOther = curr.fetchall()[0][0]
        if ethnicityOther is not None:
            label = Label(ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... " + ethnicityOther)
        else:
            curr.execute("SELECT Ethnicity FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            ethnicity = curr.fetchall()[0][0]
            if ethnicity is not None:
                label = Label(ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... " + ethnicity)
            else:
                label = Label(ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Even been...
        label = Label(ChildInfoSectionframe, text = "\nHas your child ever been...")
        label.pack(anchor = 'w')

        #ADD_ADHD
        curr.execute("SELECT ADD_ADHD FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. Yes')
            else:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. No')
        else:
            label = Label(ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. Unanswered')
        label.pack(anchor = 'w')
        
        #Learning_Disability
        curr.execute("SELECT Learning_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... Yes')
            else:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... No')
        else:
            label = Label(ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... Unanswered')
        label.pack(anchor = 'w')
        
        #Developmental_Disability
        curr.execute("SELECT Developmental_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... Yes')
            else:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... No')
        else:
            label = Label(ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... Unanswered')
        label.pack(anchor = 'w')
        
        #Mental_Health_Issues
        curr.execute("SELECT Mental_Health_Issues FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. Yes')
            else:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. No')
        else:
            label = Label(ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. Unanswered')
        label.pack(anchor = 'w')
        
        #Other_Medical_Condition
        curr.execute("SELECT Other_Medical_Condition FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... Yes')
            else:
                label = Label(ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... No')
        else:
            label = Label(ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... Unanswered')
        label.pack(anchor = 'w')
        
        #Victim_of_Abuse
        curr.execute("SELECT Victim_of_Abuse FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... Yes')
            else:
                label = Label(ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... No')
        else:
            label = Label(ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... Unanswered')
        label.pack(anchor = 'w')
        
        #Criminal_Justice_System
        curr.execute("SELECT Criminal_Justice_System FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... Yes')
            else:
                label = Label(ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... No')
        else:
            label = Label(ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... Unanswered')
        label.pack(anchor = 'w')
        
        #Custody
        curr.execute("SELECT Custody_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        custodyOther = curr.fetchall()[0][0]
        if custodyOther is not None:
            label = Label(ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... " + custodyOther)
        else:
            curr.execute("SELECT Legal_Custody FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            custody = curr.fetchall()[0][0]
            if custody is not None:
                label = Label(ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... " + custody)
            else:
                label = Label(ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... Unanswered")
        label.pack(anchor = 'w')

#Parent/ Guardian Section
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Last Name
        curr.execute("SELECT Name_Last FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................ " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Age
        curr.execute("SELECT Age FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nAge ....................................................................................................... " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nAge ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #HIV Status
        curr.execute("SELECT HIV_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Adoptive Parent
        curr.execute("SELECT Adoptive_Parent FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... Unanswered")
        label.pack(anchor = 'w')
                
        #Marital Status
        curr.execute("SELECT Marital_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Highest Level of Education Completed
        curr.execute("SELECT Education_Completed FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Employment Status
        curr.execute("SELECT Employment_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Employment Company
        label = Label(ChildInfoSectionframe, text = "\nIf employed,")
        label.pack(anchor = 'w')
        
        curr.execute("SELECT Employment_Company_Name FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "please provide Company Name ............................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "please provide Company Name ............................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Address
        curr.execute("SELECT Address_Street FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nAddress ................................................................................................ " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nAddress ................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #City
        curr.execute("SELECT Address_City FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nCity ...................................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nCity ...................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #State
        curr.execute("SELECT Address_State FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nState .................................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nState .................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Zip
        curr.execute("SELECT Address_Zip FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Work Phone
        curr.execute("SELECT WorkPhone FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #E-mail
        curr.execute("SELECT Email FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nE-mail ................................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nE-mail ................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
#Absent Parent Info
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Last Name
        curr.execute("SELECT Name_Last FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Telephone
        curr.execute("SELECT Telephone FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nTelephone .............................................................................................. " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nTelephone .............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Home Address
        curr.execute("SELECT Address_Street FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #City
        curr.execute("SELECT Address_City FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nCity ....................................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nCity ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #County
        curr.execute("SELECT Address_County FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nCounty .................................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nCounty .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Zip
        curr.execute("SELECT Address_Zip FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nZip ......................................................................................................... " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nZip ......................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #HIV Status
        curr.execute("SELECT HIV_Status FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHIV Status ............................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nHIV Status ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
#Household Info
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nHOUSEHOLD INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #list all individuals living in the household
        label = Label(ChildInfoSectionframe, text = "\nAll Individuals Living in the Household")
        label.pack(anchor = 'w')

        curr.execute("SELECT Count FROM Household_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        countArr = curr.fetchall()
        for count in countArr:
            #Name
            curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... " + val)
            else:
                label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... Unanswered")
            label.pack(anchor = 'w')
                    
            #Relationship to Child
            curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. " + val)
            else:
                label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. Unanswered")
            label.pack(anchor = 'w')
                                
            #Sex
            curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... " + val)
            else:
                label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... Unanswered")
            label.pack(anchor = 'w')
                                
            #Age
            curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... " + str(val))
            else:
                label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... Unanswered")
            label.pack(anchor = 'w')
                    
            #HIV Status
            curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ " + str(val) + "\n")
            else:
                label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ Unanswered\n")
            label.pack(anchor = 'w')
                    
        #Family Annual Income Info
        curr.execute("SELECT Fam_Annual_Income FROM Fam_Annual_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Source of Family Income
        curr.execute("SELECT Other FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        sourceOther = curr.fetchall()[0][0]
        if sourceOther is not None:
            label = Label(ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... " + sourceOther)
        else:
            curr.execute("SELECT Source_Fam_Income FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            source = curr.fetchall()[0][0]
            if source is not None:
                label = Label(ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... " + source)
            else:
                label = Label(ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... Unanswered")
        label.pack(anchor = 'w')
         
 #In Case of Emergency Contact
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #Last Name
        curr.execute("SELECT Name_Last FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................ " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
        #Relationship to Child
        curr.execute("SELECT Relationship_to_Child FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nRelationship to Child ............................................................................. " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nRelationship to Child ............................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #Home Address
        curr.execute("SELECT Address_Street FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #City
        curr.execute("SELECT Address_City FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nCity ...................................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nCity ...................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #State
        curr.execute("SELECT Address_State FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nState ..................................................................................................... " + val)
        else:
            label = Label(ChildInfoSectionframe, text = "\nState ..................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Zip
        curr.execute("SELECT Address_Zip FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
        #Home Phone Number
        curr.execute("SELECT Phone_Home FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #Cell Phone Number
        curr.execute("SELECT Phone_Cell FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Alternate Phone Number
        curr.execute("SELECT Phone_Alt FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... " + str(val))
        else:
            label = Label(ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
#H.E.R.O. Programs
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #Program(s) you wish your child to participate in
        curr.execute("SELECT HERO_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]
        if var is not None:
            label = Label(ChildInfoSectionframe, text = "\nProgram(s) you wish your child to participate in .................................... " + var)
        else:
            label = Label(ChildInfoSectionframe, text = "\nProgram(s) you wish your child to participate in .................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Program(s) you would be interested in your child to participating in
        curr.execute("SELECT Future_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        programs = curr.fetchall()[0][0]
        curr.execute("SELECT Future_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        otherPrograms = curr.fetchall()[0][0]
        if programs is not None and otherPrograms is not None:
            label = Label(ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... " + programs + ": " + otherPrograms)
        elif programs is not None:
            label = Label(ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... " + programs)
        else:
            label = Label(ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... Unanswered")
        label.pack(anchor = 'w')
                    
#Referral Needs
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #Needs
        curr.execute("SELECT Referral FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        Referral = curr.fetchall()[0][0]
        curr.execute("SELECT Referral_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        otherReferral = curr.fetchall()[0][0]
        if Referral is not None and otherReferral is not None:
            label = Label(ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... " + Referral + ": " + otherReferral)
        elif Referral is not None:
            label = Label(ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... " + Referral)
        else:
            label = Label(ChildInfoSectionframe, text = "\nReferral Needs ........................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
#Statement of Understanding
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))
        
        #one
        curr.execute("SELECT Statement_One FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Signed")
            else:
                label = Label(ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Unsigned")
        else:
            label = Label(ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #two
        curr.execute("SELECT Statement_Two FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Signed")
            else:
                label = Label(ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Unsigned")
        else:
            label = Label(ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #three
        curr.execute("SELECT Statement_Three FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Signed")
            else:
                label = Label(ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Unsigned")
        else:
            label = Label(ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #four
        curr.execute("SELECT Statement_Four FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Signed")
            else:
                label = Label(ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Unsigned")
        else:
            label = Label(ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #five
        curr.execute("SELECT Statement_Five FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Signed")
            else:
                label = Label(ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Unsigned")
        else:
            label = Label(ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #six
        curr.execute("SELECT Statement_Six FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Signed")
            else:
                label = Label(ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Unsigned")
        else:
            label = Label(ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #seven
        curr.execute("SELECT Statement_Seven FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Signed")
            else:
                label = Label(ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Unsigned")
        else:
            label = Label(ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
#Signature
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nSIGNATURE")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        curr.execute("SELECT Signature FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(ChildInfoSectionframe, text = "\nSignature .............................................................................................. Signed")
            else:
                label = Label(ChildInfoSectionframe, text = "\nSignature .............................................................................................. Unsigned")
        else:
            label = Label(ChildInfoSectionframe, text = "\nSignature .............................................................................................. Unanswered")
        label.pack(anchor = 'w')

#Close Database Connection
        curr.close()
        db.close()

    def backSecondChildProfilePage(self, id):
        self.PrevPage = 'SecondChildProfilePage'
        self.FirstProfilePage(id)


    def editProfilePageButton(self, id, date):
        self.PrevPage = 'SecondChildProfilePage'
        self.EditChildProfilePage(id, date)

#******************************************************************************************************************************************************

    def EditChildProfilePage(self, id, date):

        #setup
        self.EditChildProfilePageRoot = Toplevel()
        root = self.EditChildProfilePageRoot
        if self.PrevPage is 'SecondChildProfilePage':
            self.SecondChildProfilePageRoot.withdraw()
        
        root.title("Edit Child Profile Page")

        self.canvas = Canvas(root)
        master = Frame(self.canvas)

        scrollbarY = Scrollbar(root, orient = "vertical", command = self.canvas.yview)
        scrollbarY.pack(side = RIGHT, fill = Y)
        scrollbarX = Scrollbar(root, orient = "horizontal", command = self.canvas.xview)
        scrollbarX.pack(side = BOTTOM, fill = X)

        self.canvas.configure(xscrollcommand = scrollbarX.set, yscrollcommand = scrollbarY.set)
        self.canvas.pack(side = "left", fill = "both", expand = True)
        self.canvas.create_window((4,4), window = master, anchor="nw", 
                                  tags="master")

        master.bind("<Configure>", self.onFrameConfigure)
        root.geometry("740x1000")

        #Database Connection
        db = self.connect()
        curr = db.cursor()

#Buttons
        #frame
        buttonframe = Frame(master)
        buttonframe.pack(side = "top", fill = "x")

        #back
        backButton = Button(buttonframe, text = "Back", command = lambda:self.backEditChildProfilePage(id, date))
        backButton.pack(side = "left")
        
        #delete
        deleteButton = Button(buttonframe, text = "Delete Application", command = lambda:self.deleteChildApp(id, date))
        deleteButton.pack(side = "right")
        
#Child info section ************************************************************************************************************************
        ChildInfoSectionframe = Frame(master)
        ChildInfoSectionframe.pack(fill = 'y', side = 'left') 
        r = 0

        #header
        labelChildInfoSection = Label(ChildInfoSectionframe, text = "\nCHILD'S INFORMATION")
        labelChildInfoSection.grid(row = r, column = 0)
        labelChildInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        #global childInfo0
        childInfo0 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo0.insert(0, val)
        else:
            childInfo0.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo0(childInfo0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global childInfo1
        childInfo1 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo1.insert(0, val)
        else:
            childInfo1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #nickname
        curr.execute("SELECT Name_Nickname FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nNickname .............................................................................................. ")
        global childInfo2
        childInfo2 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo2.insert(0, val)
        else:
            childInfo2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        curr.execute("SELECT Address_Street FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global childInfo3
        childInfo3 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo3.insert(0, val)
        else:
            childInfo3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        curr.execute("SELECT Address_City FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global childInfo4
        childInfo4 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo4.insert(0, val)
        else:
            childInfo4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        curr.execute("SELECT Address_County FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global childInfo5
        childInfo5 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo5.insert(0, val)
        else:
            childInfo5.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #address zip
        curr.execute("SELECT Address_Zip FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global childInfo6
        childInfo6 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo6.insert(0, val)
        else:
            childInfo6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #home phone
        curr.execute("SELECT Home_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... ")
        global childInfo7
        childInfo7 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo7.insert(0, val)
        else:
            childInfo7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian phone
        curr.execute("SELECT Guardian_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ ")
        global childInfo8
        childInfo8 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo8.insert(0, val)
        else:
            childInfo8.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo8())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian email
        curr.execute("SELECT Guardian_Email FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... ")
        global childInfo9
        childInfo9 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo9.insert(0, val)
        else:
            childInfo9.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo9())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        curr.execute("SELECT Age FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global childInfo10
        childInfo10 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo10.insert(0, val)
        else:
            childInfo10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo10())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #birthday
        curr.execute("SELECT Birthday FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ ")
        global childInfo11
        childInfo11 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo11.insert(0, val)
        else:
            childInfo11.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo11())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        label = Label(ChildInfoSectionframe, text = "\nGender .................................................................................................. ")

        curr.execute("SELECT Gender FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global childInfo12
        childInfo12 = StringVar()
        
        choices = ['Male','Female']
        option = tk.OptionMenu(ChildInfoSectionframe, childInfo12, *choices)

        if val is not None:
            childInfo12.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo12())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #HIV status
        label = Label(ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global childInfo13
        childInfo13 = StringVar()
        
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(ChildInfoSectionframe, childInfo13, *choices)

        if val is not None:
            childInfo13.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo13())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #aware
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... ')

        curr.execute("SELECT Aware FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo14
        childInfo14 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo14, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo14, value=2)

        if val is not None:
            if val is 0:
                childInfo14.set(2)
            else:
                childInfo14.set(1)
 
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo14())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #why
        curr.execute("SELECT Why FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "If no, please provide a reason why child is not aware .............................. ")
        global childInfo15
        childInfo15 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo15.insert(0, val)
        else:
            childInfo15.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo15())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Referral source
        curr.execute("SELECT Referral_Source FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... ")
        global childInfo16
        childInfo16 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo16.insert(0, val)
        else:
            childInfo16.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo16())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #school attending
        curr.execute("SELECT School_attending FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. ")
        global childInfo17
        childInfo17 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo17.insert(0, val)
        else:
            childInfo17.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo17())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Grade Level
        curr.execute("SELECT School_grade_level FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... ")
        global childInfo18
        childInfo18 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo18.insert(0, val)
        else:
            childInfo18.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo18())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo18.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Ethnicity
        label = Label(ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... ")

        curr.execute("SELECT Ethnicity FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global childInfo19
        childInfo19 = StringVar()
        
        choices = ['White/Caucasian','Black/African-American','Hispanic/Latino',
        'Native American','Asian/Pacific Islander/Indian Sub-Continent','Multi-racial','Other']
        option = tk.OptionMenu(ChildInfoSectionframe, childInfo19, *choices)

        if val is not None:
            childInfo19.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo19())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Ethnicity Other
        curr.execute("SELECT Ethnicity_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global childInfo20
        childInfo20 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo20.insert(0, val)
        else:
            childInfo20.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo20())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Even been...
        label = Label(ChildInfoSectionframe, text = "\nHas your child ever been...")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')
        
        #ADD_ADHD
        r = r+1
        label = Label(ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. ')

        curr.execute("SELECT ADD_ADHD FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo21
        childInfo21 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo21, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo21, value=2)

        if val is not None:
            if val is 0:
                childInfo21.set(2)
            else:
                childInfo21.set(1)
 
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo21())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Learning_Disability
        r = r+1
        label = Label(ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')

        curr.execute("SELECT Learning_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo22
        childInfo22 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo22, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo22, value=2)

        if val is not None:
            if val is 0:
                childInfo22.set(2)
            else:
                childInfo22.set(1)
 
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo22())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Developmental_Disability
        r = r+1
        label = Label(ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... ')

        curr.execute("SELECT Developmental_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo23
        childInfo23 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo23, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo23, value=2)

        if val is not None:
            if val is 0:
                childInfo23.set(2)
            else:
                childInfo23.set(1)
 
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo23())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Mental_Health_Issues
        r = r+1
        label = Label(ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. ')

        curr.execute("SELECT Mental_Health_Issues FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo24
        childInfo24 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo24, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo24, value=2)

        if val is not None:
            if val is 0:
                childInfo24.set(2)
            else:
                childInfo24.set(1)
 
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo24())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Other_Medical_Condition
        r = r+1
        label = Label(ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... ')

        curr.execute("SELECT Other_Medical_Condition FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo25
        childInfo25 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo25, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo25, value=2)

        if val is not None:
            if val is 0:
                childInfo25.set(2)
            else:
                childInfo25.set(1)
 
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo25())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Victim_of_Abuse
        r = r+1
        label = Label(ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... ')

        curr.execute("SELECT Victim_of_Abuse FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo26
        childInfo26 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo26, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo26, value=2)

        if val is not None:
            if val is 0:
                childInfo26.set(2)
            else:
                childInfo26.set(1)
 
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo26())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Criminal_Justice_System
        r = r+1
        label = Label(ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... ')

        curr.execute("SELECT Criminal_Justice_System FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo27
        childInfo27 = IntVar()

        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = childInfo27, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = childInfo27, value=2)

        if val is not None:
            if val is 0:
                childInfo27.set(2)
            else:
                childInfo27.set(1)
 
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo27())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Custody
        label = Label(ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... ")

        curr.execute("SELECT Legal_Custody FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global childInfo28
        childInfo28 = StringVar()

        choices = ['Mother','Father','Both Parents','Aunt/Uncle','Grandparent','Pending Court Action','Other']        
        option = tk.OptionMenu(ChildInfoSectionframe, childInfo28, *choices)

        if val is not None:
            childInfo28.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo28())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Custody Other
        curr.execute("SELECT Custody_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global childInfo29
        childInfo29 = Entry(ChildInfoSectionframe)

        if val is not None:
            childInfo29.insert(0, val)
        else:
            childInfo29.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildInfo29())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo29.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Section *******************************************************************************************************************
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global parentInfo0
        parentInfo0 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo0.insert(0, val)
        else:
            parentInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global parentInfo1
        parentInfo1 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo1.insert(0, val)
        else:
            parentInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global parentInfo2
        parentInfo2 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo2.insert(0, val)
        else:
            parentInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Age
        curr.execute("SELECT Age FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global parentInfo3
        parentInfo3 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo3.insert(0, val)
        else:
            parentInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #HIV status
        label = Label(ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo4
        parentInfo4 = StringVar()
        
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo4, *choices)

        if val is not None:
            parentInfo4.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Adoptive Parent
        label = Label(ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... ")

        curr.execute("SELECT Adoptive_Parent FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo5
        parentInfo5 = StringVar()
        
        choices = ['Yes','No','Not Applicable']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo5, *choices)

        if val is not None:
            parentInfo5.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Marital Status
        label = Label(ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... ")

        curr.execute("SELECT Marital_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo6
        parentInfo6 = StringVar()
        
        choices = ['Married','Single','Separated','Divorced','Widowed']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo6, *choices)

        if val is not None:
            parentInfo6.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Highest Level of Education Completed
        label = Label(ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. ")

        curr.execute("SELECT Education_Completed FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo7
        parentInfo7 = StringVar()
        
        choices = ['HS','GED','Some College','Associates Degree','Bachelor Degree','Master Degree','Doctorate']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo7, *choices)

        if val is not None:
            parentInfo7.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Status
        label = Label(ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... ")

        curr.execute("SELECT Employment_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo8
        parentInfo8 = StringVar()
        
        choices = ['Full-Time','Part-Time','Unemployed','Disability']
        option = tk.OptionMenu(ChildInfoSectionframe, parentInfo8, *choices)

        if val is not None:
            parentInfo8.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo8())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Company
        curr.execute("SELECT Employment_Company_Name FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        r= r+1
        label = Label(ChildInfoSectionframe, text = "\nIf employed,")
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(ChildInfoSectionframe, text = "please provide Company Name ............................................................. ")

        global parentInfo9
        parentInfo9 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo9.insert(0, val)
        else:
            parentInfo9.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo9())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Address
        curr.execute("SELECT Address_Street FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nAddress ................................................................................................ ")
        global parentInfo10
        parentInfo10 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo10.insert(0, val)
        else:
            parentInfo10.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo10())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global parentInfo11
        parentInfo11 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo11.insert(0, val)
        else:
            parentInfo11.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo11())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        curr.execute("SELECT Address_State FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nState .................................................................................................... ")
        global parentInfo12
        parentInfo12 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo12.insert(0, val)
        else:
            parentInfo12.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo12())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global parentInfo13
        parentInfo13 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo13.insert(0, val)
        else:
            parentInfo13.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo13())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Work Phone
        curr.execute("SELECT WorkPhone FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... ")
        global parentInfo14
        parentInfo14 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo14.insert(0, val)
        else:
            parentInfo14.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo14())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #E-mail
        curr.execute("SELECT Email FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nE-mail ................................................................................................... ")
        global parentInfo15
        parentInfo15 = Entry(ChildInfoSectionframe)

        if val is not None:
            parentInfo15.insert(0, val)
        else:
            parentInfo15.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildparentInfo15())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Absent Parent Info ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global absParentInfo0
        absParentInfo0 = Entry(ChildInfoSectionframe)

        if val is not None:
            absParentInfo0.insert(0, val)
        else:
            absParentInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildabsParentInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global absParentInfo1
        absParentInfo1 = Entry(ChildInfoSectionframe)

        if val is not None:
            absParentInfo1.insert(0, val)
        else:
            absParentInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildabsParentInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Telephone
        curr.execute("SELECT Telephone FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nTelephone .............................................................................................. ")
        global absParentInfo2
        absParentInfo2 = Entry(ChildInfoSectionframe)

        if val is not None:
            absParentInfo2.insert(0, val)
        else:
            absParentInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildabsParentInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        curr.execute("SELECT Address_Street FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global absParentInfo3
        absParentInfo3 = Entry(ChildInfoSectionframe)

        if val is not None:
            absParentInfo3.insert(0, val)
        else:
            absParentInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildabsParentInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global absParentInfo4
        absParentInfo4 = Entry(ChildInfoSectionframe)

        if val is not None:
            absParentInfo4.insert(0, val)
        else:
            absParentInfo4.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildabsParentInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #County
        curr.execute("SELECT Address_County FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global absParentInfo5
        absParentInfo5 = Entry(ChildInfoSectionframe)

        if val is not None:
            absParentInfo5.insert(0, val)
        else:
            absParentInfo5.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildabsParentInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nZip ......................................................................................................... ")
        global absParentInfo6
        absParentInfo6 = Entry(ChildInfoSectionframe)

        if val is not None:
            absParentInfo6.insert(0, val)
        else:
            absParentInfo6.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildabsParentInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #HIV status
        label = Label(ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global absParentInfo7
        absParentInfo7 = StringVar()
        
        choices = ['HIV Positive','HIV Negative', 'Unkown']
        option = tk.OptionMenu(ChildInfoSectionframe, absParentInfo7, *choices)

        if val is not None:
            absParentInfo7.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildabsParentInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

#HouChildsehold Info ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nHOUSEHOLD INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #list all individuals living in the household
        label = Label(ChildInfoSectionframe, text = "\nAll Individuals Living in the Household")
        r = r+1
        label.grid(row = r, column = 0)

    #person1
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 1')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildhouseInfo(1))
        buttonUpdate.grid(row = r, column = 2)

        person = 1
        
        #Name1
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo10
        houseInfo10 = Entry(ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            houseInfo10.insert(0, 'Unanswered')
        else: 
            houseInfo10.insert(0, val[0][0])

        r = r+1
        houseInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child1
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo11
        houseInfo11 = Entry(ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            houseInfo11.insert(0, 'Unanswered')
        else: 
            houseInfo11.insert(0, val[0][0])

        r = r+1
        houseInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex1
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo12
        houseInfo12 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo12, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo12.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)    

        #Age1
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo13
        houseInfo13 = Entry(ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            houseInfo13.insert(0, 'Unanswered')
        else: 
            houseInfo13.insert(0, val[0][0])

        r = r+1
        houseInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status1
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo14
        houseInfo14 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo14, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo14.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)       

    #person2
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 2')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildhouseInfo(2))
        buttonUpdate.grid(row = r, column = 2)

        person = 2
        
        #Name2
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo20
        houseInfo20 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo20.insert(0, 'Unanswered')
        else: 
            houseInfo20.insert(0, val[0][0])

        r = r+1
        houseInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child2
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo21
        houseInfo21 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo21.insert(0, 'Unanswered')
        else: 
            houseInfo21.insert(0, val[0][0])

        r = r+1
        houseInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex2
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo22
        houseInfo22 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo22, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo22.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)    

        #Age2
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo23
        houseInfo23 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo23.insert(0, 'Unanswered')
        else: 
            houseInfo23.insert(0, val[0][0])

        r = r+1
        houseInfo23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status2
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo24
        houseInfo24 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo24, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo24.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)        

    #person3
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 3')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildhouseInfo(3))
        buttonUpdate.grid(row = r, column = 2)


        person = 3
        
        #Name3
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo30
        houseInfo30 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo30.insert(0, 'Unanswered')
        else: 
            houseInfo30.insert(0, val[0][0])

        r = r+1
        houseInfo30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child3
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo31
        houseInfo31 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo31.insert(0, 'Unanswered')
        else: 
            houseInfo31.insert(0, val[0][0])

        r = r+1
        houseInfo31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex3
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo32
        houseInfo32 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo32, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo32.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)   

        #Age3
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo33
        houseInfo33 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo33.insert(0, 'Unanswered')
        else: 
            houseInfo33.insert(0, val[0][0])

        r = r+1
        houseInfo33.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status3
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo34
        houseInfo34 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo34, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo34.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)     

    #person4
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 4')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildhouseInfo(4))
        buttonUpdate.grid(row = r, column = 2)

        person = 4
        
        #Name4
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo40
        houseInfo40 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo40.insert(0, 'Unanswered')
        else: 
            houseInfo40.insert(0, val[0][0])

        r = r+1
        houseInfo40.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child4
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo41
        houseInfo41 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo41.insert(0, 'Unanswered')
        else: 
            houseInfo41.insert(0, val[0][0])

        r = r+1
        houseInfo41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex4
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo42
        houseInfo42 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo42, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo42.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0) 

        #Age4
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo43
        houseInfo43 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo43.insert(0, 'Unanswered')
        else: 
            houseInfo43.insert(0, val[0][0])

        r = r+1
        houseInfo43.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status4
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo44
        houseInfo44 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo44, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo44.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)         

    #person5
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 5')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildhouseInfo(5))
        buttonUpdate.grid(row = r, column = 2)

        person = 5
        
        #Name5
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo50
        houseInfo50 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo50.insert(0, 'Unanswered')
        else: 
            houseInfo50.insert(0, val[0][0])

        r = r+1
        houseInfo50.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child5
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo51
        houseInfo51 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo51.insert(0, 'Unanswered')
        else: 
            houseInfo51.insert(0, val[0][0])

        r = r+1
        houseInfo51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex5
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo52
        houseInfo52 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo52, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo52.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0) 

        #Age5
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo53
        houseInfo53 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo53.insert(0, 'Unanswered')
        else: 
            houseInfo53.insert(0, val[0][0])

        r = r+1
        houseInfo53.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status5
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo54
        houseInfo54 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo54, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo54.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person6
        r = r+1
        label = Label(ChildInfoSectionframe, text = '\nPerson 6')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildhouseInfo(6))
        buttonUpdate.grid(row = r, column = 2)

        person = 6

        #Name6
        label = Label(ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo60
        houseInfo60 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo60.insert(0, 'Unanswered')
        else: 
            houseInfo60.insert(0, val[0][0])

        r = r+1
        houseInfo60.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child6
        label = Label(ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo61
        houseInfo61 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo61.insert(0, 'Unanswered')
        else: 
            houseInfo61.insert(0, val[0][0])

        r = r+1
        houseInfo61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex6
        label = Label(ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo62
        houseInfo62 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo62, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo62.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0) 

        #Age6
        label = Label(ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo63
        houseInfo63 = Entry(ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo63.insert(0, 'Unanswered')
        else: 
            houseInfo63.insert(0, val[0][0])

        r = r+1
        houseInfo63.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status6
        label = Label(ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo64
        houseInfo64 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(ChildInfoSectionframe, houseInfo64, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo64.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


        #Family Annual Income Info
        label = Label(ChildInfoSectionframe, text = "\n\nFamily Annual Income Information ......................................................... ")

        curr.execute("SELECT Fam_Annual_Income FROM Fam_Annual_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global famIncome0
        famIncome0 = StringVar()
        
        choices = ['$0-10,000','$10,001-15,000','$15,001-20,000','$20,000-25,000','$25,001-30,000','$30,001-35,000','$35,001-40,000','$40,001-45,000','$50,000+']
        option = tk.OptionMenu(ChildInfoSectionframe, famIncome0, *choices)

        if val is not None:
            famIncome0.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildfamIncome0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income
        label = Label(ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... ")

        curr.execute("SELECT Source_Fam_Income FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global famIncome1
        famIncome1 = StringVar()
        
        choices = ['Employment','Government Support','Public Assistance', 'Unemployment Benefits','Medicaid','Social Security','Veterans Benefits','Other']
        option = tk.OptionMenu(ChildInfoSectionframe, famIncome1, *choices)

        if val is not None:
            famIncome1.set(val)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildfamIncome1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income Other
        curr.execute("SELECT Other FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global famIncome2
        famIncome2 = Entry(ChildInfoSectionframe)

        if val is not None:
            famIncome2.insert(0, val)
        else:
            famIncome2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildfamIncome2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        famIncome2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#In Case of Emergency Contact ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global emergencyInfo0
        emergencyInfo0 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo0.insert(0, val)
        else:
            emergencyInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global emergencyInfo1
        emergencyInfo1 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo1.insert(0, val)
        else:
            emergencyInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global emergencyInfo2
        emergencyInfo2 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo2.insert(0, val)
        else:
            emergencyInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Home Address
        curr.execute("SELECT Address_Street FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global emergencyInfo3
        emergencyInfo3 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo3.insert(0, val)
        else:
            emergencyInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global emergencyInfo4
        emergencyInfo4 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo4.insert(0, val)
        else:
            emergencyInfo4.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        curr.execute("SELECT Address_State FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nState ..................................................................................................... ")
        global emergencyInfo5
        emergencyInfo5 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo5.insert(0, val)
        else:
            emergencyInfo5.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global emergencyInfo6
        emergencyInfo6 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo6.insert(0, val)
        else:
            emergencyInfo6.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Phone Number
        curr.execute("SELECT Phone_Home FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. ")
        global emergencyInfo7
        emergencyInfo7 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo7.insert(0, val)
        else:
            emergencyInfo7.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Cell Phone Number
        curr.execute("SELECT Phone_Cell FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... ")
        global emergencyInfo8
        emergencyInfo8 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo8.insert(0, val)
        else:
            emergencyInfo8.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo8())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Alternate Phone Number
        curr.execute("SELECT Phone_Alt FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... ")
        global emergencyInfo9
        emergencyInfo9 = Entry(ChildInfoSectionframe)

        if val is not None:
            emergencyInfo9.insert(0, val)
        else:
            emergencyInfo9.insert(0, 'Unanswered')

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildemergencyInfo9())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#H.E.R.O. Programs ************************************************************************************************************************
        #header               
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS\n")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Program(s) you wish your child to participate in
        label = Label(ChildInfoSectionframe, text = "Program(s) you wish your child to participate in .................................... ")
        r = r+1
        label.grid(row = r, column = 0)
            
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildPrograms0())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT HERO_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]

        #Super HEROes Program
        global programs0
        programs0 = IntVar()
        Checkbutton(ChildInfoSectionframe, text="Super HEROes Program", variable = programs0).grid(row = r,  column = 1, sticky = W)

        #TODO: apply None check to all checkboxes
        if (var is not None) and 'Super HEROes Program' in var:
            programs0.set(1)

        #Bright HEROs Program
        global programs1
        programs1 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Bright HEROs Program", variable = programs1).grid(row = r,  column = 1, sticky = W)

        if 'Bright HEROs Program' in var:
            programs1.set(1)
            
        #Camp High Five
        global programs2
        programs2 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Camp High Five", variable = programs2).grid(row = r,  column = 1, sticky = W)

        if 'Camp High Five' in var:
            programs2.set(1)
            
        #Holiday of HEROs
        global programs3
        programs3 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Holiday of HEROs", variable = programs3).grid(row = r,  column = 1, sticky = W)

        if 'Holiday of HEROs' in var:
            programs3.set(1)
            
        #Transition to Adulthood
        global programs4
        programs4 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Transition to Adulthood", variable = programs4).grid(row = r,  column = 1, sticky = W)

        if 'Transition to Adulthood' in var:
            programs4.set(1)

    #Program(s) you would be interested in your child to participating in
        label = Label(ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildPrograms1())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT Future_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]
        
        #Healthy HEROs (health curriculum)
        global programs5
        programs5 = IntVar()
        Checkbutton(ChildInfoSectionframe, text="Healthy HEROs", variable = programs5).grid(row = r,  column = 1, sticky = SW)

        if 'Healthy HEROs' in var:
            programs5.set(1)

        #Career Development/Job Readiness
        global programs6
        programs6 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Career Development/Job Readiness", variable = programs6).grid(row = r,  column = 1, sticky = W)

        if 'Career Development/Job Readiness' in var:
            programs6.set(1)
            
        #Other
        global programs7
        programs7 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Other", variable = programs7).grid(row = r,  column = 1, sticky = W)

        if 'Other' in var:
            programs7.set(1)

        #if other
        global programs8
        programs8 = Entry(ChildInfoSectionframe, width = 19)
        programs8.grid(row = r, column = 1, sticky = E)

        curr.execute("SELECT Future_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        if val is not None:
            programs8.insert(0, val)
        else:
            programs8.insert(0, 'Unanswered')
            
#Referral Needs ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Referral
        label = Label(ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildReferral())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT Referral FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]
        
        #Food
        global Referral0
        Referral0 = IntVar()
        Checkbutton(ChildInfoSectionframe, text="Food", variable = Referral0).grid(row = r,  column = 1, sticky = SW)

        if 'Healthy HEROs' in var:
            Referral0.set(1)

        #Transitional Housing/Shelter
        global Referral1
        Referral1 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Transitional Housing/Shelter", variable = Referral1).grid(row = r,  column = 1, sticky = W)

        if 'Transitional Housing/Shelter' in var:
            Referral1.set(1)

        #Rent/Utilities Assistance
        global Referral2
        Referral2 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Rent/Utilities Assistance", variable = Referral2).grid(row = r,  column = 1, sticky = W)

        if 'Rent/Utilities Assistance' in var:
            Referral2.set(1)

        #Clothing/Furniture
        global Referral3
        Referral3 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Clothing/Furniture", variable = Referral3).grid(row = r,  column = 1, sticky = W)

        if 'Clothing/Furniture' in var:
            Referral3.set(1)

        #Financial/Public Assistance
        global Referral4
        Referral4 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Financial/Public Assistance", variable = Referral4).grid(row = r,  column = 1, sticky = W)

        if 'Financial/Public Assistance' in var:
            Referral4.set(1)

        #Other
        global Referral5
        Referral5 = IntVar()
        r = r+1
        Checkbutton(ChildInfoSectionframe, text="Other", variable = Referral5).grid(row = r,  column = 1, sticky = W)

        if 'Other' in var:
            Referral5.set(1)

        #if other
        global Referral6
        Referral6 = Entry(ChildInfoSectionframe, width = 19)
        Referral6.grid(row = r, column = 1, sticky = E)

        curr.execute("SELECT Referral_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        if val is not None:
            Referral6.insert(0, val)
        else:
            Referral6.insert(0, 'Unanswered')

#Statement of Understanding ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))
       
        #one
        label = Label(ChildInfoSectionframe, text = "Statement 1 ........................................................................................... ")
        curr.execute("SELECT Statement_One FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement0
        statement0 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement0, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement0, value=2)

        if val is not None:
            if val is 0:
                statement0.set(2)
            else:
                statement0.set(1)

        r = r+1
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildStatement())
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #two
        label = Label(ChildInfoSectionframe, text = "Statement 2 .......................................................................................... ")
        curr.execute("SELECT Statement_Two FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement1
        statement1 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement1, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement1, value=2)

        if val is not None:
            if val is 0:
                statement1.set(2)
            else:
                statement1.set(1)
                
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #three
        label = Label(ChildInfoSectionframe, text = "Statement 3 .......................................................................................... ")
        curr.execute("SELECT Statement_Three FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement2
        statement2 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement2, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement2, value=2)

        if val is not None:
            if val is 0:
                statement2.set(2)
            else:
                statement2.set(1)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #four
        label = Label(ChildInfoSectionframe, text = "Statement 4 .......................................................................................... ")
        curr.execute("SELECT Statement_Four FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement3
        statement3 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement3, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement3, value=2)

        if val is not None:
            if val is 0:
                statement3.set(2)
            else:
                statement3.set(1)
                
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #five
        label = Label(ChildInfoSectionframe, text = "Statement 5 .......................................................................................... ")
        curr.execute("SELECT Statement_Five FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement4
        statement4 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement4, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement4, value=2)

        if val is not None:
            if val is 0:
                statement4.set(2)
            else:
                statement4.set(1)
                
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #six
        label = Label(ChildInfoSectionframe, text = "Statement 6 .......................................................................................... ")
        curr.execute("SELECT Statement_Six FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement5
        statement5 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement5, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement5, value=2)

        if val is not None:
            if val is 0:
                statement5.set(2)
            else:
                statement5.set(1)
                
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #seven
        label = Label(ChildInfoSectionframe, text = "Statement 7 .......................................................................................... ")
        curr.execute("SELECT Statement_Seven FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement6
        statement6 = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = statement6, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = statement6, value=2)

        if val is not None:
            if val is 0:
                statement6.set(2)
            else:
                statement6.set(1)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

 #Signature ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(ChildInfoSectionframe, text = "\n\nSIGNATURE")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        label = Label(ChildInfoSectionframe, text = "\nSignature .............................................................................................. ")
        curr.execute("SELECT Signature FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global signature
        signature = IntVar()
        Yes = Radiobutton(ChildInfoSectionframe, text = "Yes", variable = signature, value=1)
        No = Radiobutton(ChildInfoSectionframe, text = "No", variable = signature, value=2)

        if val is not None:
            if val is 0:
                signature.set(2)
            else:
                signature.set(1)

        r = r+1
        buttonUpdate = Button(ChildInfoSectionframe, text = "Update", command = lambda:self.updateChildSignature())
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#Close Database Connection
        curr.close()
        db.close()

#Child Info ************************************************************************************************************************
    def updateChildInfo0(self, childInfo0, id, date):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
        
        #feedback    
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo1(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
        
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo2(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_Nickname = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_Nickname = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo3(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo4(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo5(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_County = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_County = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo6(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Childs_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")

            
        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo7(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo7.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Home_Phone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Home_Phone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo8(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo8.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Guardian_Phone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Guardian_Phone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo9(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Guardian_Email = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Guardian_Email = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo10(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo10.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Age = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Childs_Information SET Age = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAge must be only numbers.")

    def updateChildInfo11(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo11.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Birthday = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Childs_Information SET Birthday = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo12(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo12.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Gender = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo13(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo13.get()
        curr.execute("UPDATE Childs_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo14(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo14.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Aware = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo15(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo15.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Why = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Why = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo16(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo16.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Referral_Source = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Referral_Source = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo17(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo17.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET School_attending = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET School_attending = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo18(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo18.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET School_grade_level = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET School_grade_level = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo19(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo19.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Ethnicity = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo20(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo20.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Ethnicity_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Ethnicity_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo21(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo21.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET ADD_ADHD = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo22(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo22.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Learning_Disability = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo23(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo23.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Developmental_Disability = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo24(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo24.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Mental_Health_Issues = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo25(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo25.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Other_Medical_Condition = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo26(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo26.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Victim_of_Abuse = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo27(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo27.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Criminal_Justice_System = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo28(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo28.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Legal_Custody = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildInfo29(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = childInfo29.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Custody_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Custody_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Parent Info ************************************************************************************************************************

    def updateChildparentInfo0(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo1(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo2(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Relationship_to_Child = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Relationship_to_Child = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo3(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Age = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Parent_Guardian_Information SET Age = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAge code must be only numbers.")

    def updateChildparentInfo4(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo4.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo5(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo5.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Adoptive_Parent = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo6(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo6.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Marital_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo7(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo7.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Education_Completed = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo8(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo8.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo9(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Company_Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Company_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo10(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo10.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo11(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo11.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo12(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo12.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo13(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo13.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo14(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo14.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET WorkPhone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET WorkPhone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildparentInfo15(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = parentInfo15.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Email = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Email = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Absent Parent Info ************************************************************************************************************************

    def updateChildabsParentInfo0(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = absParentInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildabsParentInfo1(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = absParentInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildabsParentInfo2(self):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = absParentInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Telephone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Telephone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildabsParentInfo3(self):

        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = absParentInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildabsParentInfo4(self):

        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = absParentInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildabsParentInfo5(self):

        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = absParentInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_County = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_County = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildabsParentInfo6(self):

        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = absParentInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")

    def updateChildabsParentInfo7(self):

        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = absParentInfo7.get()
        if newVal != '':
            curr.execute("UPDATE Absent_Parent_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Household Info ************************************************************************************************************************

    def updateChildhouseInfo(self, count):

        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        if count == 1:
            newVal0 = houseInfo10.get()
            newVal1 = houseInfo11.get()
            newVal2 = houseInfo12.get()
            newVal3 = houseInfo13.get()
            newVal4 = houseInfo14.get()

        elif count == 2:
            newVal0 = houseInfo20.get()
            newVal1 = houseInfo21.get()
            newVal2 = houseInfo22.get()
            newVal3 = houseInfo23.get()
            newVal4 = houseInfo24.get()

        elif count == 3:
            newVal0 = houseInfo30.get()
            newVal1 = houseInfo31.get()
            newVal2 = houseInfo32.get()
            newVal3 = houseInfo33.get()
            newVal4 = houseInfo34.get()

        elif count == 4:
            newVal0 = houseInfo40.get()
            newVal1 = houseInfo41.get()
            newVal2 = houseInfo42.get()
            newVal3 = houseInfo43.get()
            newVal4 = houseInfo44.get()

        elif count == 5:
            newVal0 = houseInfo50.get()
            newVal1 = houseInfo51.get()
            newVal2 = houseInfo52.get()
            newVal3 = houseInfo53.get()
            newVal4 = houseInfo54.get()

        elif count == 6:
            newVal0 = houseInfo60.get()
            newVal1 = houseInfo61.get()
            newVal2 = houseInfo62.get()
            newVal3 = houseInfo63.get()
            newVal4 = houseInfo64.get()

        if (newVal0 == 'Unanswered') or (newVal0 == ''):
            newVal0 = None
        
        if (newVal1 == 'Unanswered') or (newVal1 == ''):
            newVal1 = None

        if newVal2 == '':
            newVal2 = None

        goodData = 1
        if (newVal3 == 'Unanswered') or (newVal3 == ''):
            newVal3 = None
        elif (not self.is_number(newVal3)):
            goodData = 0
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAge must be only numbers.")
            #stop input to database !!!!!!@#@@#!@

        if newVal4 == '':
            newVal4 = None


        if goodData:
            curr.execute("SELECT * FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count,))
            current = curr.fetchall()
            if current is ():
                curr.execute("""INSERT INTO Household_Information VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s);""", 
                    (id, date, count, newVal0, newVal1, newVal2, newVal3, newVal4,))
            else:
                curr.execute("""UPDATE Household_Information 
                    SET Name = %s, Relationship = %s, Sex = %s, Age = %s, HIV_Status = %s 
                    WHERE ID = %s AND Date_Submitted = %s AND Count = %s;""", 
                    (newVal0, newVal1, newVal2, newVal3, newVal4, id, date, count,))

            db.commit()
            
            #feedback
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        
        #Close Database Connection
        curr.close()
        db.close()

    def updateChildfamIncome0(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = famIncome0.get()
        if newVal != '':
            curr.execute("UPDATE Fam_Annual_Income SET Fam_Annual_Income = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildfamIncome1(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = famIncome1.get()
        if newVal != '':
            curr.execute("UPDATE Source_Fam_Income SET Source_Fam_Income = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateChildfamIncome2(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = famIncome2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Source_Fam_Income SET Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Source_Fam_Income SET Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#In Case of Emergency Contact ************************************************************************************************************************
    def updateChildemergencyInfo0(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateChildemergencyInfo1(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateChildemergencyInfo2(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Relationship_to_Child = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Relationship_to_Child = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateChildemergencyInfo3(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateChildemergencyInfo4(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateChildemergencyInfo5(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 


    def updateChildemergencyInfo6(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateChildemergencyInfo7(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo7.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Home = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Home = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateChildemergencyInfo8(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo8.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Cell = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Cell = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateChildemergencyInfo9(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Alt = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Alt = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#H.E.R.O. Programs ************************************************************************************************************************

    def updateChildPrograms0(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''

        if programs0.get():
            newVal = newVal + 'Super HEROes Program,'

        if programs1.get():
            newVal = newVal + 'Bright HEROs Program,'

        if programs2.get():
            newVal = newVal + 'Camp High Five,'

        if programs3.get():
            newVal = newVal + 'Holiday of HEROs,'

        if programs4.get():
            newVal = newVal + 'Transition to Adulthood,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET HERO_Programs = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET HERO_Programs = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()


    def updateChildPrograms1(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''

        if programs5.get():
            newVal = newVal + 'Healthy HEROs,'

        if programs6.get():
            newVal = newVal + 'Career Development/Job Readiness,'

        if programs7.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET Future_Programs = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET Future_Programs = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))

        newValOther = programs8.get()
        if (newValOther == 'Unanswered') or (newValOther == ''):
            curr.execute("UPDATE Child_Application SET Future_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Child_Application SET Future_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newValOther, id, date,))
        
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Referral Needs ************************************************************************************************************************

    def updateChildReferral(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''

        if Referral0.get():
            newVal = newVal + 'Food,'

        if Referral1.get():
            newVal = newVal + 'Transitional Housing/Shelter,'

        if Referral2.get():
            newVal = newVal + 'Rent/Utilities Assistance,'

        if Referral3.get():
            newVal = newVal + 'Clothing/Furniture,'

        if Referral4.get():
            newVal = newVal + 'Financial/Public Assistance,'

        if Referral5.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET Referral = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET Referral = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))

        newValOther = Referral6.get()
        if (newValOther == 'Unanswered') or (newValOther == ''):
            curr.execute("UPDATE Child_Application SET Referral_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Child_Application SET Referral_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newValOther, id, date,))
        
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Statement of Understanding & signeture **************************************************************************************************************

    def updateChildStatement(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        s0 = statement0.get()
        if s0 == 0:
            s0 = None
        elif s0 == 2:
            s0 = 0

        s1 = statement1.get()
        if s1 == 0:
            s1 = None
        elif s1 == 2:
            s1 = 0

        s2 = statement2.get()
        if s2 == 0:
            s2 = None
        elif s2 == 2:
            s2 = 0

        s3 = statement3.get()
        if s3 == 0:
            s3 = None
        elif s3 == 2:
            s3 = 0

        s4 = statement4.get()
        if s4 == 0:
            s4 = None
        elif s4 == 2:
            s4 = 0

        s5 = statement5.get()
        if s5 == 0:
            s5 = None
        elif s5 == 2:
            s5 = 0

        s6 = statement6.get()
        if s6 == 0:
            s6 = None
        elif s6 == 2:
            s6 = 0

        curr.execute("""UPDATE Statement_Of_Understanding SET Statement_One = %s, Statement_Two = %s, Statement_Three = %s, Statement_Four = %s,
            Statement_Five = %s, Statement_Six = %s, Statement_Seven = %s WHERE ID = %s AND Date_Submitted = %s;""",
            (s0, s1, s2, s3, s4, s5, s6, id, date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateSignature(self):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        newVal = signature.get()
        if newVal == 0:
            newVal = None
        elif newVal == 2:
            newVal = 0

        curr.execute("""UPDATE Child_Application SET Signature = %s WHERE ID = %s AND Date_Submitted = %s;""", (newVal, id, date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()


#check string entry is a number
    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

#check string entry is a date (YYYY-MM-DD)
    def is_date(self, s):
        if len(s) != 10:
            return False
        if (s[4] != s[7]) or (s[4] != '-') or (not self.is_number(s[0:4])) or (not self.is_number(s[5:7])) or (not self.is_number(s[-2:])):
            return False
        if (1 > int(s[0:4])) or (1 > int(s[5:7])) or (int(s[5:7]) > 12) or (1 > int(s[-2:])):
            return False
        if int(s[5:7]) == 02:
            if (int(s[-2:]) > 29):
                return False
        elif (int(s[5:7]) == 04) or (int(s[5:7]) == 06) or (int(s[5:7]) == 9) or (int(s[5:7]) == 11):
            if (int(s[-2:]) > 30): 
                return False
        elif int(s[-2:]) > 31:
            return False

        return True


#button definitions
    def backEditChildProfilePage(self, id, date):
        if self.PrevPage is 'SecondChildProfilePage':
            self.PrevPage = 'EditChildProfilePage'
            self.SecondChildProfilePage(id, date)


    def deleteChildApp(self, id, date):
        if askyesno('Verify', 'Really delete?'):
            #Delete application from database

            #Open Database Connection
            db = self.connect()
            curr = db.cursor()

            #Execute
            curr.execute("DELETE FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()

            #Close Database Connection
            curr.close()
            db.close()

            #UI feedback
            showwarning('Delete', 'Application Deleted')

            self.backSecondChildProfilePage(id)

        else:
            #Delete cancelled
            showinfo('No', 'Delete has been cancelled')

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))


root = Tk()
Main(root)
root.mainloop()
