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
        self.ChildInfoSectionframe = Frame(self.frame)
        self.ChildInfoSectionframe.pack(fill = 'y', side = 'left') 
        r = 0

        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\nCHILD'S INFORMATION")
        labelChildInfoSection.grid(row = r, column = 0)
        labelChildInfoSection.config(font=("Helvetica", 20))

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        curr.execute("SELECT Address_City FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global childInfo4
        childInfo4 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo4.insert(0, val)
        else:
            childInfo4.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        curr.execute("SELECT Address_County FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global childInfo5
        childInfo5 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo5.insert(0, val)
        else:
            childInfo5.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #address zip
        curr.execute("SELECT Address_Zip FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global childInfo6
        childInfo6 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo6.insert(0, val)
        else:
            childInfo6.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #home phone
        curr.execute("SELECT Home_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... ")
        global childInfo7
        childInfo7 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo7.insert(0, val)
        else:
            childInfo7.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian phone
        curr.execute("SELECT Guardian_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ ")
        global childInfo8
        childInfo8 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo8.insert(0, val)
        else:
            childInfo8.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian email
        curr.execute("SELECT Guardian_Email FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... ")
        global childInfo9
        childInfo9 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo9.insert(0, val)
        else:
            childInfo9.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        curr.execute("SELECT Age FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global childInfo10
        childInfo10 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo10.insert(0, val)
        else:
            childInfo10.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #birthday
        curr.execute("SELECT Birthday FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (Y/M/D) ............................................................................. ")
        global childInfo11
        childInfo11 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo11.insert(0, val)
        else:
            childInfo11.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. ")

        curr.execute("SELECT Gender FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global childInfo12
        childInfo12 = StringVar()
        
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo12, *choices)

        if val is not None:
            childInfo12.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global childInfo13
        childInfo13 = StringVar()
        
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo13, *choices)

        if val is not None:
            childInfo13.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #aware
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... ')

        curr.execute("SELECT Aware FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo14
        childInfo14 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo14, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo14, value=2)

        if val is not None:
            if val is 0:
                childInfo14.set(2)
            else:
                childInfo14.set(1)
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #why
        curr.execute("SELECT Why FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "If no, please provide a reason why child is not aware .............................. ")
        global childInfo15
        childInfo15 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo15.insert(0, val)
        else:
            childInfo15.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #refferal source
        curr.execute("SELECT Refferal_Source FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... ")
        global childInfo16
        childInfo16 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo16.insert(0, val)
        else:
            childInfo16.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #school attending
        curr.execute("SELECT School_attending FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. ")
        global childInfo17
        childInfo17 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo17.insert(0, val)
        else:
            childInfo17.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Grade Level
        curr.execute("SELECT School_grade_level FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... ")
        global childInfo18
        childInfo18 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo18.insert(0, val)
        else:
            childInfo18.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo18.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Ethnicity
        label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... ")

        curr.execute("SELECT Ethnicity FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global childInfo19
        childInfo19 = StringVar()
        
        choices = ['White/Caucasian','Black/African-American','Hispanic/Latino',
        'Native American','Asian/Pacific Islander/Indian Sub-Continent','Multi-racial','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo19, *choices)

        if val is not None:
            childInfo19.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Ethnicity Other
        curr.execute("SELECT Ethnicity_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global childInfo20
        childInfo20 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo20.insert(0, val)
        else:
            childInfo20.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Even been...
        label = Label(self.ChildInfoSectionframe, text = "\nHas your child ever been...")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')
        
        #ADD_ADHD
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. ')

        curr.execute("SELECT ADD_ADHD FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo21
        childInfo21 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo21, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo21, value=2)

        if val is not None:
            if val is 0:
                childInfo21.set(2)
            else:
                childInfo21.set(1)
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Learning_Disability
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')

        curr.execute("SELECT Learning_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo22
        childInfo22 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo22, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo22, value=2)

        if val is not None:
            if val is 0:
                childInfo22.set(2)
            else:
                childInfo22.set(1)
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Developmental_Disability
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')

        curr.execute("SELECT Developmental_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo23
        childInfo23 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo23, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo23, value=2)

        if val is not None:
            if val is 0:
                childInfo23.set(2)
            else:
                childInfo23.set(1)
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Mental_Health_Issues
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')

        curr.execute("SELECT Mental_Health_Issues FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo24
        childInfo24 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo24, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo24, value=2)

        if val is not None:
            if val is 0:
                childInfo24.set(2)
            else:
                childInfo24.set(1)
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Other_Medical_Condition
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')

        curr.execute("SELECT Other_Medical_Condition FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo25
        childInfo25 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo25, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo25, value=2)

        if val is not None:
            if val is 0:
                childInfo25.set(2)
            else:
                childInfo25.set(1)
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Victim_of_Abuse
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')

        curr.execute("SELECT Victim_of_Abuse FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo26
        childInfo26 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo26, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo26, value=2)

        if val is not None:
            if val is 0:
                childInfo26.set(2)
            else:
                childInfo26.set(1)
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Criminal_Justice_System
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')

        curr.execute("SELECT Criminal_Justice_System FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        global childInfo27
        childInfo27 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo27, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo27, value=2)

        if val is not None:
            if val is 0:
                childInfo27.set(2)
            else:
                childInfo27.set(1)
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Custody
        label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... ")

        curr.execute("SELECT Legal_Custody FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global childInfo28
        childInfo28 = StringVar()

        choices = ['Mother','Father','Both Parents','Aunt/Uncle','Grandparent','Pending Court Action','Other']        
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo28, *choices)

        if val is not None:
            childInfo28.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Custody Other
        curr.execute("SELECT Custody_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global childInfo29
        childInfo29 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo29.insert(0, val)
        else:
            childInfo29.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo29.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Section
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

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
