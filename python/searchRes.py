from tkinter import *


class adminUserPage:
	def __init__(self, master):
		self.master = master
		master.title("Search Results Page")
		#5 columns at least 3 rows
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

		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.place(relx=0.08, rely=0.07, anchor=CENTER)

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

			profBut = Button(master, text = "See Profile", command = self.closeWindow)
			profBut.grid(row = 2 + num, column = 4)





		#possibly add a back button
	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = adminUserPage(master)
master.mainloop()