import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import tkMessageBox
import MySQLdb


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.title("H.E.R.O. For Children")

#size & centering
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry("650x350")

        self.frames = {}

        for F in (LoginPage, HomePage, AdminUserPage, AddUser, DeleteUserPage, SearchPage, SearchResultsPage, FirstProfilePage, SecondProfilePage, EditProfile, AddNewApp, NewAppReturning, NameBirthEntryPage, NewChildApp):
            frame = F(self.frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)


        self.shared_data = {
            "username": tk.StringVar(),
        }

    def get_page(self, page_class):
        return self.frames[page_class]


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


#******************************************************************************************************************************************************


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

       #Database Connection
        db = MySQLdb.connect(
            host = "localhost", 
            user="root", 
            passwd = "Darling",
            db="HERO")
        curr = db.cursor()

        master = self

        #self.label = Label(master, text = "Welcome!")
        #self.label.pack()

        labelUsername = Label(master, text = "Username")
        #labelUsername.pack(side = LEFT)
        labelUsername.grid(row = 1, column = 1)

        self.entryUsername = Entry(master, bd = 5)
        #entryUsername = tk.Entry(master, bd = 5, textvariable=self.controller.shared_data["username"])

        #entryUsername.pack(side = RIGHT)
        self.entryUsername.grid(row = 1, column = 2)



        labelPassword = Label(master, text = "Password")
        #labelPassword.pack(side = LEFT)
        labelPassword.grid(row = 2, column = 1)

        entryPassword = Entry(master, bd = 5, show = "*")
        #entryPassword.pack(side = RIGHT)
        entryPassword.grid(row = 2, column = 2)

        db = MySQLdb.connect(
            host = "localhost",
            user="root",
            passwd = "Darling",
            db="HERO")
        curr = db.cursor()

        """These are the Buttons for the page"""

        # need to set things as callbacks so they dont get called immediately, so lambda
        loginButton = Button(master, text = "login", command = lambda: self.login(parent, controller, self.entryUsername, entryPassword, curr))
        loginButton.grid(row = 3, column = 2)

        closeButton = Button(master, text = "close", command=lambda: controller.destroy())
        closeButton.grid(row = 0, column = 0)

        global loggedIn
        loggedIn = 0


    def login(self, parent, controller, entryUsername, entryPassword, curr):

        curr.execute("SELECT * FROM User WHERE Username = %s AND Password = SHA1(%s)", (entryUsername.get(), entryPassword.get(),))
        result = curr.fetchone()

        if result is not None: # if the result isn't None then there is a user/password combination match
            loggedIn = 1
            username = entryUsername.get()
            Tk.update(controller)
            controller.show_frame(HomePage)
        else:
            tkMessageBox.showinfo("Login Page", "Either password or username was incorrect, try again")


#******************************************************************************************************************************************************


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        #Login_Page = self.controller.get_page(LoginPage)
        #
        #Login_Page.entryUsername.get()
        #username = self.controller.shared_data["username"].get()
        #self.Login= LoginPage(parent, controller)
        #username = self.Login.entryUsername.get()

        username = controller.get_page(LoginPage).entryUsername.get()
        
        print username
        print loggedIn

        if username is not '':

            db = MySQLdb.connect(
                host = "localhost",
                user="root",
                passwd = "Darling",
                db="HERO")
            curr = db.cursor()

            #TODO: pass in username
            #username = "Oz"

            pulled = curr.execute("SELECT User_Type FROM User WHERE Username = %s;", (username,))
            credentials = curr.fetchall()[0][0]

            closeButton = tk.Button(self, text = "Close", command=lambda: controller.destroy())
            closeButton.grid(row = 0, column = 0)

            newAppButton = tk.Button(self, text = "Add New Application", command=lambda: controller.show_frame(AddNewApp))
            newAppButton.grid(row = 1, column = 3, padx = 185, pady = 10)

            if (credentials == 'Administrator' or credentials == 'Manager'):

                searchButton = tk.Button(self, text = "Search",  command=lambda: controller.show_frame(SearchPage))
                searchButton.grid(row = 2, column = 3, padx = 185, pady = 10)

            if (credentials == 'Administrator'):
                adminButton = tk.Button(self, text = "Administrate Users", command=lambda: controller.show_frame(AdminUserPage))
                adminButton.grid(row = 3, column = 3, padx = 185, pady = 10)


            curr.close()
            db.close()



#******************************************************************************************************************************************************


class AdminUserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #TODO pass in username
        username = 'SonikaFInch'
        back = tk.Button(self, text = "Back", command = lambda: controller.show_frame(HomePage, username))
        back.grid(row = 0, column = 0)

        addButton = tk.Button(self, text = "Add", command=lambda: controller.show_frame(AddUser))
        addButton.grid(row = 1, column = 1, padx = 225, pady = 10)
        deleteButton = tk.Button(self, text = "Delete", command = lambda: controller.show_frame(DeleteUserPage))
        deleteButton.grid(row = 2, column = 1, padx = 225, pady = 10)



#******************************************************************************************************************************************************


class AddUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.frame = self
        self.frame.pack()

        global __entry1
        global __entry2
        global __entry3
        global __variable

        name = Label(self.frame, text="Name").grid(row=1)
        __entry1 = Entry(self.frame)
        __entry1.grid(row=1, column=1)

        username = Label(self.frame, text="Username").grid(row=2)
        __entry2 = Entry(self.frame)
        __entry2.grid(row=2, column=1)

        password = Label(self.frame, text="Password").grid(row=3)
        __entry3 = Entry(self.frame)
        __entry3.grid(row=3, column=1)

        level = Label(self.frame, text="Type").grid(row=4)
        __variable = StringVar(self)
        __variable.set("Regular")
        menu = OptionMenu(self.frame, __variable, 'Administrator', 'Manager', 'Regular').grid(row=4, column=1)

        add = Button(self.frame, text="Add User", command = lambda: self.addUser(parent, controller)).grid(row=6, column=3)
        back = Button(self.frame, text="Back", command = lambda: controller.show_frame(AdminUserPage)).grid(row=6, column=0)


    def addUser(self, parent, controller):

        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        curr.execute("""INSERT INTO User VALUES (%s, %s, SHA1(%s), %s);""", (__entry1.get(), __entry2.get(), __entry3.get(), __variable.get(),))
        db.commit()

        curr.close()
        db.close()

        tkMessageBox.showinfo("Add User", "Update Successful!")




#******************************************************************************************************************************************************


#TODO
#rn always deltes the last user
class DeleteUserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        nameHead = Label(self, text = "Nameame", font= "Verdana 10 underline")
        nameHead.grid(row = 1, column = 0)

        usernameHead = Label(self, text = "Username", font= "Verdana 10 underline")
        usernameHead.grid(row = 1, column = 1)

        critHead = Label(self, text = "User Type", font= "Verdana 10 underline")
        critHead.grid(row = 1, column = 2)

        back = Button(self, text="Back", command = lambda: controller.show_frame(AdminUserPage))
        back.grid(row = 0, column = 0)

        curr.execute("SELECT * FROM User")
        results = curr.fetchall()


        for i in range(len(results)):
            nameLabel = Label(self, text = results[i][0], font= "Verdana 10")
            nameLabel.grid(row = 2 + i, column = 0)

            usernameLabel = Label(self, text = results[i][1], font= "Verdana 10")
            usernameLabel.grid(row = 2 + i, column = 1)

            usertypeLabel = Label(self, text = results[i][3], font= "Verdana 10")
            usertypeLabel.grid(row = 2 + i, column = 2)

            deleteButton = Button(self, text = "Delete", command = lambda: self.deleteUser(parent, controller, results[i][1]))
            deleteButton.grid(row = 2 + i, column = 3)

        curr.close()
        db.close()
        '''
        count = 0
        for name,username,_,usertype in results:
            nameLabel = Label(self, text = name, font= "Verdana 10")
            nameLabel.grid(row = 2 + count, column = 0)

            usernameLabel = Label(self, text = username, font= "Verdana 10")
            usernameLabel.grid(row = 2 + count, column = 1)

            usertypeLabel = Label(self, text = usertype, font= "Verdana 10")
            usertypeLabel.grid(row = 2 + count, column = 2)

            deleteButton = Button(self, text = "Delete", command = lambda: self.deleteUser(parent, controller, )) # TODO: Fix deleteUser
            deleteButton.grid(row = 2 + count, column = 3)
            count += 1

        curr.close()
        db.close()
        '''

    def deleteUser(parent, controller, self, username):

        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        curr.execute("DELETE FROM User WHERE Username = %s", (username,))
        db.commit()

        curr.close()

        db.close()

        tkMessageBox.showinfo("Add User", "Update Successful!")



#******************************************************************************************************************************************************

class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        master = self

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


        programList = ['Any', 'None', "Child Application", "Camp High Five Application"]
        global __programs
        __programs = StringVar(master)
        __programs.set('Programs')

        dropdownProgram = OptionMenu(master, __programs, *programList)
        dropdownProgram.grid(row = 1, column = 1)



        #grab all dat submitted, remove duplicates, set to yearList
        childDatesSubmitted = curr.execute("SELECT Year(Date_Submitted) FROM Child_Application;")
        val1 = curr.fetchall()
        campDatesSubmitted = curr.execute("SELECT Year(Date_Submitted) FROM Camp_Application;")
        val2 = curr.fetchall()
        yearList = []

        for item in val1:
            if item not in yearList:
                yearList.append(item)

        for item in val2:
            if item not in yearList:
                yearList.append(item)

        global __years
        __years = StringVar(master)
        __years.set("Year")

        #add back yearlist

        dropdownYear = OptionMenu(master, __years, "Any", "None", *yearList)
        dropdownYear.grid(row = 1, column = 2)

        categoriesList = ['None', 'Zip Code', 'City', "County", 'Referral Source', "Child's Age",
                    "Child's Gender", "Child's Race/Ethnicity",
                    "Child's HIV Status (infected or affected)", "Child's Other Issues",
                    "Child's HERO Program Participation", "Child's Allergies", "Child's Years with HERO",
                    "Household Composition", "Parent(s) HIV Status (infected or affected)",
                    "Household Income Range", "Household Income Source", "Parent(s) Highest Level of Education",
                    "Parent(s) Employment Status"]

        global __categories
        __categories = StringVar(master)
        __categories.set("Category")

        dropdownCategories = OptionMenu(master, __categories, *categoriesList)
        dropdownCategories.grid(row = 3, column = 1)


        catEntry = Entry(master, width=15)
        catEntry.grid(row = 3, column = 2)

        searchCatButton = Button(master, text = "Search", command=lambda: controller.show_frame(SearchResultsPage))
        searchCatButton.grid(row = 3, column = 3)

        #TODO: pass in username
        username = 'SonikaFinch'
        back = Button(master, text = "Back", command = lambda: controller.show_frame(HomePage, username))
        back.grid(row = 0, column = 0)

        txt = Label(master, text = "First Name:")
        txt.grid(row = 5, column = 1)

        firstName = Entry(master, width=15)
        firstName.grid(row = 5, column = 2)

        txt = Label(master, text = "Last Name:")
        txt.grid(row = 6, column = 1)

        lastName = Entry(master, width=15)
        lastName.grid(row = 6, column = 2)

        searchNameButton = Button(master, text = "Search", command=lambda: controller.show_frame(SearchResultsPage))
        searchNameButton.grid(row = 5, column = 3)

        curr.close()
        db.close()




#******************************************************************************************************************************************************

class SearchResultsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        master = self

        camp = ''
        child = ''

        db = MySQLdb.connect(host="localhost", user="root", passwd="Darling", db="HERO")
        curr = db.cursor()

        #check for program selection
        selectedProgram = "Child Application"
        #TODO: pass in programs
        #programs.get()
        programParam = 1
        if (selectedProgram == 'Program') or (selectedProgram == 'None'):
            #no program input
            programParam = 0

        #check for year selection
        selectedYear = '2016'
        #TODO: pass in years
        #years.get()
        yearParam = 1
        if (selectedYear == 'Year') or (selectedYear == 'None'):
            #no year input
            yearParam = 0
        else:
            selectedYear = selectedYear[1:5]

        #check for category selection
        selectedCategory = "Child's Gender"
        #TODO: pass in categories
        #
        #categories.get()
        catParam = 1

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

        back = Button(master, text = "Back", command = lambda: controller.show_frame(SearchPage))
        back.grid(row = 0, column = 0)


#******************************************************************************************************************************************************


class FirstProfilePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        # Connect to database
        db = MySQLdb.connect(host="localhost", user="root", passwd="Darling", db="HERO")
        curr = db.cursor()

        # id
        id = 1
        name_first = 'John'
        name_last = 'Osman'

        self.frame = self
        self.frame.pack()

        # Back button will take you to previous page
        back = Button(self.frame, text="Back", command = lambda: self.back(parent, controller)).grid(row=0, column=0)
        # Delete will permanently remove child from database
        delete = Button(self.frame, text="Delete", command=lambda: self.delete(parent, controller))
        delete.grid(row=0, column=10)

        #name title
        firstNameLabel = Label(self.frame, text= name_first, font="Arial 12 underline").grid(row=1, column=3)
        lastNameLabel = Label(self.frame, text= name_last, font="Arial 12 underline").grid(row=1, column=4)

        #child app
        childAppLabel = Label(self.frame, text= "Child Applications").grid(row=2, column=0)

        curr.execute("SELECT Date_Submitted FROM Child_Application WHERE ID = %s;", (id,))
        childDateArr = curr.fetchall()

        r = 3
        for childDate in childDateArr:
            #date of program attended
            dateLabel = Label(self.frame, text= childDate[0]).grid(row=r, column=1)

            # Details button will take you to another page
            details = Button(self.frame, text="See Details", command=lambda: controller.show_frame(SecondProfilePage)).grid(row=r, column=5)
            r = r + 1

        #camp app
        campAppLabel = Label(self.frame, text= "Camp Applications").grid(row=r, column=0)

        curr.execute("SELECT Date_Submitted FROM Camp_Application WHERE ID = %s;", (id,))
        campDateArr = curr.fetchall()

        r = r + 1
        for campDate in campDateArr:
            #date of program attended
            dateLabel = Label(self.frame, text= campDate[0]).grid(row=r, column=1)

            # Details button will take you to another page
            details = Button(self.frame, text="See Details", command=lambda: controller.show_frame(SecondProfilePage)).grid(row=r, column=5)
            r = r + 1



        curr.close()
        db.close()

    #TODO:
    #trace prev places
    def back(self, parent, controller):
        if 1:
            controller.show_frame(SearchResultsPage)
        else:
            controller.show_frame(NameBirthEntryPage)

    def delete(self, parent, controller):
        controller.destroy()



#******************************************************************************************************************************************************


class SecondProfilePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.frame = self

#Buttons
    #back button frame + back button
        self.buttonframe = Frame(self.frame)
        self.buttonframe.pack(side = "top", fill = "x")

        #fix alignment
        backButton = Button(self.buttonframe, text = "Back", command = lambda: controller.show_frame(FirstProfilePage))
        backButton.pack(side = "left")

        #edit
        editButton = Button(self.buttonframe, text = "Edit Application", command = lambda: controller.show_frame(EditProfile))
        editButton.pack(side = "right")

        #delete
        deleteButton = Button(self.buttonframe, text = "Delete Application", command = lambda: self.delete(parent, controller))
        deleteButton.pack(side = "right")

#figure out how to pass in parameters
        id = 1
        date = '2016-11-24'

#Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

#Database dump frame
        self.ChildInfoSectionframe = Frame(self.frame)
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
        label = Label(self.ChildInfoSectionframe, text = "\nDate Submitted...................................................................................... " + date)
        label.pack(anchor = 'w')

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

        #Referral source
        curr.execute("SELECT Referral_Source FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #school attending
        curr.execute("SELECT School_attending FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Grade Level
        curr.execute("SELECT School_grade_level FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Ethnicity
        curr.execute("SELECT Ethnicity_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        ethnicityOther = curr.fetchall()[0][0]
        if ethnicityOther is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... " + ethnicityOther)
        else:
            curr.execute("SELECT Ethnicity FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            ethnicity = curr.fetchall()[0][0]
            if ethnicity is not None:
                label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... " + ethnicity)
            else:
                label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Even been...
        label = Label(self.ChildInfoSectionframe, text = "\nHas your child ever been...")
        label.pack(anchor = 'w')

        #ADD_ADHD
        curr.execute("SELECT ADD_ADHD FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. Unanswered')
        label.pack(anchor = 'w')

        #Learning_Disability
        curr.execute("SELECT Learning_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... Unanswered')
        label.pack(anchor = 'w')

        #Developmental_Disability
        curr.execute("SELECT Developmental_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... Unanswered')
        label.pack(anchor = 'w')

        #Mental_Health_Issues
        curr.execute("SELECT Mental_Health_Issues FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. Unanswered')
        label.pack(anchor = 'w')

        #Other_Medical_Condition
        curr.execute("SELECT Other_Medical_Condition FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... Unanswered')
        label.pack(anchor = 'w')

        #Victim_of_Abuse
        curr.execute("SELECT Victim_of_Abuse FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... Unanswered')
        label.pack(anchor = 'w')

        #Criminal_Justice_System
        curr.execute("SELECT Criminal_Justice_System FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... Unanswered')
        label.pack(anchor = 'w')

        #Custody
        curr.execute("SELECT Custody_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        custodyOther = curr.fetchall()[0][0]
        if custodyOther is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... " + custodyOther)
        else:
            curr.execute("SELECT Legal_Custody FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            custody = curr.fetchall()[0][0]
            if custody is not None:
                label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... " + custody)
            else:
                label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... Unanswered")
        label.pack(anchor = 'w')


#Parent/ Guardian Section
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Last Name
        curr.execute("SELECT Name_Last FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Age
        curr.execute("SELECT Age FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #HIV Status
        curr.execute("SELECT HIV_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Adoptive Parent
        curr.execute("SELECT Adoptive_Parent FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Marital Status
        curr.execute("SELECT Marital_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Highest Level of Education Completed
        curr.execute("SELECT Education_Completed FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. Unanswered")
        label.pack(anchor = 'w')

        #Employment Status
        curr.execute("SELECT Employment_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Employment Company
        label = Label(self.ChildInfoSectionframe, text = "\nIf employed,")
        label.pack(anchor = 'w')

        curr.execute("SELECT Employment_Company_Name FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "please provide Company Name ............................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "please provide Company Name ............................................................. Unanswered")
        label.pack(anchor = 'w')

        #Address
        curr.execute("SELECT Address_Street FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAddress ................................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAddress ................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #City
        curr.execute("SELECT Address_City FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #State
        curr.execute("SELECT Address_State FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nState .................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nState .................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Zip
        curr.execute("SELECT Address_Zip FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Work Phone
        curr.execute("SELECT WorkPhone FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #E-mail
        curr.execute("SELECT Email FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nE-mail ................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nE-mail ................................................................................................... Unanswered")
        label.pack(anchor = 'w')


#Absent Parent Info
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Last Name
        curr.execute("SELECT Name_Last FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Telephone
        curr.execute("SELECT Telephone FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nTelephone .............................................................................................. " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nTelephone .............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Home Address
        curr.execute("SELECT Address_Street FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #City
        curr.execute("SELECT Address_City FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #County
        curr.execute("SELECT Address_County FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Zip
        curr.execute("SELECT Address_Zip FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ......................................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ......................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #HIV Status
        curr.execute("SELECT HIV_Status FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

#Household Info
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nHOUSEHOLD INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #list all individuals living in the household
        label = Label(self.ChildInfoSectionframe, text = "\nAll Individuals Living in the Household")
        label.pack(anchor = 'w')

        curr.execute("SELECT Count FROM Household_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        countArr = curr.fetchall()
        for count in countArr:
            #Name
            curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... " + val)
            else:
                label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... Unanswered")
            label.pack(anchor = 'w')

            #Relationship to Child
            curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. " + val)
            else:
                label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. Unanswered")
            label.pack(anchor = 'w')

            #Sex
            curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... " + val)
            else:
                label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... Unanswered")
            label.pack(anchor = 'w')

            #Age
            curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... " + str(val))
            else:
                label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... Unanswered")
            label.pack(anchor = 'w')

            #HIV Status
            curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ " + str(val) + "\n")
            else:
                label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ Unanswered\n")
            label.pack(anchor = 'w')

        #Family Annual Income Info
        curr.execute("SELECT Fam_Annual_Income FROM Fam_Annual_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... Unanswered")
        label.pack(anchor = 'w')

        #Source of Family Income
        curr.execute("SELECT Other FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        sourceOther = curr.fetchall()[0][0]
        if sourceOther is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... " + sourceOther)
        else:
            curr.execute("SELECT Source_Fam_Income FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            source = curr.fetchall()[0][0]
            if source is not None:
                label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... " + source)
            else:
                label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... Unanswered")
        label.pack(anchor = 'w')


 #In Case of Emergency Contact
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Last Name
        curr.execute("SELECT Name_Last FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Relationship to Child
        curr.execute("SELECT Relationship_to_Child FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nRelationship to Child ............................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nRelationship to Child ............................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Home Address
        curr.execute("SELECT Address_Street FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #City
        curr.execute("SELECT Address_City FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #State
        curr.execute("SELECT Address_State FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nState ..................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nState ..................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Zip
        curr.execute("SELECT Address_Zip FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Home Phone Number
        curr.execute("SELECT Phone_Home FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Cell Phone Number
        curr.execute("SELECT Phone_Cell FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Alternate Phone Number
        curr.execute("SELECT Phone_Alt FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... Unanswered")
        label.pack(anchor = 'w')

#H.E.R.O. Programs
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #Program(s) you wish your child to participate in
        curr.execute("SELECT HERO_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]
        if var is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you wish your child to participate in .................................... " + var)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you wish your child to participate in .................................... Unanswered")
        label.pack(anchor = 'w')

        #Program(s) you would be interested in your child to participating in
        curr.execute("SELECT Future_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        programs = curr.fetchall()[0][0]
        curr.execute("SELECT Future_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        otherPrograms = curr.fetchall()[0][0]
        if programs is not None and otherPrograms is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... " + programs + ", " + otherPrograms)
        elif programs is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... " + programs)
        elif otherPrograms is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... " + otherPrograms)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... Unanswered")
        label.pack(anchor = 'w')

#Referral Needs
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #Needs
        curr.execute("SELECT Referral FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        Referral = curr.fetchall()[0][0]
        curr.execute("SELECT Referral_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        otherReferral = curr.fetchall()[0][0]
        if Referral is not None and otherReferral is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... " + Referral + ", " + otherReferral)
        elif Referral is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... " + Referral)
        elif otherReferral is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ........................................................................................ " + otherReferral)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ........................................................................................ Unanswered")
        label.pack(anchor = 'w')

#Statement of Understanding
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #one
        curr.execute("SELECT Statement_One FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #two
        curr.execute("SELECT Statement_Two FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #three
        curr.execute("SELECT Statement_Three FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #four
        curr.execute("SELECT Statement_Four FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #five
        curr.execute("SELECT Statement_Five FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #six
        curr.execute("SELECT Statement_Six FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #seven
        curr.execute("SELECT Statement_Seven FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

#Signature
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSIGNATURE")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        curr.execute("SELECT Signature FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. Unanswered")
        label.pack(anchor = 'w')

#Close Database Connection
        curr.close()
        db.close()


    def delete(self, parent, controller):
        if askyesno('Verify', 'Really delete?'):
            #Delete application from database

            #Open Database Connection
            db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
            curr = db.cursor()

            #Execute
            curr.execute("DELETE FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()

            #Close Database Connection
            curr.close()
            db.close()

            #UI feedback
            showwarning('Delete', 'Application Deleted')

            #Go back to 1st level profile page (call back if you can)
            self.master.destroy()

        else:
            #Delete cancelled
            showinfo('No', 'Delete has been cancelled')



#******************************************************************************************************************************************************


class EditProfile(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



#TODO
    #figure out how to pass in parameters
    #deal with changing these? I think naw
        global __id
        global __date
        __id = 1
        __date = '2016-11-24'


#Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        self.frame = self

#Buttons
        #frame
        self.buttonframe = Frame(self.frame)
        self.buttonframe.pack(side = "top", fill = "x")

        #back
        backButton = Button(self.buttonframe, text = "Back", command = lambda: controller.show_frame(SecondProfilePage))
        backButton.pack(side = "left")

        #home
        #TODO pass in username
        username = 'SonikaFinch'
        backButton = Button(self.buttonframe, text = "Home", command = lambda: controller.show_frame(HomePage, username))
        backButton.pack(side = "left")

        #delete
        deleteButton = Button(self.buttonframe, text = "Delete Application", command = lambda: self.delete())
        deleteButton.pack(side = "right")

#Child info section ************************************************************************************************************************
        self.ChildInfoSectionframe = Frame(self.frame)
        self.ChildInfoSectionframe.pack(fill = 'y', side = 'left')
        r = 0

        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\nCHILD'S INFORMATION")
        labelChildInfoSection.grid(row = r, column = 0)
        labelChildInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        #childInfo0
        __childInfo0 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo0.insert(0, val)
        else:
            __childInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global __childInfo1
        __childInfo1 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo1.insert(0, val)
        else:
            __childInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #nickname
        curr.execute("SELECT Name_Nickname FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. ")
        global __childInfo2
        __childInfo2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo2.insert(0, val)
        else:
            __childInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        curr.execute("SELECT Address_Street FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global __childInfo3
        __childInfo3 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo3.insert(0, val)
        else:
            __childInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        curr.execute("SELECT Address_City FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global __childInfo4
        __childInfo4 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo4.insert(0, val)
        else:
            __childInfo4.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        curr.execute("SELECT Address_County FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global __childInfo5
        __childInfo5 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo5.insert(0, val)
        else:
            __childInfo5.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        curr.execute("SELECT Address_Zip FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global __childInfo6
        __childInfo6 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo6.insert(0, val)
        else:
            __childInfo6.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #home phone
        curr.execute("SELECT Home_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... ")
        global __childInfo7
        __childInfo7 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo7.insert(0, val)
        else:
            __childInfo7.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian phone
        curr.execute("SELECT Guardian_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ ")
        global __childInfo8
        __childInfo8 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo8.insert(0, val)
        else:
            __childInfo8.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo8())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian email
        curr.execute("SELECT Guardian_Email FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... ")
        global __childInfo9
        __childInfo9 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo9.insert(0, val)
        else:
            __childInfo9.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo9())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        curr.execute("SELECT Age FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global __childInfo10
        __childInfo10 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo10.insert(0, val)
        else:
            __childInfo10.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo10())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #birthday
        curr.execute("SELECT Birthday FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ ")
        global __childInfo11
        __childInfo11 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo11.insert(0, val)
        else:
            __childInfo11.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo11())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. ")

        curr.execute("SELECT Gender FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __childInfo12
        __childInfo12 = StringVar()

        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __childInfo12, *choices)

        if val is not None:
            __childInfo12.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo12())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __childInfo13
        __childInfo13 = StringVar()

        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __childInfo13, *choices)

        if val is not None:
            __childInfo13.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo13())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #aware
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... ')

        curr.execute("SELECT Aware FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]
        global __childInfo14
        __childInfo14 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __childInfo14, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __childInfo14, value=2)

        if val is not None:
            if val is 0:
                __childInfo14.set(2)
            else:
                __childInfo14.set(1)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo14())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #why
        curr.execute("SELECT Why FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "If no, please provide a reason why child is not aware .............................. ")
        global __childInfo15
        __childInfo15 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo15.insert(0, val)
        else:
            __childInfo15.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo15())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Referral source
        curr.execute("SELECT Referral_Source FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... ")
        global __childInfo16
        __childInfo16 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo16.insert(0, val)
        else:
            __childInfo16.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo16())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #school attending
        curr.execute("SELECT School_attending FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. ")
        global __childInfo17
        __childInfo17 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo17.insert(0, val)
        else:
            __childInfo17.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo17())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Grade Level
        curr.execute("SELECT School_grade_level FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... ")
        global __childInfo18
        __childInfo18 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo18.insert(0, val)
        else:
            __childInfo18.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo18())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo18.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Ethnicity
        label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... ")

        curr.execute("SELECT Ethnicity FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __childInfo19
        __childInfo19 = StringVar()

        choices = ['White/Caucasian','Black/African-American','Hispanic/Latino',
        'Native American','Asian/Pacific Islander/Indian Sub-Continent','Multi-racial','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __childInfo19, *choices)

        if val is not None:
            __childInfo19.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo19())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Ethnicity Other
        curr.execute("SELECT Ethnicity_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global __childInfo20
        __childInfo20 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo20.insert(0, val)
        else:
            __childInfo20.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo20())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Even been...
        label = Label(self.ChildInfoSectionframe, text = "\nHas your child ever been...")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #ADD_ADHD
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. ')

        curr.execute("SELECT ADD_ADHD FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]
        global __childInfo21
        __childInfo21 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __childInfo21, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __childInfo21, value=2)

        if val is not None:
            if val is 0:
                __childInfo21.set(2)
            else:
                __childInfo21.set(1)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo21())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Learning_Disability
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')

        curr.execute("SELECT Learning_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]
        global __childInfo22
        __childInfo22 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __childInfo22, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __childInfo22, value=2)

        if val is not None:
            if val is 0:
                __childInfo22.set(2)
            else:
                __childInfo22.set(1)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo22())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Developmental_Disability
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... ')

        curr.execute("SELECT Developmental_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]
        global __childInfo23
        __childInfo23 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __childInfo23, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __childInfo23, value=2)

        if val is not None:
            if val is 0:
                __childInfo23.set(2)
            else:
                __childInfo23.set(1)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo23())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Mental_Health_Issues
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. ')

        curr.execute("SELECT Mental_Health_Issues FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]
        global __childInfo24
        __childInfo24 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __childInfo24, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __childInfo24, value=2)

        if val is not None:
            if val is 0:
                __childInfo24.set(2)
            else:
                __childInfo24.set(1)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo24())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Other_Medical_Condition
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... ')

        curr.execute("SELECT Other_Medical_Condition FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]
        global __childInfo25
        __childInfo25 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __childInfo25, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __childInfo25, value=2)

        if val is not None:
            if val is 0:
                __childInfo25.set(2)
            else:
                __childInfo25.set(1)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo25())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Victim_of_Abuse
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... ')

        curr.execute("SELECT Victim_of_Abuse FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]
        global __childInfo26
        __childInfo26 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __childInfo26, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __childInfo26, value=2)

        if val is not None:
            if val is 0:
                __childInfo26.set(2)
            else:
                __childInfo26.set(1)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo26())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Criminal_Justice_System
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... ')

        curr.execute("SELECT Criminal_Justice_System FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]
        global __childInfo27
        __childInfo27 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __childInfo27, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __childInfo27, value=2)

        if val is not None:
            if val is 0:
                __childInfo27.set(2)
            else:
                __childInfo27.set(1)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo27())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Custody
        label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... ")

        curr.execute("SELECT Legal_Custody FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __childInfo28
        __childInfo28 = StringVar()

        choices = ['Mother','Father','Both Parents','Aunt/Uncle','Grandparent','Pending Court Action','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __childInfo28, *choices)

        if val is not None:
            __childInfo28.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo28())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Custody Other
        curr.execute("SELECT Custody_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global __childInfo29
        __childInfo29 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __childInfo29.insert(0, val)
        else:
            __childInfo29.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo29())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __childInfo29.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Section ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global __parentInfo0
        __parentInfo0 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo0.insert(0, val)
        else:
            __parentInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global __parentInfo1
        __parentInfo1 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo1.insert(0, val)
        else:
            __parentInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global __parentInfo2
        __parentInfo2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo2.insert(0, val)
        else:
            __parentInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Age
        curr.execute("SELECT Age FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global __parentInfo3
        __parentInfo3 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo3.insert(0, val)
        else:
            __parentInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __parentInfo4
        __parentInfo4 = StringVar()

        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __parentInfo4, *choices)

        if val is not None:
            __parentInfo4.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Adoptive Parent
        label = Label(self.ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... ")

        curr.execute("SELECT Adoptive_Parent FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __parentInfo5
        __parentInfo5 = StringVar()

        choices = ['Yes','No','Not Applicable']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __parentInfo5, *choices)

        if val is not None:
            __parentInfo5.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Marital Status
        label = Label(self.ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... ")

        curr.execute("SELECT Marital_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __parentInfo6
        __parentInfo6 = StringVar()

        choices = ['Married','Single','Separated','Divorced','Widowed']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __parentInfo6, *choices)

        if val is not None:
            __parentInfo6.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Highest Level of Education Completed
        label = Label(self.ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. ")

        curr.execute("SELECT Education_Completed FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __parentInfo7
        __parentInfo7 = StringVar()

        choices = ['HS','GED','Some College','Associates Degree','Bachelor Degree','Master Degree','Doctorate']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __parentInfo7, *choices)

        if val is not None:
            __parentInfo7.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Status
        label = Label(self.ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... ")

        curr.execute("SELECT Employment_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __parentInfo8
        __parentInfo8 = StringVar()

        choices = ['Full-Time','Part-Time','Unemployed','Disability']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __parentInfo8, *choices)

        if val is not None:
            __parentInfo8.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo8())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Company
        curr.execute("SELECT Employment_Company_Name FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        r= r+1
        label = Label(self.ChildInfoSectionframe, text = "\nIf employed,")
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = "please provide Company Name ............................................................. ")

        global __parentInfo9
        __parentInfo9 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo9.insert(0, val)
        else:
            __parentInfo9.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo9())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Address
        curr.execute("SELECT Address_Street FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nAddress ................................................................................................ ")
        global __parentInfo10
        __parentInfo10 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo10.insert(0, val)
        else:
            __parentInfo10.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo10())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global __parentInfo11
        __parentInfo11 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo11.insert(0, val)
        else:
            __parentInfo11.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo11())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        curr.execute("SELECT Address_State FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nState .................................................................................................... ")
        global __parentInfo12
        __parentInfo12 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo12.insert(0, val)
        else:
            __parentInfo12.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo12())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global __parentInfo13
        __parentInfo13 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo13.insert(0, val)
        else:
            __parentInfo13.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo13())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Work Phone
        curr.execute("SELECT WorkPhone FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... ")
        global __parentInfo14
        __parentInfo14 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo14.insert(0, val)
        else:
            __parentInfo14.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo14())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #E-mail
        curr.execute("SELECT Email FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nE-mail ................................................................................................... ")
        global __parentInfo15
        __parentInfo15 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __parentInfo15.insert(0, val)
        else:
            __parentInfo15.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo15())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __parentInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Absent Parent Info ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global __absParentInfo0
        __absParentInfo0 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __absParentInfo0.insert(0, val)
        else:
            __absParentInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __absParentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global __absParentInfo1
        __absParentInfo1 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __absParentInfo1.insert(0, val)
        else:
            __absParentInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __absParentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Telephone
        curr.execute("SELECT Telephone FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nTelephone .............................................................................................. ")
        global __absParentInfo2
        __absParentInfo2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __absParentInfo2.insert(0, val)
        else:
            __absParentInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __absParentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        curr.execute("SELECT Address_Street FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global __absParentInfo3
        __absParentInfo3 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __absParentInfo3.insert(0, val)
        else:
            __absParentInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __absParentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global __absParentInfo4
        __absParentInfo4 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __absParentInfo4.insert(0, val)
        else:
            __absParentInfo4.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __absParentInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #County
        curr.execute("SELECT Address_County FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global __absParentInfo5
        __absParentInfo5 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __absParentInfo5.insert(0, val)
        else:
            __absParentInfo5.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __absParentInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nZip ......................................................................................................... ")
        global __absParentInfo6
        __absParentInfo6 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __absParentInfo6.insert(0, val)
        else:
            __absParentInfo6.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __absParentInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __absParentInfo7
        __absParentInfo7 = StringVar()

        choices = ['HIV Positive','HIV Negative', 'Unkown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __absParentInfo7, *choices)

        if val is not None:
            __absParentInfo7.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

#Household Info ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nHOUSEHOLD INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #list all individuals living in the household
        label = Label(self.ChildInfoSectionframe, text = "\nAll Individuals Living in the Household")
        r = r+1
        label.grid(row = r, column = 0)

    #person1
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 1')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(1))
        buttonUpdate.grid(row = r, column = 2)

        person = 1

        #Name1
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo10
        __houseInfo10 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo10.insert(0, 'Unanswered')
        else:
            __houseInfo10.insert(0, val[0][0])

        r = r+1
        __houseInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child1
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo11
        __houseInfo11 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo11.insert(0, 'Unanswered')
        else:
            __houseInfo11.insert(0, val[0][0])

        r = r+1
        __houseInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex1
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo12
        __houseInfo12 = StringVar()

        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo12, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo12.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age1
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo13
        __houseInfo13 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo13.insert(0, 'Unanswered')
        else:
            __houseInfo13.insert(0, val[0][0])

        r = r+1
        __houseInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status1
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo14
        __houseInfo14 = StringVar()

        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo14, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo14.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person2
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 2')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(2))
        buttonUpdate.grid(row = r, column = 2)

        person = 2

        #Name2
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo20
        __houseInfo20 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo20.insert(0, 'Unanswered')
        else:
            __houseInfo20.insert(0, val[0][0])

        r = r+1
        __houseInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child2
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo21
        __houseInfo21 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo21.insert(0, 'Unanswered')
        else:
            __houseInfo21.insert(0, val[0][0])

        r = r+1
        __houseInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex2
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo22
        __houseInfo22 = StringVar()

        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo22, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo22.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age2
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo23
        __houseInfo23 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo23.insert(0, 'Unanswered')
        else:
            __houseInfo23.insert(0, val[0][0])

        r = r+1
        __houseInfo23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status2
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo24
        __houseInfo24 = StringVar()

        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo24, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo24.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person3
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 3')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(3))
        buttonUpdate.grid(row = r, column = 2)


        person = 3

        #Name3
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo30
        __houseInfo30 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo30.insert(0, 'Unanswered')
        else:
            __houseInfo30.insert(0, val[0][0])

        r = r+1
        __houseInfo30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child3
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo31
        __houseInfo31 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo31.insert(0, 'Unanswered')
        else:
            __houseInfo31.insert(0, val[0][0])

        r = r+1
        __houseInfo31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex3
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo32
        __houseInfo32 = StringVar()

        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo32, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo32.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age3
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo33
        __houseInfo33 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo33.insert(0, 'Unanswered')
        else:
            __houseInfo33.insert(0, val[0][0])

        r = r+1
        __houseInfo33.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status3
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo34
        __houseInfo34 = StringVar()

        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo34, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo34.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person4
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 4')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(4))
        buttonUpdate.grid(row = r, column = 2)

        person = 4

        #Name4
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo40
        __houseInfo40 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo40.insert(0, 'Unanswered')
        else:
            __houseInfo40.insert(0, val[0][0])

        r = r+1
        __houseInfo40.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child4
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo41
        __houseInfo41 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo41.insert(0, 'Unanswered')
        else:
            __houseInfo41.insert(0, val[0][0])

        r = r+1
        __houseInfo41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex4
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo42
        __houseInfo42 = StringVar()

        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo42, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo42.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age4
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo43
        __houseInfo43 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo43.insert(0, 'Unanswered')
        else:
            __houseInfo43.insert(0, val[0][0])

        r = r+1
        __houseInfo43.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status4
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo44
        __houseInfo44 = StringVar()

        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo44, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo44.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person5
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 5')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(5))
        buttonUpdate.grid(row = r, column = 2)

        person = 5

        #Name5
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo50
        __houseInfo50 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo50.insert(0, 'Unanswered')
        else:
            __houseInfo50.insert(0, val[0][0])

        r = r+1
        __houseInfo50.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child5
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo51
        __houseInfo51 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo51.insert(0, 'Unanswered')
        else:
            __houseInfo51.insert(0, val[0][0])

        r = r+1
        __houseInfo51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex5
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo52
        __houseInfo52 = StringVar()

        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo52, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo52.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age5
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo53
        __houseInfo53 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo53.insert(0, 'Unanswered')
        else:
            __houseInfo53.insert(0, val[0][0])

        r = r+1
        __houseInfo53.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status5
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo54
        __houseInfo54 = StringVar()

        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo54, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo54.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person6
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 6')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(6))
        buttonUpdate.grid(row = r, column = 2)

        person = 6

        #Name6
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo60
        __houseInfo60 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo60.insert(0, 'Unanswered')
        else:
            __houseInfo60.insert(0, val[0][0])

        r = r+1
        __houseInfo60.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child6
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo61
        __houseInfo61 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo61.insert(0, 'Unanswered')
        else:
            __houseInfo61.insert(0, val[0][0])

        r = r+1
        __houseInfo61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex6
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo62
        __houseInfo62 = StringVar()

        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo62, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo62.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age6
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo63
        __houseInfo63 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            __houseInfo63.insert(0, 'Unanswered')
        else:
            __houseInfo63.insert(0, val[0][0])

        r = r+1
        __houseInfo63.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status6
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, person,))
        val = curr.fetchall()

        global __houseInfo64
        __houseInfo64 = StringVar()

        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __houseInfo64, *choices)

        if (val is not ()) and (val[0][0] is not None):
            __houseInfo64.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


        #Family Annual Income Info
        label = Label(self.ChildInfoSectionframe, text = "\n\nFamily Annual Income Information ......................................................... ")

        curr.execute("SELECT Fam_Annual_Income FROM Fam_Annual_Income WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __famIncome0
        __famIncome0 = StringVar()

        choices = ['$0-10,000','$10,001-15,000','$15,001-20,000','$20,000-25,000','$25,001-30,000','$30,001-35,000','$35,001-40,000','$40,001-45,000','$50,000+']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __famIncome0, *choices)

        if val is not None:
            __famIncome0.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatefamIncome0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income
        label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... ")

        curr.execute("SELECT Source_Fam_Income FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __famIncome1
        __famIncome1 = StringVar()

        choices = ['Employment','Government Support','Public Assistance', 'Unemployment Benefits','Medicaid','Social Security','Veterans Benefits','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, __famIncome1, *choices)

        if val is not None:
            __famIncome1.set(val)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatefamIncome1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income Other
        curr.execute("SELECT Other FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global __famIncome2
        __famIncome2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __famIncome2.insert(0, val)
        else:
            __famIncome2.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatefamIncome2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __famIncome2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#In Case of Emergency Contact ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global __emergencyInfo0
        __emergencyInfo0 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo0.insert(0, val)
        else:
            __emergencyInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global __emergencyInfo1
        __emergencyInfo1 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo1.insert(0, val)
        else:
            __emergencyInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global __emergencyInfo2
        __emergencyInfo2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo2.insert(0, val)
        else:
            __emergencyInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        curr.execute("SELECT Address_Street FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global __emergencyInfo3
        __emergencyInfo3 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo3.insert(0, val)
        else:
            __emergencyInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global __emergencyInfo4
        __emergencyInfo4 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo4.insert(0, val)
        else:
            __emergencyInfo4.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        curr.execute("SELECT Address_State FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nState ..................................................................................................... ")
        global __emergencyInfo5
        __emergencyInfo5 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo5.insert(0, val)
        else:
            __emergencyInfo5.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global __emergencyInfo6
        __emergencyInfo6 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo6.insert(0, val)
        else:
            __emergencyInfo6.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Phone Number
        curr.execute("SELECT Phone_Home FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. ")
        global __emergencyInfo7
        __emergencyInfo7 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo7.insert(0, val)
        else:
            __emergencyInfo7.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Cell Phone Number
        curr.execute("SELECT Phone_Cell FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... ")
        global __emergencyInfo8
        __emergencyInfo8 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo8.insert(0, val)
        else:
            __emergencyInfo8.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo8())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Alternate Phone Number
        curr.execute("SELECT Phone_Alt FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... ")
        global __emergencyInfo9
        __emergencyInfo9 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            __emergencyInfo9.insert(0, val)
        else:
            __emergencyInfo9.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo9())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        __emergencyInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#H.E.R.O. Programs ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS\n")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Program(s) you wish your child to participate in
        label = Label(self.ChildInfoSectionframe, text = "Program(s) you wish your child to participate in .................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatePrograms0())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT HERO_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))

        var = curr.fetchall()[0][0]

        #Super HEROes Program
        global __programs0
        __programs0 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Super HEROes Program", variable = __programs0).grid(row = r,  column = 1, sticky = W)

        if 'Super HEROes Program' in var:
            __programs0.set(1)

        #Bright HEROs Program
        global __programs1
        __programs1 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Bright HEROs Program", variable = __programs1).grid(row = r,  column = 1, sticky = W)

        if 'Bright HEROs Program' in var:
            __programs1.set(1)

        #Camp High Five
        global __programs2
        __programs2 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Camp High Five", variable = __programs2).grid(row = r,  column = 1, sticky = W)

        if 'Camp High Five' in var:
            __programs2.set(1)

        #Holiday of HEROs
        global __programs3
        __programs3 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Holiday of HEROs", variable = __programs3).grid(row = r,  column = 1, sticky = W)

        if 'Holiday of HEROs' in var:
            __programs3.set(1)

        #Transition to Adulthood
        global __programs4
        __programs4 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Transition to Adulthood", variable = __programs4).grid(row = r,  column = 1, sticky = W)

        if 'Transition to Adulthood' in var:
            __programs4.set(1)


    #Program(s) you would be interested in your child to participating in
        label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatePrograms1())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT Future_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))

        var = curr.fetchall()[0][0]

        #Healthy HEROs (health curriculum)
        global __programs5
        __programs5 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Healthy HEROs", variable = __programs5).grid(row = r,  column = 1, sticky = SW)

        if 'Healthy HEROs' in var:
            __programs5.set(1)

        #Career Development/Job Readiness
        global __programs6
        __programs6 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Career Development/Job Readiness", variable = __programs6).grid(row = r,  column = 1, sticky = W)

        if 'Career Development/Job Readiness' in var:
            __programs6.set(1)

        #Other
        global __programs7
        __programs7 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Other", variable = __programs7).grid(row = r,  column = 1, sticky = W)

        if 'Other' in var:
            __programs7.set(1)

        #if other
        global __programs8
        __programs8 = Entry(self.ChildInfoSectionframe, width = 19)
        __programs8.grid(row = r, column = 1, sticky = E)

        curr.execute("SELECT Future_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        if val is not None:
            __programs8.insert(0, val)
        else:
            __programs8.insert(0, 'Unanswered')

#Referral Needs ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Referral
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateReferral())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT Referral FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))

        var = curr.fetchall()[0][0]

        #Food
        global __Referral0
        __Referral0 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Food", variable = __Referral0).grid(row = r,  column = 1, sticky = SW)

        if 'Healthy HEROs' in var:
            __Referral0.set(1)

        #Transitional Housing/Shelter
        global __Referral1
        __Referral1 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Transitional Housing/Shelter", variable = __Referral1).grid(row = r,  column = 1, sticky = W)

        if 'Transitional Housing/Shelter' in var:
            __Referral1.set(1)

        #Rent/Utilities Assistance
        global __Referral2
        __Referral2 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Rent/Utilities Assistance", variable = __Referral2).grid(row = r,  column = 1, sticky = W)

        if 'Rent/Utilities Assistance' in var:
            __Referral2.set(1)

        #Clothing/Furniture
        global __Referral3
        __Referral3 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Clothing/Furniture", variable = __Referral3).grid(row = r,  column = 1, sticky = W)

        if 'Clothing/Furniture' in var:
            __Referral3.set(1)

        #Financial/Public Assistance
        global __Referral4
        __Referral4 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Financial/Public Assistance", variable = __Referral4).grid(row = r,  column = 1, sticky = W)

        if 'Financial/Public Assistance' in var:
            __Referral4.set(1)

        #Other
        global __Referral5
        __Referral5 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Other", variable = __Referral5).grid(row = r,  column = 1, sticky = W)

        if 'Other' in var:
            __Referral5.set(1)

        #if other
        global __Referral6
        __Referral6 = Entry(self.ChildInfoSectionframe, width = 19)
        __Referral6.grid(row = r, column = 1, sticky = E)

        curr.execute("SELECT Referral_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        if val is not None:
            __Referral6.insert(0, val)
        else:
            __Referral6.insert(0, 'Unanswered')

#Statement of Understanding ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #one
        label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... ")
        curr.execute("SELECT Statement_One FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __statement0
        __statement0 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __statement0, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __statement0, value=2)

        if val is not None:
            if val is 0:
                __statement0.set(2)
            else:
                __statement0.set(1)

        r = r+1
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateStatement())
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #two
        label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... ")
        curr.execute("SELECT Statement_Two FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __statement1
        __statement1 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __statement1, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __statement1, value=2)

        if val is not None:
            if val is 0:
                __statement1.set(2)
            else:
                __statement1.set(1)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #three
        label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... ")
        curr.execute("SELECT Statement_Three FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __statement2
        __statement2 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __statement2, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __statement2, value=2)

        if val is not None:
            if val is 0:
                __statement2.set(2)
            else:
                __statement2.set(1)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #four
        label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... ")
        curr.execute("SELECT Statement_Four FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __statement3
        __statement3 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __statement3, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __statement3, value=2)

        if val is not None:
            if val is 0:
                __statement3.set(2)
            else:
                __statement3.set(1)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #five
        label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... ")
        curr.execute("SELECT Statement_Five FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __statement4
        __statement4 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __statement4, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __statement4, value=2)

        if val is not None:
            if val is 0:
                __statement4.set(2)
            else:
                __statement4.set(1)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #six
        label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... ")
        curr.execute("SELECT Statement_Six FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __statement5
        __statement5 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __statement5, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __statement5, value=2)

        if val is not None:
            if val is 0:
                __statement5.set(2)
            else:
                __statement5.set(1)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #seven
        label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... ")
        curr.execute("SELECT Statement_Seven FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __statement6
        __statement6 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __statement6, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __statement6, value=2)

        if val is not None:
            if val is 0:
                __statement6.set(2)
            else:
                __statement6.set(1)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

 #Signature ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSIGNATURE")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. ")
        curr.execute("SELECT Signature FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        val = curr.fetchall()[0][0]

        global __signature
        __signature = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = __signature, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = __signature, value=2)

        if val is not None:
            if val is 0:
                __signature.set(2)
            else:
                __signature.set(1)

        r = r+1
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateSignature())
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)


#Close Database Connection
        curr.close()
        db.close()

#Button Definitions
    def delete(self):
        if askyesno('Verify', 'Really delete?'):

            #Open Database Connection
            db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
            curr = db.cursor()

            #Execute
            curr.execute("DELETE FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
            db.commit()

            #Close Database Connection
            curr.close()
            db.close()

            #UI feedback
            showwarning('Delete', 'Application Deleted')

            #Go back to 1st level profile page (call back if you can)
            self.master.destroy()

        else:
            #Delete canclled
            showinfo('No', 'Delete has been cancelled')


#Child Info ************************************************************************************************************************
    def updatechildInfo0(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo1(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo2(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_Nickname = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_Nickname = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo3(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo4(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo5(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_County = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_County = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo6(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Childs_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")


        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo7(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo7.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Home_Phone = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Home_Phone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo8(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo8.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Guardian_Phone = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Guardian_Phone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo9(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Guardian_Email = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Guardian_Email = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo10(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo10.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Age = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Childs_Information SET Age = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAge must be only numbers.")

    def updatechildInfo11(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo11.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Birthday = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
            db.commit()
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Childs_Information SET Birthday = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:

            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo12(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo12.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Gender = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo13(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo13.get()
        curr.execute("UPDATE Childs_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo14(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo14.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Aware = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo15(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo15.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Why = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Why = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo16(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo16.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Referral_Source = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Referral_Source = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo17(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo17.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET School_attending = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET School_attending = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo18(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo18.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET School_grade_level = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET School_grade_level = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo19(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo19.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Ethnicity = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo20(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo20.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Ethnicity_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Ethnicity_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo21(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo21.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET ADD_ADHD = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo22(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo22.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Learning_Disability = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo23(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo23.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Developmental_Disability = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo24(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo24.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Mental_Health_Issues = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo25(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo25.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Other_Medical_Condition = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo26(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo26.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Victim_of_Abuse = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo27(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo27.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Criminal_Justice_System = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo28(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo28.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Legal_Custody = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo29(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __childInfo29.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Custody_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Childs_Information SET Custody_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Parent Info ************************************************************************************************************************

    def updateparentInfo0(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo1(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo2(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Relationship_to_Child = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Relationship_to_Child = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo3(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Age = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Parent_Guardian_Information SET Age = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAge code must be only numbers.")

    def updateparentInfo4(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo4.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo5(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo5.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Adoptive_Parent = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo6(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo6.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Marital_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo7(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo7.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Education_Completed = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo8(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo8.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo9(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Company_Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Company_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo10(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo10.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo11(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo11.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo12(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo12.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo13(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo13.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo14(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo14.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET WorkPhone = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET WorkPhone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo15(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __parentInfo15.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Email = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Email = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Absent Parent Info ************************************************************************************************************************

    def updateabsParentInfo0(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __absParentInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo1(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __absParentInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo2(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __absParentInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Telephone = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Telephone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo3(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __absParentInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo4(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __absParentInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo5(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __absParentInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_County = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_County = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo6(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __absParentInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")

    def updateabsParentInfo7(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __absParentInfo7.get()
        if newVal != '':
            curr.execute("UPDATE Absent_Parent_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Household Info ************************************************************************************************************************

    def updatehouseInfo(self, count):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        if count == 1:
            newVal0 = __houseInfo10.get()
            newVal1 = __houseInfo11.get()
            newVal2 = __houseInfo12.get()
            newVal3 = __houseInfo13.get()
            newVal4 = __houseInfo14.get()

        elif count == 2:
            newVal0 = __houseInfo20.get()
            newVal1 = __houseInfo21.get()
            newVal2 = __houseInfo22.get()
            newVal3 = __houseInfo23.get()
            newVal4 = __houseInfo24.get()

        elif count == 3:
            newVal0 = __houseInfo30.get()
            newVal1 = __houseInfo31.get()
            newVal2 = __houseInfo32.get()
            newVal3 = __houseInfo33.get()
            newVal4 = __houseInfo34.get()

        elif count == 4:
            newVal0 = __houseInfo40.get()
            newVal1 = __houseInfo41.get()
            newVal2 = __houseInfo42.get()
            newVal3 = __houseInfo43.get()
            newVal4 = __houseInfo44.get()

        elif count == 5:
            newVal0 = __houseInfo50.get()
            newVal1 = __houseInfo51.get()
            newVal2 = __houseInfo52.get()
            newVal3 = __houseInfo53.get()
            newVal4 = __houseInfo54.get()

        elif count == 6:
            newVal0 = __houseInfo60.get()
            newVal1 = __houseInfo61.get()
            newVal2 = __houseInfo62.get()
            newVal3 = __houseInfo63.get()
            newVal4 = __houseInfo64.get()

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
            curr.execute("SELECT * FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (__id, __date, count,))
            current = curr.fetchall()
            if current is ():
                curr.execute("""INSERT INTO Household_Information VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s);""", 
                    (__id, __date, count, newVal0, newVal1, newVal2, newVal3, newVal4,))
            else:
                curr.execute("""UPDATE Household_Information 
                    SET Name = %s, Relationship = %s, Sex = %s, Age = %s, HIV_Status = %s 
                    WHERE ID = %s AND Date_Submitted = %s AND Count = %s;""", 
                    (newVal0, newVal1, newVal2, newVal3, newVal4, __id, __date, count,))

            db.commit()

            #feedback
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatefamIncome0(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __famIncome0.get()
        if newVal != '':
            curr.execute("UPDATE Fam_Annual_Income SET Fam_Annual_Income = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatefamIncome1(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __famIncome1.get()
        if newVal != '':
            curr.execute("UPDATE Source_Fam_Income SET Source_Fam_Income = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatefamIncome2(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __famIncome2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Source_Fam_Income SET Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Source_Fam_Income SET Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#In Case of Emergency Contact ************************************************************************************************************************
    def updateemergencyInfo0(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateemergencyInfo1(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateemergencyInfo2(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Relationship_to_Child = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Relationship_to_Child = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateemergencyInfo3(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateemergencyInfo4(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateemergencyInfo5(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()


    def updateemergencyInfo6(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateemergencyInfo7(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo7.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Home = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Home = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateemergencyInfo8(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo8.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Cell = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Cell = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateemergencyInfo9(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = __emergencyInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Alt = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Alt = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatePrograms0(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = ''

        if __programs0.get():
            newVal = newVal + 'Super HEROes Program,'

        if __programs1.get():
            newVal = newVal + 'Bright HEROs Program,'

        if __programs2.get():
            newVal = newVal + 'Camp High Five,'

        if __programs3.get():
            newVal = newVal + 'Holiday of HEROs,'

        if __programs4.get():
            newVal = newVal + 'Transition to Adulthood,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET HERO_Programs = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET HERO_Programs = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()


    def updatePrograms1(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = ''

        if __programs5.get():
            newVal = newVal + 'Healthy HEROs,'

        if __programs6.get():
            newVal = newVal + 'Career Development/Job Readiness,'

        if __programs7.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET Future_Programs = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET Future_Programs = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))

        newValOther = __programs8.get()
        if (newValOther == 'Unanswered') or (newValOther == ''):
            curr.execute("UPDATE Child_Application SET Future_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Child_Application SET Future_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newValOther, __id, __date,))
        
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateReferral(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = ''

        if __Referral0.get():
            newVal = newVal + 'Food,'

        if __Referral1.get():
            newVal = newVal + 'Transitional Housing/Shelter,'

        if __Referral2.get():
            newVal = newVal + 'Rent/Utilities Assistance,'

        if __Referral3.get():
            newVal = newVal + 'Clothing/Furniture,'

        if __Referral4.get():
            newVal = newVal + 'Financial/Public Assistance,'

        if __Referral5.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET Referral = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET Referral = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, __id, __date,))

        newValOther = __Referral6.get()
        if (newValOther == 'Unanswered') or (newValOther == ''):
            curr.execute("UPDATE Child_Application SET Referral_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (__id, __date,))
        else:
            curr.execute("UPDATE Child_Application SET Referral_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newValOther, __id, __date,))
        
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateStatement(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        s0 = __statement0.get()
        if s0 == 0:
            s0 = None
        elif s0 == 2:
            s0 = 0

        s1 = __statement1.get()
        if s1 == 0:
            s1 = None
        elif s1 == 2:
            s1 = 0

        s2 = __statement2.get()
        if s2 == 0:
            s2 = None
        elif s2 == 2:
            s2 = 0

        s3 = __statement3.get()
        if s3 == 0:
            s3 = None
        elif s3 == 2:
            s3 = 0

        s4 = __statement4.get()
        if s4 == 0:
            s4 = None
        elif s4 == 2:
            s4 = 0

        s5 = __statement5.get()
        if s5 == 0:
            s5 = None
        elif s5 == 2:
            s5 = 0

        s6 = __statement6.get()
        if s6 == 0:
            s6 = None
        elif s6 == 2:
            s6 = 0

        curr.execute("""UPDATE Statement_Of_Understanding SET Statement_One = %s, Statement_Two = %s, Statement_Three = %s, Statement_Four = %s,
            Statement_Five = %s, Statement_Six = %s, Statement_Seven = %s WHERE ID = %s AND Date_Submitted = %s;""",
            (s0, s1, s2, s3, s4, s5, s6, __id, __date,))
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateSignature(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()


        newVal = __signature.get()
        if newVal == 0:
            newVal = None
        elif newVal == 2:
            newVal = 0

        curr.execute("""UPDATE Child_Application SET Signature = %s WHERE ID = %s AND Date_Submitted = %s;""", (newVal, __id, __date,))
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

    #check string entry is a __date (YYYY-MM-DD)
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





class AddNewApp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        """Pull in a request from the database
        about the programs that are offered
        and then add them to a list and pull them into the programList"""

        master = self

        #get this program list from the DB
        programList = ['Child Application', 'Camper Application']
        global __programs
        __programs = StringVar()
        __programs.set('Programs')
        dropdownProgram = OptionMenu(master, __programs, *programList)
        dropdownProgram.grid(row = 0, column = 3)


        labelDate = Label(master, text = "Date Submitted (YYYY-MM-DD)")
        labelDate.grid(row = 1, column = 3)

        global __entryDate
        __entryDate = Entry(master, bd = 3)
        __entryDate.grid(row = 1, column = 4)

        returningTxt = Label(master, text = "Returning Child?")
        returningTxt.grid(row = 2, column = 3)

        global __v
        __v = StringVar()
        returningInq = Radiobutton(master, text="Yes", variable=__v, value=1)
        returningInq.grid(row = 2,column = 4)

        returningInq = Radiobutton(master, text="No", variable= __v, value=2)
        returningInq.grid(row = 2,column = 5)

        __v.set(0)

        createButton = Button(master, text = "Create", command = lambda: self.create(parent, controller))
        createButton.grid(row = 3, column = 3)

        #TODO pass in username
        username = 'SonikaFinch'
        closeButton = Button(master, text = "Back", command = lambda: controller.show_frame(HomePage, username))
        closeButton.grid(row  = 0, column = 0)


    def create(self, parent, controller):
        #send to create page
        #add an application form to the DB

        db = MySQLdb.connect(
            host = "localhost",
            user="root",
            passwd="Darling",
            db="HERO" )
        curr = db.cursor()


        if __v.get() == '2':             # If they are not a returning child, add them and date submitted into Child()
            curr.execute("INSERT INTO Child() VALUES ();") #is this actually auto incrementing
            db.commit()

            #get variables from user input
            curr.execute("SELECT MAX(ID) FROM Child;")
            ID = curr.fetchall()[0][0]
            Date = __entryDate.get()
            program = __programs.get()

            #Add the ID and Date_Submitted into the program specified by the user
            #Needs a check for valid date format
            if (program == 'Programs'):
                tkMessageBox.showinfo("Add a New Applicaiton","Please select a program")
            else:
                if self.is_date(Date):
                    if program == 'Child Application':
                        curr.execute("INSERT INTO Child_Application(ID, Date_Submitted) VALUES (%s,%s);",(ID,Date))
                        db.commit()

                        controller.show_frame(NewChildApp)
                    elif program == "Camper Application":
                        curr.execute("INSERT INTO Camp_Application(ID,Date_Submitted) VALUES(%s,%s);",(ID,Date))
                        db.commit()

                        controller.show_frame(NewChildApp)
                    else:
                        tkMessageBox.showinfo("Add a New Applicaiton","Please select a program")
                else:
                    tkMessageBox.showinfo("Add a New Applicaiton","Date must be if YYYY-MM-DD format\nAnd must be a real date.")


        elif __v.get() == '1':       #if they are a returning child, send them to newAppReturning.py
            controller.show_frame(NewAppReturning)

        else:         #user failed to select Yes/No for returning Child
            tkMessageBox.showinfo("Add a New Application","Please select Yes or No for 'Returning User?'")

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


class NewAppReturning(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        master = self

        idLabel = Label(master, text = "ID")
        idLabel.grid(row = 2, column = 0)

        global idEntry
        idEntry = Entry(master, bd =3)
        idEntry.grid(row = 2, column = 1)

        divider = Label(master, text = "Or", font= "Verdana 10 underline")
        divider.grid(row = 3, column = 1)

        programLabel = Label(master, text = "Program")
        programLabel.grid(row = 0, column = 3)

        programList = ['Child Application', 'Camper Application']
        global programs
        programs = StringVar()
        programs.set('Programs')
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

        continueButton = Button(master, text = "Continue", command = lambda: self.Continue(parent, controller))
        continueButton.grid(row = 7, column = 3)

        back = Button(master, text = "Back", command = lambda: controller.show_frame(AddNewApp))
        back.grid(row = 0, column = 0)

    def Continue(self, parent, controller):
        db = MySQLdb.connect(
                host = "localhost",
                user="root",
                passwd="Darling",
                db="HERO" )
        curr = db.cursor()
        program = programs.get()
        ID = idEntry.get()
        firstName = nameEntry.get()
        lastName = name2Entry.get()
        bd = bdEntry.get()

        #error handling
        if firstName != '' and lastName != '' and ID == '' and bd != '': # checks if the filled name and bd fields and left ID blank
                if program != 'Programs':
                    #select data if from child
                    if program == 'Child Application':
                            curr.execute("SELECT ID FROM Childs_Information WHERE Name_First = %s AND Name_Last = %s AND Birthday = %s;",(firstName,lastName,bd))
                            data = curr.fetchall()
                            if data == ():
                                tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                            else:
                                data = data[0][0]
                                controller.show_frame(NameBirthEntryPage)
                    #select data if from camper
                    elif program == 'Camper Application':
                            curr.execute("SELECT ID FROM Demographic_Information WHERE First_Name = %s AND Last_Name = %s AND Date_Of_Birth = %s;",(firstName,lastName,bd))
                            data = curr.fetchall()
                            if data == ():
                                tkMessageBox.showinfo("Returning Child","Error: no such child exists.")
                            else:
                                data = data[0][0]
                                controller.show_frame(NameBirthEntryPage)



                else:
                    tkMessageBox.showinfo("Returning Child","Please select a program from the list")

        else: #user entered the child ID
            ###Link me somewhere
            #placeholder, this should send user to childs information page
            controller.show_frame(FirstProfilePage)

#******************************************************************************************************************************************************


class NameBirthEntryPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        master = self
        #5 columns at least 3 rows

        nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = 1, column = 0)

        progHead = Label(master, text = "Program", font= "Verdana 10 underline")
        progHead.grid(row = 1, column = 1)

        yearHead = Label(master, text = "Year", font= "Verdana 10 underline")
        yearHead.grid(row = 1, column = 2)

        self.back = Button(master, text = "Back", command = lambda: controller.show_frame(AddNewApp))
        self.back.grid(row = 0, column = 0)

        ###
        ID = 1 ##get this ID from another page
        ###
        program = "Child Application" #get me too!
        ###

        db = MySQLdb.connect( host = "localhost",
                              user="root",
                              passwd="Darling",
                              db="HERO" )
        curr = db.cursor()

        #selects all instances of specified ID in child and camper applications
        curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted) FROM Childs_Information WHERE ID = %s;",(ID,))
        childNameDate = curr.fetchall()
        curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted) FROM Demographic_Information WHERE ID = %s;",(ID,))
        camperNameDate = curr.fetchall()


        if program == 'none':
                for num in range(len(childNameDate)):
                        name = Label(master, text = childNameDate[num][0]+' '+childNameDate[num][1])
                        name.grid(row = 2 + num, column = 0)

                        prog = Label(master, text = "Child Application")
                        prog.grid(row = 2 + num, column = 1)

                        year = Label(master, text = childNameDate[num][2])
                        year.grid(row = 2 + num, column = 2)

                        profBut = Button(master, text = "Add New App", command = lambda: controller.show_frame(NewChildApp))
                        profBut.grid(row = 2 + num, column = 3)

                for num in range(len(camperNameDate)):
                        name = Label(master, text = camperNameDate[num][0]+' '+camperNameDate[num][1])
                        name.grid(row = 2 + num +len(childNameDate), column = 0)

                        prog = Label(master, text = "Camper Application")
                        prog.grid(row = 2 + num +len(childNameDate), column = 1)

                        year = Label(master, text = camperNameDate[num][2])
                        year.grid(row = 2 + num +len(childNameDate), column = 2)

                        profBut = Button(master, text = "Add New App", command = lambda: controller.show_frame(NewChildApp))
                        profBut.grid(row = 2 + num +len(childNameDate), column = 3)

                total = len(childNameDate)+len(camperNameDate)

        elif program == 'Child Application':
                for num in range(len(childNameDate)):
                        if (childNameDate[num][0] is not None) and (childNameDate[num][1] is not None):
                                name = Label(master, text = childNameDate[num][0]+' '+childNameDate[num][1])
                                name.grid(row = 2 + num, column = 0)
                        elif childNameDate[num][0] is not None:
                                name = Label(master, text = childNameDate[num][0])
                                name.grid(row = 2 + num, column = 0)
                        elif childNameDate[num][1] is not None:
                                name = Label(master, text = childNameDate[num][1])
                                name.grid(row = 2 + num, column = 0)

                        prog = Label(master, text = "Child Application")
                        prog.grid(row = 2 + num, column = 1)

                        year = Label(master, text = childNameDate[num][2])
                        year.grid(row = 2 + num, column = 2)

                        profBut = Button(master, text = "Add New App", command = lambda: controller.show_frame(NewChildApp))
                        profBut.grid(row = 2 + num, column = 3)
                total = len(childNameDate)

        else:
                for num in range(len(camperNameDate)):
                        if (camperNameDate[num][0] is not None) and (camperNameDate[num][1] is not None):
                                name = Label(master, text = camperNameDate[num][0]+' '+camperNameDate[num][1])
                                name.grid(row = 2 + num, column = 0)
                        elif camperNameDate[num][0] is not None:
                                name = Label(master, text = camperNameDate[num][0])
                                name.grid(row = 2 + num, column = 0)
                        elif camperNameDate[num][1] is not None:
                                name = Label(master, text = camperNameDate[num][1])
                                name.grid(row = 2 + num, column = 0)



                        prog = Label(master, text = "Camper Application")
                        prog.grid(row = 2 + num, column = 1)

                        year = Label(master, text = camperNameDate[num][2])
                        year.grid(row = 2 + num, column = 2)

                        profBut = Button(master, text = "Add New App", command = lambda: controller.show_frame(NewChildApp))
                        profBut.grid(row = 2 + num, column = 3)
                total = len(camperNameDate)


        #print total number of matches
        count = Label(master, text = "Total Matches: " + str(total))
        count.grid(row = 0, column = 3)




#******************************************************************************************************************************************************



class NewChildApp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.frame = self

#TODO
    #figure out how to pass in parameters
        global id
        global date

        id = 1
        date = '2016-11-24'

#Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

#Top Buttons
    #back button frame + back button
        self.buttonframe = Frame(self.frame)
        self.buttonframe.pack(side = "top", fill = "x")

        #fix alignment
        backButton = Button(self.buttonframe, text = "Back", command = lambda: controller.show_frame(AddNewApp))
        backButton.pack(side = "left")

#Child info section
        self.ChildInfoSectionframe = Frame(self.frame)
        self.ChildInfoSectionframe.pack(fill = 'y', side = 'left')
        r = 0

        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\nCHILD'S INFORMATION")
        labelChildInfoSection.grid(row = r, column = 0)
        labelChildInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global childInfo0
        childInfo0 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global childInfo1
        childInfo1 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #nickname
        label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. ")
        global childInfo2
        childInfo2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global childInfo3
        childInfo3 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global childInfo4
        childInfo4 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global childInfo5
        childInfo5 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global childInfo6
        childInfo6 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #home phone
        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... ")
        global childInfo7
        childInfo7 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian phone
        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ ")
        global childInfo8
        childInfo8 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian email
        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... ")
        global childInfo9
        childInfo9 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global childInfo10
        childInfo10 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #birthday
        label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ ")
        global childInfo11
        childInfo11 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. ")
        global childInfo12
        childInfo12 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo12, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")
        global childInfo13
        childInfo13 = StringVar()
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo13, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #aware
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... ')
        global childInfo14
        childInfo14 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo14, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo14, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #why
        label = Label(self.ChildInfoSectionframe, text = "If no, please provide a reason why child is not aware .............................. ")
        global childInfo15
        childInfo15 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Referral source
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... ")
        global childInfo16
        childInfo16 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #school attending
        label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. ")
        global childInfo17
        childInfo17 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Grade Level
        label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... ")
        global childInfo18
        childInfo18 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo18.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Ethnicity
        label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... ")
        global childInfo19
        childInfo19 = StringVar()
        choices = ['White/Caucasian','Black/African-American','Hispanic/Latino',
        'Native American','Asian/Pacific Islander/Indian Sub-Continent','Multi-racial','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo19, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Ethnicity Other
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global childInfo20
        childInfo20 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Even been...
        label = Label(self.ChildInfoSectionframe, text = "\nHas your child ever been...")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #ADD_ADHD
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. ')
        global childInfo21
        childInfo21 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo21, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo21, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Learning_Disability
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')
        global childInfo22
        childInfo22 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo22, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo22, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Developmental_Disability
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... ')
        global childInfo23
        childInfo23 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo23, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo23, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Mental_Health_Issues
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. ')
        global childInfo24
        childInfo24 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo24, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo24, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Other_Medical_Condition
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... ')
        global childInfo25
        childInfo25 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo25, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo25, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Victim_of_Abuse
        label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... ')
        global childInfo26
        childInfo26 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo26, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo26, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Criminal_Justice_System
        label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... ')
        global childInfo27
        childInfo27 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo27, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo27, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Custody
        label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... ")
        global childInfo28
        childInfo28 = StringVar()
        choices = ['Mother','Father','Both Parents','Aunt/Uncle','Grandparent','Pending Court Action','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo28, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Custody Other
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global childInfo29
        childInfo29 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo29.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Section
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global parentInfo0
        parentInfo0 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global parentInfo1
        parentInfo1 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global parentInfo2
        parentInfo2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Age
        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global parentInfo3
        parentInfo3 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ ")
        global parentInfo4
        parentInfo4 =  StringVar()
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo4, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Adoptive Parent
        label = Label(self.ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... ")
        global parentInfo5
        parentInfo5 = StringVar()
        choices = ['Yes','No','Not Applicable']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo5, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Marital Status
        label = Label(self.ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... ")
        global parentInfo6
        parentInfo6 = StringVar()
        choices = ['Married','Single','Separated','Divorced','Widowed']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo6, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Highest Level of Education Completed
        label = Label(self.ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. ")
        global parentInfo7
        parentInfo7 = StringVar()
        choices = ['HS','GED','Some College','Associates Degree','Bachelor Degree','Master Degree','Doctorate']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo7, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Status
        label = Label(self.ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... ")
        global parentInfo8
        parentInfo8 = StringVar()
        choices = ['Full-Time','Part-Time','Unemployed','Disability']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo8, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Company
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = "\nIf employed,")
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = "please provide Company Name ............................................................. ")
        global parentInfo9
        parentInfo9 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Address
        label = Label(self.ChildInfoSectionframe, text = "\nAddress ................................................................................................ ")
        global parentInfo10
        parentInfo10 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global parentInfo11
        parentInfo11 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        label = Label(self.ChildInfoSectionframe, text = "\nState .................................................................................................... ")
        global parentInfo12
        parentInfo12 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global parentInfo13
        parentInfo13 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Work Phone
        label = Label(self.ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... ")
        global parentInfo14
        parentInfo14 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #E-mail
        label = Label(self.ChildInfoSectionframe, text = "\nE-mail ................................................................................................... ")
        global parentInfo15
        parentInfo15 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Absent Parent Info
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global absParentInfo0
        absParentInfo0 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global absParentInfo1
        absParentInfo1 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Telephone
        label = Label(self.ChildInfoSectionframe, text = "\nTelephone .............................................................................................. ")
        global absParentInfo2
        absParentInfo2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global absParentInfo3
        absParentInfo3 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global absParentInfo4
        absParentInfo4 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #County
        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global absParentInfo5
        absParentInfo5 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ......................................................................................................... ")
        global absParentInfo6
        absParentInfo6 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ ")
        global absParentInfo7
        absParentInfo7 =  StringVar()
        choices = ['HIV Positive','HIV Negative', 'Unkown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, absParentInfo7, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

#Household Info
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nHOUSEHOLD INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #list all individuals living in the household
        label = Label(self.ChildInfoSectionframe, text = "\nAll Individuals Living in the Household")
        r = r+1
        label.grid(row = r, column = 0)

    #person1
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 1')
        label.grid(row = r, column = 0, sticky = 'w')

        #Name1
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo10
        houseInfo10 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child1
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo11
        houseInfo11 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex1
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo12
        houseInfo12 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo12, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age1
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo13
        houseInfo13 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status1
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo14
        houseInfo14 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo14, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person2
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 2')
        label.grid(row = r, column = 0, sticky = 'w')

        #Name2
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo20
        houseInfo20 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child2
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo21
        houseInfo21 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex2
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo22
        houseInfo22 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo22, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age2
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo23
        houseInfo23 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status2
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo24
        houseInfo24 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo24, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person3
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 3')
        label.grid(row = r, column = 0, sticky = 'w')

        #Name3
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo30
        houseInfo30 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child3
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo31
        houseInfo31 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex3
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo32
        houseInfo32 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo32, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age3
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo33
        houseInfo33 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo33.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status3
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo34
        houseInfo34 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo34, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person4
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 4')
        label.grid(row = r, column = 0, sticky = 'w')

        #Name4
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo40
        houseInfo40 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo40.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child4
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo41
        houseInfo41 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex4
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo42
        houseInfo42 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo42, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age4
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo43
        houseInfo43 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo43.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status4
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo44
        houseInfo44 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo44, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person5
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 5')
        label.grid(row = r, column = 0, sticky = 'w')

        #Name5
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo50
        houseInfo50 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo50.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child5
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo51
        houseInfo51 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex5
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo52
        houseInfo52 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo52, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age5
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo53
        houseInfo53 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo53.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status5
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo54
        houseInfo54 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo54, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person6
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 6')
        label.grid(row = r, column = 0, sticky = 'w')

        #Name6
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo60
        houseInfo60 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo60.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to Child6
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo61
        houseInfo61 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex6
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo62
        houseInfo62 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo62, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age6
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo63
        houseInfo63 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo63.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status6
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo64
        houseInfo64 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo64, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Family Annual Income Info
        label = Label(self.ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... ")
        global famIncome0
        famIncome0 = StringVar()
        choices = ['$0-10,000','$10,001-15,000','$15,001-20,000','$20,000-25,000','$25,001-30,000','$30,001-35,000','$35,001-40,000','$40,001-45,000','$50,000+']
        option = tk.OptionMenu(self.ChildInfoSectionframe, famIncome0, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income
        label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... ")
        global famIncome1
        famIncome1 = StringVar()
        choices = ['Employment','Government Support','Public Assistance', 'Unemployment Benefits','Medicaid','Social Security','Veterans Benefits','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, famIncome1, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income Other
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global famIncome2
        famIncome2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        famIncome2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#In Case of Emergency Contact
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global emergencyInfo0
        emergencyInfo0 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global emergencyInfo1
        emergencyInfo1 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global emergencyInfo2
        emergencyInfo2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global emergencyInfo3
        emergencyInfo3 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global emergencyInfo4
        emergencyInfo4 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        label = Label(self.ChildInfoSectionframe, text = "\nState ..................................................................................................... ")
        global emergencyInfo5
        emergencyInfo5 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global emergencyInfo6
        emergencyInfo6 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Phone Number
        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. ")
        global emergencyInfo7
        emergencyInfo7 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Cell Phone Number
        label = Label(self.ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... ")
        global emergencyInfo8
        emergencyInfo8 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Alternate Phone Number
        label = Label(self.ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... ")
        global emergencyInfo9
        emergencyInfo9 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#H.E.R.O. Programs
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS\n")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Program(s) you wish your child to participate in
        label = Label(self.ChildInfoSectionframe, text = "Program(s) you wish your child to participate in .................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Super HEROes Program
        global programs0
        programs0 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Super HEROes Program", variable = programs0).grid(row = r,  column = 1, sticky = W)

        #Bright HEROs Program
        global programs1
        programs1 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Bright HEROs Program", variable = programs1).grid(row = r,  column = 1, sticky = W)

        #Camp High Five
        global programs2
        programs2 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Camp High Five", variable = programs2).grid(row = r,  column = 1, sticky = W)

        #Holiday of HEROs
        global programs3
        programs3 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Holiday of HEROs", variable = programs3).grid(row = r,  column = 1, sticky = W)

        #Transition to Adulthood
        global programs4
        programs4 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Transition to Adulthood", variable = programs4).grid(row = r,  column = 1, sticky = W)

    #Program(s) you would be interested in your child to participating in
        label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Healthy HEROs (health curriculum)
        global programs5
        programs5 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Healthy HEROs", variable = programs5).grid(row = r,  column = 1, sticky = SW)

        #Career Development/Job Readiness
        global programs6
        programs6 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Career Development/Job Readiness", variable = programs6).grid(row = r,  column = 1, sticky = W)

        #Other
        global programs7
        programs7 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Other", variable = programs7).grid(row = r,  column = 1, sticky = W)

        global programs8
        programs8 = Entry(self.ChildInfoSectionframe, width = 19)
        programs8.grid(row = r, column = 1, sticky = E)

#Referral Needs
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Referral
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Food
        global Referral0
        Referral0 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Food", variable = Referral0).grid(row = r,  column = 1, sticky = SW)

        #Transitional Housing/Shelter
        global Referral1
        Referral1 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Transitional Housing/Shelter", variable = Referral1).grid(row = r,  column = 1, sticky = W)

        #Rent/Utilities Assistance
        global Referral2
        Referral2 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Rent/Utilities Assistance", variable = Referral2).grid(row = r,  column = 1, sticky = W)

        #Clothing/Furniture
        global Referral3
        Referral3 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Clothing/Furniture", variable = Referral3).grid(row = r,  column = 1, sticky = W)

        #Financial/Public Assistance
        global Referral4
        Referral4 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Financial/Public Assistance", variable = Referral4).grid(row = r,  column = 1, sticky = W)

        #Other
        global Referral5
        Referral5 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Other", variable = Referral5).grid(row = r,  column = 1, sticky = W)

        global Referral6
        Referral6 = Entry(self.ChildInfoSectionframe, width = 19)
        Referral6.grid(row = r, column = 1, sticky = E)

#Statement of Understanding
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #one
        label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... ")
        global statement0
        statement0 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement0, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement0, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #two
        label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... ")
        global statement1
        statement1 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement1, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement1, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #three
        label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... ")
        global statement2
        statement2 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement2, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement2, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #four
        label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... ")
        global statement3
        statement3 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement3, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement3, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #five
        label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... ")
        global statement4
        statement4 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement4, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement4, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #six
        label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... ")
        global statement5
        statement5 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement5, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement5, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #seven
        label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... ")
        global statement6
        statement6 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement6, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement6, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#Signature
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSIGNATURE")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. ")
        global signature
        signature = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = signature, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = signature, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)



#Submit Button
        r = r+1
        submitProfileButton = Button(self.ChildInfoSectionframe, text = "Submit Profile", command = lambda:self.submitProfile(parent, controller))
        submitProfileButton.grid(sticky = 'w, e', row = r, columnspan = 2)

#Close Database Connection
        curr.close()
        db.close()

#Button Definitions
    def back(self):
        if askyesno('Verify', '\nAre you sure you want to leave this page?\nYour work will not be saved.'):
            #Go back to 1st level profile page (call back if you can)
            self.master.destroy()


    def submitProfile(self, parent, controller):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

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

        source0 = famIncome1.get()
        if source0 == '':
            source0 = None

        source1 = famIncome2.get()
        if source1 == '':
            source1 = None

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


#Insert into DB
        if goodData:
            try:
                curr.execute("""INSERT INTO Child_Application VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, sig, programsC, ReferralOther, programsB, programsOther, programsA,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""INSERT INTO Childs_Information VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                             (id, date, cI0, cI1, cI2, cI3, cI4, cI5, cI6, cI7, cI8, cI9, cI10, cI11, cI12, cI13, cI14, cI15, cI16,
                                 cI17, cI18, cI19, cI20, cI21, cI22, cI23, cI24, cI25, cI26, cI27, cI28, cI29,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""INSERT INTO Parent_Guardian_Information VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                             (id, date, pI0, pI1, pI2, pI3, pI4, pI5, pI6, pI7, pI8, pI9, pI10, pI11,
                                 pI12, pI13, pI14, pI15,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""INSERT INTO Absent_Parent_Information VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                                 (id, date, abs0, abs1, abs2, abs3, abs4, abs5, abs6, abs7,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            if person1:
                try:
                    count = 1
                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house10, house11, house12, house13, house14,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person2:
                try:
                    count = 2
                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house20, house21, house22, house23, house24,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person3:
                try:
                    count = 3
                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house30, house31, house32, house33, house34,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person4:
                try:
                    count = 4
                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house40, house41, house42, house43, house44,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person5:
                try:
                    count = 5
                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house50, house51, house52, house53, house54,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person6:
                try:
                    count = 6
                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house60, house61, house62, house63, house64,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            try:
                curr.execute("""INSERT INTO Fam_Annual_Income VALUES
                    (%s, %s, %s);""",
                    (id, date, income,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""INSERT INTO Source_Fam_Income VALUES
                    (%s, %s, %s, %s);""",
                    (id, date, source0, source1,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
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

                #TODO pass in username
                username = 'SonikaFinch'
                controller.show_frame(HomePage, username)

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

app = Main()
app.mainloop()
