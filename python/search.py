from Tkinter import *


class searchPage:
	def __init__(self, master):
		self.master = master
		master.title("Search Page")
		count = Label(master, text = "Total: ")
		count.grid(row = 0, column = 4)

		nameHead = Label(master, text = "Search by Category", font= "Verdana 10 underline")
		nameHead.grid(row = 1, column = 0)

		nameHead2 = Label(master, text = "Search by Name", font= "Verdana 10 underline")
		nameHead2.grid(row = 4, column = 0)


		programList = ['None', "Child Application", "Camp High Five Application"]
		programs = StringVar(master)
		programs.set('Program') 

		dropdownProgram = OptionMenu(master, programs, *programList)
		dropdownProgram.grid(row = 2, column = 1)


		#grab all dat submitted, remove duplicates, set to yearList

		childDatesSubmitted = curr.execute("SELECT DISTINCT Year(Date_Submitted) FROM Child Application")
		campDatesSubmitted = curr.execute("SELECT DISTINCT Year(Date_Submitted) FROM Camp_Application")
		yearList = []

		for item in childDatesSubmitted:
			if item not in yearList:
				yearList.append(item)

		for item in campDatesSubmitted:
			if item not in yearList:
				yearList.append(item)

		years = StringVar(master)
		years.set("Year")

		dropdownYear = OptionMenu(master, years, "None", *yearList)
		dropdownYear.grid(row = 2, column = 2)


		categoriesList = ['None', 'City', "County", 'Referral Source', "Child's Age",
					"Child's Gender", "Child's Race/Ethnicity",
					"Child's HIV Status (infected or affected)", "Child's Learning Disabilities",
					"Child's HERO Program Participation", "Child's Allergies", "Child's Years with HERO",
					"Household Composition", "Parent(s) HIV Status (infected or affected)",
					"Household Income Range", "Household Income Source", "Parent(s) Highest Level of Education",
					"Parent(s) Employment Status"]
		categories = StringVar(master)
		categories.set("Category")

		dropdownCategories = OptionMenu(master, categories, *categoriesList)
		dropdownCategories.grid(row = 3, column = 1)

		cat = Entry(master, width=15)
		cat.grid(row = 3, column = 2)

		searchButton = Button(master, text = "Search", command = self.closeWindow)
		searchButton.grid(row = 3, column = 3)

		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.grid(row = 0, column = 0)

		txt = Label(master, text = "Name:")
		txt.grid(row = 5, column = 1)

		nam = Entry(master, width=15)
		nam.grid(row = 5, column = 2)

		searchButton2 = Button(master, text = "Search", command = self.closeWindow)
		searchButton2.grid(row = 5, column = 3)








		#possibly add a back button
	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = searchPage(master)
master.mainloop()