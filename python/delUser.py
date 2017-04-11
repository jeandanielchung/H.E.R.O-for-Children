from Tkinter import *
import MySQLdb


class DeleteUserPage:
	def __init__(self, master):
		self.master = master
		master.title("Delete User Page")

                db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
		curr = db.cursor()

		nameHead = Label(master, text = "Nameame", font= "Verdana 10 underline")
		nameHead.grid(row = 1, column = 0)

		usernameHead = Label(master, text = "Username", font= "Verdana 10 underline")
		usernameHead.grid(row = 1, column = 1)

		critHead = Label(master, text = "User Type", font= "Verdana 10 underline")
		critHead.grid(row = 1, column = 2)

		self.back = Button(master, text = "Back", command = self.closeWindow)
		self.back.grid(row = 0, column = 0)

		curr.execute("SELECT * FROM User")
		results = curr.fetchall()


		# for i in range(len(results)):
		# 	nameLabel = Label(master, text = results[i][0], font= "Verdana 10")
		# 	nameLabel.grid(row = 2 + i, column = 0)

		# 	usernameLabel = Label(master, text = results[i][1], font= "Verdana 10")
		# 	usernameLabel.grid(row = 2 + i, column = 1)

		# 	usertypeLabel = Label(master, text = results[i][3], font= "Verdana 10")
		# 	usertypeLabel.grid(row = 2 + i, column = 2)

		# 	deleteButton = Button(master, text = "Delete", command = lambda: self.deleteUser(results[i][1]))
		# 	deleteButton.grid(row = 2 + i, column = 3)

		# curr.close()
		# db.close()

		count = 0
		for name,username,_,usertype in results:
			nameLabel = Label(master, text = name, font= "Verdana 10")
			nameLabel.grid(row = 2 + count, column = 0)

			usernameLabel = Label(master, text = username, font= "Verdana 10")
			usernameLabel.grid(row = 2 + count, column = 1)

			usertypeLabel = Label(master, text = usertype, font= "Verdana 10")
			usertypeLabel.grid(row = 2 + count, column = 2)

			deleteButton = Button(master, text = "Delete", command = lambda: self.closeWindow()) # TODO: Fix deleteUser
			deleteButton.grid(row = 2 + count, column = 3)
			count += 1

		curr.close()
		db.close()


	def deleteUser(self, username):

		print username
		# db = MySQLdb.connect(host = "localhost", user = "root", db = "HERO")
		# curr = db.cursor()

		# curr.execute("DELETE FROM User WHERE Username = %s", (username,))
		# db.commit()

		# curr.close()
		# db.close()

	def closeWindow(self):
		self.master.destroy()

master = Tk()
my_gui = DeleteUserPage(master)
master.mainloop()
