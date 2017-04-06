from Tkinter import *


class DeleteUserPage:
	def __init__(self, master):
		self.master = master
		master.title("Delete User Page")

		nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
		nameHead.grid(row = 1, column = 0)

		critHead = Label(master, text = "Username", font= "Verdana 10 underline")
		critHead.grid(row = 1, column = 1)

		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.grid(row = 0, column = 0)

        #example data
		for num in range(0,5):
			name = Label(master, text = "Test Name " + str(1+num))
			name.grid(row = 2 + num, column = 0)

			user = Label(master, text = "poonsl@ya2"+str(num))
			user.grid(row = 2 + num, column = 1)

			delBut = Button(master, text = "Delete", command = self.closeWindow)
			delBut.grid(row = 2 + num, column = 2)

	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = DeleteUserPage(master)
master.mainloop()