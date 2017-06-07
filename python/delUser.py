from Tkinter import *
import MySQLdb
from tkMessageBox import *
import tkMessageBox

class DeleteUserPage:
    def __init__(self, master):
        self.master = master
        master.title("Delete User Page")

        nameHead = Label(master, text = "Nameame", font= "Verdana 10 underline")
        nameHead.grid(row = 1, column = 0)

        usernameHead = Label(master, text = "Username", font= "Verdana 10 underline")
        usernameHead.grid(row = 1, column = 1)

        critHead = Label(master, text = "User Type", font= "Verdana 10 underline")
        critHead.grid(row = 1, column = 2)

        #back button
        self.back = Button(master, text = "Back", command = self.closeWindow)
        self.back.grid(row = 0, column = 0)

        #database fetch
        db = MySQLdb.connect(host = "localhost", user="root", passwd = "Darling", db="HERO")
        curr = db.cursor()
        curr.execute("SELECT * FROM User")
        results = curr.fetchall()
        curr.close()
        db.close()

        count = 0
        deleteButtonArr = [0 for x in range(len(results))]
        for name,username,_,usertype in results:
            nameLabel = Label(master, text = name, font= "Verdana 10")
            nameLabel.grid(row = 2 + count, column = 0)

            usernameLabel = Label(master, text = username, font= "Verdana 10")
            usernameLabel.grid(row = 2 + count, column = 1)

            usertypeLabel = Label(master, text = usertype, font= "Verdana 10")
            usertypeLabel.grid(row = 2 + count, column = 2)

            deleteButtonArr[count] = Button(master, text = "Delete", command = lambda username1 = username: self.deleteUser(username1))
            deleteButtonArr[count].grid(row = 2 + count, column = 3)
            count += 1


    def deleteUser(self, username):        
        db = MySQLdb.connect(host = "localhost", user="root", passwd = "Darling", db="HERO")
        curr = db.cursor()

        curr.execute("DELETE FROM User WHERE Username = %s", (username,)) # will delete the last user in the table
        db.commit()

        curr.close()
        db.close()

        tkMessageBox.showinfo("Delete user","User "+username+" has been deleted.")

        # link page back to itself here

    def closeWindow(self):
        self.master.destroy()

master = Tk()
my_gui = DeleteUserPage(master)
master.mainloop()
