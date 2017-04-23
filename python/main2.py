import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import tkMessageBox
import MySQLdb

#TODO: figure out why you can only exit from login

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

        if self.PrevPage is 'HomePage':
            self.HomePageRoot.withdraw()
        self.PrevPage = 'LoginPage'

        self.root.deiconify()
        master=Frame(self.root)
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
            self.root.withdraw()
        elif self.PrevPage is 'AdminUserPage':
            self.AdminUserPageRoot.withdraw()
        elif self.PrevPage is 'SearchPage':
            self.SearchPageRoot.withdraw()
        self.PrevPage = 'HomePage'

        root.title("Home Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        username = self.session['username']
        credentials = self.session['credentials']
        
        logoutButton = Button(master, text = "Log Out", command=lambda: self.LoginPage())
        logoutButton.grid(row = 0, column = 0)

        newAppButton = Button(master, text = "Add New Application")
            #, command=lambda: controller.show_frame(AddNewApp))
        newAppButton.grid(row = 1, column = 3, padx = 185, pady = 10)

        if (credentials == 'Administrator' or credentials == 'Manager'):
            searchButton = Button(master, text = "Search",  command=lambda: self.SearchPage())
            searchButton.grid(row = 2, column = 3, padx = 185, pady = 10)

        if (credentials == 'Administrator'):
            adminButton = Button(master, text = "Administrate Users", command=lambda: self.AdminUserPage())
            adminButton.grid(row = 3, column = 3, padx = 185, pady = 10)


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


#TODO: rn always deletes the last user
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

        back = Button(master, text="Back", command = lambda: self.AdminUserPage())
        back.grid(row = 0, column = 0)

        db = self.connect()
        curr = db.cursor()

        curr.execute("SELECT * FROM User")
        results = curr.fetchall()

        curr.close()
        db.close()

        for i in range(len(results)):
            nameLabel = Label(master, text = results[i][0], font= "Verdana 10")
            nameLabel.grid(row = 2 + i, column = 0)

            usernameLabel = Label(master, text = results[i][1], font= "Verdana 10")
            usernameLabel.grid(row = 2 + i, column = 1)

            usertypeLabel = Label(master, text = results[i][3], font= "Verdana 10")
            usertypeLabel.grid(row = 2 + i, column = 2)

            deleteButton = Button(master, text = "Delete", command = lambda: self.deleteUser(results[i][1]))
            deleteButton.grid(row = 2 + i, column = 3)

        '''
        count = 0
        for name,username,_,usertype in results:
            nameLabel = Label(master, text = name, font= "Verdana 10")
            nameLabel.grid(row = 2 + count, column = 0)

            usernameLabel = Label(master, text = username, font= "Verdana 10")
            usernameLabel.grid(row = 2 + count, column = 1)

            usertypeLabel = Label(master, text = usertype, font= "Verdana 10")
            usertypeLabel.grid(row = 2 + count, column = 2)

            deleteButton = Button(master, text = "Delete", command = lambda: self.deleteUser(parent, controller, ))
            deleteButton.grid(row = 2 + count, column = 3)
            count += 1

        curr.close()
        db.close()
        '''

    def deleteUser(self, username):

        db = self.connect()
        curr = db.cursor()

        curr.execute("DELETE FROM User WHERE Username = %s", (username,))
        
        db.commit()
        curr.close()
        db.close()

        tkMessageBox.showinfo("Add User", "Update Successful!")


#******************************************************************************************************************************************************

    def SearchPage(self):

        self.SearchPageRoot = Toplevel()
        root = self.SearchPageRoot
        if self.PrevPage is 'HomePage':
            self.HomePageRoot.withdraw()
        elif self.PrevPage is 'SearchResultsPage':
            self.SearchResultsPageRoot.withdraw()
        self.PrevPage = 'SearchPage'
        
        root.title("Search Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        db = self.connect()
        curr = db.cursor()

        curr.execute("SELECT COUNT(ID) FROM Child;")
        total = curr.fetchall()[0][0]

        count = Label(master, text = "Total: " + str(total))
        count.grid(row = 0, column = 4)

        catLabel = Label(master, text = "Search by Category", font= "Verdana 10 underline")
        catLabel.grid(row = 2, column = 0)

        nameLabel = Label(master, text = "Search by Name", font= "Verdana 10 underline")
        nameLabel.grid(row = 4, column = 0)


        programList = ['Any', 'None', "Child Application", "Camp High Five Application"]
        programs = StringVar(master)
        programs.set('Programs')

        dropdownProgram = OptionMenu(master, programs, *programList)
        dropdownProgram.grid(row = 1, column = 1)



        #grab all dat submitted, remove duplicates, set to yearList
        childDatesSubmitted = curr.execute("SELECT Year(Date_Submitted) FROM Child_Application;")
        val1 = curr.fetchall()
        campDatesSubmitted = curr.execute("SELECT Year(Date_Submitted) FROM Camp_Application;")
        val2 = curr.fetchall()
        
        curr.close()
        db.close()

        yearList = []

        for item in val1:
            if item not in yearList:
                yearList.append(item)

        for item in val2:
            if item not in yearList:
                yearList.append(item)

        years = StringVar(master)
        years.set("Year")

        #add back yearlist

        dropdownYear = OptionMenu(master, years, "Any", "None", *yearList)
        dropdownYear.grid(row = 1, column = 2)

        categoriesList = ['None', 'Zip Code', 'City', "County", 'Referral Source', "Child's Age",
                    "Child's Gender", "Child's Race/Ethnicity",
                    "Child's HIV Status (infected or affected)", "Child's Other Issues",
                    "Child's HERO Program Participation", "Child's Allergies", "Child's Years with HERO",
                    "Household Composition", "Parent(s) HIV Status (infected or affected)",
                    "Household Income Range", "Household Income Source", "Parent(s) Highest Level of Education",
                    "Parent(s) Employment Status"]

        categories = StringVar(master)
        categories.set("Category")

        dropdownCategories = OptionMenu(master, categories, *categoriesList)
        dropdownCategories.grid(row = 3, column = 1)


        catEntry = Entry(master, width=15)
        catEntry.grid(row = 3, column = 2)

        searchCatButton = Button(master, text = "Search", command=lambda: self.searchCriteriaAssignment(programs.get(), years.get(), categories.get()))
        searchCatButton.grid(row = 3, column = 3)

        back = Button(master, text = "Back", command = lambda: self.HomePage())
        back.grid(row = 0, column = 0)

        txt = Label(master, text = "First Name:")
        txt.grid(row = 5, column = 1)

        firstName = Entry(master, width=15)
        firstName.grid(row = 5, column = 2)

        txt = Label(master, text = "Last Name:")
        txt.grid(row = 6, column = 1)

        lastName = Entry(master, width=15)
        lastName.grid(row = 6, column = 2)

        searchNameButton = Button(master, text = "Search", command=lambda: self.searchCriteriaAssignment(programs.get(), years.get(), categories.get()))
        searchNameButton.grid(row = 5, column = 3)

    def searchCriteriaAssignment(self, selectedProgram, selectedYear, selectedCategory):
        self.searchCriteria['program'] = selectedProgram
        self.searchCriteria['year'] = selectedYear
        self.searchCriteria['category'] = selectedCategory

        self.SearchResultsPage()


#******************************************************************************************************************************************************


    #TODO: implement search results.
    def SearchResultsPage(self):

        self.SearchResultsPageRoot = Toplevel()
        root = self.SearchResultsPageRoot
        if self.PrevPage is 'SearchPage':
            self.SearchPageRoot.withdraw()
        if self.PrevPage is 'FirstProfilePage':
            self.FirstProfilePageRoot.withdraw()
        self.PrevPage = 'SearchResultsPage'
        
        root.title("Search Results Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        camp = ''
        child = ''

        selectedProgram = self.searchCriteria['program'] 
        selectedYear = self.searchCriteria['year']
        selectedCategory = self.searchCriteria['category']

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

        #check for category selection
        catParam = 1
        
        db = self.connect()
        curr = db.cursor()

        #no category input
        if (selectedCategory == 'Category') or (selectedCategory == 'None') or (selectedCategory == "Child's HERO Program Participation"):

            #no year & no program OR no year & child
            #first, last, year in child
            if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                    curr.execute("SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted) FROM Childs_Information;")
                    child = curr.fetchall()

            #no year & no program OR no year & camp
            #first, last, year in camp
            if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                    curr.execute("SELECT ID, Date_Submitted, First_Name, Last_Name, YEAR(Date_Submitted) FROM Demographic_Information;")
                    camp = curr.fetchall()

            #year & no program OR year & child
            #first, last in child
            check = yearParam and ((not programParam) or (selectedProgram == 'Child Application'))
            if (check):
                    curr.execute("SELECT ID, Date_Submitted, Name_First, Name_Last FROM Childs_Information WHERE YEAR(Date_Submitted) = %s;", (selectedYear,))
                    child = curr.fetchall()

            #year & no program OR year & camp
            #first, last in camp
            if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                    curr.execute("SELECT ID, Date_Submitted, First_Name, Last_Name FROM Demographic_Information WHERE YEAR(Date_Submitted) = %s;", (selectedYear,))
                    camp = curr.fetchall()


        elif selectedCategory == 'Zip Code':

            #no year & no program OR no year & child
            #first, last, year, cat in child
            if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), Address_Zip FROM Childs_Information
                        WHERE Address_Zip != 'NULL';""")
                    child = curr.fetchall()

            #no year & no program OR no year & camp
            #first, last, year, cat in camp
            if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, YEAR(Date_Submitted), Address_Zip FROM Demographic_Information
                        WHERE Address_Zip != 'NULL';""")
                    camp = curr.fetchall()

            #year & no program OR year & child
            #first, last, cat in child
            check = yearParam and ((not programParam) or (selectedProgram == 'Child Application'))
            if (check):
                    curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_Zip FROM Childs_Information
                        WHERE YEAR(Date_Submitted) = %s AND Address_Zip != 'NULL';""", (selectedYear,))
                    child = curr.fetchall()

            #year & no program OR year & camp
            #first, last, cat in camp
            if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
                    curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_Zip FROM Demographic_Information
                        WHERE YEAR(Date_Submitted) = %s AND Address_Zip != 'NULL';""", (selectedYear,))
                    camp = curr.fetchall()

        total = len(child) + len(camp)
        count = Label(master, text = "Total: " + str(total))
        count.grid(row = 0, column = 4)

        nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = 1, column = 0)

        critHead = Label(master, text = "Criteria", font= "Verdana 10 underline")
        critHead.grid(row = 1, column = 1)

        progHead = Label(master, text = "Program", font= "Verdana 10 underline")
        progHead.grid(row = 1, column = 2)

        yearHead = Label(master, text = "Year", font= "Verdana 10 underline")
        yearHead.grid(row = 1, column = 3)

        back = Button(master, text = "Back", command = lambda: self.SearchPage())
        back.grid(row = 0, column = 0)


        #TODO: pass in ID when implemented
        placeHolder = Button(master, text = "Place Holder", command = lambda: self.FirstProfilePage(1))
        placeHolder.grid(row = 0, column = 2)

#******************************************************************************************************************************************************

    def FirstProfilePage(self, id):

        self.FirstProfilePageRoot = Toplevel()
        root = self.FirstProfilePageRoot
        if self.PrevPage is 'SearchResultsPage':
            self.SearchResultsPageRoot.withdraw()
        if self.PrevPage is 'SecondProfilePage':
            self.SecondProfilePageRoot.withdraw()
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
            details = Button(master, text="See Details", command=lambda: self.seeDetails(id, childDate[0])).grid(row=r, column=5)
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
            details = Button(master, text="See Details", command=lambda: self.seeDetails(id, campDate[0])).grid(row=r, column=5)
            r = r + 1

        curr.close()
        db.close()

    def backFirstProfilePage(self):
        if self.PrevPage is 'SearchResultsPage' or 'SecondProfilePage':
            self.PrevPage = 'FirstProfilePage'
            self.SearchResultsPage()

    def seeDetails(self, id, date):
        self.PrevPage = 'FirstProfilePage'
        self.SecondProfilePage(id, date)


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
        #TODO: figure out scrolling

    def SecondProfilePage(self, id, date):

        #setup
        self.SecondProfilePageRoot = Toplevel()
        root = self.SecondProfilePageRoot
        if self.PrevPage is 'FirstProfilePage':
            self.FirstProfilePageRoot.withdraw()
        if self.prevSection is 1:
            self.SecondProfilePageRoot1.withdraw()

        self.prevSection = 0
        
        root.title("Second Level Profile Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Buttons
        #back button frame + back button
        self.buttonframe = Frame(master)
        self.buttonframe.pack(side = "top", fill = "x")

        #fix alignment
        backButton = Button(self.buttonframe, text = "Back", command = lambda: self.backSecondProfilePage(id))
        backButton.pack(side = "left")

        #edit
        editButton = Button(self.buttonframe, text = "Edit Application")
        #TODO
        #, command = lambda: controller.show_frame(EditProfile))
        editButton.pack(side = "right")

        #delete
        deleteButton = Button(self.buttonframe, text = "Delete Application", command = lambda: self.deleteChildApp(id, date))
        deleteButton.pack(side = "right")



#Database dump frame
        self.ChildInfoSectionframe = Frame(master)
        self.ChildInfoSectionframe.pack(fill = 'y', side = 'left')

#Identifying Info Section
        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\nIDENTIFYING INFORMATION")
        labelChildInfoSection.pack(fill = "x")
        labelChildInfoSection.config(font=("Helvetica", 20))

        #id
        label = Label(self.ChildInfoSectionframe, text = "\nChild ID.................................................................................................. " + str(id))
        label.pack(anchor = 'w')

        #date
        label = Label(self.ChildInfoSectionframe, text = "\nDate Submitted...................................................................................... " + str(date))
        label.pack(anchor = 'w')

        #Continue
        continueButton = Button(self.ChildInfoSectionframe, text = "Continue", command = lambda: self.continueButtonHandler(id, date)).pack(anchor = 'se')


    def SecondProfilePage1(self, id, date):

        #setup
        self.SecondProfilePageRoot1 = Toplevel()
        root = self.SecondProfilePageRoot1
        if self.prevSection is 0:
            self.SecondProfilePageRoot.withdraw()
        elif self.prevSection is 2:
            self.SecondProfilePageRoot2.withdraw()

        self.prevSection = 1
        
        root.title("Second Level Profile Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Buttons
        #back button frame + back button
        self.buttonframe = Frame(master)
        self.buttonframe.pack(side = "top", fill = "x")

        #fix alignment
        backButton = Button(self.buttonframe, text = "Back", command = lambda: self.backSecondProfilePage(id))
        backButton.pack(side = "left")

        #edit
        editButton = Button(self.buttonframe, text = "Edit Application")
        #TODO
        #, command = lambda: controller.show_frame(EditProfile))
        editButton.pack(side = "right")

        #delete
        deleteButton = Button(self.buttonframe, text = "Delete Application", command = lambda: self.deleteChildApp(id, date))
        deleteButton.pack(side = "right")

#Database dump frame
        self.ChildInfoSectionframe = Frame(master)
        self.ChildInfoSectionframe.pack(fill = 'x')

    #Child info section
        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nCHILD'S INFORMATION")
        labelChildInfoSection.pack(fill = "x")
        labelChildInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #last name
        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name  ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #nickname
        curr.execute("SELECT Name_Nickname FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #address street
        curr.execute("SELECT Address_Street FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address city
        curr.execute("SELECT Address_City FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address county
        curr.execute("SELECT Address_County FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                
        #address zip
        curr.execute("SELECT Address_Zip FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #home phone
        curr.execute("SELECT Home_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #guardian phone
        curr.execute("SELECT Guardian_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #guardian email
        curr.execute("SELECT Guardian_Email FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #age
        curr.execute("SELECT Age FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                
        #birthday
        curr.execute("SELECT Birthday FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #gender
        curr.execute("SELECT Gender FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

#Close Database Connection
        curr.close()
        db.close()


        #Bottom Buttons
        self.bottoomButtonframe = Frame(master)
        self.bottoomButtonframe.pack(side = "bottom", fill = "x")

        #Continue
        continueButton = Button(self.bottoomButtonframe, text = "Continue", command = lambda: self.continueButtonHandler(id, date)).pack(side = 'right')
        #Previous
        previousButton = Button(self.bottoomButtonframe, text = "Previous", command = lambda: self.previousButtonHandler(id, date)).pack(side = 'left')


    def SecondProfilePage2(self, id, date):

        #setup
        self.SecondProfilePageRoot2 = Toplevel()
        root = self.SecondProfilePageRoot2
        if self.prevSection is 1:
            self.SecondProfilePageRoot1.withdraw()
        elif self.prevSection is 3:
            self.SecondProfilePageRoot3.withdraw()
        
        self.prevSection = 2
        
        root.title("Second Level Profile Page")
        master = Frame(root)
        master.grid(row=0, column=0, sticky = NW)

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Buttons
        #back button frame + back button
        self.buttonframe = Frame(master)
        self.buttonframe.pack(side = "top", fill = "x")

        #fix alignment
        backButton = Button(self.buttonframe, text = "Back", command = lambda: self.backSecondProfilePage(id))
        backButton.pack(side = "left")

        #edit
        editButton = Button(self.buttonframe, text = "Edit Application")
        #TODO
        #, command = lambda: controller.show_frame(EditProfile))
        editButton.pack(side = "right")

        #delete
        deleteButton = Button(self.buttonframe, text = "Delete Application", command = lambda: self.deleteChildApp(id, date))
        deleteButton.pack(side = "right")

        #Database dump frame
        self.ChildInfoSectionframe = Frame(master)
        self.ChildInfoSectionframe.pack(fill = 'x')

        #Child info section continued
        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nCHILD'S INFORMATION CONTINUED")
        labelChildInfoSection.pack(fill = "x")
        labelChildInfoSection.config(font=("Helvetica", 20))


        #HIV status
        curr.execute("SELECT HIV_Status FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #aware
        label = Label(self.ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.pack(anchor = 'w')
        curr.execute("SELECT Aware FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... Unanswered')
        label.pack(anchor = 'w')
        
        #why
        label = Label(self.ChildInfoSectionframe, text = "\nIf no,")
        label.pack(anchor = 'w')
        curr.execute("SELECT Why FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "please provide a reason why child is not aware ...................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "please provide a reason why child is not aware ...................................... Unanswered")
        label.pack(anchor = 'w')
        
#Close Database Connection
        curr.close()
        db.close()


        #Bottom Buttons
        self.bottoomButtonframe = Frame(master)
        self.bottoomButtonframe.pack(side = "bottom", fill = "x")

        #Continue
        continueButton = Button(self.bottoomButtonframe, text = "Continue", command = lambda: self.continueButtonHandler(id, date)).pack(side = 'right')
        #Previous
        previousButton = Button(self.bottoomButtonframe, text = "Previous", command = lambda: self.previousButtonHandler(id, date)).pack(side = 'left')



    def backSecondProfilePage(self, id):
        if self.prevSection is 1:
            self.SecondProfilePageRoot1.withdraw()
        if self.prevSection is 2:
            self.SecondProfilePageRoot2.withdraw()
        
        if self.PrevPage is 'FirstProfilePage':
            self.PrevPage = 'SecondProfilePage'
            self.FirstProfilePage(id)


    def continueButtonHandler(self, id, date):

        if self.prevSection is 0:
            self.SecondProfilePage1(id, date)

        elif self.prevSection is 1:
            self.SecondProfilePage2(id, date)
        
        elif self.prevSection is 2:
            self.root.destroy()


    def previousButtonHandler(self, id, date):
        if self.prevSection is 1:
            self.SecondProfilePage(id, date)
        
        elif self.prevSection is 2:
            self.SecondProfilePage1(id, date)


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

            self.backSecondProfilePage(id)

        else:
            #Delete cancelled
            showinfo('No', 'Delete has been cancelled')


root = Tk()
Main(root)
root.mainloop()
