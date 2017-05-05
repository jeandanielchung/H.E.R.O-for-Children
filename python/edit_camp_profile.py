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
        
#Camper info section ************************************************************************************************************************
        self.CamperInfoSectionframe = Frame(self.frame)
        self.CamperInfoSectionframe.pack(fill = 'y', side = 'left') 
        r = 0

        #header
        labelCamperInfoSection = Label(self.CamperInfoSectionframe, text = "\nCAMPER INFORMATION")
        labelCamperInfoSection.grid(row = r, column = 0)
        labelCamperInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT First_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global camperInfo0
        camperInfo0 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo0.insert(0, val)
        else:
            camperInfo0.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Last_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nLast Name ............................................................................................ ")
        global camperInfo1
        camperInfo1 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo1.insert(0, val)
        else:
            camperInfo1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #middle initial
        curr.execute("SELECT Middle_Initial FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nMiddle Initial ........................................................................................ ")
        global camperInfo3
        camperInfo3 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo3.insert(0, val)
        else:
            camperInfo3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Date of Birth
        curr.execute("SELECT Date_Of_Birth FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nDate of Birth ...................................................................................... ")
        global camperInfo4
        camperInfo4 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo4.insert(0, val)
        else:
            camperInfo4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        curr.execute("SELECT Age FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nAge .................................................................................................. ")
        global camperInfo5
        camperInfo5 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo5.insert(0, val)
        else:
            camperInfo5.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        curr.execute("SELECT Gender FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nGender .............................................................................................. ")
        global camperInfo6
        camperInfo6 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo6.insert(0, val)
        else:
            camperInfo6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #race
        curr.execute("SELECT Race FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nRace ................................................................................................ ")
        global camperInfo7
        camperInfo7 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo7.insert(0, val)
        else:
            camperInfo7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #primary language
        curr.execute("SELECT Primary_Language FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nPrimary Language ...................................................................................... ")
        global camperInfo8
        camperInfo8 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo8.insert(0, val)
        else:
            camperInfo8.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        curr.execute("SELECT Address_Street FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nAddress Street ............................................................................................ ")
        global camperInfo9
        camperInfo9 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo9.insert(0, val)
        else:
            camperInfo9.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        curr.execute("SELECT Address_City FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nAddress City ............................................................................................ ")
        global camperInfo10
        camperInfo10 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo10.insert(0, val)
        else:
            camperInfo10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address state
        curr.execute("SELECT Address_State FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nAddress State ............................................................................................ ")
        global camperInfo11
        camperInfo11 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo11.insert(0, val)
        else:
            camperInfo11.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        curr.execute("SELECT Address_Zip FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nAddress Zip ............................................................................................ ")
        global camperInfo12
        camperInfo12 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo12.insert(0, val)
        else:
            camperInfo12.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        curr.execute("SELECT Address_County FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nAddress County ............................................................................................ ")
        global camperInfo13
        camperInfo13 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo13.insert(0, val)
        else:
            camperInfo13.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #camper email
        curr.execute("SELECT Camper_Email FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nCamper Email ............................................................................................ ")
        global camperInfo14
        camperInfo14 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo14.insert(0, val)
        else:
            camperInfo14.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #parent email
        curr.execute("SELECT Parent_Email FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nParent Email ............................................................................................ ")
        global camperInfo15
        camperInfo15 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo15.insert(0, val)
        else:
            camperInfo15.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #g name
        curr.execute("SELECT Guardian_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nGuardian Name ............................................................................................ ")
        global camperInfo16
        camperInfo16 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo16.insert(0, val)
        else:
            camperInfo16.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #relationship
        curr.execute("SELECT Guardian_Camper_Relationship FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nGuardian Camper Relationship ............................................................................................ ")
        global camperInfo17
        camperInfo17 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo17.insert(0, val)
        else:
            camperInfo17.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last grade
        curr.execute("SELECT Last_Grade_Completed FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nLast Grade Completed ............................................................................................ ")
        global camperInfo18
        camperInfo18 = Entry(self.CamperInfoSectionframe)

        if val is not None:
            camperInfo18.insert(0, val)
        else:
            camperInfo18.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        camperInfo18.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #sped classes
        curr.execute("SELECT Special_Ed_Classes FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nSpecial Ed Classes? ............................................................................................ ")
        global camperInfo19
        camperInfo19 = IntVar()

        Yes = Radiobutton(self.CamperInfoSectionframe, text = "Yes", variable = camperInfo19, value=1)
        No = Radiobutton(self.CamperInfoSectionframe, text = "No", variable = camperInfo19, value=2)

        if val is not None:
            if val is 0:
                camperInfo19.set(2)
            else:
                camperInfo19.set(1)
 
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo14())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #siblings applying
        curr.execute("SELECT Siblings_Applying FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.CamperInfoSectionframe, text = "\nSiblings Apllying? ............................................................................................ ")
        global camperInfo20
        camperInfo20 = IntVar()

        Yes = Radiobutton(self.CamperInfoSectionframe, text = "Yes", variable = camperInfo19, value=1)
        No = Radiobutton(self.CamperInfoSectionframe, text = "No", variable = camperInfo19, value=2)

        if val is not None:
            if val is 0:
                camperInfo20.set(2)
            else:
                childInfo20.set(1)
 
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo14())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #tshirt
        label = Label(self.CamperInfoSectionframe, text = "\nT-Shirt Size ............................................................................................. ")

        curr.execute("SELECT T_Shirt FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global camperInfo21
        camperInfo21 = StringVar()
        
        choices = ['Youth S','Youth M','Youth L','Adult S','Adult M','Adult L','Adult XL','Adult XXL']
        option = tk.OptionMenu(self.CamperInfoSectionframe, camperInfo21, *choices)

        if val is not None:
            camperInfo21.set(val)
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo21())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #planned trans
        label = Label(self.CamperInfoSectionframe, text = "\nPlanned Transportation ............................................................................................. ")

        curr.execute("SELECT Planned_Transportation FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global camperInfo22
        camperInfo22 = StringVar()
        
        choices = ['Atlanta Bus','Augusta Bus','Albany Bus','Athens Bus','Savannah Bus','Car/Drop off','Adult XL','Adult XXL']
        option = tk.OptionMenu(self.CamperInfoSectionframe, camperInfo22, *choices)

        if val is not None:
            camperInfo22.set(val)
            
        buttonUpdate = Button(self.CamperInfoSectionframe, text = "Update", command = lambda:self.updatecamperInfo21())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)        

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
            curr.execute("DELETE FROM Camp_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
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


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    master=tk.Tk()
    Example(master).pack(side="top", fill="both", expand=True)
    master.mainloop()