from Tkinter import *
import MySQLdb
import tkMessageBox


class searchPage:
	def __init__(self, master):
		self.master = master
		master.title("Search Page")

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

		searchCatButton = Button(master, text = "Search", command = self.searchCat)
		searchCatButton.grid(row = 3, column = 3)

		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.grid(row = 0, column = 0)

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

		searchNameButton = Button(master, text = "Search", command = self.searchName)
		searchNameButton.grid(row = 5, column = 3)

		curr.close()
		db.close()
        

	#search by category with possible parameters: program, year, category
	#spit out name, 
	#if category chosen: criteria selction
	#if program not chosen: program
	#if year not chosen: year
	def searchCat(self):

		camp = ''
		child = ''

		db = MySQLdb.connect(host="localhost", user="root", passwd="Darling", db="HERO")
		curr = db.cursor()

		#check for program selection
		selectedProgram = programs.get()
		programParam = 1
		if (selectedProgram == 'Program') or (selectedProgram == 'None'):
			#no program input
			programParam = 0

		#check for year selection
		selectedYear = years.get()
		yearParam = 1
		if (selectedYear == 'Year') or (selectedYear == 'None'):
			#no year input
			yearParam = 0
		else:
			selectedYear = selectedYear[1:5]

		#check for category selection
		selectedCategory = categories.get()
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


		elif selectedCategory == 'City':
			
			#no year & no program OR no year & child
			#first, last, year, cat in child
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), Address_City FROM Childs_Information 
						WHERE Address_City != 'NULL';""")
					child = curr.fetchall()

			#no year & no program OR no year & camp
			#first, last, year, cat in camp
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, YEAR(Date_Submitted), Address_City FROM Demographic_Information 
						WHERE Address_City != 'NULL';""")
					camp = curr.fetchall()

			#year & no program OR year & child
			#first, last, cat in child
			check = yearParam and ((not programParam) or (selectedProgram == 'Child Application'))
			if (check):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_City FROM Childs_Information 
						WHERE YEAR(Date_Submitted) = %s AND Address_City != 'NULL';""", (selectedYear,))
					child = curr.fetchall()

			#year & no program OR year & camp
			#first, last, cat in camp
			if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_City FROM Demographic_Information 
						WHERE YEAR(Date_Submitted) = %s AND Address_City != 'NULL';""", (selectedYear,))
					camp = curr.fetchall()


		elif selectedCategory == 'County':

			#no year & no program OR no year & child
			#first, last, year, cat in child
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), Address_County FROM Childs_Information 
						WHERE Address_County != 'NULL';""")
					child = curr.fetchall()

			#no year & no program OR no year & camp
			#first, last, year, cat in camp
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, YEAR(Date_Submitted), Address_County FROM Demographic_Information 
						WHERE Address_County != 'NULL';""")
					camp = curr.fetchall()

			#year & no program OR year & child
			#first, last, cat in child
			if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Address_County FROM Childs_Information 
						WHERE YEAR(Date_Submitted) = %s AND Address_County != 'NULL';""", (selectedYear,))
					child = curr.fetchall()

			#year & no program OR year & camp
			#first, last, cat in camp
			if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Address_County FROM Demographic_Information 
						WHERE YEAR(Date_Submitted) = %s AND Address_County != 'NULL';""", (selectedYear,))
					camp = curr.fetchall()


		elif selectedCategory == 'Referral Source':

			#no year & no program OR no year & child
			#first, last, year, cat in child
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), Referral_Source FROM Childs_Information 
						WHERE Referral_Source != 'NULL';""")
					child = curr.fetchall()


			#year & no program OR year & child
			#first, last, cat in child
			if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Referral_Source FROM Childs_Information 
						WHERE YEAR(Date_Submitted) = %s AND Referral_Source != 'NULL';""", (selectedYear,))
					child = curr.fetchall()

			if (selectedProgram == 'Camp High Five Application'):
				tkMessageBox.showinfo("Search", "This application does not contain the category")



		elif selectedCategory == "Child's Age":

			#no year & no program OR no year & child
			#first, last, year, cat in child
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), Age FROM Childs_Information 
						WHERE Age != 'NULL';""")
					child = curr.fetchall()

			#no year & no program OR no year & camp
			#first, last, year, cat in camp
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, YEAR(Date_Submitted), Age FROM Demographic_Information 
						WHERE Age != 'NULL';""")
					camp = curr.fetchall()

			#year & no program OR year & child
			#first, last, cat in child
			if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Age FROM Childs_Information 
						WHERE YEAR(Date_Submitted) = %s AND Age != 'NULL';""", (selectedYear,))
					child = curr.fetchall()

			#year & no program OR year & camp
			#first, last, cat in camp
			if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Age FROM Demographic_Information 
						WHERE YEAR(Date_Submitted) = %s AND Age != 'NULL';""", (selectedYear,))
					camp = curr.fetchall()


		elif selectedCategory == "Child's Gender":

			#no year & no program OR no year & child
			#first, last, year, cat in child
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), Gender FROM Childs_Information 
						WHERE Gender != 'NULL';""")
					child = curr.fetchall()

			#no year & no program OR no year & camp
			#first, last, year, cat in camp
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, YEAR(Date_Submitted), Gender FROM Demographic_Information 
						WHERE Gender != 'NULL';""")
					camp = curr.fetchall()

			#year & no program OR year & child
			#first, last, cat in child
			if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Gender FROM Childs_Information 
						WHERE YEAR(Date_Submitted) = %s AND Gender != 'NULL';""", (selectedYear,))
					child = curr.fetchall()

			#year & no program OR year & camp
			#first, last, cat in camp
			if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, First_Name, Last_Name, Gender FROM Demographic_Information 
						WHERE YEAR(Date_Submitted) = %s AND Gender != 'NULL';""", (selectedYear,))
					camp = curr.fetchall()


		elif selectedCategory == "Child's Race/Ethnicity":

			#no year & no program OR no year & child
			#first, last, year, cat in child
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), Ethnicity, Ethnicity_Other FROM Childs_Information 
						WHERE Ethnicity != 'NULL' OR Ethnicity_Other != 'NULL';""")
					child = curr.fetchall()

			#year & no program OR year & child
			#first, last, cat in child
			if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, Ethnicity, Ethnicity_Other FROM Childs_Information 
						WHERE YEAR(Date_Submitted) = %s AND (Ethnicity != 'NULL' OR Ethnicity_Other != 'NULL');""", (selectedYear,))
					child = curr.fetchall()

			if (selectedProgram == 'Camp High Five Application'):
				tkMessageBox.showinfo("Search", "This application does not contain the category")


		elif selectedCategory == "Child's HIV Status (infected or affected)":

			#no year & no program OR no year & child
			#first, last, year, cat in child
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), HIV_Status FROM Childs_Information 
						WHERE HIV_Status != 'NULL';""")
					child = curr.fetchall()

			#year & no program OR year & child
			#first, last, cat in child
			if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, HIV_Status FROM Childs_Information 
						WHERE YEAR(Date_Submitted) = %s AND HIV_Status != 'NULL';""", (selectedYear,))
					child = curr.fetchall()

			if (selectedProgram == 'Camp High Five Application'):
				tkMessageBox.showinfo("Search", "This application does not contain the category")


		elif selectedCategory == "Child's Other Issues":

			#no year & no program OR no year & child
			#first, last, year, cat in child
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, YEAR(Date_Submitted), 
						ADD_ADHD, Learning_Disability, Developmental_Disability, Mental_Health_Issues, 
						Other_Medical_Condition, Victim_of_Abuse, Criminal_Justice_System
						FROM Childs_Information 
						WHERE ADD_ADHD != 'NULL' OR Learning_Disability != 'NULL' OR Developmental_Disability != 'NULL' OR
						Mental_Health_Issues != 'NULL' OR Other_Medical_Condition != 'NULL' OR Victim_of_Abuse != 'NULL' OR 
						Criminal_Justice_System != 'NULL';""")
					child = curr.fetchall()


			#year & no program OR year & child
			#first, last, cat in child
			if (yearParam and ((not programParam) or (selectedProgram == 'Child Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Name_First, Name_Last, 
						ADD_ADHD, Learning_Disability, Developmental_Disability, Mental_Health_Issues, 
						Other_Medical_Condition, Victim_of_Abuse, Criminal_Justice_System 
						FROM Childs_Information WHERE YEAR(Date_Submitted) = %s 
						AND (ADD_ADHD != 'NULL' OR Learning_Disability != 'NULL' OR Developmental_Disability != 'NULL' OR
						Mental_Health_Issues != 'NULL' OR Other_Medical_Condition != 'NULL' OR Victim_of_Abuse != 'NULL' OR 
						Criminal_Justice_System != 'NULL');""", (selectedYear,))
					child = curr.fetchall()

			if (selectedProgram == 'Camp High Five Application'):
				tkMessageBox.showinfo("Search", "This application does not contain the category")


		#elif selectedCategory == "Child's HERO Program Participation":
		#	print 'nope'

#TODO figure out name situation
		elif selectedCategory == "Child's Allergies":

			#no year & no program OR no year & camp
			#first, last, year, cat in camp
			if ((not yearParam) and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, YEAR(Date_Submitted), Med_Allergy, Food_Allergy, Env_Allergy FROM Allergies 
						WHERE Med_Allergy != 'NULL' OR Food_Allergy != 'NULL' OR Env_Allergy != 'NULL';""")
					camp = curr.fetchall()

			#year & no program OR year & camp
			#first, last, cat in camp
			if (yearParam and ((not programParam) or (selectedProgram == 'Camp High Five Application'))):
					curr.execute("""SELECT ID, Date_Submitted, Med_Allergy, Food_Allergy, Env_Allergy FROM Allergies 
						WHERE YEAR(Date_Submitted) = %s 
						AND (Med_Allergy != 'NULL' OR Food_Allergy != 'NULL' OR Env_Allergy != 'NULL');""", (selectedYear,))
					camp = curr.fetchall()

			if (selectedProgram == 'Child Application'):
				tkMessageBox.showinfo("Search", "This application does not contain the category")


		'''elif selectedCategory == "Child's Years with HERO":
			print 'nope'

		elif selectedCategory == "Household Composition":
			print 'nope'

		elif selectedCategory == "Parent(s) HIV Status (infected or affected)":
			print 'nope'

		elif selectedCategory == "Household Income Range":
			print 'nope'

		elif selectedCategory == "Household Income Source":
			print 'nope'

		elif selectedCategory == "Parent(s) Highest Level of Education":
			print 'nope'

		elif selectedCategory == "Parent(s) Employment Status":
			print 'nope' '''

		print child
		print camp

		curr.close()
		db.close()

	#search by name with possible parameters: program, year, first name, last name
	def searchName(self):
		self.master.destroy()

	#possibly add a back button
	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = searchPage(master)
master.mainloop()
