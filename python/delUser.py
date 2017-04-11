from Tkinter import *
import MySQLdb


class DeleteUserPage:
	def __init__(self, master):
		self.master = master
		master.title("Delete User Page")

		db = MySQLdb.connect(host = "localhost", user = "root", db = "HERO")
		curr = db.cursor()

		nameHead = Label(master, text = "Username", font= "Verdana 10 underline")
		nameHead.grid(row = 1, column = 0)

		critHead = Label(master, text = "User Type", font= "Verdana 10 underline")
		critHead.grid(row = 1, column = 1)

		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.grid(row = 0, column = 0)

		curr.execute("SELECT * FROM User")
		results = curr.fetchall()

		count = 0
		for username,_,usertype in results:
			usernameLabel = Label(master, text = username, font= "Verdana 10")
			usernameLabel.grid(row = 2 + count, column = 0)

			usertypeLabel = Label(master, text = usertype, font= "Verdana 10")
			usertypeLabel.grid(row = 2 + count, column = 1)

			deleteButton = Button(master, text = "Delete", command = self.closeWindow)
			deleteButton.grid(row = 2 + count, column = 2)
			count += 1


	# def deleteUser(self, curr, username):
	# 	curr.execute()

	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = DeleteUserPage(master)
master.mainloop()