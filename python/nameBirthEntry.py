from Tkinter import *


class nameBirthEntryPage:
	def __init__(self, master):
		self.master = master
		master.title("Name and Birthday Search Results Page")
		#5 columns at least 3 rows
		count = Label(master, text = "Total Matches: ")
		count.grid(row = 0, column = 3)

		nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
		nameHead.grid(row = 1, column = 0)

		progHead = Label(master, text = "Program", font= "Verdana 10 underline")
		progHead.grid(row = 1, column = 1)

		yearHead = Label(master, text = "Year", font= "Verdana 10 underline")
		yearHead.grid(row = 1, column = 2)

		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.grid(row = 0, column = 0)

        #example data
		for num in range(0,5):
			name = Label(master, text = "Test Name")
			name.grid(row = 2 + num, column = 0)

			prog = Label(master, text = "Summer")
			prog.grid(row = 2 + num, column = 1)

			year = Label(master, text = "2012")
			year.grid(row = 2 + num, column = 2)

			profBut = Button(master, text = "Profile", command = self.closeWindow)
			profBut.grid(row = 2 + num, column = 3)





		#possibly add a back button
	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = nameBirthEntryPage(master)
master.mainloop()
