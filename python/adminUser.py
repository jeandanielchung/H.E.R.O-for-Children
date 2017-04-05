from Tkinter import *


class adminUserPage:
	def __init__(self, master):
		self.master = master
		master.title("Admin User Page")
		self.addButton = Button(master, text = "Add", command = self.closeWindow)
		self.addButton.place(relx=0.5, rely=0.4, anchor=CENTER)
		self.deleteButton = Button(master, text = "Delete", command = self.closeWindow)
		self.deleteButton.place(relx=0.5, rely=0.6, anchor=CENTER)

		#possibly add a back button
		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.place(relx=0.1, rely=0.1, anchor=CENTER)
	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = adminUserPage(master)
master.mainloop()
