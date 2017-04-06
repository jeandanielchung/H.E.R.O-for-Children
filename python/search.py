from Tkinter import *


class searchPage:
	def __init__(self, master):
		self.master = master
		master.title("Search Page")
		count = Label(master, text = "Total: ")
		count.grid(row = 0, column = 4)

		nameHead = Label(master, text = "Search by Category", font= "Verdana 10 underline")
		nameHead.grid(row = 1, column = 0)

		nameHead2 = Label(master, text = "Search by name", font= "Verdana 10 underline")
		nameHead2.grid(row = 4, column = 0)

		var = StringVar(master)
		var.set("Program") 

		option1 = OptionMenu(master, var, "one", "two", "three", "four")
		option1.grid(row = 2, column = 1)

		var1 = StringVar(master)
		var1.set("Year")

		option2 = OptionMenu(master, var1, "one", "two", "three", "four")
		option2.grid(row = 2, column = 2)

		var2 = StringVar(master)
		var2.set("Category")

		option3 = OptionMenu(master, var2, "one", "two", "three", "four")
		option3.grid(row = 3, column = 1)

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