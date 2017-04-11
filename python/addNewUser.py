from Tkinter import *
import MySQLdb

class AddUser:
    def __init__(self, master):


    
        self.frame = Frame(master)
        self.frame.pack()

        global entry1
        global entry2
        global entry3
        global variable

        name = Label(self.frame, text="Name").grid(row=1)
        entry1 = Entry(self.frame)
        entry1.grid(row=1, column=1)

        username = Label(self.frame, text="Username").grid(row=2)
        entry2 = Entry(self.frame)
        entry2.grid(row=2, column=1)

        password = Label(self.frame, text="Password").grid(row=3)
        entry3 = Entry(self.frame)
        entry3.grid(row=3, column=1)

        level = Label(self.frame, text="Type").grid(row=4)
        variable = StringVar(master)
        variable.set("Regular")
        menu = OptionMenu(self.frame, variable, 'Administrator', 'Manager', 'Regular').grid(row=4, column=1)

        add = Button(self.frame, text="Add User", command = self.addUser).grid(row=6, column=3)
        back = Button(self.frame, text="Go Back", command = self.back).grid(row=6, column=0)


    def addUser(self):

        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()
        
        curr.execute("""INSERT INTO User VALUES ('son', 'finch', SHA1('ew'), 'Regular');""")
            #, (entry1.get(), entry2.get(), entry3.get(), variable.get(),))
        db.commit()

        curr.close()
        db.close()

    def back(self):
        self.master.destroy()


master = Tk()
addUserPage = AddUser(master)
master.mainloop()