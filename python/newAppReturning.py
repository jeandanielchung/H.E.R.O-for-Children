from Tkinter import *


class NewAppReturningPage:
	def __init__(self, master):
		self.master = master
		master.title("Returning Child")
		#5 columns at least 3 rows
		idLabel = Label(master, text = "ID")
		idLabel.grid(row = 1, column = 0)

		idEntry = Entry(master, bd =3)
		idEntry.grid(row = 1, column = 1)

		divider = Label(master, text = "Or", font= "Verdana 10 underline")
		divider.grid(row = 2, column = 1)

		nameLabel = Label(master, text = "Name")
		nameLabel.grid(row = 3, column = 0)

		nameEntry = Entry(master,bd = 3)
		nameEntry.grid(row = 3, column = 1)

		bdLabel = Label(master, text = "Birthday (YYYY-MM-DD)")
		bdLabel.grid(row = 3, column = 2)

		bdEntry = Entry(master, bd = 3)
		bdEntry.grid(row = 3, column = 3)

		continueButton = Button(master, text = "Continue", command = self.closeWindow)
		continueButton.grid(row = 4, column = 3)

		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.grid(row = 0, column = 0)

	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = NewAppReturningPage(master)
master.mainloop()