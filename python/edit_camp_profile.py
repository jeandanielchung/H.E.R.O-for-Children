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
        master.geometry("1100x1000")

# parameters
        global id
        global date
        id = 1
        date = '2016-11-24'
        
#Database connection
        db = self.connect()
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
        
#Database dump frame
        DemographicSectionframe = Frame(self.frame)
        DemographicSectionframe.pack(fill = 'y', side = 'left') 
        r = 0

#
#parent sections
#

#Demographic info section ************************************************************************************************************************
        #header
        labelDemographicSection = Label(DemographicSectionframe, text = "\n\nDEMOGRAPHIC INFORMATION")
        labelDemographicSection.grid(row = r, columnspan = 2)
        labelDemographicSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT First_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFirst Name ................................................................................................................................. ")
        demInfo0 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo0.insert(0, val)
        else:
            demInfo0.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo0(demInfo0, id, date, demInfo5))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Last_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nLast Name ................................................................................................................................. ")
        demInfo1 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo1.insert(0, val)
        else:
            demInfo1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo1(demInfo1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #middle initial
        curr.execute("SELECT Middle_Initial FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMiddle Initial .............................................................................................................................. ")
        demInfo2 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo2.insert(0, val)
        else:
            demInfo2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo2(demInfo2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        curr.execute("SELECT Age FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nAge ............................................................................................................................................ ")
        demInfo3 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo3.insert(0, val)
        else:
            demInfo3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo3(demInfo3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Date of Birth
        curr.execute("SELECT Date_Of_Birth FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ..................................................................................................... ")
        demInfo4 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo4.insert(0, val)
        else:
            demInfo4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo4(demInfo4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        label = Label(DemographicSectionframe, text = "\nGender ...................................................................................................................................... ")

        curr.execute("SELECT Gender FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        demInfo5 = StringVar()

        choices = ['Male', 'Female']
        option = tk.OptionMenu(DemographicSectionframe, demInfo5, *choices)        
        
        if val is not None:
            demInfo5.set(val)
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo5(demInfo5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #race
        curr.execute("SELECT Race FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nRace .......................................................................................................................................... ")
        demInfo6 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo6.insert(0, val)
        else:
            demInfo6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo6(demInfo6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #primary language
        curr.execute("SELECT Primary_Language FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nPrimary Language ...................................................................................................................... ")
        demInfo7 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo7.insert(0, val)
        else:
            demInfo7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo7(demInfo7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        curr.execute("SELECT Address_Street FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nStreet Address ........................................................................................................................... ")
        demInfo8 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo8.insert(0, val)
        else:
            demInfo8.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo8(demInfo8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        curr.execute("SELECT Address_City FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nCity ........................................................................................................................................... ")
        demInfo9 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo9.insert(0, val)
        else:
            demInfo9.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo9(demInfo9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address state
        curr.execute("SELECT Address_State FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nState ......................................................................................................................................... ")
        demInfo10 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo10.insert(0, val)
        else:
            demInfo10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo10(demInfo10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        curr.execute("SELECT Address_County FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nCounty ...................................................................................................................................... ")
        demInfo11 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo11.insert(0, val)
        else:
            demInfo11.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo11(demInfo11, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        curr.execute("SELECT Address_Zip FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nZip ............................................................................................................................................ ")
        demInfo12 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo12.insert(0, val)
        else:
            demInfo12.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo12(demInfo12, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #camper email
        curr.execute("SELECT Camper_Email FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nCamper Email ............................................................................................................................ ")
        demInfo13 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo13.insert(0, val)
        else:
            demInfo13.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo13(demInfo13, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #parent email
        curr.execute("SELECT Parent_Email FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nParent Email .............................................................................................................................. ")
        demInfo14 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo14.insert(0, val)
        else:
            demInfo14.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo14(demInfo14, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #g name
        curr.execute("SELECT Guardian_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nGuardian Name .......................................................................................................................... ")
        demInfo15 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo15.insert(0, val)
        else:
            demInfo15.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo15(demInfo15, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #relationship
        curr.execute("SELECT Guardian_Camper_Relationship FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nGuardian Camper Relationship ................................................................................................... ")
        demInfo16 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo16.insert(0, val)
        else:
            demInfo16.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo16(demInfo16, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last grade
        curr.execute("SELECT Last_Grade_Completed FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nLast Grade Completed ............................................................................................................... ")
        demInfo17 = Entry(DemographicSectionframe)

        if val is not None:
            demInfo17.insert(0, val)
        else:
            demInfo17.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo17(demInfo17, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #sped classes
        curr.execute("SELECT Special_Ed_Classes FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nSpecial Ed Classes? ................................................................................................................... ")
        demInfo18 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = demInfo18, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = demInfo18, value=2)

        if val is not None:
            if val is 0:
                demInfo18.set(2)
            else:
                demInfo18.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo18(demInfo18, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #siblings applying
        curr.execute("SELECT Siblings_Applying FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nSiblings Apllying? ..................................................................................................................... ")
        demInfo19 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = demInfo19, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = demInfo19, value=2)

        if val is not None:
            if val is 0:
                demInfo19.set(2)
            else:
                demInfo19.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo19(demInfo19, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #tshirt
        label = Label(DemographicSectionframe, text = "\nT-Shirt Size ............................................................................................................................... ")

        curr.execute("SELECT T_Shirt FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        demInfo20 = StringVar()
        
        choices = ['Youth S','Youth M','Youth L','Adult S','Adult M','Adult L','Adult XL','Adult XXL']
        option = tk.OptionMenu(DemographicSectionframe, demInfo20, *choices)

        if val is not None:
            demInfo20.set(val)
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo20(demInfo20, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #planned trans
        label = Label(DemographicSectionframe, text = "\nPlanned Transportation ............................................................................................................. ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDemInfo21(demTrans0, demTrans1, demTrans2, demTrans3,
            demTrans4, demTrans5, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Planned_Transportation FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        #Atlanta
        demTrans0 = IntVar()
        Checkbutton(DemographicSectionframe, text="Atlanta Bus", variable = demTrans0).grid(row = r,  column = 1, sticky = W)

        #Augusta
        demTrans1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Augusta Bus", variable = demTrans1).grid(row = r,  column = 1, sticky = W)
        
        #Albany
        demTrans2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Albany Bus", variable = demTrans2).grid(row = r,  column = 1, sticky = W)
        
        #Athens
        demTrans3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Athens Bus", variable = demTrans3).grid(row = r,  column = 1, sticky = W)
        
        #Savannah
        demTrans4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Savannah Bus", variable = demTrans4).grid(row = r,  column = 1, sticky = W)
        
        #Car
        demTrans5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Car/Drop off", variable = demTrans5).grid(row = r,  column = 1, sticky = W)

        if val is not None:
            if 'Atlanta bus' in val:
                demTrans0.set(1)
            if 'Augusta bus' in val:
                demTrans1.set(1)
            if 'Albany bus' in val:
                demTrans2.set(1)
            if 'Athens bus' in val:
                demTrans3.set(1)
            if 'Savannah bus' in val:
                demTrans4.set(1)
            if 'Car/drop' in val:
                demTrans5.set(1)

#demographic contacts ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nCONTACT INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #CELL
        #type
        label = Label(DemographicSectionframe, text = "\nCell Number")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #Name
        curr.execute("SELECT Name FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Contact Name ............................................................................................................................ ")
        demContactInfo10 = Entry(DemographicSectionframe)

        if val is not None:
            demContactInfo10.insert(0, val)
        else:
            demContactInfo10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo10(demContactInfo10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demContactInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #time pref
        label = Label(DemographicSectionframe, text = "Time Preference ......................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo11(demContactInfoTime10, demContactInfoTime11, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Time_Preference FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
        val = curr.fetchall()[0][0]

        #Day
        demContactInfoTime10 = IntVar()
        Checkbutton(DemographicSectionframe, text="Day", variable = demContactInfoTime10).grid(row = r,  column = 1, sticky = W)

        #Evening
        demContactInfoTime11 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Evening", variable = demContactInfoTime11).grid(row = r,  column = 1, sticky = W)

        if val is not None:
            if 'Day' in val:
                demContactInfoTime10.set(1)

            if 'Evening' in val:
                demContactInfoTime11.set(1)

        #phone number
        curr.execute("SELECT Phone_Number FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Phone Number ............................................................................................................................ ")
        demContactInfo11 = Entry(DemographicSectionframe)

        if val is not None:
            demContactInfo11.insert(0, val)
        else:
            demContactInfo11.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo12(demContactInfo11, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demContactInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HOME
        #type
        label = Label(DemographicSectionframe, text = "\nHome Number")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #Name
        curr.execute("SELECT Name FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Contact Name ............................................................................................................................ ")
        demContactInfo20 = Entry(DemographicSectionframe)

        if val is not None:
            demContactInfo20.insert(0, val)
        else:
            demContactInfo20.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo20(demContactInfo20, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demContactInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #time pref
        label = Label(DemographicSectionframe, text = "Time Preference ......................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo21(demContactInfoTime20, demContactInfoTime21, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Time_Preference FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (id, date,))
        val = curr.fetchall()[0][0]

        #Day
        demContactInfoTime20 = IntVar()
        Checkbutton(DemographicSectionframe, text="Day", variable = demContactInfoTime20).grid(row = r,  column = 1, sticky = W)

        #Evening
        demContactInfoTime21 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Evening", variable = demContactInfoTime21).grid(row = r,  column = 1, sticky = W)

        if val is not None:
            if 'Day' in val:
                demContactInfoTime20.set(1)

            if 'Evening' in val:
                demContactInfoTime21.set(1)

        #phone number
        curr.execute("SELECT Phone_Number FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Phone Number ............................................................................................................................ ")
        demContactInfo21 = Entry(DemographicSectionframe)

        if val is not None:
            demContactInfo21.insert(0, val)
        else:
            demContactInfo21.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo22(demContactInfo21, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demContactInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #WORK
        #type
        label = Label(DemographicSectionframe, text = "\nWork Number")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #Name
        curr.execute("SELECT Name FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Contact Name ............................................................................................................................ ")
        demContactInfo30 = Entry(DemographicSectionframe)

        if val is not None:
            demContactInfo30.insert(0, val)
        else:
            demContactInfo30.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo30(demContactInfo30, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demContactInfo30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #time pref
        label = Label(DemographicSectionframe, text = "Time Preference ......................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo31(demContactInfoTime30, demContactInfoTime31, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Time_Preference FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (id, date,))
        val = curr.fetchall()[0][0]

        #Day
        demContactInfoTime30 = IntVar()
        Checkbutton(DemographicSectionframe, text="Day", variable = demContactInfoTime30).grid(row = r,  column = 1, sticky = W)

        #Evening
        demContactInfoTime31 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Evening", variable = demContactInfoTime31).grid(row = r,  column = 1, sticky = W)

        if val is not None:
            if 'Day' in val:
                demContactInfoTime30.set(1)

            if 'Evening' in val:
                demContactInfoTime31.set(1)

        #phone number
        curr.execute("SELECT Phone_Number FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Phone Number ............................................................................................................................ ")
        demContactInfo31 = Entry(DemographicSectionframe)

        if val is not None:
            demContactInfo31.insert(0, val)
        else:
            demContactInfo31.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateContactDemInfo32(demContactInfo31, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        demContactInfo31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Emergency Contact Section ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nEMERGENCY CONTACT INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #contacts
        curr.execute("SELECT Name FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        
        if emergencyContacts is ():
            emergencyContacts = []

        if len(emergencyContacts) > 0:        
            
            #Name
            label = Label(DemographicSectionframe, text = "\nEmergency Contact Name 1 ....................................................................................................... ")
            emergencyInfo10 = Entry(DemographicSectionframe)

            emergencyInfo10.insert(0, emergencyContacts[0][0])
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo0(emergencyInfo10, 1, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo10.grid(row = r, column = 1)
            label.grid(row = r, column = 0)


            #Relationship
            curr.execute("SELECT Relationship FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, emergencyContacts[0][0]))
            val = curr.fetchall()[0][0]

            label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. ")
            emergencyInfo11 = Entry(DemographicSectionframe)

            if val is not None:
                emergencyInfo11.insert(0, val)
            else:
                emergencyInfo11.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo1(emergencyInfo11, 1, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo11.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Daytime Phone
            curr.execute("SELECT Daytime_Phone FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, emergencyContacts[0][0]))
            val = curr.fetchall()[0][0]

            label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... ")
            emergencyInfo12 = Entry(DemographicSectionframe)

            if val is not None:
                emergencyInfo12.insert(0, val)
            else:
                emergencyInfo12.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo2(emergencyInfo12, 1, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo12.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Evening Phone
            curr.execute("SELECT Evening_Phone FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, emergencyContacts[0][0]))
            val = curr.fetchall()[0][0]

            label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... ")
            emergencyInfo13 = Entry(DemographicSectionframe)

            if val is not None:
                emergencyInfo13.insert(0, val)
            else:
                emergencyInfo13.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo3(emergencyInfo13, 1, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo13.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

        else:

            #Name
            label = Label(DemographicSectionframe, text = "\nEmergency Contact Name 1 ....................................................................................................... ")
            emergencyInfo10 = Entry(DemographicSectionframe)
            emergencyInfo10.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo0(emergencyInfo10, 1, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo10.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Relationship
            label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. ")
            emergencyInfo11 = Entry(DemographicSectionframe)

            emergencyInfo11.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo1(emergencyInfo11, 1, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo11.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Daytime Phone
            label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... ")
            emergencyInfo12 = Entry(DemographicSectionframe)

            emergencyInfo12.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo2(emergencyInfo12, 1, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo12.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Evening Phone
            label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... ")
            emergencyInfo13 = Entry(DemographicSectionframe)

            emergencyInfo13.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo3(emergencyInfo13, 1, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo13.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

        if len(emergencyContacts) < 2:
            
            #Name
            label = Label(DemographicSectionframe, text = "\nEmergency Contact Name 2 ....................................................................................................... ")
            emergencyInfo20 = Entry(DemographicSectionframe)
            emergencyInfo20.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo0(emergencyInfo20, 2, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo20.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Relationship
            label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. ")
            emergencyInfo21 = Entry(DemographicSectionframe)

            emergencyInfo21.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo1(emergencyInfo21, 2, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo21.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Daytime Phone
            label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... ")
            emergencyInfo22 = Entry(DemographicSectionframe)

            emergencyInfo22.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo2(emergencyInfo22, 2, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo22.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Evening Phone
            label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... ")
            emergencyInfo23 = Entry(DemographicSectionframe)

            emergencyInfo23.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo3(emergencyInfo23, 2, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo23.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

        else:
            #Name
            label = Label(DemographicSectionframe, text = "\nEmergency Contact Name 2 ....................................................................................................... ")
            emergencyInfo20 = Entry(DemographicSectionframe)

            emergencyInfo20.insert(0, emergencyContacts[1][0])
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo0(emergencyInfo20, 2, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo20.grid(row = r, column = 1)
            label.grid(row = r, column = 0)


            #Relationship
            curr.execute("SELECT Relationship FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, emergencyContacts[1][0]))
            val = curr.fetchall()[0][0]

            label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. ")
            emergencyInfo21 = Entry(DemographicSectionframe)

            if val is not None:
                emergencyInfo21.insert(0, val)
            else:
                emergencyInfo21.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo1(emergencyInfo21, 2, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo21.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Daytime Phone
            curr.execute("SELECT Daytime_Phone FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, emergencyContacts[1][0]))
            val = curr.fetchall()[0][0]

            label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... ")
            emergencyInfo22 = Entry(DemographicSectionframe)

            if val is not None:
                emergencyInfo22.insert(0, val)
            else:
                emergencyInfo22.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo2(emergencyInfo22, 2, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo22.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

            #Evening Phone
            curr.execute("SELECT Evening_Phone FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, emergencyContacts[1][0]))
            val = curr.fetchall()[0][0]

            label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... ")
            emergencyInfo23 = Entry(DemographicSectionframe)

            if val is not None:
                emergencyInfo23.insert(0, val)
            else:
                emergencyInfo23.insert(0, 'Unanswered')
                
            buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateEmergencyInfo3(emergencyInfo23, 2, id, date))

            r = r+1
            buttonUpdate.grid(row = r, column = 2)
            emergencyInfo23.grid(row = r, column = 1)
            label.grid(row = r, column = 0)

#Insurance Info Section ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nINSURANCE INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #Insurer
        label = Label(DemographicSectionframe, text = "\nHealth Insurance Provider .......................................................................................................... ")

        curr.execute("SELECT Type_of_Health_Insurance FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        insuranceInfo0 = StringVar()
        
        choices = ['Medicaid','PeachCare','Private','None']
        option = tk.OptionMenu(DemographicSectionframe, insuranceInfo0, *choices)

        if val is not None:
            insuranceInfo0.set(val)
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateInsuranceInfo0(insuranceInfo0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Private Insurer Name
        curr.execute("SELECT Private_Insurance_Name FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nIf Private, Insurance Provider Name ........................................................................................... ")
        insuranceInfo1 = Entry(DemographicSectionframe)

        if val is not None:
            insuranceInfo1.insert(0, val)
        else:
            insuranceInfo1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateInsuranceInfo1(insuranceInfo1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        insuranceInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Policy Number
        curr.execute("SELECT Policy_Number FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nPolicy Number ........................................................................................................................... ")
        insuranceInfo2 = Entry(DemographicSectionframe)

        if val is not None:
            insuranceInfo2.insert(0, val)
        else:
            insuranceInfo2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateInsuranceInfo2(insuranceInfo2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        insuranceInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Group Number
        curr.execute("SELECT Group_Number FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nGroup Number ........................................................................................................................... ")
        insuranceInfo3 = Entry(DemographicSectionframe)

        if val is not None:
            insuranceInfo3.insert(0, val)
        else:
            insuranceInfo3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateInsuranceInfo3(insuranceInfo3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        insuranceInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Medical Provider Section ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #Name
        curr.execute("SELECT Medical_Provider_Name FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMedical Provider Name .............................................................................................................. ")
        medProviderInfo0 = Entry(DemographicSectionframe)

        if val is not None:
            medProviderInfo0.insert(0, val)
        else:
            medProviderInfo0.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProviderInfo0(medProviderInfo0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProviderInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Office Phone
        curr.execute("SELECT Phone_Office FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMedical Provider Name .............................................................................................................. ")
        medProviderInfo1 = Entry(DemographicSectionframe)

        if val is not None:
            medProviderInfo1.insert(0, val)
        else:
            medProviderInfo1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProviderInfo1(medProviderInfo1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProviderInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Pharmacy name
        curr.execute("SELECT Pharmacy_Name FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nName of Pharmacy ..................................................................................................................... ")
        medProviderInfo2 = Entry(DemographicSectionframe)

        if val is not None:
            medProviderInfo2.insert(0, val)
        else:
            medProviderInfo2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProviderInfo2(medProviderInfo2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProviderInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Pharmacy Phone Number
        curr.execute("SELECT Phone_Pharmacy FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nPharmacy Phone Number ........................................................................................................... ")
        medProviderInfo3 = Entry(DemographicSectionframe)

        if val is not None:
            medProviderInfo3.insert(0, val)
        else:
            medProviderInfo3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProviderInfo3(medProviderInfo3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProviderInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Medical Information Section ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nMEDICAL INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #Conditions
        label = Label(DemographicSectionframe, text = "\nCurrent Medical Conditions ........................................................................................................ ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedInfoCurr(medInfoCurr0, medInfoCurr1, medInfoCurr2, medInfoCurr3, medInfoCurr4,
            medInfoCurr5, medInfoCurr6, medInfoCurr7, medInfoCurr8, medInfoCurr9, medInfoCurr10, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Current_Medical_Conditions FROM Medical_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        #HIV
        medInfoCurr0 = IntVar()
        Checkbutton(DemographicSectionframe, text="HIV", variable = medInfoCurr0).grid(row = r,  column = 1, sticky = W)

        #Hepatitis B
        medInfoCurr1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Hepatitis B", variable = medInfoCurr1).grid(row = r,  column = 1, sticky = W)
        
        #Hepatitis C
        medInfoCurr2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Hepatitis C", variable = medInfoCurr2).grid(row = r,  column = 1, sticky = W)
        
        #ADD or ADHD
        medInfoCurr3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="ADD or ADHD", variable = medInfoCurr3).grid(row = r,  column = 1, sticky = W)
        
        #Sickle Cell Disease
        medInfoCurr4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Sickle Cell Disease", variable = medInfoCurr4).grid(row = r,  column = 1, sticky = W)
        
        #Asthma
        medInfoCurr5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Asthma", variable = medInfoCurr5).grid(row = r,  column = 1, sticky = W)
        
        #Tubes in Ears
        medInfoCurr6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Tubes in Ears", variable = medInfoCurr6).grid(row = r,  column = 1, sticky = W)
        
        #Heart Problems
        medInfoCurr7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Heart Problems", variable = medInfoCurr7).grid(row = r,  column = 1, sticky = W)
        
        #Mental Health Diagnoses
        medInfoCurr8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Mental Health Diagnoses", variable = medInfoCurr8).grid(row = r,  column = 1, sticky = W)
        
        #Other
        medInfoCurr9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Other", variable = medInfoCurr9).grid(row = r,  column = 1, sticky = W)

        if val is not None:
            if 'HIV' in val:
                medInfoCurr0.set(1)
            if 'Hepatitis B' in val:
                medInfoCurr1.set(1)
            if 'Hepatitis C' in val:
                medInfoCurr2.set(1)
            if 'ADD or ADHD' in val:
                medInfoCurr3.set(1)
            if 'Sickle Cell Disease' in val:
                medInfoCurr4.set(1)
            if 'Asthma' in val:
                medInfoCurr5.set(1)
            if 'Tubes in Ears' in val:
                medInfoCurr6.set(1)
            if 'Heart Problems' in val:
                medInfoCurr7.set(1)
            if 'Mental Health Diagnoses' in val:
                medInfoCurr8.set(1)
            if 'Other' in val:
                medInfoCurr9.set(1)

        #Conditions other
        curr.execute("SELECT Other FROM Medical_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        medInfoCurr10 = Entry(DemographicSectionframe, width = 14)

        if val is not None:
            medInfoCurr10.insert(0, val)
        else:
            medInfoCurr10.insert(0, 'Unanswered')
        medInfoCurr10.grid(row = r, column = 1, sticky = E)

        #Conditions Explained
        curr.execute("SELECT Medical_Condition_Explanation FROM Medical_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nDescription of Medical Conditions .............................................................................................. ")
        medInfo1 = Entry(DemographicSectionframe)

        if val is not None:
            medInfo1.insert(0, val)
        else:
            medInfo1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedInfo1(medInfo1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Allergies Section ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nALLERGY INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))        

        #Med Allergy
        curr.execute("SELECT Med_Allergy FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMedical Allergies? ...................................................................................................................... ")
        allergyInfo0 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = allergyInfo0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = allergyInfo0, value=2)

        if val is not None:
            if val is 0:
                allergyInfo0.set(2)
            else:
                allergyInfo0.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateAllergyInfo0(allergyInfo0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Med Allergy Reaction
        curr.execute("SELECT Med_Reaction FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMedical Allergy Reaction ............................................................................................................ ")
        allergyInfo1 = Entry(DemographicSectionframe)

        if val is not None:
            allergyInfo1.insert(0, val)
        else:
            allergyInfo1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateAllergyInfo1(allergyInfo1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        allergyInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Food Allergy
        curr.execute("SELECT Food_Allergy FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFood Allergies? .......................................................................................................................... ")
        allergyInfo2 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = allergyInfo2, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = allergyInfo2, value=2)

        if val is not None:
            if val is 0:
                allergyInfo2.set(2)
            else:
                allergyInfo2.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateAllergyInfo2(allergyInfo2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Food Allergy Reaction
        curr.execute("SELECT Food_Reaction FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFood Allergy Reaction ................................................................................................................ ")
        allergyInfo3 = Entry(DemographicSectionframe)

        if val is not None:
            allergyInfo3.insert(0, val)
        else:
            allergyInfo3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateAllergyInfo3(allergyInfo3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        allergyInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Environmental Allergies
        curr.execute("SELECT Env_Allergy FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nEnvironmental Allergies? ............................................................................................................ ")
        allergyInfo4 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = allergyInfo4, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = allergyInfo4, value=2)

        if val is not None:
            if val is 0:
                allergyInfo4.set(2)
            else:
                allergyInfo4.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateAllergyInfo4(allergyInfo4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Environmental Allergy Reaction
        curr.execute("SELECT Env_Reaction FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nEnvironmental Allergy Reaction .................................................................................................. ")
        allergyInfo5 = Entry(DemographicSectionframe)

        if val is not None:
            allergyInfo5.insert(0, val)
        else:
            allergyInfo5.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateAllergyInfo5(allergyInfo5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        allergyInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Epi Pen
        curr.execute("SELECT EpiPen FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nEpiPen for any of the above allergies? ........................................................................................ ")
        allergyInfo6 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = allergyInfo6, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = allergyInfo6, value=2)

        if val is not None:
            if val is 0:
                allergyInfo6.set(2)
            else:
                allergyInfo6.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateAllergyInfo6(allergyInfo6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#Dietary Needs Section ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nDIETARY INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))   

        #Special Dietary Needs
        curr.execute("SELECT Special_Dietary_Needs FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nSpecial Dietary Needs ................................................................................................................ ")
        dietaryNeedsInfo0 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = dietaryNeedsInfo0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = dietaryNeedsInfo0, value=2)

        if val is not None:
            if val is 0:
                dietaryNeedsInfo0.set(2)
            else:
                dietaryNeedsInfo0.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo0(dietaryNeedsInfo0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Vegetarian
        curr.execute("SELECT Vegetarian FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nVegetarian ................................................................................................................................. ")
        dietaryNeedsInfo1 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = dietaryNeedsInfo1, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = dietaryNeedsInfo1, value=2)

        if val is not None:
            if val is 0:
                dietaryNeedsInfo1.set(2)
            else:
                dietaryNeedsInfo1.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo1(dietaryNeedsInfo1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Food Restrictions
        curr.execute("SELECT Food_Restrictions FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFood Restrictions ....................................................................................................................... ")
        dietaryNeedsInfo2 = Entry(DemographicSectionframe)

        if val is not None:
            dietaryNeedsInfo2.insert(0, val)
        else:
            dietaryNeedsInfo2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo2(dietaryNeedsInfo2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        dietaryNeedsInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #G Tube
        label = Label(DemographicSectionframe, text = "\nG-Tube ...................................................................................................................................... ")

        curr.execute("SELECT G_Tube FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        dietaryNeedsInfo3 = StringVar()
        
        choices = ['None','Medicine','Formula','Both']
        option = tk.OptionMenu(DemographicSectionframe, dietaryNeedsInfo3, *choices)

        if val is not None:
            dietaryNeedsInfo3.set(val)
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo3(dietaryNeedsInfo3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Formula Supplements
        curr.execute("SELECT Formula_Supplement FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFormula Supplements ................................................................................................................ ")
        dietaryNeedsInfo4 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = dietaryNeedsInfo4, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = dietaryNeedsInfo4, value=2)

        if val is not None:
            if val is 0:
                dietaryNeedsInfo4.set(2)
            else:
                dietaryNeedsInfo4.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo4(dietaryNeedsInfo4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Formula Supplements How
        label = Label(DemographicSectionframe, text = "\nFormula Supplements How? ....................................................................................................... ")

        curr.execute("SELECT Formula_Supplement_How FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        dietaryNeedsInfo5 = StringVar()
        
        choices = ['By Mouth','By G-Tube']
        option = tk.OptionMenu(DemographicSectionframe, dietaryNeedsInfo5, *choices)

        if val is not None:
            dietaryNeedsInfo5.set(val)
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo5(dietaryNeedsInfo5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Formula Type
        curr.execute("SELECT Food_Restrictions FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFormula Type ............................................................................................................................. ")
        dietaryNeedsInfo6 = Entry(DemographicSectionframe)

        if val is not None:
            dietaryNeedsInfo6.insert(0, val)
        else:
            dietaryNeedsInfo6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo6(dietaryNeedsInfo6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        dietaryNeedsInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #cans per day
        curr.execute("SELECT Formula_Cans_Per_Day FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFormula Cans Per Day ................................................................................................................ ")
        dietaryNeedsInfo7 = Entry(DemographicSectionframe)

        if val is not None:
            dietaryNeedsInfo7.insert(0, val)
        else:
            dietaryNeedsInfo7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo7(dietaryNeedsInfo7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        dietaryNeedsInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Feeding Pump
        curr.execute("SELECT Feeding_Pump FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFeeding Pump ............................................................................................................................ ")
        dietaryNeedsInfo8 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = dietaryNeedsInfo8, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = dietaryNeedsInfo8, value=2)

        if val is not None:
            if val is 0:
                dietaryNeedsInfo8.set(2)
            else:
                dietaryNeedsInfo8.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo8(dietaryNeedsInfo8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Feeding Pump Type
        curr.execute("SELECT Pump_Type FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nPump Type ................................................................................................................................ ")
        dietaryNeedsInfo9 = Entry(DemographicSectionframe)

        if val is not None:
            dietaryNeedsInfo9.insert(0, val)
        else:
            dietaryNeedsInfo9.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo9(dietaryNeedsInfo9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        dietaryNeedsInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Feeding schedule
        curr.execute("SELECT Feeding_Schedule FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFeeding Schedule ...................................................................................................................... ")
        dietaryNeedsInfo10 = Entry(DemographicSectionframe)

        if val is not None:
            dietaryNeedsInfo10.insert(0, val)
        else:
            dietaryNeedsInfo10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDietaryNeedsInfo10(dietaryNeedsInfo10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        dietaryNeedsInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#General health ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nGENERAL HEALTH INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #Physical Limitations
        label = Label(DemographicSectionframe, text = "\nPhysical Limitations ................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.genHealthLimit(genHealthLimit0, genHealthLimit1, genHealthLimit2, genHealthLimit3, genHealthLimit4,
            genHealthLimit5, genHealthLimit6, genHealthLimit7, genHealthLimit8, genHealthLimit9, genHealthLimit10, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Physical_Limitations FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        #Dressing
        genHealthLimit0 = IntVar()
        Checkbutton(DemographicSectionframe, text="Dressing", variable = genHealthLimit0).grid(row = r,  column = 1, sticky = W)

        #Showering
        genHealthLimit1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Showering", variable = genHealthLimit1).grid(row = r,  column = 1, sticky = W)
        
        #Eating
        genHealthLimit2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Eating", variable = genHealthLimit2).grid(row = r,  column = 1, sticky = W)
        
        #Toileting
        genHealthLimit3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Toileting", variable = genHealthLimit3).grid(row = r,  column = 1, sticky = W)

        #Walking/Balance
        genHealthLimit4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Walking/Balance", variable = genHealthLimit4).grid(row = r,  column = 1, sticky = W)

        #Braces
        genHealthLimit5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Braces", variable = genHealthLimit5).grid(row = r,  column = 1, sticky = W)

        #Casts
        genHealthLimit6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Casts", variable = genHealthLimit6).grid(row = r,  column = 1, sticky = W)

        #Walker
        genHealthLimit7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Walker", variable = genHealthLimit7).grid(row = r,  column = 1, sticky = W)

        #Wheelchair
        genHealthLimit8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Wheelchair", variable = genHealthLimit8).grid(row = r,  column = 1, sticky = W)

        #Other
        genHealthLimit9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Other", variable = genHealthLimit9).grid(row = r,  column = 1, sticky = W)

        if val is not None:
            if 'Dressing' in val:
                genHealthLimit0.set(1)
            if 'Showering' in val:
                genHealthLimit1.set(1)
            if 'Eating' in val:
                genHealthLimit2.set(1)
            if 'Toileting' in val:
                genHealthLimit3.set(1)
            if 'Walking/Balance' in val:
                genHealthLimit4.set(1)
            if 'Braces' in val:
                genHealthLimit5.set(1)
            if 'Casts' in val:
                genHealthLimit6.set(1)
            if 'Walker' in val:
                genHealthLimit7.set(1)
            if 'Wheelchair' in val:
                genHealthLimit8.set(1)
            if 'Other' in val:
                genHealthLimit9.set(1)

        #Physical Limitations other
        curr.execute("SELECT Other FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        genHealthLimit10 = Entry(DemographicSectionframe, width = 14)

        if val is not None:
            genHealthLimit10.insert(0, val)
        else:
            genHealthLimit10.insert(0, 'Unanswered')
        genHealthLimit10.grid(row = r, column = 1, sticky = E)

        #Tire Easily
        curr.execute("SELECT Tire_Easily FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nTire Easily .................................................................................................................................. ")
        genHealth1 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth1, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth1, value=2)

        if val is not None:
            if val is 0:
                genHealth1.set(2)
            else:
                genHealth1.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateGenHealth1(genHealth1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Swim
        curr.execute("SELECT Swim FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nCan Swim ................................................................................................................................... ")
        genHealth2 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth2, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth2, value=2)

        if val is not None:
            if val is 0:
                genHealth2.set(2)
            else:
                genHealth2.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateGenHealth2(genHealth2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Chicken Pox
        curr.execute("SELECT Chicken_Pox FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nChicken Pox Vaccinated? ............................................................................................................ ")
        genHealth3 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth3, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth3, value=2)

        if val is not None:
            if val is 0:
                genHealth3.set(2)
            else:
                genHealth3.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateGenHealth3(genHealth3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #c pox date
        curr.execute("SELECT Chicken_Pox_Date FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nChicken Pox Date (YYYY-MM-DD) ............................................................................................... ")
        genHealth4 = Entry(DemographicSectionframe)

        if val is not None:
            genHealth4.insert(0, val)
        else:
            genHealth4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateGenHealth4(genHealth4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        genHealth4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Menstrual Cycle
        curr.execute("SELECT Menstrual_Cycle FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMenstrual Cycle ......................................................................................................................... ")
        genHealth5 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth5, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth5, value=2)

        if val is not None:
            if val is 0:
                genHealth5.set(2)
            else:
                genHealth5.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateGenHealth5(genHealth5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #m cycle difficulties
        curr.execute("SELECT Menstrual_Difficulties FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMenstrual Difficulties ................................................................................................................. ")
        genHealth6 = Entry(DemographicSectionframe)

        if val is not None:
            genHealth6.insert(0, val)
        else:
            genHealth6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateGenHealth6(genHealth6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        genHealth6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Behavior ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nBEHAVIORAL INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #Camper knows
        curr.execute("SELECT Camper_Knows FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nCamper knows that someone in his/her family has HIV/AIDS ...................................................... ")
        behavior0 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = behavior0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = behavior0, value=2)

        if val is not None:
            if val is 0:
                behavior0.set(2)
            else:
                behavior0.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateBehavior0(behavior0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #How long Camper known
        label = Label(DemographicSectionframe, text = "\nHow Long has Camper Been Aware of HIV/AIDS Impacting Them? .............................................. ")

        curr.execute("SELECT Time_Camper_Known FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        behavior1 = StringVar()
        
        choices = ['less than 6 months', 'less than 1 year', 'a few years', 'always']
        option = tk.OptionMenu(DemographicSectionframe, behavior1, *choices)

        if val is not None:
            behavior1.set(val)
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateBehavior1(behavior1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Camper experiences
        label = Label(DemographicSectionframe, text = "\nExperiences of Camper .............................................................................................................. ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateBehaviorExperiances(behaviorExperiances0, behaviorExperiances1, behaviorExperiances2, behaviorExperiances3, behaviorExperiances4,
            behaviorExperiances5, behaviorExperiances6, behaviorExperiances7, behaviorExperiances8, behaviorExperiances9, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Camper_Experiences FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        #Anxiety
        behaviorExperiances0 = IntVar()
        Checkbutton(DemographicSectionframe, text="Anxiety", variable = behaviorExperiances0).grid(row = r,  column = 1, sticky = W)

        #Fear of dark
        behaviorExperiances1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Fear of dark", variable = behaviorExperiances1).grid(row = r,  column = 1, sticky = W)
 
        #Homesickness
        behaviorExperiances2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Homesickness", variable = behaviorExperiances2).grid(row = r,  column = 1, sticky = W)

        #Sleeps with night light
        behaviorExperiances3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Sleeps with night light", variable = behaviorExperiances3).grid(row = r,  column = 1, sticky = W)

        #Fights easily
        behaviorExperiances4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Fights easily", variable = behaviorExperiances4).grid(row = r,  column = 1, sticky = W)

        #School suspension due to behavior
        behaviorExperiances5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="School suspension due to behavior", variable = behaviorExperiances5).grid(row = r,  column = 1, sticky = W)

        #Bedwetting
        behaviorExperiances6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Bedwetting", variable = behaviorExperiances6).grid(row = r,  column = 1, sticky = W)

        #Sleeps with comfort item
        behaviorExperiances7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Sleeps with comfort item", variable = behaviorExperiances7).grid(row = r,  column = 1, sticky = W)

        #Hyperactivity or problems with attention
        behaviorExperiances8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Hyperactivity or problems with attention", variable = behaviorExperiances8).grid(row = r,  column = 1, sticky = W)

        #History of trauma or sexual abuse
        behaviorExperiances9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="History of trauma or sexual abuse", variable = behaviorExperiances9).grid(row = r,  column = 1, sticky = W)

        if val is not None:
            if 'Anxiety' in val:
                behaviorExperiances0.set(1)
            if 'Fear of dark' in val:
                behaviorExperiances1.set(1)
            if 'Homesickness' in val:
                behaviorExperiances2.set(1)
            if 'Sleeps with night light' in val:
                behaviorExperiances3.set(1)
            if 'Fights easily' in val:
                behaviorExperiances4.set(1)
            if 'School suspension due to behavior' in val:
                behaviorExperiances5.set(1)
            if 'Bedwetting' in val:
                behaviorExperiances6.set(1)
            if 'Sleeps with comfort item' in val:
                behaviorExperiances7.set(1)
            if 'Hyperactivity or problems with attention' in val:
                behaviorExperiances8.set(1)
            if 'History of trauma or sexual abuse' in val:
                behaviorExperiances9.set(1)

        #medication for hyperactivity
        curr.execute("SELECT Med_Hyper_AttentionProb FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nCamper Takes Medicine for Hyperactivity ................................................................................... ")
        behavior2 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = behavior2, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = behavior2, value=2)

        if val is not None:
            if val is 0:
                behavior2.set(2)
            else:
                behavior2.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateBehavior2(behavior2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #experience explanation
        curr.execute("SELECT Explanation FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nExplanation of Experiences ........................................................................................................ ")
        behavior3 = Entry(DemographicSectionframe)

        if val is not None:
            behavior3.insert(0, val)
        else:
            behavior3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateBehavior3(behavior3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        behavior3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Camper interests
        label = Label(DemographicSectionframe, text = "\nInterests of Camper ................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateBehaviorInterests(behaviorInterests0, behaviorInterests1, behaviorInterests2, behaviorInterests3, behaviorInterests4,
            behaviorInterests5, behaviorInterests6, behaviorInterests7, behaviorInterests8, behaviorInterests9,
            behaviorInterests10, behaviorInterests11, behaviorInterests12, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Camper_Interests FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        #Reading
        behaviorInterests0 = IntVar()
        Checkbutton(DemographicSectionframe, text="Reading", variable = behaviorInterests0).grid(row = r,  column = 1, sticky = W)

        #Music
        behaviorInterests1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Music", variable = behaviorInterests1).grid(row = r,  column = 1, sticky = W)
 
        #Swimming
        behaviorInterests2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Swimming", variable = behaviorInterests2).grid(row = r,  column = 1, sticky = W)
 
        #Dance
        behaviorInterests3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Dance", variable = behaviorInterests3).grid(row = r,  column = 1, sticky = W)
 
        #Sports
        behaviorInterests4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Sports", variable = behaviorInterests4).grid(row = r,  column = 1, sticky = W)
 
        #Arts/Crafts
        behaviorInterests5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Arts/Crafts", variable = behaviorInterests5).grid(row = r,  column = 1, sticky = W)
 
        #Fishing
        behaviorInterests6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Fishing", variable = behaviorInterests6).grid(row = r,  column = 1, sticky = W)
 
        #Boating
        behaviorInterests7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Boating", variable = behaviorInterests7).grid(row = r,  column = 1, sticky = W)
 
        #Archery
        behaviorInterests8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Archery", variable = behaviorInterests8).grid(row = r,  column = 1, sticky = W)
 
        #Golf
        behaviorInterests9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Golf", variable = behaviorInterests9).grid(row = r,  column = 1, sticky = W)
 
        #Bicycling
        behaviorInterests10 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Bicycling", variable = behaviorInterests10).grid(row = r,  column = 1, sticky = W)
 
        #Animals
        behaviorInterests11 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Animals", variable = behaviorInterests11).grid(row = r,  column = 1, sticky = W)
 
        #Nature
        behaviorInterests12 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Nature", variable = behaviorInterests12).grid(row = r,  column = 1, sticky = W)

        if val is not None:
            if 'Reading' in val:
                behaviorInterests0.set(1)
            if 'Music' in val:
                behaviorInterests1.set(1)
            if 'Swimming' in val:
                behaviorInterests2.set(1)
            if 'Dance' in val:
                behaviorInterests3.set(1)
            if 'Sports' in val:
                behaviorInterests4.set(1)
            if 'Arts/Crafts' in val:
                behaviorInterests5.set(1)
            if 'Fishing' in val:
                behaviorInterests6.set(1)
            if 'Boating' in val:
                behaviorInterests7.set(1)
            if 'Archery' in val:
                behaviorInterests8.set(1)
            if 'Golf' in val:
                behaviorInterests9.set(1)
            if 'Bicycling' in val:
                behaviorInterests10.set(1)
            if 'Animals' in val:
                behaviorInterests11.set(1)
            if 'Nature' in val:
                behaviorInterests12.set(1)

        #Recent major events
        curr.execute("SELECT Recent_Major_Events FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nRecent Events for Camper .......................................................................................................... ")
        behavior4 = Entry(DemographicSectionframe)

        if val is not None:
            behavior4.insert(0, val)
        else:
            behavior4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateBehavior4(behavior4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        behavior4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Medication Info ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nMEDICATION INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        curr.execute("SELECT Medication FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        medArr = curr.fetchall()

        #med 1
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 1')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 0:
            name = medArr[0][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med10 = Entry(DemographicSectionframe)
        med10.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med10, 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med11 = Entry(DemographicSectionframe)
        med11.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med11, 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med12 = Entry(DemographicSectionframe)
        med12.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med12, 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 2
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 2')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 1:
            name = medArr[1][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med20 = Entry(DemographicSectionframe)
        med20.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med20, 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med21 = Entry(DemographicSectionframe)
        med21.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med21, 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med22 = Entry(DemographicSectionframe)
        med22.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med22, 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med22.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 3
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 3')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 2:
            name = medArr[2][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med30 = Entry(DemographicSectionframe)
        med30.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med30, 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med31 = Entry(DemographicSectionframe)
        med31.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med31, 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med32 = Entry(DemographicSectionframe)
        med32.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med32, 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med32.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 4
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 4')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 3:
            name = medArr[3][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med40 = Entry(DemographicSectionframe)
        med40.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med40, 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med40.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med41 = Entry(DemographicSectionframe)
        med41.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med41, 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med42 = Entry(DemographicSectionframe)
        med42.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med42, 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med42.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 5
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 5')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 4:
            name = medArr[4][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med50 = Entry(DemographicSectionframe)
        med50.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med50, 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med50.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med51 = Entry(DemographicSectionframe)
        med51.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med51, 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med52 = Entry(DemographicSectionframe)
        med52.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med52, 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med52.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 6
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 6')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 5:
            name = medArr[5][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med60 = Entry(DemographicSectionframe)
        med60.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMe0(med60, 6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med60.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med61 = Entry(DemographicSectionframe)
        med61.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med61, 6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med62 = Entry(DemographicSectionframe)
        med62.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med62, 6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med62.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 7
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 7')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 6:
            name = medArr[6][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med70 = Entry(DemographicSectionframe)
        med70.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med70, 7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med70.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med71 = Entry(DemographicSectionframe)
        med71.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med71, 7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med71.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med72 = Entry(DemographicSectionframe)
        med72.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med72, 7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med72.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 8
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 8')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 7:
            name = medArr[7][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med80 = Entry(DemographicSectionframe)
        med80.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med80, 8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med80.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med81 = Entry(DemographicSectionframe)
        med81.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med81, 8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med81.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med82 = Entry(DemographicSectionframe)
        med82.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med82, 8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med82.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 9
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 9')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 8:
            name = medArr[8][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med90 = Entry(DemographicSectionframe)
        med90.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med90, 9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med90.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med91 = Entry(DemographicSectionframe)
        med91.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med91, 9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med91.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med92 = Entry(DemographicSectionframe)
        med92.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med92, 9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med92.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 10
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 10')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 9:
            name = medArr[9][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med100 = Entry(DemographicSectionframe)
        med100.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med100, 10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med100.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med101 = Entry(DemographicSectionframe)
        med101.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med101, 10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med101.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med102 = Entry(DemographicSectionframe)
        med102.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med102, 10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med102.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 11
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 11')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 10:
            name = medArr[10][0]
            
            curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med110 = Entry(DemographicSectionframe)
        med110.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed0(med110, 11, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med110.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med111 = Entry(DemographicSectionframe)
        med111.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed1(med111, 11, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med111.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med112 = Entry(DemographicSectionframe)
        med112.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMed2(med112, 11, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        med112.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Preliminary signatures ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nPARENTAL CONSENT INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #parent camper contract
        curr.execute("SELECT Parent_Camper_Contract FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nParent Camper Contract ............................................................................................................. ")
        parentSig0 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig0, value=2)

        if val is not None:
            if val is 0:
                parentSig0.set(2)
            else:
                parentSig0.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateParentSig0(parentSig0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #participation release
        curr.execute("SELECT Partcipation_Consent_Liability_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nParticipation Consent/Liability Release/Disputes Form Signed .................................................... ")
        parentSig1 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig1, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig1, value=2)

        if val is not None:
            if val is 0:
                parentSig1.set(2)
            else:
                parentSig1.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateParentSig1(parentSig1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Media release
        curr.execute("SELECT Media_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMedia Release Form Signed ........................................................................................................ ")
        parentSig2 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig2, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig2, value=2)

        if val is not None:
            if val is 0:
                parentSig2.set(2)
            else:
                parentSig2.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateParentSig2(parentSig2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #hiv ed waiver
        curr.execute("SELECT Camper_HIV_Education FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nHIV Education Waiver Signed ...................................................................................................... ")
        parentSig3 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig3, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig3, value=2)

        if val is not None:
            if val is 0:
                parentSig3.set(2)
            else:
                parentSig3.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateParentSig3(parentSig3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #camp rules form signed
        curr.execute("SELECT Camp_Twin_Lakes_Rules FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nRules Acknowledgement Form Signed ......................................................................................... ")
        parentSig4 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig4, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig4, value=2)

        if val is not None:
            if val is 0:
                parentSig4.set(2)
            else:
                parentSig4.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateParentSig4(parentSig4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #parental consent and release
        curr.execute("SELECT Parental_Consent_And_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nParental Consent and Release Form Signed ................................................................................. ")
        parentSig5 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig5, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig5, value=2)

        if val is not None:
            if val is 0:
                parentSig5.set(2)
            else:
                parentSig5.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateParentSig5(parentSig5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#
#Medical provider sections
#

#medical history ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nMEDICAL INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        curr.execute("SELECT Diagnosis FROM Med_Hist_Diagnosis WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        diagnosisArr = curr.fetchall()

        #medical diagnosises 1
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 1 ................................................................................................................... ")
        medProvider0 = Entry(DemographicSectionframe)

        if len(diagnosisArr) > 0:
            medProvider0.insert(0, diagnosisArr[0][0])
        else:
            medProvider0.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDiagnosis(medProvider0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvider0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #medical diagnosises 2
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 2 ................................................................................................................... ")
        medProvider1 = Entry(DemographicSectionframe)

        if len(diagnosisArr) > 1:
            medProvider1.insert(0, diagnosisArr[1][0])
        else:
            medProvider1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDiagnosis(medProvider1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvider1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #medical diagnosises 3
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 3 ................................................................................................................... ")
        medProvider2 = Entry(DemographicSectionframe)

        if len(diagnosisArr) > 2:
            medProvider2.insert(0, diagnosisArr[2][0])
        else:
            medProvider2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDiagnosis(medProvider2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvider2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #medical diagnosises 4
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 4 ................................................................................................................... ")
        medProvider3 = Entry(DemographicSectionframe)

        if len(diagnosisArr) > 3:
            medProvider3.insert(0, diagnosisArr[3][0])
        else:
            medProvider3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDiagnosis(medProvider3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvider3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #medical diagnosises 5
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 5 ................................................................................................................... ")
        medProvider4 = Entry(DemographicSectionframe)

        if len(diagnosisArr) > 4:
            medProvider4.insert(0, diagnosisArr[4][0])
        else:
            medProvider4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateDiagnosis(medProvider4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvider4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #management
        curr.execute("SELECT Management FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMedical Management Comments ................................................................................................ ")
        medProvider5 = Entry(DemographicSectionframe)

        if val is not None:
            medProvider5.insert(0, val)
        else:
            medProvider5.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvider5(medProvider5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvider5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #nutritional supplements
        curr.execute("SELECT Nutritional_Supplements FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nNutritional Supplements Taken? ................................................................................................. ")
        medProvider6 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = medProvider6, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = medProvider6, value=2)

        if val is not None:
            if val is 0:
                medProvider6.set(2)
            else:
                medProvider6.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvider6(medProvider6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #supplement comment
        curr.execute("SELECT Feeding_Care FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nFeeding Care Comments ............................................................................................................ ")
        medProvider7 = Entry(DemographicSectionframe)

        if val is not None:
            medProvider7.insert(0, val)
        else:
            medProvider7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvider7(medProvider7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvider7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #formula type
        label = Label(DemographicSectionframe, text = "\nFormula Type ............................................................................................................................. ")

        curr.execute("SELECT Formula_Type FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        medProvider8 = StringVar()
        choices = ['Oral', 'G-tube', 'N-G tube']
        option = tk.OptionMenu(DemographicSectionframe, medProvider8, *choices)

        if val is not None:
            medProvider8.set(val)
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvider8(medProvider8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #allergies
        #FOOD
        label = Label(DemographicSectionframe, text = "\nFood Allergy")
        r = r+1
        label.grid(row = r, column = 0)

        curr.execute("SELECT Allergy FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Type = 'Food';", (id, date,))
        allergyArr = curr.fetchall()

        #allergy1
        if len(allergyArr) > 0:
            allergy = allergyArr[0][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Food';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 1 .................................................................................................................................... ")
        foodAllergy1 = Entry(DemographicSectionframe)
        foodAllergy1.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(foodAllergy1, 'Food', 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodAllergy1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 1 .................................................................................................................................. ")
        foodReaction1 = Entry(DemographicSectionframe)
        foodReaction1.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(foodReaction1, 'Food', 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodReaction1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy2
        if len(allergyArr) > 1:
            allergy = allergyArr[1][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Food';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 2 .................................................................................................................................... ")
        foodAllergy2 = Entry(DemographicSectionframe)
        foodAllergy2.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(foodAllergy2, 'Food', 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodAllergy2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 2 .................................................................................................................................. ")
        foodReaction2 = Entry(DemographicSectionframe)
        foodReaction2.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(foodReaction2, 'Food', 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodReaction2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy3
        if len(allergyArr) > 2:
            allergy = allergyArr[2][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Food';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 3 .................................................................................................................................... ")
        foodAllergy3 = Entry(DemographicSectionframe)
        foodAllergy3.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(foodAllergy3, 'Food', 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodAllergy3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 3 .................................................................................................................................. ")
        foodReaction3 = Entry(DemographicSectionframe)
        foodReaction3.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(foodReaction3, 'Food', 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodReaction3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy4
        if len(allergyArr) > 3:
            allergy = allergyArr[3][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Food';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 4 .................................................................................................................................... ")
        foodAllergy4 = Entry(DemographicSectionframe)
        foodAllergy4.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(foodAllergy4, 'Food', 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodAllergy4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 4 .................................................................................................................................. ")
        foodReaction4 = Entry(DemographicSectionframe)
        foodReaction4.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(foodReaction4, 'Food', 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodReaction4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy5
        if len(allergyArr) > 4:
            allergy = allergyArr[4][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Food';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 5 .................................................................................................................................... ")
        foodAllergy5 = Entry(DemographicSectionframe)
        foodAllergy5.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(foodAllergy5, 'Food', 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodAllergy5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 5 .................................................................................................................................. ")
        foodReaction5 = Entry(DemographicSectionframe)
        foodReaction5.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(foodReaction5, 'Food', 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        foodReaction5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION
        label = Label(DemographicSectionframe, text = "\nMedication Allergy")
        r = r+1
        label.grid(row = r, column = 0)

        curr.execute("SELECT Allergy FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Type = 'Medication';", (id, date,))
        allergyArr = curr.fetchall()

        #allergy1
        if len(allergyArr) > 0:
            allergy = allergyArr[0][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Medication';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 1 .................................................................................................................................... ")
        medAllergy1 = Entry(DemographicSectionframe)
        medAllergy1.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(medAllergy1, 'Medication', 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medAllergy1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 1 .................................................................................................................................. ")
        medReaction1 = Entry(DemographicSectionframe)
        medReaction1.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(medReaction1, 'Medication', 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medReaction1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy2
        if len(allergyArr) > 1:
            allergy = allergyArr[1][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Medication';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 2 .................................................................................................................................... ")
        medAllergy2 = Entry(DemographicSectionframe)
        medAllergy2.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(medAllergy2, 'Medication', 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medAllergy2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 2 .................................................................................................................................. ")
        medReaction2 = Entry(DemographicSectionframe)
        medReaction2.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(medReaction2, 'Medication', 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medReaction2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy3
        if len(allergyArr) > 2:
            allergy = allergyArr[2][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Medication';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 3 .................................................................................................................................... ")
        medAllergy3 = Entry(DemographicSectionframe)
        medAllergy3.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(medAllergy3, 'Medication', 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medAllergy3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 3 .................................................................................................................................. ")
        medReaction3 = Entry(DemographicSectionframe)
        medReaction3.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(medReaction3, 'Medication', 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medReaction3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy4
        if len(allergyArr) > 3:
            allergy = allergyArr[3][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Medication';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 4 .................................................................................................................................... ")
        medAllergy4 = Entry(DemographicSectionframe)
        medAllergy4.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(medAllergy4, 'Medication', 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medAllergy4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 4 .................................................................................................................................. ")
        medReaction4 = Entry(DemographicSectionframe)
        medReaction4.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(medReaction4, 'Medication', 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medReaction4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy5
        if len(allergyArr) > 4:
            allergy = allergyArr[4][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Medication';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 5 .................................................................................................................................... ")
        medAllergy5 = Entry(DemographicSectionframe)
        medAllergy5.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(medAllergy5, 'Medication', 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medAllergy5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 5 .................................................................................................................................. ")
        medReaction5 = Entry(DemographicSectionframe)
        medReaction5.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(medReaction5, 'Medication', 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medReaction5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #ENVIRONMENTAL
        label = Label(DemographicSectionframe, text = "\nEnvironmental Allergy")
        r = r+1
        label.grid(row = r, column = 0)

        curr.execute("SELECT Allergy FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Type = 'Environmental';", (id, date,))
        allergyArr = curr.fetchall()

        #allergy1
        if len(allergyArr) > 0:
            allergy = allergyArr[0][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Environmental';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 1 .................................................................................................................................... ")
        envAllergy1 = Entry(DemographicSectionframe)
        envAllergy1.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(envAllergy1, 'Environmental', 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envAllergy1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 1 .................................................................................................................................. ")
        envReaction1 = Entry(DemographicSectionframe)
        envReaction1.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(envReaction1, 'Environmental', 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envReaction1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy2
        if len(allergyArr) > 1:
            allergy = allergyArr[1][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Environmental';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 2 .................................................................................................................................... ")
        envAllergy2 = Entry(DemographicSectionframe)
        envAllergy2.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(envAllergy2, 'Environmental', 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envAllergy2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 2 .................................................................................................................................. ")
        envReaction2 = Entry(DemographicSectionframe)
        envReaction2.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(envReaction2, 'Environmental', 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envReaction2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy3
        if len(allergyArr) > 2:
            allergy = allergyArr[2][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Environmental';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 3 .................................................................................................................................... ")
        envAllergy3 = Entry(DemographicSectionframe)
        envAllergy3.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(envAllergy3, 'Environmental', 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envAllergy3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 3 .................................................................................................................................. ")
        envReaction3 = Entry(DemographicSectionframe)
        envReaction3.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(envReaction3, 'Environmental', 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envReaction3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy4
        if len(allergyArr) > 3:
            allergy = allergyArr[3][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Environmental';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 4 .................................................................................................................................... ")
        envAllergy4 = Entry(DemographicSectionframe)
        envAllergy4.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(envAllergy4, 'Environmental', 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envAllergy4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 4 .................................................................................................................................. ")
        envReaction4 = Entry(DemographicSectionframe)
        envReaction4.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(envReaction4, 'Environmental', 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envReaction4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy5
        if len(allergyArr) > 4:
            allergy = allergyArr[4][0]
            
            curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s AND Type = 'Environmental';", (id, date, allergy,))
            reaction = curr.fetchall()[0][0]
            if reaction is None:
                reaction = 'Unanswered'
        else:
            allergy = 'Unanswered'
            reaction = 'Unanswered'

        #allergic to
        label = Label(DemographicSectionframe, text = "\nAllergy 5 .................................................................................................................................... ")
        envAllergy5 = Entry(DemographicSectionframe)
        envAllergy5.insert(0, allergy)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistAllergy(envAllergy5, 'Environmental', 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envAllergy5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction
        label = Label(DemographicSectionframe, text = "Reaction 5 .................................................................................................................................. ")
        envReaction5 = Entry(DemographicSectionframe)
        envReaction5.insert(0, reaction)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedHistReaction(envReaction5, 'Environmental', 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        envReaction5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#physical ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nMOST RECENT PHYSICAL INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #date completed
        curr.execute("SELECT Date_Completed FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nDate Completed (YYY-MM-DD) ................................................................................................... ")
        physical0 = Entry(DemographicSectionframe)

        if val is not None:
            physical0.insert(0, val)
        else:
            physical0.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical0(physical0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #height
        curr.execute("SELECT Height FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nHeight ........................................................................................................................................ ")
        physical1 = Entry(DemographicSectionframe)

        if val is not None:
            physical1.insert(0, val)
        else:
            physical1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical1(physical1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #weight
        curr.execute("SELECT Weight FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nWeight (lb) ................................................................................................................................. ")
        physical2 = Entry(DemographicSectionframe)

        if val is not None:
            physical2.insert(0, val)
        else:
            physical2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical2(physical2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #pulse
        curr.execute("SELECT Pulse FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nPulse (bpm) ................................................................................................................................ ")
        physical3 = Entry(DemographicSectionframe)

        if val is not None:
            physical3.insert(0, val)
        else:
            physical3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical3(physical3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #respirations
        curr.execute("SELECT Resperations FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nRespirations ............................................................................................................................... ")
        physical4 = Entry(DemographicSectionframe)

        if val is not None:
            physical4.insert(0, val)
        else:
            physical4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical4(physical4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #bp
        curr.execute("SELECT Blood_Pressure FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nBlood Pressure ............................................................................................................................... ")
        physical5 = Entry(DemographicSectionframe)

        if val is not None:
            physical5.insert(0, val)
        else:
            physical5.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical5(physical5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HEENT
        curr.execute("SELECT HEENT FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nHEENT ........................................................................................................................................ ")
        physical6 = Entry(DemographicSectionframe)

        if val is not None:
            physical6.insert(0, val)
        else:
            physical6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical6(physical6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #skin
        curr.execute("SELECT Skin FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nSkin ............................................................................................................................................ ")
        physical7 = Entry(DemographicSectionframe)

        if val is not None:
            physical7.insert(0, val)
        else:
            physical7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical7(physical7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #cardio
        curr.execute("SELECT Cardiovascular FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nCardiovascular ........................................................................................................................... ")
        physical8 = Entry(DemographicSectionframe)

        if val is not None:
            physical8.insert(0, val)
        else:
            physical8.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical8(physical8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gu gyn
        curr.execute("SELECT GU_GYN FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nGU/GYN ...................................................................................................................................... ")
        physical9 = Entry(DemographicSectionframe)

        if val is not None:
            physical9.insert(0, val)
        else:
            physical9.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical9(physical9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #pulmonary
        curr.execute("SELECT Pulmonary FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nPulmonary .................................................................................................................................. ")
        physical10 = Entry(DemographicSectionframe)

        if val is not None:
            physical10.insert(0, val)
        else:
            physical10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical10(physical10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #g ha
        curr.execute("SELECT Glasses_HearingAids_PE FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nGlasses/Contacts/Hearing Aids/PE tubes .................................................................................... ")
        physical11 = Entry(DemographicSectionframe)

        if val is not None:
            physical11.insert(0, val)
        else:
            physical11.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical11(physical11, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Abdomen
        curr.execute("SELECT Abdomen FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nAbdomen ................................................................................................................................... ")
        physical12 = Entry(DemographicSectionframe)

        if val is not None:
            physical12.insert(0, val)
        else:
            physical12.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical12(physical12, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #LN
        curr.execute("SELECT Lymph_Nodes FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nLymph Nodes ............................................................................................................................. ")
        physical13 = Entry(DemographicSectionframe)

        if val is not None:
            physical13.insert(0, val)
        else:
            physical13.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical13(physical13, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Extremities
        curr.execute("SELECT Extremities FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nExtremities ................................................................................................................................. ")
        physical14 = Entry(DemographicSectionframe)

        if val is not None:
            physical14.insert(0, val)
        else:
            physical14.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical14(physical14, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #spine
        curr.execute("SELECT Spine FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nSpine ......................................................................................................................................... ")
        physical15 = Entry(DemographicSectionframe)

        if val is not None:
            physical15.insert(0, val)
        else:
            physical15.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical15(physical15, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Misc
        curr.execute("SELECT Miscellaneous FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMiscellaneous ............................................................................................................................ ")
        physical16 = Entry(DemographicSectionframe)

        if val is not None:
            physical16.insert(0, val)
        else:
            physical16.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical16(physical16, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #comm
        curr.execute("SELECT Comments FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nComments .................................................................................................................................. ")
        physical17 = Entry(DemographicSectionframe)

        if val is not None:
            physical17.insert(0, val)
        else:
            physical17.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updatePhysical17(physical17, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        physical17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#cognative development level ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nCOGNITIVE DEVELOPMENT INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #development level
        label = Label(DemographicSectionframe, text = "\nDevelopment Level ..................................................................................................................... ")

        curr.execute("SELECT Development_Level FROM Cognitive_Development_Level WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        cogDev0 = StringVar()
        choices = ['Age Appropriate', 'Mild Delay', 'Moderate Delay', 'Severe Delay']
        option = tk.OptionMenu(DemographicSectionframe, cogDev0, *choices)

        if val is not None:
            cogDev0.set(val)
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateCogDev0(cogDev0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #other info
        curr.execute("SELECT Other_Psychosocial_Information FROM Cognitive_Development_Level WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nOther Psychosocoal Information ................................................................................................. ")
        cogDev1 = Entry(DemographicSectionframe)

        if val is not None:
            cogDev1.insert(0, val)
        else:
            cogDev1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateCogDev1(cogDev1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        cogDev1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Varicella screening ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nVARICELLA SCREENING")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #Two_Doses
        curr.execute("SELECT Two_Doses FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nTwo doses of vaccine ................................................................................................................. ")
        varicella0 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = varicella0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = varicella0, value=2)

        if val is not None:
            if val is 0:
                varicella0.set(2)
            else:
                varicella0.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateVaricella0(varicella0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Chicken_Pox
        curr.execute("SELECT Chicken_Pox FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nHistory of chicken pox or shingles? ............................................................................................ ")
        varicella1 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = varicella1, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = varicella1, value=2)

        if val is not None:
            if val is 0:
                varicella1.set(2)
            else:
                varicella1.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateVaricella1(varicella1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Chicken_Pox_Date
        curr.execute("SELECT Chicken_Pox_Date FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nChicken pox/ shingles date (YYYY-MM-DD) ................................................................................ ")
        varicella2 = Entry(DemographicSectionframe)

        if val is not None:
            varicella2.insert(0, val)
        else:
            varicella2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateVaricella2(varicella2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        varicella2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Varicella_Antibody
        curr.execute("SELECT Varicella_Antibody FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nVaricella antibody ....................................................................................................................... ")
        varicella3 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = varicella3, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = varicella3, value=2)

        if val is not None:
            if val is 0:
                varicella3.set(2)
            else:
                varicella3.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateVaricella3(varicella3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Varicella_Antibody_Date
        curr.execute("SELECT Varicella_Antibody_Date FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nVaricella antibody date (YYYY-MM-DD) ...................................................................................... ")
        varicella4 = Entry(DemographicSectionframe)

        if val is not None:
            varicella4.insert(0, val)
        else:
            varicella4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateVaricella4(varicella4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        varicella4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#tuberculosis screening ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nTUBERCULOSIS SCREENING")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #Tuberculin Skin Test
        label = Label(DemographicSectionframe, text = "\nTuberculin Skin Test")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #date
        curr.execute("SELECT Date_Screened FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Tuberculin Skin Test';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ ")
        tuberculosis10 = Entry(DemographicSectionframe)

        if val is not None:
            tuberculosis10.insert(0, val)
        else:
            tuberculosis10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateTuberculosis1(tuberculosis10, 'Tuberculin Skin Test', id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        tuberculosis10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Result
        curr.execute("SELECT Result FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Tuberculin Skin Test';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... ")
        tuberculosis11 = Entry(DemographicSectionframe)

        if val is not None:
            tuberculosis11.insert(0, val)
        else:
            tuberculosis11.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateTuberculosis2(tuberculosis11, 'Tuberculin Skin Test', id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        tuberculosis11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        labelContactsSection.config(font=("Helvetica", 20))

        #Quantiferon Testing
        label = Label(DemographicSectionframe, text = "\nQuantiferon Testing")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #date
        curr.execute("SELECT Date_Screened FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Quantiferon Testing';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ ")
        tuberculosis20 = Entry(DemographicSectionframe)

        if val is not None:
            tuberculosis20.insert(0, val)
        else:
            tuberculosis20.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateTuberculosis1(tuberculosis20, 'Quantiferon Testing', id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        tuberculosis20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Result
        curr.execute("SELECT Result FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Quantiferon Testing';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... ")
        tuberculosis21 = Entry(DemographicSectionframe)

        if val is not None:
            tuberculosis21.insert(0, val)
        else:
            tuberculosis21.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateTuberculosis2(tuberculosis21, 'Quantiferon Testing', id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        tuberculosis21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Chest X-ray
        label = Label(DemographicSectionframe, text = "\nChest X-ray")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #date
        curr.execute("SELECT Date_Screened FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Chest X-ray';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ ")
        tuberculosis30 = Entry(DemographicSectionframe)

        if val is not None:
            tuberculosis30.insert(0, val)
        else:
            tuberculosis30.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateTuberculosis1(tuberculosis30, 'Chest X-ray', id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        tuberculosis30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Result
        curr.execute("SELECT Result FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Chest X-ray';", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... ")
        tuberculosis31 = Entry(DemographicSectionframe)

        if val is not None:
            tuberculosis31.insert(0, val)
        else:
            tuberculosis31.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateTuberculosis2(tuberculosis31, 'Chest X-ray', id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        tuberculosis31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Restrictions_And_Recommendations ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nRESTRICTIONS AND RECOMMENDATIONS")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #Restrictions and recommendations
        curr.execute("SELECT Restrictions_And_Recommendations FROM Medical_Care_Provider WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nRestrictions and recommendations ............................................................................................ ")
        restrictionsRec = Entry(DemographicSectionframe)

        if val is not None:
            restrictionsRec.insert(0, val)
        else:
            restrictionsRec.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateRestrictionsRec(restrictionsRec, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        restrictionsRec.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#medcare provider medications ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER MEDICATION INFORMATION")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        curr.execute("SELECT Medication_Name FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        medArr = curr.fetchall()

        #med 1
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 1')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 0:
            name = medArr[0][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed11 = Entry(DemographicSectionframe)
        medProMed11.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed11, 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed12 = Entry(DemographicSectionframe)
        medProMed12.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed12, 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed13 = Entry(DemographicSectionframe)
        medProMed13.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed13, 1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 2
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 2')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 1:
            name = medArr[1][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed21 = Entry(DemographicSectionframe)
        medProMed21.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed21, 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed22 = Entry(DemographicSectionframe)
        medProMed22.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed22, 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed22.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed23 = Entry(DemographicSectionframe)
        medProMed23.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed23, 2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 3
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 3')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 2:
            name = medArr[2][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed31 = Entry(DemographicSectionframe)
        medProMed31.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed31, 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed32 = Entry(DemographicSectionframe)
        medProMed32.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed32, 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed32.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed33 = Entry(DemographicSectionframe)
        medProMed33.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed33, 3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed33.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 4
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 4')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 3:
            name = medArr[3][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed41 = Entry(DemographicSectionframe)
        medProMed41.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed41, 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed42 = Entry(DemographicSectionframe)
        medProMed42.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed42, 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed42.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed43 = Entry(DemographicSectionframe)
        medProMed43.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed43, 4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed43.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 5
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 5')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 4:
            name = medArr[4][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed51 = Entry(DemographicSectionframe)
        medProMed51.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed51, 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed52 = Entry(DemographicSectionframe)
        medProMed52.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed52, 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed52.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed53 = Entry(DemographicSectionframe)
        medProMed53.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed53, 5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed53.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 6
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 6')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 5:
            name = medArr[5][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed61 = Entry(DemographicSectionframe)
        medProMed61.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed61, 6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed62 = Entry(DemographicSectionframe)
        medProMed62.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed62, 6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed62.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed63 = Entry(DemographicSectionframe)
        medProMed63.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed63, 6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed63.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 7
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 7')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 6:
            name = medArr[6][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed71 = Entry(DemographicSectionframe)
        medProMed71.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed71, 7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed71.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed72 = Entry(DemographicSectionframe)
        medProMed72.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed72, 7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed72.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed73 = Entry(DemographicSectionframe)
        medProMed73.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed73, 7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed73.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 8
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 8')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 7:
            name = medArr[7][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed81 = Entry(DemographicSectionframe)
        medProMed81.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed81, 8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed81.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed82 = Entry(DemographicSectionframe)
        medProMed82.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed82, 8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed82.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed83 = Entry(DemographicSectionframe)
        medProMed83.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed83, 8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed83.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 9
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 9')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 8:
            name = medArr[8][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed91 = Entry(DemographicSectionframe)
        medProMed91.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed91, 9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed91.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed92 = Entry(DemographicSectionframe)
        medProMed92.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed92, 9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed92.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed93 = Entry(DemographicSectionframe)
        medProMed93.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed93, 9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed93.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #MEDICATION 10
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 10')
        label.grid(row = r, column = 0, sticky = 'w')

        if len(medArr) > 9:
            name = medArr[9][0]
            
            curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            amount = curr.fetchall()[0][0]
            if amount is None:
                amount = 'Unanswered'

            curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, name,))
            frequency = curr.fetchall()[0][0]
            if frequency is None:
                frequency = 'Unanswered'
        else:
            name = 'Unanswered'
            amount = 'Unanswered'
            frequency = 'Unanswered'

        #taken
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed101 = Entry(DemographicSectionframe)
        medProMed101.insert(0, name)              
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed1(medProMed101, 10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed101.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed102 = Entry(DemographicSectionframe)
        medProMed102.insert(0, amount)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed2(medProMed102, 10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed102.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed103 = Entry(DemographicSectionframe)
        medProMed103.insert(0, frequency)
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProMed3(medProMed103, 10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProMed103.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#medcare provider verification statement ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER VERIFICATION STATEMENT")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #signature
        curr.execute("SELECT Signature FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nSignature Provided? ................................................................................................................... ")
        medProvVerState0 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = medProvVerState0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = medProvVerState0, value=2)

        if val is not None:
            if val is 0:
                medProvVerState0.set(2)
            else:
                medProvVerState0.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState0(medProvVerState0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #signature date
        curr.execute("SELECT Sig_Date FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nDate (YYYY-MM-DD) .................................................................................................................. ")
        medProvVerState1 = Entry(DemographicSectionframe)

        if val is not None:
            medProvVerState1.insert(0, val)
        else:
            medProvVerState1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState1(medProvVerState1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvVerState1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #name
        curr.execute("SELECT Name FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nExaminer Name .......................................................................................................................... ")
        medProvVerState2 = Entry(DemographicSectionframe)

        if val is not None:
            medProvVerState2.insert(0, val)
        else:
            medProvVerState2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState2(medProvVerState2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvVerState2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        curr.execute("SELECT Address_Street FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nAddress Street ........................................................................................................................... ")
        medProvVerState3 = Entry(DemographicSectionframe)

        if val is not None:
            medProvVerState3.insert(0, val)
        else:
            medProvVerState3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState3(medProvVerState3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvVerState3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        curr.execute("SELECT Address_City FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nAddress City .............................................................................................................................. ")
        medProvVerState4 = Entry(DemographicSectionframe)

        if val is not None:
            medProvVerState4.insert(0, val)
        else:
            medProvVerState4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState4(medProvVerState4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvVerState4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address state
        curr.execute("SELECT Address_State FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nAddress State ............................................................................................................................ ")
        medProvVerState5 = Entry(DemographicSectionframe)

        if val is not None:
            medProvVerState5.insert(0, val)
        else:
            medProvVerState5.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState5(medProvVerState5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvVerState5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        curr.execute("SELECT Address_Zip FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nAddress Zipcode ........................................................................................................................ ")
        medProvVerState6 = Entry(DemographicSectionframe)

        if val is not None:
            medProvVerState6.insert(0, val)
        else:
            medProvVerState6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState6(medProvVerState6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvVerState6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #phone
        curr.execute("SELECT Phone FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nPhone ........................................................................................................................................ ")
        medProvVerState7 = Entry(DemographicSectionframe)

        if val is not None:
            medProvVerState7.insert(0, val)
        else:
            medProvVerState7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState7(medProvVerState7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvVerState7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #emergency contact
        curr.execute("SELECT Emergency_Contact FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nEmergency Contact .................................................................................................................... ")
        medProvVerState8 = Entry(DemographicSectionframe)

        if val is not None:
            medProvVerState8.insert(0, val)
        else:
            medProvVerState8.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateMedProvVerState8(medProvVerState8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        medProvVerState8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#
#HIV provider sections
#

#health history ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nHEALTH HISTORY INFORMATION FROM HIV PROVIDER")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #surgical history
        curr.execute("SELECT Major_Surgical_History FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nMajor Surgical History ................................................................................................................ ")
        healthHistory0 = Entry(DemographicSectionframe)

        if val is not None:
            healthHistory0.insert(0, val)
        else:
            healthHistory0.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateHealthHistory0(healthHistory0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        healthHistory0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #health history
        label = Label(DemographicSectionframe, text = "\nHealth History ............................................................................................................................ ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateHealthHistory1(healthHistory1, healthHistory2, healthHistory3, healthHistory4, healthHistory5,
            healthHistory6, healthHistory7, healthHistory8, healthHistory9, healthHistory10, healthHistory11, healthHistory12, healthHistory13, healthHistory14, healthHistory15, healthHistory16, healthHistory17,
            healthHistory18, healthHistory19, id, date))
        buttonUpdate.grid(row = r, column = 2)

        curr.execute("SELECT Health_History FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        #HIV
        healthHistory1 = IntVar()
        Checkbutton(DemographicSectionframe, text="HIV", variable = healthHistory1).grid(row = r,  column = 1, sticky = W)

        #Hepatitis B
        healthHistory2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Hepatitis B", variable = healthHistory2).grid(row = r,  column = 1, sticky = W)
 
        #Hepatitis C
        healthHistory3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Hepatitis C", variable = healthHistory3).grid(row = r,  column = 1, sticky = W)
 
        #Poor growth
        healthHistory4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Poor growth", variable = healthHistory4).grid(row = r,  column = 1, sticky = W)
 
        #Bleeding disorders
        healthHistory5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Bleeding disorders", variable = healthHistory5).grid(row = r,  column = 1, sticky = W)
 
        #Asthma
        healthHistory6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Asthma", variable = healthHistory6).grid(row = r,  column = 1, sticky = W)
 
        #Pulmonary Disease
        healthHistory7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Pulmonary Disease", variable = healthHistory7).grid(row = r,  column = 1, sticky = W)

        #Chronic Cough
        healthHistory8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Chronic Cough", variable = healthHistory8).grid(row = r,  column = 1, sticky = W)
 
        #ADD or ADHD
        healthHistory9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="ADD or ADHD", variable = healthHistory9).grid(row = r,  column = 1, sticky = W)
  
        #Renal Disease
        healthHistory10 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Renal Disease", variable = healthHistory10).grid(row = r,  column = 1, sticky = W)
   
        #Sickle Cell disease
        healthHistory11 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Sickle Cell disease", variable = healthHistory11).grid(row = r,  column = 1, sticky = W)
   
        #Congenital Heart Disease
        healthHistory12 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Congenital Heart Disease", variable = healthHistory12).grid(row = r,  column = 1, sticky = W)
   
        #Hypertension
        healthHistory13 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Hypertension", variable = healthHistory13).grid(row = r,  column = 1, sticky = W)
   
        #Cryptosporidium
        healthHistory14 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Cryptosporidium", variable = healthHistory14).grid(row = r,  column = 1, sticky = W)
   
        #Chronic diarrhea
        healthHistory15 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Chronic diarrhea", variable = healthHistory15).grid(row = r,  column = 1, sticky = W)
   
        #Seizures
        healthHistory16 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Seizures", variable = healthHistory16).grid(row = r,  column = 1, sticky = W)
   
        #Diabetes
        healthHistory17 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Diabetes", variable = healthHistory17).grid(row = r,  column = 1, sticky = W)
   
        #Other
        healthHistory18 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text="Other", variable = healthHistory18).grid(row = r,  column = 1, sticky = W)
 
        if val is not None:
            if 'HIV' in val:
                healthHistory1.set(1)
            if 'Hepatitis B' in val:
                healthHistory2.set(1)
            if 'Hepatitis C' in val:
                healthHistory3.set(1)
            if 'Poor growth' in val:
                healthHistory4.set(1)
            if 'Bleeding disorders' in val:
                healthHistory5.set(1)
            if 'Asthma' in val:
                healthHistory6.set(1)
            if 'Pulmonary Disease' in val:
                healthHistory7.set(1)
            if 'Chronic Cough' in val:
                healthHistory8.set(1)
            if 'ADD or ADHD' in val:
                healthHistory9.set(1)
            if 'Renal Disease' in val:
                healthHistory10.set(1)
            if 'Sickle Cell disease' in val:
                healthHistory11.set(1)
            if 'Congenital Heart Disease' in val:
                healthHistory12.set(1)
            if 'Hypertension' in val:
                healthHistory13.set(1)
            if 'Cryptosporidium' in val:
                healthHistory14.set(1)
            if 'Chronic diarrhea' in val:
                healthHistory15.set(1)
            if 'Seizures' in val:
                healthHistory16.set(1)
            if 'Diabetes' in val:
                healthHistory17.set(1)
            if 'Other' in val:
                healthHistory18.set(1)

        #If other
        curr.execute("SELECT Other FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        healthHistory19 = Entry(DemographicSectionframe, width = 14)
        if val is not None:
            healthHistory19.insert(0, val)
        else:
            healthHistory19.insert(0, 'Unanswered')

        healthHistory19.grid(row = r, column = 1, sticky = E)

        #history of noncompliance
        curr.execute("SELECT History_of_Noncompliance FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nHistory of Noncompliance? ......................................................................................................... ")
        healthHistory20 = IntVar()

        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = healthHistory20, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = healthHistory20, value=2)

        if val is not None:
            if val is 0:
                healthHistory20.set(2)
            else:
                healthHistory20.set(1)
 
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateHealthHistory2(healthHistory20, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #explanation
        curr.execute("SELECT Explanation FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nExplanation of Noncompliance .................................................................................................... ")
        healthHistory21 = Entry(DemographicSectionframe)

        if val is not None:
            healthHistory21.insert(0, val)
        else:
            healthHistory21.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateHealthHistory3(healthHistory21, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        healthHistory21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#lab data ************************************************************************************************************************
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nLAB DATA")
        r = r+1
        labelContactsSection.grid(row = r, columnspan = 2)
        labelContactsSection.config(font=("Helvetica", 20))

        #lab1 date
        curr.execute("SELECT Lab1_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nDate of First Lab Examination (YYYY-MM-DD) ............................................................................ ")
        lab0 = Entry(DemographicSectionframe)

        if val is not None:
            lab0.insert(0, val)
        else:
            lab0.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab0(lab0, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab1 wbc
        curr.execute("SELECT Lab1_WBC FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "White Blood Cell Count .............................................................................................................. ")
        lab1 = Entry(DemographicSectionframe)

        if val is not None:
            lab1.insert(0, val)
        else:
            lab1.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab1(lab1, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab1 wbc
        curr.execute("SELECT Lab1_HGB FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Hemoglobin Level ....................................................................................................................... ")
        lab2 = Entry(DemographicSectionframe)

        if val is not None:
            lab2.insert(0, val)
        else:
            lab2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab2(lab2, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab1 hct
        curr.execute("SELECT Lab1_HCT FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Hematocrit Level ........................................................................................................................ ")
        lab3 = Entry(DemographicSectionframe)

        if val is not None:
            lab3.insert(0, val)
        else:
            lab3.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab3(lab3, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab1 plt
        curr.execute("SELECT Lab1_Plt_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Plt Count .................................................................................................................................... ")
        lab4 = Entry(DemographicSectionframe)

        if val is not None:
            lab4.insert(0, val)
        else:
            lab4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab4(lab4, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #spacing
        r = r+1
        label = Label(DemographicSectionframe).grid(row = r, column = 1)

        #lab2 date
        curr.execute("SELECT Lab2_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nDate of Second Lab Examination (YYYY-MM-DD) ........................................................................ ")
        lab5 = Entry(DemographicSectionframe)

        if val is not None:
            lab5.insert(0, val)
        else:
            lab5.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab5(lab5, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab2 cd4
        curr.execute("SELECT Lab2_CD4_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "CD4 (T-Cell) Count ..................................................................................................................... ")
        lab6 = Entry(DemographicSectionframe)

        if val is not None:
            lab6.insert(0, val)
        else:
            lab6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab6(lab6, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab2 viral load
        curr.execute("SELECT Lab2_Viral_Load FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Viral Load ................................................................................................................................... ")
        lab7 = Entry(DemographicSectionframe)

        if val is not None:
            lab7.insert(0, val)
        else:
            lab7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab7(lab7, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #spacing
        r = r+1
        label = Label(DemographicSectionframe).grid(row = r, column = 1)

        #lab3 date
        curr.execute("SELECT Lab3_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "\nDate of Third Lab Examination (YYYY-MM-DD) ........................................................................... ")
        lab8 = Entry(DemographicSectionframe)

        if val is not None:
            lab8.insert(0, val)
        else:
            lab8.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab8(lab8, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab3 cd4
        curr.execute("SELECT Lab3_CD4_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "CD4 (T-Cell) Count ..................................................................................................................... ")
        lab9 = Entry(DemographicSectionframe)

        if val is not None:
            lab9.insert(0, val)
        else:
            lab9.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab9(lab9, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab3 viral load
        curr.execute("SELECT Lab3_Viral_Load FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(DemographicSectionframe, text = "Viral Load ................................................................................................................................... ")
        lab10 = Entry(DemographicSectionframe)

        if val is not None:
            lab10.insert(0, val)
        else:
            lab10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(DemographicSectionframe, text = "Update", command = lambda:self.updateLab10(lab10, id, date))

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        lab10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#************************************************************************************************************************

#Close Database Connection
        curr.close()
        db.close()

# Database connection
    def connect(self):
        try:
            db = MySQLdb.connect(
                host = "localhost",
                user="root",
                passwd = "Darling",
                db="HERO")
            return db
        except:
            tkMessageBox.showinfo("Error!","Check your internet connection.")

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

#************************************************************************************************************************

#
#parent sections
#

#Update Demographic info ************************************************************************************************************************
    def updateDemInfo0(self, demInfo0, id, date, test):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        print test.get()

        #Execute
        newVal = demInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET First_Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Demographic_Information SET First_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo1(self, demInfo1, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = demInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Last_Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Demographic_Information SET Last_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Middle_Initial = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 1):
            curr.execute("UPDATE Demographic_Information SET Middle_Initial = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 1 character.")        

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Age = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Demographic_Information SET Age = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMust be only numbers.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo4(self, newWidget, id, date):

        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Date_Of_Birth = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Demographic_Information SET Date_Of_Birth = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo5(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Demographic_Information SET Gender = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Race = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 20):
            curr.execute("UPDATE Demographic_Information SET Race = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 20 characters.")        

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo7(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Primary_Language = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 20):
            curr.execute("UPDATE Demographic_Information SET Primary_Language = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 20 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo8(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            curr.execute("UPDATE Demographic_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo9(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Demographic_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo10(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 2):
            curr.execute("UPDATE Demographic_Information SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 2 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo11(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Address_County = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Demographic_Information SET Address_County = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo12(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Demographic_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMust be only numbers.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo13(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Camper_Email = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 70):
            curr.execute("UPDATE Demographic_Information SET Camper_Email = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 70 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo14(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Parent_Email = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 70):
            curr.execute("UPDATE Demographic_Information SET Parent_Email = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 70 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo15(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Guardian_Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 60):
            curr.execute("UPDATE Demographic_Information SET Guardian_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 60 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo16(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Guardian_Camper_Relationship = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Demographic_Information SET Guardian_Camper_Relationship = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo17(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Last_Grade_Completed = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Demographic_Information SET Last_Grade_Completed = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo18(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Demographic_Information SET Special_Ed_Classes = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo19(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Demographic_Information SET Siblings_Applying = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo20(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Demographic_Information SET T_Shirt = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()
    
    def updateDemInfo21(self, demTrans0, demTrans1, demTrans2, demTrans3,
            demTrans4, demTrans5, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if demTrans0.get():
            newVal = newVal + 'Atlanta bus,'

        if demTrans1.get():
            newVal = newVal + 'Augusta bus,'

        if demTrans2.get():
            newVal = newVal + 'Albany bus,'

        if demTrans3.get():
            newVal = newVal + 'Athens bus,'

        if demTrans4.get():
            newVal = newVal + 'Savannah bus,'

        if demTrans5.get():
            newVal = newVal + 'Car/drop,'

        if newVal == '':
            curr.execute("UPDATE Demographic_Information SET Planned_Transportation = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Demographic_Information SET Planned_Transportation = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#demographic contacts ************************************************************************************************************************
    def updateContactDemInfo10(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Contacts SET Name = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 60):
            curr.execute("UPDATE Demographic_Contacts SET Name = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 60 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()
        
    def updateContactDemInfo11(self, demContactInfoTime10, demContactInfoTime11, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if demContactInfoTime10.get():
            newVal = newVal + 'Day,'
        
        if demContactInfoTime11.get():
            newVal = newVal + 'Evening,'

        if newVal == '':
            curr.execute("UPDATE Demographic_Contacts SET Time_Preference = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Demographic_Contacts SET Time_Preference = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateContactDemInfo12(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Contacts SET Phone_Number = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 10):
            curr.execute("UPDATE Demographic_Contacts SET Phone_Number = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 10 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateContactDemInfo20(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Contacts SET Name = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 60):
            curr.execute("UPDATE Demographic_Contacts SET Name = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 60 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()
        
    def updateContactDemInfo21(self, demContactInfoTime20, demContactInfoTime21, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if demContactInfoTime20.get():
            newVal = newVal + 'Day,'
        
        if demContactInfoTime21.get():
            newVal = newVal + 'Evening,'

        if newVal == '':
            curr.execute("UPDATE Demographic_Contacts SET Time_Preference = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Demographic_Contacts SET Time_Preference = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateContactDemInfo22(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Contacts SET Phone_Number = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 10):
            curr.execute("UPDATE Demographic_Contacts SET Phone_Number = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Home';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 10 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateContactDemInfo30(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Contacts SET Name = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 60):
            curr.execute("UPDATE Demographic_Contacts SET Name = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 60 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()
        
    def updateContactDemInfo31(self, demContactInfoTime30, demContactInfoTime31, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if demContactInfoTime30.get():
            newVal = newVal + 'Day,'
        
        if demContactInfoTime31.get():
            newVal = newVal + 'Evening,'

        if newVal == '':
            curr.execute("UPDATE Demographic_Contacts SET Time_Preference = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Demographic_Contacts SET Time_Preference = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateContactDemInfo32(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Contacts SET Phone_Number = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 10):
            curr.execute("UPDATE Demographic_Contacts SET Phone_Number = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Work';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 10 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Parent/ Guardian Emergency Contact Section ************************************************************************************************************************
    def updateEmergencyInfo0(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Name FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        if len(emergencyContacts) > 0 and count is 1:
            oldName = emergencyContacts[0][0]
        elif len(emergencyContacts) > 1 and count is 2:
            oldName = emergencyContacts[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                if askyesno('Verify', '\nDeleting the name of an emergency contact will delete all of the information for that contact.\nAre you sure you want to delete?'):
                    curr.execute("DELETE FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, oldName,))
                    tkMessageBox.showinfo("Edit Profile", "Update Successful!")
                else:
                    tkMessageBox.showinfo("Edit Profile", "Update Canceled")
        elif (len(newVal) <= 60):
            if oldName is not None:
                curr.execute("UPDATE Parent_Emergency_Contact SET Name = %s WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (newVal, id, date, oldName,))
            else:
                curr.execute("INSERT INTO Parent_Emergency_Contact (Name, ID, Date_Submitted) VALUES (%s, %s, %s);", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 60 characters.")        

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateEmergencyInfo1(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Name FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        if len(emergencyContacts) > 0 and count is 1:
            oldName = emergencyContacts[0][0]
        elif len(emergencyContacts) > 1 and count is 2:
            oldName = emergencyContacts[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE Parent_Emergency_Contact SET Relationship = NULL WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, oldName,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            if oldName is not None:
                curr.execute("UPDATE Parent_Emergency_Contact SET Relationship = %s WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (newVal, id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAn emergency contact must have a name.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()


    def updateEmergencyInfo2(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Name FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        if len(emergencyContacts) > 0 and count is 1:
            oldName = emergencyContacts[0][0]
        elif len(emergencyContacts) > 1 and count is 2:
            oldName = emergencyContacts[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE Parent_Emergency_Contact SET Daytime_Phone = NULL WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, oldName,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) == 10):
            if oldName is not None:
                curr.execute("UPDATE Parent_Emergency_Contact SET Daytime_Phone = %s WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (newVal, id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAn emergency contact must have a name.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 10 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateEmergencyInfo3(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Name FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        if len(emergencyContacts) > 0 and count is 1:
            oldName = emergencyContacts[0][0]
        elif len(emergencyContacts) > 1 and count is 2:
            oldName = emergencyContacts[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE Parent_Emergency_Contact SET Evening_Phone = NULL WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, oldName,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) == 10):
            if oldName is not None:
                curr.execute("UPDATE Parent_Emergency_Contact SET Evening_Phone = %s WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (newVal, id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAn emergency contact must have a name.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 10 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Insurance Info Section ************************************************************************************************************************
    def updateInsuranceInfo0(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Insurance_Information SET Type_of_Health_Insurance = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateInsuranceInfo1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Insurance_Information SET Private_Insurance_Name = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            curr.execute("UPDATE Insurance_Information SET Private_Insurance_Name = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateInsuranceInfo2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Insurance_Information SET Policy_Number = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Insurance_Information SET Policy_Number = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()


    def updateInsuranceInfo3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Insurance_Information SET Group_Number = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Insurance_Information SET Group_Number = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Medical Provider Section ************************************************************************************************************************
    def updateMedProviderInfo0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Information SET Medical_Provider_Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            curr.execute("UPDATE Medical_Provider_Information SET Medical_Provider_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProviderInfo1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Information SET Phone_Office = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 10):
            curr.execute("UPDATE Medical_Provider_Information SET Phone_Office = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 10 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProviderInfo2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Information SET Pharmacy_Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            curr.execute("UPDATE Medical_Provider_Information SET Pharmacy_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProviderInfo3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Information SET Phone_Pharmacy = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 10):
            curr.execute("UPDATE Medical_Provider_Information SET Phone_Pharmacy = %s WHERE ID = %s AND Date_Submitted = %s AND Type = 'Cell';", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 10 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Medical Information Section ************************************************************************************************************************
    def updateMedInfoCurr(self, medInfoCurr0, medInfoCurr1, medInfoCurr2, medInfoCurr3, medInfoCurr4,
            medInfoCurr5, medInfoCurr6, medInfoCurr7, medInfoCurr8, medInfoCurr9, medInfoCurr10, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if medInfoCurr0.get():
            newVal = newVal + 'HIV,'

        if medInfoCurr1.get():
            newVal = newVal + 'Hepatitis B,'

        if medInfoCurr2.get():
            newVal = newVal + 'Hepatitis C,'

        if medInfoCurr3.get():
            newVal = newVal + 'ADD or ADHD,'

        if medInfoCurr4.get():
            newVal = newVal + 'Sickle Cell Disease,'

        if medInfoCurr5.get():
            newVal = newVal + 'Asthma,'

        if medInfoCurr6.get():
            newVal = newVal + 'Tubes in Ears,'
        
        if medInfoCurr7.get():
            newVal = newVal + 'Heart Problems,'
        
        if medInfoCurr8.get():
            newVal = newVal + 'Mental Health Diagnoses,'
        
        if medInfoCurr9.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE Medical_Information SET Current_Medical_Conditions = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Medical_Information SET Current_Medical_Conditions = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))

        other = medInfoCurr10.get()
        if (other == 'Unanswered') or (other == ''):
            curr.execute("UPDATE Medical_Information SET Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(other) <= 20):
            curr.execute("UPDATE Medical_Information SET Other = %s WHERE ID = %s AND Date_Submitted = %s;", (other, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 20 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedInfo1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Information SET Medical_Condition_Explanation = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 500):
            curr.execute("UPDATE Medical_Provider_Information SET Medical_Provider_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 500 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Allergies Section ************************************************************************************************************************
    def updateAllergyInfo0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Allergies SET Med_Allergy = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateAllergyInfo1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Allergies SET Med_Reaction = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 200):
            curr.execute("UPDATE Allergies SET Med_Reaction = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 200 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateAllergyInfo2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Allergies SET Food_Allergy = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateAllergyInfo3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Allergies SET Food_Reaction = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 200):
            curr.execute("UPDATE Allergies SET Food_Reaction = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 200 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()
    
    def updateAllergyInfo4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Allergies SET Env_Allergy = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateAllergyInfo5(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Allergies SET Env_Reaction = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 200):
            curr.execute("UPDATE Allergies SET Env_Reaction = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 200 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()
    
    def updateAllergyInfo6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Allergies SET EpiPen = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Dietary Needs Section ************************************************************************************************************************
    def updateDietaryNeedsInfo0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Dietary_Needs SET Special_Dietary_Needs = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Dietary_Needs SET Vegetarian = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Dietary_Needs SET Food_Restrictions = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 200):
            curr.execute("UPDATE Dietary_Needs SET Food_Restrictions = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 200 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo3(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Dietary_Needs SET G_Tube = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Dietary_Needs SET Formula_Supplement = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo5(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Dietary_Needs SET Formula_Supplement_How = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Dietary_Needs SET Formula_Type = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Dietary_Needs SET Formula_Type = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo7(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Dietary_Needs SET Formula_Cans_Per_Day = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Dietary_Needs SET Formula_Cans_Per_Day = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMust be only numbers.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo8(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Dietary_Needs SET Feeding_Pump = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo9(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Dietary_Needs SET Pump_Type = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Dietary_Needs SET Pump_Type = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo10(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Dietary_Needs SET Feeding_Schedule = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 200):
            curr.execute("UPDATE Dietary_Needs SET Feeding_Schedule = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 200 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#General health ************************************************************************************************************************
    def genHealthLimit(self, genHealthLimit0, genHealthLimit1, genHealthLimit2, genHealthLimit3, genHealthLimit4,
            genHealthLimit5, genHealthLimit6, genHealthLimit7, genHealthLimit8, genHealthLimit9, genHealthLimit10, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if genHealthLimit0.get():
            newVal = newVal + 'Dressing,'

        if genHealthLimit1.get():
            newVal = newVal + 'Showering,'

        if genHealthLimit2.get():
            newVal = newVal + 'Eating,'

        if genHealthLimit3.get():
            newVal = newVal + 'Toileting,'

        if genHealthLimit4.get():
            newVal = newVal + 'Walking/Balance,'

        if genHealthLimit5.get():
            newVal = newVal + 'Braces,'

        if genHealthLimit6.get():
            newVal = newVal + 'Casts,'

        if genHealthLimit7.get():
            newVal = newVal + 'Walker,'

        if genHealthLimit8.get():
            newVal = newVal + 'Wheelchair,'

        if genHealthLimit9.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE General_Health SET Physical_Limitations = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE General_Health SET Physical_Limitations = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))

        other = genHealthLimit10.get()
        if (other == 'Unanswered') or (other == ''):
            curr.execute("UPDATE General_Health SET Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(other) <= 50):
            curr.execute("UPDATE General_Health SET Other = %s WHERE ID = %s AND Date_Submitted = %s;", (other, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE General_Health SET Tire_Easily = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE General_Health SET Swim = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE General_Health SET Chicken_Pox = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()


    def updateGenHealth4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE General_Health SET Chicken_Pox_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE General_Health SET Chicken_Pox_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth5(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE General_Health SET Menstrual_Cycle = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE General_Health SET Menstrual_Difficulties = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 300):
            curr.execute("UPDATE General_Health SET Menstrual_Difficulties = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 300 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Behavior ************************************************************************************************************************
    def updateBehavior0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Camper_Knows = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateBehavior1(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Time_Camper_Known = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateBehaviorExperiances(self, behaviorExperiances0, behaviorExperiances1, behaviorExperiances2, behaviorExperiances3, behaviorExperiances4,
            behaviorExperiances5, behaviorExperiances6, behaviorExperiances7, behaviorExperiances8, behaviorExperiances9, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if behaviorExperiances0.get():
            newVal = newVal + 'Anxiety,'
        
        if behaviorExperiances1.get():
            newVal = newVal + 'Fear of dark,'
        
        if behaviorExperiances2.get():
            newVal = newVal + 'Homesickness,'
        
        if behaviorExperiances3.get():
            newVal = newVal + 'Sleeps with night light,'
        
        if behaviorExperiances4.get():
            newVal = newVal + 'Fights easily,'
        
        if behaviorExperiances5.get():
            newVal = newVal + 'School suspension due to behavior,'
        
        if behaviorExperiances6.get():
            newVal = newVal + 'Bedwetting,'
        
        if behaviorExperiances7.get():
            newVal = newVal + 'Sleeps with comfort item,'
        
        if behaviorExperiances8.get():
            newVal = newVal + 'Hyperactivity or problems with attention,'
        
        if behaviorExperiances9.get():
            newVal = newVal + 'History of trauma or sexual abuse,'

        if newVal == '':
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Camper_Experiences = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Camper_Experiences = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateBehavior2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Med_Hyper_AttentionProb = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateBehavior3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE General_Health SET Explanation = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 600):
            curr.execute("UPDATE General_Health SET Explanation = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 600 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateBehaviorInterests(self, behaviorInterests0, behaviorInterests1, behaviorInterests2, behaviorInterests3, behaviorInterests4,
            behaviorInterests5, behaviorInterests6, behaviorInterests7, behaviorInterests8, behaviorInterests9,
            behaviorInterests10, behaviorInterests11, behaviorInterests12, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if behaviorInterests0.get():
            newVal = newVal + 'Reading,'

        if behaviorInterests1.get():
            newVal = newVal + 'Music,'

        if behaviorInterests2.get():
            newVal = newVal + 'Swimming,'

        if behaviorInterests3.get():
            newVal = newVal + 'Dance,'

        if behaviorInterests4.get():
            newVal = newVal + 'Sports,'

        if behaviorInterests5.get():
            newVal = newVal + 'Arts/Crafts,'

        if behaviorInterests6.get():
            newVal = newVal + 'Fishing,'

        if behaviorInterests7.get():
            newVal = newVal + 'Boating,'

        if behaviorInterests8.get():
            newVal = newVal + 'Archery,'

        if behaviorInterests9.get():
            newVal = newVal + 'Golf,'

        if behaviorInterests10.get():
            newVal = newVal + 'Bicycling,'

        if behaviorInterests11.get():
            newVal = newVal + 'Animals,'

        if behaviorInterests12.get():
            newVal = newVal + 'Nature,'

        if newVal == '':
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Camper_Interests = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Camper_Interests = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateBehavior4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Recent_Major_Events = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 500):
            curr.execute("UPDATE Pyschosocial_and_Behavioral_info SET Recent_Major_Events = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 500 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Medication Info ************************************************************************************************************************
    def updateMed0(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Medication FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        if len(emergencyContacts) > 0 and count is 1:
            oldName = emergencyContacts[0][0]
        elif len(emergencyContacts) > 1 and count is 2:
            oldName = emergencyContacts[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                if askyesno('Verify', '\nDeleting the name of a medication will delete all of the information for that medication.\nAre you sure you want to delete?'):
                    curr.execute("DELETE FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, oldName,))
                    tkMessageBox.showinfo("Edit Profile", "Update Successful!")
                else:
                    tkMessageBox.showinfo("Edit Profile", "Update Canceled")
        elif (len(newVal) <= 50):
            if oldName is not None:
                curr.execute("UPDATE Parent_Medications SET Medication = %s WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (newVal, id, date, oldName,))
            else:
                curr.execute("INSERT INTO Parent_Medications (Medication, ID, Date_Submitted) VALUES (%s, %s, %s);", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMed1(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Medication FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        if len(emergencyContacts) > 0 and count is 1:
            oldName = emergencyContacts[0][0]
        elif len(emergencyContacts) > 1 and count is 2:
            oldName = emergencyContacts[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE Parent_Medications SET Amount = NULL WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, oldName,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            if oldName is not None:
                curr.execute("UPDATE Parent_Medications SET Amount = %s WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (newVal, id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMedication must have a name.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()


    def updateMed2(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Medication FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        if len(emergencyContacts) > 0 and count is 1:
            oldName = emergencyContacts[0][0]
        elif len(emergencyContacts) > 1 and count is 2:
            oldName = emergencyContacts[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE Parent_Medications SET Time_Instruction = NULL WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, oldName,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            if oldName is not None:
                curr.execute("UPDATE Parent_Medications SET Time_Instruction = %s WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (newVal, id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMedication must have a name.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Preliminary signatures ************************************************************************************************************************
    def updateParentSig0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Release_Forms_Signed SET Parent_Camper_Contract = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateParentSig1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Release_Forms_Signed SET Partcipation_Consent_Liability_Release = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateParentSig2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Release_Forms_Signed SET Media_Release = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateParentSig3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Release_Forms_Signed SET Camper_HIV_Education = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateParentSig4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Release_Forms_Signed SET Camp_Twin_Lakes_Rules = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateParentSig5(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Release_Forms_Signed SET Parental_Consent_and_Release = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#
#Medical provider sections
#

#medical history ************************************************************************************************************************
    def updateDiagnosis(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Diagnosis FROM Med_Hist_Diagnosis WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldName = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldName = arr[1][0]
        elif len(arr) > 2 and count is 3:
            oldName = arr[2][0]
        elif len(arr) > 3 and count is 4:
            oldName = arr[3][0]
        elif len(arr) > 4 and count is 5:
            oldName = arr[4][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("DELETE FROM Med_Hist_Diagnosis WHERE ID = %s AND Date_Submitted = %s AND Diagnosis = %s;", (id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            if oldName is not None:
                curr.execute("UPDATE Med_Hist_Diagnosis SET Diagnosis = %s WHERE ID = %s AND Date_Submitted = %s AND Diagnosis = %s;", (newVal, id, date, oldName,))
            else:
                curr.execute("INSERT INTO Med_Hist_Diagnosis (Diagnosis, ID, Date_Submitted) VALUES (%s, %s, %s);", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvider5(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_History SET Management = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 500):
            curr.execute("UPDATE Medical_History SET Management = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 500 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvider6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Medical_History SET Nutritional_Supplements = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvider7(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_History SET Feeding_Care = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 500):
            curr.execute("UPDATE Medical_History SET Feeding_Care = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 500 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvider8(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Medical_History SET Formula_Type = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()
    
    def updateMedHistAllergy(self, newWidget, type, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Allergy FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, type,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldAllergy = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldAllergy = arr[1][0]
        elif len(arr) > 2 and count is 3:
            oldAllergy = arr[2][0]
        elif len(arr) > 3 and count is 4:
            oldAllergy = arr[3][0]
        elif len(arr) > 4 and count is 5:
            oldAllergy = arr[4][0]
        else:
            oldAllergy = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldAllergy is not None:
                if askyesno('Verify', '\nDeleting the name of an allergy will delete all of the information for that allergy.\nAre you sure you want to delete?'):
                    curr.execute("DELETE FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Type = %s AND Allergy = %s;", (id, date, type, oldAllergy,))
                    tkMessageBox.showinfo("Edit Profile", "Update Successful!")
                else:
                    tkMessageBox.showinfo("Edit Profile", "Update Canceled")
        elif (len(newVal) <= 30):
            if oldAllergy is not None:
                curr.execute("UPDATE Med_Hist_Allergies SET Allergy = %s WHERE ID = %s AND Date_Submitted = %s AND Type = %s AND Allergy = %s;", (newVal, id, date, type, oldAllergy,))
            else:
                curr.execute("INSERT INTO Med_Hist_Allergies (Type, Allergy, ID, Date_Submitted) VALUES (%s, %s, %s);", (type, newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedHistReaction(self, newWidget, type, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Allergy FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, type,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldAllergy = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldAllergy = arr[1][0]
        elif len(arr) > 2 and count is 3:
            oldAllergy = arr[2][0]
        elif len(arr) > 3 and count is 4:
            oldAllergy = arr[3][0]
        elif len(arr) > 4 and count is 5:
            oldAllergy = arr[4][0]
        else:
            oldAllergy = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldAllergy is not None:
                curr.execute("DELETE FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s;", (id, date, oldAllergy,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            if oldAllergy is not None:
                curr.execute("UPDATE Med_Hist_Allergies SET Allergy = %s WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s;", (newVal, id, date, oldAllergy,))
            else:
                curr.execute("INSERT INTO Med_Hist_Allergies (Allergy, ID, Date_Submitted) VALUES (%s, %s, %s);", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedHistReaction(self, newWidget, type, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()
        
        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Allergy FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, type,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldAllergy = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldAllergy = arr[1][0]
        elif len(arr) > 2 and count is 3:
            oldAllergy = arr[2][0]
        elif len(arr) > 3 and count is 4:
            oldAllergy = arr[3][0]
        elif len(arr) > 4 and count is 5:
            oldAllergy = arr[4][0]
        else:
            oldAllergy = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE Med_Hist_Allergies SET Reaction = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = %s AND Allergy = %s;", (id, date, type, oldAllergy,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            if oldName is not None:
                curr.execute("UPDATE Med_Hist_Allergies SET Reaction = %s WHERE ID = %s AND Date_Submitted = %s AND Type = %s AND Allergy = %s;", (newVal, id, date, type, oldAllergy,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nReaction must have an allergy.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#physical ************************************************************************************************************************
    def updatePhysical0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Date_Completed = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Physical_Exam SET Date_Completed = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Height = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Height = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Weight = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Physical_Exam SET Weight = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMust be only numbers.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Pulse = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Physical_Exam SET Pulse = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMust be only numbers.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Resperations = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Physical_Exam SET Resperations = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMust be only numbers.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical5(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Blood_Pressure = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Blood_Pressure = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET HEENT = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET HEENT = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical7(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Skin = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Skin = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical8(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Cardiovascular = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Cardiovascular = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical9(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET GU_GYN = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET GU_GYN = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical10(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Pulmonary = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Pulmonary = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical11(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Glasses_HearingAids_PE = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Glasses_HearingAids_PE = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical12(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Abdomen = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Abdomen = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical13(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Lymph_Nodes = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Lymph_Nodes = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical14(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Extremities = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Extremities = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical15(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Spine = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            curr.execute("UPDATE Physical_Exam SET Spine = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical16(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Miscellaneous = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 500):
            curr.execute("UPDATE Physical_Exam SET Miscellaneous = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 500 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updatePhysical17(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Physical_Exam SET Comments = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 500):
            curr.execute("UPDATE Physical_Exam SET Comments = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 500 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#cognative development level ************************************************************************************************************************
    def updateCogDev0(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Cognitive_Development_Level SET Development_Level = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateCogDev1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Cognitive_Development_Level SET Other_Psychosocial_Information = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 1000):
            curr.execute("UPDATE Cognitive_Development_Level SET Other_Psychosocial_Information = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 1000 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Varicella screening ************************************************************************************************************************
    def updateVaricella0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Varicella_Screening SET Two_Doses = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateVaricella1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Varicella_Screening SET Chicken_Pox = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Varicella_Screening SET Chicken_Pox_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Varicella_Screening SET Chicken_Pox_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateVaricella3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Varicella_Screening SET Varicella_Antibody = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Varicella_Screening SET Varicella_Antibody_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Varicella_Screening SET Varicella_Antibody_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#tuberculosis screening ************************************************************************************************************************
    def updateTuberculosis1(self, newWidget, type, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Tuberculosis_Screening SET Date_Screened = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, type,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Tuberculosis_Screening SET Date_Screened = %s WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (newVal, id, date, type,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateTuberculosis2(self, newWidget, type, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Tuberculosis_Screening SET Result = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, type,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 70):
            curr.execute("UPDATE Tuberculosis_Screening SET Result = %s WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (newVal, id, date, type,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 70 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#Restrictions_And_Recommendations ************************************************************************************************************************
    def updateRestrictionsRec(self, newWidget, type, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Care_Provider SET Restrictions_And_Recommendations = NULL WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, type,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 1000):
            curr.execute("UPDATE Medical_Care_Provider SET Restrictions_And_Recommendations = %s WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (newVal, id, date, type,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 1000 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#medcare provider medications ************************************************************************************************************************
    def updateMedProMed1(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Medication_Name FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldName = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldName = arr[1][0]
        elif len(arr) > 2 and count is 3:
            oldName = arr[2][0]
        elif len(arr) > 3 and count is 4:
            oldName = arr[3][0]
        elif len(arr) > 4 and count is 5:
            oldName = arr[4][0]
        elif len(arr) > 5 and count is 6:
            oldName = arr[5][0]
        elif len(arr) > 6 and count is 7:
            oldName = arr[6][0]
        elif len(arr) > 7 and count is 8:
            oldName = arr[7][0]
        elif len(arr) > 8 and count is 9:
            oldName = arr[8][0]
        elif len(arr) > 9 and count is 10:
            oldName = arr[9][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                if askyesno('Verify', '\nDeleting the name of a medication will delete all of the information for that medication.\nAre you sure you want to delete?'):
                    curr.execute("DELETE FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, oldName,))
                    tkMessageBox.showinfo("Edit Profile", "Update Successful!")
                else:
                    tkMessageBox.showinfo("Edit Profile", "Update Canceled")
        elif (len(newVal) <= 100):
            if oldName is not None:
                curr.execute("UPDATE MedCareProvider_Medications SET Medication_Name = %s WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (newVal, id, date, oldName,))
            else:
                curr.execute("INSERT INTO MedCareProvider_Medications (Medication_Name, ID, Date_Submitted) VALUES (%s, %s, %s);", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProMed2(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Medication_Name FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldName = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldName = arr[1][0]
        elif len(arr) > 2 and count is 3:
            oldName = arr[2][0]
        elif len(arr) > 3 and count is 4:
            oldName = arr[3][0]
        elif len(arr) > 4 and count is 5:
            oldName = arr[4][0]
        elif len(arr) > 5 and count is 6:
            oldName = arr[5][0]
        elif len(arr) > 6 and count is 7:
            oldName = arr[6][0]
        elif len(arr) > 7 and count is 8:
            oldName = arr[7][0]
        elif len(arr) > 8 and count is 9:
            oldName = arr[8][0]
        elif len(arr) > 9 and count is 10:
            oldName = arr[9][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE MedCareProvider_Medications SET Amount_Including_Dosage = NULL WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, oldName,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            if oldName is not None:
                curr.execute("UPDATE MedCareProvider_Medications SET Amount_Including_Dosage = %s WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (newVal, id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMedication must have a name.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()


    def updateMedProMed3(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Medication_Name FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldName = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldName = arr[1][0]
        elif len(arr) > 2 and count is 3:
            oldName = arr[2][0]
        elif len(arr) > 3 and count is 4:
            oldName = arr[3][0]
        elif len(arr) > 4 and count is 5:
            oldName = arr[4][0]
        elif len(arr) > 5 and count is 6:
            oldName = arr[5][0]
        elif len(arr) > 6 and count is 7:
            oldName = arr[6][0]
        elif len(arr) > 7 and count is 8:
            oldName = arr[7][0]
        elif len(arr) > 8 and count is 9:
            oldName = arr[8][0]
        elif len(arr) > 9 and count is 10:
            oldName = arr[9][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE MedCareProvider_Medications SET Times_To_Give = NULL WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, oldName,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 100):
            if oldName is not None:
                curr.execute("UPDATE MedCareProvider_Medications SET Times_To_Give = %s WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (newVal, id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMedication must have a name.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 100 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#medcare provider verification statement ************************************************************************************************************************
    def updateMedProvVerState0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Signature = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvVerState1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Sig_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Sig_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvVerState2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 40):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 40 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvVerState3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvVerState4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 30):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 30 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvVerState5(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 2):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 2 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvVerState6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMust be only numbers.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvVerState7(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Phone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 10):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Phone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 10 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMedProvVerState8(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Emergency_Contact = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            curr.execute("UPDATE Medical_Provider_Verification_Statement SET Emergency_Contact = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#
#HIV provider sections
#

#health history ************************************************************************************************************************
    def updateHealthHistory0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Health_History SET Major_Surgical_History = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 500):
            curr.execute("UPDATE Health_History SET Major_Surgical_History = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 500 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateHealthHistory1(self, healthHistory1, healthHistory2, healthHistory3, healthHistory4, healthHistory5, healthHistory6, healthHistory7, 
        healthHistory8, healthHistory9, healthHistory10, healthHistory11, healthHistory12, healthHistory13, healthHistory14, healthHistory15, 
        healthHistory16, healthHistory17, healthHistory18, healthHistory19, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if healthHistory1.get():
            newVal = newVal + 'HIV,'

        if healthHistory2.get():
            newVal = newVal + 'Hepatitis B,'

        if healthHistory3.get():
            newVal = newVal + 'Hepatitis C,'

        if healthHistory4.get():
            newVal = newVal + 'Poor growth,'

        if healthHistory5.get():
            newVal = newVal + 'Bleeding disorders,'

        if healthHistory6.get():
            newVal = newVal + 'Asthma,'

        if healthHistory7.get():
            newVal = newVal + 'Pulmonary Disease,'

        if healthHistory8.get():
            newVal = newVal + 'Chronic Cough,'

        if healthHistory9.get():
            newVal = newVal + 'ADD or ADHD,'

        if healthHistory10.get():
            newVal = newVal + 'Renal Disease,'

        if healthHistory11.get():
            newVal = newVal + 'Sickle Cell disease,'

        if healthHistory12.get():
            newVal = newVal + 'Congenital Heart Disease,'

        if healthHistory13.get():
            newVal = newVal + 'Hypertension,'

        if healthHistory14.get():
            newVal = newVal + 'Cryptosporidium,'

        if healthHistory15.get():
            newVal = newVal + 'Chronic diarrhea,'

        if healthHistory16.get():
            newVal = newVal + 'Seizures,'

        if healthHistory17.get():
            newVal = newVal + 'Diabetes,'

        if healthHistory18.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE Health_History SET Health_History = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Health_History SET Health_History = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))

        other = healthHistory19.get()
        if (other == 'Unanswered') or (other == ''):
            curr.execute("UPDATE Health_History SET Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(other) <= 20):
            curr.execute("UPDATE Health_History SET Other = %s WHERE ID = %s AND Date_Submitted = %s;", (other, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 20 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateHealthHistory2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Health_History SET History_of_Noncompliance = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateHealthHistory3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Health_History SET Explanation = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 500):
            curr.execute("UPDATE Health_History SET Explanation = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 500 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

#lab data ************************************************************************************************************************
    def updateLab0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Lab_Data SET Lab1_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_WBC = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 6):
            curr.execute("UPDATE Lab_Data SET Lab1_WBC = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 6 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_HGB = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 4):
            curr.execute("UPDATE Lab_Data SET Lab1_HGB = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 4 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_HCT = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 3):
            curr.execute("UPDATE Lab_Data SET Lab1_HCT = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 3 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_Plt_Count = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 6):
            curr.execute("UPDATE Lab_Data SET Lab1_Plt_Count = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 6 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab5(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab2_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Lab_Data SET Lab2_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab2_CD4_Count = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 4):
            curr.execute("UPDATE Lab_Data SET Lab2_CD4_Count = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 4 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab7(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab2_Viral_Load = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 5):
            curr.execute("UPDATE Lab_Data SET Lab2_Viral_Load = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 5 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab8(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab3_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Lab_Data SET Lab3_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab9(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab3_CD4_Count = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 4):
            curr.execute("UPDATE Lab_Data SET Lab3_CD4_Count = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 4 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab10(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab3_Viral_Load = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 5):
            curr.execute("UPDATE Lab_Data SET Lab3_Viral_Load = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 5 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()





if __name__ == "__main__":
    master=tk.Tk()
    Example(master).pack(side="top", fill="both", expand=True)
    master.mainloop()