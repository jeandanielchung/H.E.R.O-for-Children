from Tkinter import *
import MySQLdb

class ProfilePage:
    def __init__(self, master):
        # Connect to database
        db = MySQLdb.connect(host="localhost", user="root", passwd="Darling", db="HERO")
        curr = db.cursor()

        # id and date
        id = 1
        name_first = 'John'
        name_last = 'Osman'

        self.frame = Frame(master)
        self.frame.pack()

        # Back button will take you to previous page
        back = Button(self.frame, text="Back").grid(row=0, column=0)
        # Delete will permanently remove child from database
        delete = Button(self.frame, text="Delete", command=self.back).grid(row=0, column=10)

        #name title
        firstNameLabel = Label(self.frame, text= name_first, font="Arial 12 underline").grid(row=1, column=3)
        lastNameLabel = Label(self.frame, text= name_last, font="Arial 12 underline").grid(row=1, column=4)

        #child app
        childAppLabel = Label(self.frame, text= "Child Applications").grid(row=2, column=0)

        curr.execute("SELECT Date_Submitted FROM Child_Application WHERE ID = %s;", (id,))
        childDateArr = curr.fetchall()

        r = 3
        for childDate in childDateArr:
            #date of program attended
            dateLabel = Label(self.frame, text= childDate[0]).grid(row=r, column=1)
            
            # Details button will take you to another page
            details = Button(self.frame, text="See Details").grid(row=r, column=5)
            r = r + 1

        #camp app
        campAppLabel = Label(self.frame, text= "Camp Applications").grid(row=r, column=0)

        curr.execute("SELECT Date_Submitted FROM Camp_Application WHERE ID = %s;", (id,))
        campDateArr = curr.fetchall()

        r = r + 1
        for campDate in campDateArr:
            #date of program attended
            dateLabel = Label(self.frame, text= campDate[0]).grid(row=r, column=1)
            
            # Details button will take you to another page
            details = Button(self.frame, text="See Details").grid(row=r, column=5)
            r = r + 1



        curr.close()
        db.close()

    def back(self):
        self.destroy();

master = Tk()
addUserPage = ProfilePage(master)
master.mainloop()
