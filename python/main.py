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
        self.geometry("740x1000")

        self.frames = {}

        for F in (HomePage, AdminUserPage, AddUser, DeleteUserPage, SearchPage, SearchResultsPage, PageTwo):

            frame = F(self.frame, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


#******************************************************************************************************************************************************


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #TODO LINK
        newAppButton = tk.Button(self, text = "Add New Application", command=lambda: controller.show_frame(PageTwo))
        newAppButton.grid(row = 1, column = 1)

        searchButton = tk.Button(self, text = "Search",  command=lambda: self.search(parent, controller))
        searchButton.grid(row = 2, column = 1)

        adminButton = tk.Button(self, text = "Admin Users", command=lambda: self.admin(parent, controller))
        #probably want to change the text on this button....
        adminButton.grid(row = 3, column = 1)

        closeButton = tk.Button(self, text = "Close", command=lambda: controller.destroy())
        closeButton.grid(row = 5, column = 1)

    def search(self, parent, controller):
        #goes to the search Page

        db = MySQLdb.connect(
            host = "localhost", 
            user="root", 
            passwd = "Darling",
            db="HERO")
        curr = db.cursor()

        username = "FSonika"
        pulled = curr.execute("SELECT User_Type FROM User WHERE Username = %s;", (username,))
        credentials = curr.fetchall()[0][0]

        #need to be able to get the user credentials
        if (credentials == 'Administrator' or credentials == 'Manager'):
            #TODO LINK
            controller.show_frame(SearchPage)

        else:
            "Sorry, you do not have the needed credentials for this command."

        curr.close()
        db.close()

    def admin(self, parent, controller):
        #goes to admin the Users

        db = MySQLdb.connect(
            host = "localhost", 
            user="root", 
            passwd = "Darling",
            db="HERO")
        curr = db.cursor()

        username = "FSonika"
        pulled = curr.execute("SELECT User_Type FROM User WHERE Username = %s;", (username,))
        print pulled
        credentials = curr.fetchall()[0][0]
        print credentials

        if (credentials == 'Administrator'):
            #TODO LINK
            controller.show_frame(AdminUserPage)
        else:
            "Sorry, you do not have the needed credentials for this command."

        curr.close()
        db.close()


#******************************************************************************************************************************************************


class AdminUserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        addButton = tk.Button(self, text = "Add", command=lambda: self.add(parent, controller))
        addButton.place(relx=0.5, rely=0.4, anchor=CENTER)
        deleteButton = tk.Button(self, text = "Delete", command = lambda: self.delete(parent, controller))
        deleteButton.place(relx=0.5, rely=0.6, anchor=CENTER)

        #possibly add a back button
        back = tk.Button(self, text = "Back", command = lambda: self.back(parent, controller))
        back.place(relx=0.1, rely=0.1, anchor=CENTER)


    def back(self, parent, controller):
        controller.show_frame(HomePage)

    def add(self, parent, controller):
        controller.show_frame(AddUser)

    def delete(self, parent, controller):
        controller.show_frame(DeleteUserPage)


#******************************************************************************************************************************************************


class AddUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.frame = self
        self.frame.pack()

        global entry1
        global entry2
        global entry3
        global variable

        name = Label(self.frame, text="Name").grid(row=1)
        entry1 = Entry(self.frame)
        entry1.grid(row=1, column=1)

        username = Label(self.frame, text="Username").grid(row=2)
        entry2 = Entry(self.frame)
        entry2.grid(row=2, column=1)

        password = Label(self.frame, text="Password").grid(row=3)
        entry3 = Entry(self.frame)
        entry3.grid(row=3, column=1)

        level = Label(self.frame, text="Type").grid(row=4)
        variable = StringVar(self)
        variable.set("Regular")
        menu = OptionMenu(self.frame, variable, 'Administrator', 'Manager', 'Regular').grid(row=4, column=1)

        add = Button(self.frame, text="Add User", command = lambda: self.addUser(parent, controller)).grid(row=6, column=3)
        back = Button(self.frame, text="Go Back", command = lambda: self.back(parent, controller)).grid(row=6, column=0)


    def addUser(self, parent, controller):

        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()
        
        curr.execute("""INSERT INTO User VALUES (%s, %s, SHA1(%s), %s);""", (entry1.get(), entry2.get(), entry3.get(), variable.get(),))
        db.commit()

        curr.close()
        db.close()

        tkMessageBox.showinfo("Add User", "Update Successful!")


    def back(self, parent, controller):
        controller.show_frame(AdminUserPage)


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

        back = Button(self, text="Back", command = lambda: self.back(parent, controller))
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

        print username
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        curr.execute("DELETE FROM User WHERE Username = %s", (username,))
        db.commit()

        curr.close()
        
        db.close()

        tkMessageBox.showinfo("Add User", "Update Successful!")


    def back(self, parent, controller):
        controller.show_frame(AdminUserPage)

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

        programList = ['None', "Child Application", "Camp High Five Application"]
        global programs
        programs = StringVar(master)
        programs.set('Program') 

        dropdownProgram = OptionMenu(master, programs, *programList)
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
        global years
        years = StringVar(master)
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
        global categories
        categories = StringVar(master)
        categories.set("Category")

        dropdownCategories = OptionMenu(master, categories, *categoriesList)
        dropdownCategories.grid(row = 3, column = 1)

        global catEntry
        catEntry = Entry(master, width=15)
        catEntry.grid(row = 3, column = 2)

        searchCatButton = Button(master, text = "Search", command=lambda: controller.show_frame(SearchResultsPage))
        searchCatButton.grid(row = 3, column = 3)

        back = Button(master, text = "Back", command = lambda: self.back(parent, controller))
        back.grid(row = 0, column = 0)

        txt = Label(master, text = "First Name:")
        txt.grid(row = 5, column = 1)

        global firstName
        firstName = Entry(master, width=15)
        firstName.grid(row = 5, column = 2)
        
        txt = Label(master, text = "Last Name:")
        txt.grid(row = 6, column = 1)

        global lastName
        lastName = Entry(master, width=15)
        lastName.grid(row = 6, column = 2)

        searchNameButton = Button(master, text = "Search", command=lambda: controller.show_frame(SearchResultsPage))
        searchNameButton.grid(row = 5, column = 3)

        curr.close()
        db.close()



    def back(self, parent, controller):
        controller.show_frame(HomePage)


#******************************************************************************************************************************************************



class SearchResultsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        master = self

        count = Label(master, text = "Total: ")
        count.grid(row = 0, column = 4)

        nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = 1, column = 0)

        critHead = Label(master, text = "Criteria", font= "Verdana 10 underline")
        critHead.grid(row = 1, column = 1)

        progHead = Label(master, text = "Program", font= "Verdana 10 underline")
        progHead.grid(row = 1, column = 2)

        yearHead = Label(master, text = "Year", font= "Verdana 10 underline")
        yearHead.grid(row = 1, column = 3)

        back = Button(master, text = "Back", command = lambda: self.back(parent, controller))
        back.grid(row = 0, column = 0)

        #example data
        for num in range(0,5):
            name = Label(master, text = "Test Name")
            name.grid(row = 2 + num, column = 0)

            crit = Label(master, text = "nut allergy")
            crit.grid(row = 2 + num, column = 1)

            prog = Label(master, text = "Summer")
            prog.grid(row = 2 + num, column = 2)

            year = Label(master, text = "2012")
            year.grid(row = 2 + num, column = 3)

            profBut = Button(master, text = "See Profile", command=lambda: controller.show_frame(PageTwo))
            profBut.grid(row = 2 + num, column = 4)



    def back(self, parent, controller):
        controller.show_frame(SearchPage)











#******************************************************************************************************************************************************


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = tk.Label(self, text="Page Two!!!")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        




app = Main()
app.mainloop()