from Tkinter import *
import MySQLdb
import tkMessageBox

class Main():

    
    def __init__(self,root):
        self.root = root
        self.searchPage()

    def searchPage(self):

        #TODO: DELETE THIS WHEN IN MAIN
        self.root.withdraw() 

        self.SearchPageRoot = Toplevel()
        root = self.SearchPageRoot

        #UP TO HERE
        
        master = Frame(root)
        root.title("Search Page")

        db = MySQLdb.connect(host="localhost", user="root", passwd="Darling", db="HERO")
        curr = db.cursor()

        curr.execute("SELECT COUNT(ID) FROM Child;")
        total = curr.fetchall()[0][0]

        count = Label(root, text = "Total: " + str(total))
        count.grid(row = 0, column = 4)

        catLabel = Label(root, text = "Search by Category", font= "Verdana 10 underline")
        catLabel.grid(row = 2, column = 0)

        nameLabel = Label(root, text = "Search by Name", font= "Verdana 10 underline")
        nameLabel.grid(row = 4, column = 0)

        programList = ['None', "Child Application", "Camp High Five Application"]
        programs = StringVar(root)
        programs.set('Program') 

        dropdownProgram = OptionMenu(root, programs, *programList)
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
        dropdownYear = OptionMenu(root, years, "None", *yearList)
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

        dropdownCategories = OptionMenu(root, categories, *categoriesList)
        dropdownCategories.grid(row = 3, column = 1)
        catEntry = Entry(root, width=15)
        catEntry.grid(row = 3, column = 2)

        txt = Label(root, text = "First Name:")
        txt.grid(row = 5, column = 1)

        firstName = Entry(root, width=15)
        firstName.grid(row = 5, column = 2)
        
        txt = Label(root, text = "Last Name:")
        txt.grid(row = 6, column = 1)

        lastName = Entry(root, width=15)
        lastName.grid(row = 6, column = 2)

        searchCatButton = Button(root, text = "Search", command = lambda: self.searchCat(programs.get(), years.get(), categories.get(), catEntry.get()))
        searchCatButton.grid(row = 3, column = 3)

        self.back = Button(root, text = "Back", command = self.closeWindow)
        self.back.grid(row = 0, column = 0)

        searchNameButton = Button(root, text = "Search", command = lambda: self.searchName(programs.get(), years.get(), firstName.get(), lastName.get()))
        searchNameButton.grid(row = 5, column = 3)

        curr.close()
        db.close()
        

    #search by category with possible parameters: program, year, category
    #spit out name, 
    #if category chosen: criteria selction
    #if program not chosen: program
    #if year not chosen: year
    def searchCat(self, selectedProgram, selectedYear, selectedCategory, catEntry):

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
        
        #TODO: DELETE THIS WHEN IN MAIN
        self.SearchPageRoot.withdraw()

        self.SearchResRoot = Toplevel()
        root = self.SearchResRoot

        #UP TO HERE
        
        root.title("Search Results Page")

        #need to implement dynamic tracking of count
        countText = len(child) + len(camp)
        count = Label(root, text = "Total: " + str(countText))
        count.grid(row = 0, column = 4)

        r = 2
        idHead = Label(root, text = "ID", font= "Verdana 10 underline")
        idHead.grid(row = r, column = 0)

        dateHead = Label(root, text = "Date Submitted", font= "Verdana 10 underline")
        dateHead.grid(row = r, column = 1)

        nameHead = Label(root, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = r, column = 2)

        critHead = Label(root, text = "Criteria", font= "Verdana 10 underline")
        critHead.grid(row = r, column = 3)

        r = r+1
        childHead = Label(root, text = "Child App", font= "Verdana 10 underline")
        childHead.grid(row = r, column = 0)

        r = r+1
        if (child):
            for num in child:

                ID = Label(root, text = num[0])
                ID.grid(row = r, column = 0)

                Date_Submitted = Label(root, text = num[1])
                Date_Submitted.grid(row = r, column = 1)

                nameText = ''
                if (num[2] is not None):
                    nameText += num[2]
                if (num[3] is not None):
                    if (nameText != ''):
                        nameText += ' '
                    nameText += num[3]
                Name = Label(root, text = nameText
                    )
                Name.grid(row = r, column = 2)

                criteriaText = ''
                if (len(num) > 4):
                    for i in range(len(num) - 4):
                        if num[4+i] is not None:
                            criteriaText += str(num[4+i])
                            criteriaText += ', '

                    criteriaText = criteriaText[:-2]
                
                criteria = Label(root, text = criteriaText)
                criteria.grid(row = r, column = 3)

                profBut = Button(root, text = "See Profile", command = self.closeWindow)
                profBut.grid(row = r, column = 4)
                r = r+1

        else:
                childNope = Label(root, text = "None")
                childNope.grid(row = r, column = 0)

        r = r+1
        campHead = Label(root, text = "Camper App", font= "Verdana 10 underline")
        campHead.grid(row = r, column = 0)
        
        r = r+1
        if(camp):
            for num in camp:
                ID = Label(root, text = num[0])
                ID.grid(row = r, column = 0)

                Date_Submitted = Label(root, text = num[1])
                Date_Submitted.grid(row = r, column = 1)

                nameText = ''
                if (num[2] is not None):
                    nameText += num[2]
                if (num[3] is not None):
                    if (nameText != ''):
                        nameText += ' '
                    nameText += num[3]
                Name = Label(root, text = nameText
                    )
                Name.grid(row = r, column = 2)

                criteriaText = ''
                if (len(num) > 4):
                    for i in range(len(num) - 4):
                        if num[4+i] is not None:
                            criteriaText += str(num[4+i])
                            criteriaText += ', '
                            
                    criteriaText = criteriaText[:-2]
                
                criteria = Label(root, text = criteriaText)
                criteria.grid(row = r, column = 3)

                profBut = Button(root, text = "See Profile", command = self.closeWindow)
                profBut.grid(row = r, column = 4)
                r = r+1

        else:
                campNope = Label(root, text = "None")
                campNope.grid(row = r, column = 0)


        self.back = Button(root, text = "Close", command = self.closeWindow)
        self.back.grid(row = 0, column = 0)

    #search by name with possible parameters: program, year, first name, last name
    def searchName(self, selectedProgram, selectedYear, firstName, lastName):

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

        
        #TODO: DELETE THIS WHEN IN MAIN
        self.SearchPageRoot.withdraw()

        self.SearchResRoot = Toplevel()
        root = self.SearchResRoot

        #UP TO HERE
        
        root.title("Search Results Page")

        #need to implement dynamic tracking of count
        countText = len(child) + len(camp)
        count = Label(root, text = "Total: " + str(countText))
        count.grid(row = 0, column = 4)

        r = 2
        idHead = Label(root, text = "ID", font= "Verdana 10 underline")
        idHead.grid(row = r, column = 0)

        dateHead = Label(root, text = "Date Submitted", font= "Verdana 10 underline")
        dateHead.grid(row = r, column = 1)

        nameHead = Label(root, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = r, column = 2)

        r = r+1
        childHead = Label(root, text = "Child App", font= "Verdana 10 underline")
        childHead.grid(row = r, column = 0)

        r = r+1
        if (child):
            for num in child:

                ID = Label(root, text = num[0])
                ID.grid(row = r, column = 0)

                Date_Submitted = Label(root, text = num[1])
                Date_Submitted.grid(row = r, column = 1)

                nameText = ''
                if (num[2] is not None):
                    nameText += num[2]
                if (num[3] is not None):
                    if (nameText != ''):
                        nameText += ' '
                    nameText += num[3]
                Name = Label(root, text = nameText
                    )
                Name.grid(row = r, column = 2)

                profBut = Button(root, text = "See Profile", command = self.closeWindow)
                profBut.grid(row = r, column = 4)
                r = r+1
        
        else:
                childNope = Label(root, text = "None")
                childNope.grid(row = r, column = 0)

        r = r+1
        campHead = Label(root, text = "Camper App", font= "Verdana 10 underline")
        campHead.grid(row = r, column = 0)
        
        r = r+1
        if(camp):
            for num in camp:
                ID = Label(root, text = num[0])
                ID.grid(row = r, column = 0)

                Date_Submitted = Label(root, text = num[1])
                Date_Submitted.grid(row = r, column = 1)

                nameText = ''
                if (num[2] is not None):
                    nameText += num[2]
                if (num[3] is not None):
                    if (nameText != ''):
                        nameText += ' '
                    nameText += num[3]
                Name = Label(root, text = nameText
                    )
                Name.grid(row = r, column = 2)

                profBut = Button(root, text = "See Profile", command = self.closeWindow)
                profBut.grid(row = r, column = 4)
                r = r+1

        else:
                campNope = Label(root, text = "None")
                campNope.grid(row = r, column = 0)

    #possibly add a back button
    def closeWindow(self):
        self.root.destroy()




root = Tk()
Main(root)
root.mainloop()
