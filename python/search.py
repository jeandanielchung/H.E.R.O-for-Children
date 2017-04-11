from Tkinter import *
import MySQLdb


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

		categoriesList = ['None', 'City', "County", 'Referral Source', "Child's Age",
					"Child's Gender", "Child's Race/Ethnicity",
					"Child's HIV Status (infected or affected)", "Child's Learning Disabilities",
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

		#check for category selection
		selectedCategory = categories.get()
		catParam = 1

		#no category input
		if (selectedCategory == 'Category') or (selectedCategory == 'None'):
			
			#no program input
			if not programParam:

				#no year input
				if not yearParam:

					#child
					curr.execute("SELECT Name_First, Name_Last, YEAR(Date_Submitted) FROM Childs_Information;")
					child = curr.fetchall()

					print child

					#camp
					curr.execute("SELECT First_Name, Last_Name, YEAR(Date_Submitted) FROM Demographic_Information;")
					camp = curr.fetchall()

					print camp




			#program input
			else:	
				#search child app
				if (selectedProgram == 'Child Application'):
					print 'nope'

					#year was chosen
					if yearParam:
						print 'nope'



				#search camp app
				else:
					print 'nope'

		elif selectedCategory == 'City':
			i = i + 1
			print i

		elif selectedCategory == 'County':
			i = i + 1
			print i

		elif selectedCategory == 'Referral Source':
			i = i + 1
			print i

		elif selectedCategory == 'Child''s Age':
			i = i + 1
			print i

		elif selectedCategory == 'Child''s Gender':
			i = i + 1
			print i

		elif selectedCategory == 'Child''s Race/Ethnicity':
			i = i + 1
			print i

		elif selectedCategory == 'Child''s HIV Status (infected or affected)':
			i = i + 1
			print i

		elif selectedCategory == 'Child''s Learning Disabilities':
			i = i + 1
			print i

		elif selectedCategory == 'Child''s HERO Program Participation':
			i = i + 1
			print i

		elif selectedCategory == 'Child''s Allergies':
			i = i + 1
			print i

		elif selectedCategory == 'Child''s Years with HERO':
			i = i + 1
			print i

		elif selectedCategory == 'Household Composition':
			i = i + 1
			print i

		elif selectedCategory == 'Parent(s) HIV Status (infected or affected)':
			i = i + 1
			print i

		elif selectedCategory == 'Household Income Range':
			i = i + 1
			print i

		elif selectedCategory == 'Household Income Source':
			i = i + 1
			print i

		elif selectedCategory == 'Parent(s) Highest Level of Education':
			i = i + 1
			print i

		elif selectedCategory == 'Parent(s) Employment Status':
			i = i + 1
			print i


	#search by name with possible parameters: program, year, first name, last name
	def searchName(self):
		self.master.destroy()

	#possibly add a back button
	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = searchPage(master)
master.mainloop()
