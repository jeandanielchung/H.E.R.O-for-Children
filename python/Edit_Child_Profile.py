import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import tkMessageBox
import MySQLdb

class Example(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.canvas = tk.Canvas(master, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        master.title("Edit Profile")

#size & centering
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        x = (master.winfo_screenwidth() // 2) - (width // 2)
        y = (master.winfo_screenheight() // 2) - (height // 2)
        master.geometry("850x1000")

#TODO
    #figure out how to pass in parameters
    #deal with changing these? I think naw
        global id
        global date
        id = 1
        date = '2016-11-24'

#Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()
        
#Buttons
        #frame
        self.buttonframe = Frame(self.frame)
        self.buttonframe.pack(side = "top", fill = "x")

        #back
        backButton = Button(self.buttonframe, text = "Back", command = self.back)
        backButton.pack(side = "left")
        
        #delete
        deleteButton = Button(self.buttonframe, text = "Delete Application", command = self.delete)
        deleteButton.pack(side = "right")
        
#Child info section
        #header
        self.ChildInfoSectionHeaderframe = Frame(self.frame)
        self.ChildInfoSectionHeaderframe.pack()      
        labelChildInfoSection = Label(self.ChildInfoSectionHeaderframe, text = "\nCHILD'S INFORMATION")
        labelChildInfoSection.pack(fill = "x")
        labelChildInfoSection.config(font=("Helvetica", 20))

        self.ChildInfoSectionframe = Frame(self.frame)
        self.ChildInfoSectionframe.pack(fill = 'y', side = 'left') 

        #first name
        curr.execute("SELECT Name_First FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global childInfo0
        childInfo0 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo0.insert(0, val)
        else:
            childInfo0.insert(0, 'Unanswered')
            
        buttonUpdateChildInfo0 = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo0())

        buttonUpdateChildInfo0.grid(row = 0, column = 2)
        childInfo0.grid(row = 0, column = 1)
        label.grid(row = 0, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global childInfo1
        childInfo1 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo1.insert(0, val)
        else:
            childInfo1.insert(0, 'Unanswered')
            
        buttonUpdateChildInfo1 = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo1())

        buttonUpdateChildInfo1.grid(row = 1, column = 2)
        childInfo1.grid(row = 1, column = 1)
        label.grid(row = 1, column = 0)

        #nickname
        curr.execute("SELECT Name_Nickname FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. ")
        global childInfo2
        childInfo2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo2.insert(0, val)
        else:
            childInfo2.insert(0, 'Unanswered')
            
        buttonUpdateChildInfo2 = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo2())

        buttonUpdateChildInfo2.grid(row = 2, column = 2)
        childInfo2.grid(row = 2, column = 1)
        label.grid(row = 2, column = 0)

        #address street
        curr.execute("SELECT Address_Street FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global childInfo3
        childInfo3 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo3.insert(0, val)
        else:
            childInfo3.insert(0, 'Unanswered')
            
        buttonUpdateChildInfo3 = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        buttonUpdateChildInfo3.grid(row = 3, column = 2)
        childInfo3.grid(row = 3, column = 1)
        label.grid(row = 3, column = 0)

#Close Database Connection
        curr.close()
        db.close()

#Button Definitions
    def back(self):
        #Go back to 1st level profile page
        self.master.destroy()

    def delete(self):
        if askyesno('Verify', 'Really delete?'):

            #Open Database Connection
            db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
            curr = db.cursor()

            #Execute
            curr.execute("DELETE FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
            
            #Close Database Connection
            curr.close()
            db.close()
            
            #UI feedback
            showwarning('Delete', 'Application Deleted')

            #Go back to 1st level profile page (call back if you can)
            self.master.destroy()

        else:
            #Delete canclled
            showinfo('No', 'Delete has been cancelled')


    def updatechildInfo0(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #TODO:
            #update with error handling
        #check & feedback
        curr.execute("SELECT Name_First FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        if curr.fetchall()[0][0] == newVal:
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsuccessful.")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo1(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #TODO:
            #update with error handling
        #check & feedback
        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        if curr.fetchall()[0][0] == newVal:
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsuccessful.")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo2(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Name_Nickname = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Name_Nickname = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #TODO:
            #update with error handling
        #check & feedback
        curr.execute("SELECT Name_Nickname FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        if curr.fetchall()[0][0] == newVal:
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsuccessful.")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo3(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #TODO:
            #update with error handling
        #check & feedback
        curr.execute("SELECT Address_Street FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        if curr.fetchall()[0][0] == newVal:
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsuccessful.")

        #Close Database Connection
        curr.close()
        db.close()
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    master=tk.Tk()
    Example(master).pack(side="top", fill="both", expand=True)
    master.mainloop()
