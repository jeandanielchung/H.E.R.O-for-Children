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
        
#Child info section ************************************************************************************************************************
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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo4())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo5())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo6())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo7())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo8())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo9())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo10())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #birthday
        curr.execute("SELECT Birthday FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ ")
        global childInfo11
        childInfo11 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo11.insert(0, val)
        else:
            childInfo11.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo11())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo12())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo13())

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
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo14())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo15())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Referral source
        curr.execute("SELECT Referral_Source FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... ")
        global childInfo16
        childInfo16 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            childInfo16.insert(0, val)
        else:
            childInfo16.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo16())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo17())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo18())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo19())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo20())

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
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo21())

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
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo22())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Developmental_Disability
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... ')

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
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo23())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Mental_Health_Issues
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. ')

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
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo24())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Other_Medical_Condition
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... ')

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
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo25())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Victim_of_Abuse
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... ')

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
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo26())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Criminal_Justice_System
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... ')

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
 
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo27())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo28())

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
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo29())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        childInfo29.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Section ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global parentInfo0
        parentInfo0 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo0.insert(0, val)
        else:
            parentInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global parentInfo1
        parentInfo1 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo1.insert(0, val)
        else:
            parentInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global parentInfo2
        parentInfo2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo2.insert(0, val)
        else:
            parentInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Age
        curr.execute("SELECT Age FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global parentInfo3
        parentInfo3 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo3.insert(0, val)
        else:
            parentInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo4
        parentInfo4 = StringVar()
        
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo4, *choices)

        if val is not None:
            parentInfo4.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Adoptive Parent
        label = Label(self.ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... ")

        curr.execute("SELECT Adoptive_Parent FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo5
        parentInfo5 = StringVar()
        
        choices = ['Yes','No','Not Applicable']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo5, *choices)

        if val is not None:
            parentInfo5.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Marital Status
        label = Label(self.ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... ")

        curr.execute("SELECT Marital_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo6
        parentInfo6 = StringVar()
        
        choices = ['Married','Single','Separated','Divorced','Widowed']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo6, *choices)

        if val is not None:
            parentInfo6.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Highest Level of Education Completed
        label = Label(self.ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. ")

        curr.execute("SELECT Education_Completed FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo7
        parentInfo7 = StringVar()
        
        choices = ['HS','GED','Some College','Associates Degree','Bachelor Degree','Master Degree','Doctorate']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo7, *choices)

        if val is not None:
            parentInfo7.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Status
        label = Label(self.ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... ")

        curr.execute("SELECT Employment_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global parentInfo8
        parentInfo8 = StringVar()
        
        choices = ['Full-Time','Part-Time','Unemployed','Disability']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo8, *choices)

        if val is not None:
            parentInfo8.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo8())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Company
        curr.execute("SELECT Employment_Company_Name FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        r= r+1
        label = Label(self.ChildInfoSectionframe, text = "\nIf employed,")
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = "please provide Company Name ............................................................. ")

        global parentInfo9
        parentInfo9 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo9.insert(0, val)
        else:
            parentInfo9.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo9())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Address
        curr.execute("SELECT Address_Street FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nAddress ................................................................................................ ")
        global parentInfo10
        parentInfo10 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo10.insert(0, val)
        else:
            parentInfo10.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo10())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global parentInfo11
        parentInfo11 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo11.insert(0, val)
        else:
            parentInfo11.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo11())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        curr.execute("SELECT Address_State FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nState .................................................................................................... ")
        global parentInfo12
        parentInfo12 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo12.insert(0, val)
        else:
            parentInfo12.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo12())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global parentInfo13
        parentInfo13 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo13.insert(0, val)
        else:
            parentInfo13.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo13())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Work Phone
        curr.execute("SELECT WorkPhone FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... ")
        global parentInfo14
        parentInfo14 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo14.insert(0, val)
        else:
            parentInfo14.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo14())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #E-mail
        curr.execute("SELECT Email FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nE-mail ................................................................................................... ")
        global parentInfo15
        parentInfo15 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            parentInfo15.insert(0, val)
        else:
            parentInfo15.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateparentInfo15())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        parentInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Absent Parent Info ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global absParentInfo0
        absParentInfo0 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            absParentInfo0.insert(0, val)
        else:
            absParentInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global absParentInfo1
        absParentInfo1 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            absParentInfo1.insert(0, val)
        else:
            absParentInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Telephone
        curr.execute("SELECT Telephone FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nTelephone .............................................................................................. ")
        global absParentInfo2
        absParentInfo2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            absParentInfo2.insert(0, val)
        else:
            absParentInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        curr.execute("SELECT Address_Street FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global absParentInfo3
        absParentInfo3 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            absParentInfo3.insert(0, val)
        else:
            absParentInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global absParentInfo4
        absParentInfo4 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            absParentInfo4.insert(0, val)
        else:
            absParentInfo4.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #County
        curr.execute("SELECT Address_County FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global absParentInfo5
        absParentInfo5 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            absParentInfo5.insert(0, val)
        else:
            absParentInfo5.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nZip ......................................................................................................... ")
        global absParentInfo6
        absParentInfo6 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            absParentInfo6.insert(0, val)
        else:
            absParentInfo6.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        absParentInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")

        curr.execute("SELECT HIV_Status FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global absParentInfo7
        absParentInfo7 = StringVar()
        
        choices = ['HIV Positive','HIV Negative', 'Unkown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, absParentInfo7, *choices)

        if val is not None:
            absParentInfo7.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateabsParentInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

#Household Info ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nHOUSEHOLD INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #list all individuals living in the household
        label = Label(self.ChildInfoSectionframe, text = "\nAll Individuals Living in the Household")
        r = r+1
        label.grid(row = r, column = 0)

    #person1
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 1')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(1))
        buttonUpdate.grid(row = r, column = 2)

        person = 1
        
        #Name1
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo10
        houseInfo10 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            houseInfo10.insert(0, 'Unanswered')
        else: 
            houseInfo10.insert(0, val[0][0])

        r = r+1
        houseInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child1
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo11
        houseInfo11 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            houseInfo11.insert(0, 'Unanswered')
        else: 
            houseInfo11.insert(0, val[0][0])

        r = r+1
        houseInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex1
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo12
        houseInfo12 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo12, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo12.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)    

        #Age1
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo13
        houseInfo13 = Entry(self.ChildInfoSectionframe)

        if (val is ()) or (val[0][0] is None):
            houseInfo13.insert(0, 'Unanswered')
        else: 
            houseInfo13.insert(0, val[0][0])

        r = r+1
        houseInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status1
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo14
        houseInfo14 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo14, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo14.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)       

    #person2
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 2')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(2))
        buttonUpdate.grid(row = r, column = 2)

        person = 2
        
        #Name2
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo20
        houseInfo20 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo20.insert(0, 'Unanswered')
        else: 
            houseInfo20.insert(0, val[0][0])

        r = r+1
        houseInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child2
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo21
        houseInfo21 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo21.insert(0, 'Unanswered')
        else: 
            houseInfo21.insert(0, val[0][0])

        r = r+1
        houseInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex2
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo22
        houseInfo22 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo22, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo22.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)    

        #Age2
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo23
        houseInfo23 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo23.insert(0, 'Unanswered')
        else: 
            houseInfo23.insert(0, val[0][0])

        r = r+1
        houseInfo23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status2
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo24
        houseInfo24 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo24, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo24.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)        

    #person3
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 3')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(3))
        buttonUpdate.grid(row = r, column = 2)


        person = 3
        
        #Name3
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo30
        houseInfo30 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo30.insert(0, 'Unanswered')
        else: 
            houseInfo30.insert(0, val[0][0])

        r = r+1
        houseInfo30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child3
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo31
        houseInfo31 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo31.insert(0, 'Unanswered')
        else: 
            houseInfo31.insert(0, val[0][0])

        r = r+1
        houseInfo31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex3
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo32
        houseInfo32 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo32, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo32.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)   

        #Age3
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo33
        houseInfo33 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo33.insert(0, 'Unanswered')
        else: 
            houseInfo33.insert(0, val[0][0])

        r = r+1
        houseInfo33.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status3
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo34
        houseInfo34 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo34, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo34.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)     


    #person4
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 4')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(4))
        buttonUpdate.grid(row = r, column = 2)

        person = 4
        
        #Name4
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo40
        houseInfo40 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo40.insert(0, 'Unanswered')
        else: 
            houseInfo40.insert(0, val[0][0])

        r = r+1
        houseInfo40.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child4
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo41
        houseInfo41 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo41.insert(0, 'Unanswered')
        else: 
            houseInfo41.insert(0, val[0][0])

        r = r+1
        houseInfo41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex4
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo42
        houseInfo42 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo42, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo42.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0) 

        #Age4
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo43
        houseInfo43 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo43.insert(0, 'Unanswered')
        else: 
            houseInfo43.insert(0, val[0][0])

        r = r+1
        houseInfo43.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status4
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo44
        houseInfo44 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo44, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo44.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)         

    #person5
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 5')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(5))
        buttonUpdate.grid(row = r, column = 2)

        person = 5
        
        #Name5
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo50
        houseInfo50 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo50.insert(0, 'Unanswered')
        else: 
            houseInfo50.insert(0, val[0][0])

        r = r+1
        houseInfo50.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child5
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo51
        houseInfo51 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo51.insert(0, 'Unanswered')
        else: 
            houseInfo51.insert(0, val[0][0])

        r = r+1
        houseInfo51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex5
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo52
        houseInfo52 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo52, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo52.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0) 

        #Age5
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo53
        houseInfo53 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo53.insert(0, 'Unanswered')
        else: 
            houseInfo53.insert(0, val[0][0])

        r = r+1
        houseInfo53.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status5
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo54
        houseInfo54 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo54, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo54.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

    #person6
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 6')
        label.grid(row = r, column = 0, sticky = 'w')
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatehouseInfo(6))
        buttonUpdate.grid(row = r, column = 2)

        person = 6

        #Name6
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")

        curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo60
        houseInfo60 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo60.insert(0, 'Unanswered')
        else: 
            houseInfo60.insert(0, val[0][0])

        r = r+1
        houseInfo60.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Relationship to Child6
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")

        curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo61
        houseInfo61 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo61.insert(0, 'Unanswered')
        else: 
            houseInfo61.insert(0, val[0][0])

        r = r+1
        houseInfo61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Sex6
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")

        curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo62
        houseInfo62 = StringVar()
        
        choices = ['Male', 'Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo62, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo62.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0) 

        #Age6
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")

        curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo63
        houseInfo63 = Entry(self.ChildInfoSectionframe)
        
        if (val is ()) or (val[0][0] is None):
            houseInfo63.insert(0, 'Unanswered')
        else: 
            houseInfo63.insert(0, val[0][0])

        r = r+1
        houseInfo63.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
 
        #HIV Status6
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")

        curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, person,))
        val = curr.fetchall()

        global houseInfo64
        houseInfo64 = StringVar()
        
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo64, *choices)

        if (val is not ()) and (val[0][0] is not None):
            houseInfo64.set(val[0][0])

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


        #Family Annual Income Info
        label = Label(self.ChildInfoSectionframe, text = "\n\nFamily Annual Income Information ......................................................... ")

        curr.execute("SELECT Fam_Annual_Income FROM Fam_Annual_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global famIncome0
        famIncome0 = StringVar()
        
        choices = ['$0-10,000','$10,001-15,000','$15,001-20,000','$20,000-25,000','$25,001-30,000','$30,001-35,000','$35,001-40,000','$40,001-45,000','$50,000+']
        option = tk.OptionMenu(self.ChildInfoSectionframe, famIncome0, *choices)

        if val is not None:
            famIncome0.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatefamIncome0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income
        label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... ")

        curr.execute("SELECT Source_Fam_Income FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global famIncome1
        famIncome1 = StringVar()
        
        choices = ['Employment','Government Support','Public Assistance', 'Unemployment Benefits','Medicaid','Social Security','Veterans Benefits','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, famIncome1, *choices)

        if val is not None:
            famIncome1.set(val)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatefamIncome1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income Other
        curr.execute("SELECT Other FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global famIncome2
        famIncome2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            famIncome2.insert(0, val)
        else:
            famIncome2.insert(0, 'Unanswered')
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatefamIncome2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        famIncome2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#In Case of Emergency Contact ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global emergencyInfo0
        emergencyInfo0 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo0.insert(0, val)
        else:
            emergencyInfo0.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo0())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        curr.execute("SELECT Name_Last FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global emergencyInfo1
        emergencyInfo1 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo1.insert(0, val)
        else:
            emergencyInfo1.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo1())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global emergencyInfo2
        emergencyInfo2 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo2.insert(0, val)
        else:
            emergencyInfo2.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo2())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Home Address
        curr.execute("SELECT Address_Street FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global emergencyInfo3
        emergencyInfo3 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo3.insert(0, val)
        else:
            emergencyInfo3.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo3())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        curr.execute("SELECT Address_City FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global emergencyInfo4
        emergencyInfo4 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo4.insert(0, val)
        else:
            emergencyInfo4.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo4())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        curr.execute("SELECT Address_State FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nState ..................................................................................................... ")
        global emergencyInfo5
        emergencyInfo5 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo5.insert(0, val)
        else:
            emergencyInfo5.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo5())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        curr.execute("SELECT Address_Zip FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global emergencyInfo6
        emergencyInfo6 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo6.insert(0, val)
        else:
            emergencyInfo6.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo6())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Phone Number
        curr.execute("SELECT Phone_Home FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. ")
        global emergencyInfo7
        emergencyInfo7 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo7.insert(0, val)
        else:
            emergencyInfo7.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo7())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Cell Phone Number
        curr.execute("SELECT Phone_Cell FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... ")
        global emergencyInfo8
        emergencyInfo8 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo8.insert(0, val)
        else:
            emergencyInfo8.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo8())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Alternate Phone Number
        curr.execute("SELECT Phone_Alt FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        label = Label(self.ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... ")
        global emergencyInfo9
        emergencyInfo9 = Entry(self.ChildInfoSectionframe)

        if val is not None:
            emergencyInfo9.insert(0, val)
        else:
            emergencyInfo9.insert(0, 'Unanswered')

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateemergencyInfo9())

        r = r+1
        buttonUpdate.grid(row = r, column = 2)
        emergencyInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#H.E.R.O. Programs ************************************************************************************************************************
        #header               
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS\n")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Program(s) you wish your child to participate in
        label = Label(self.ChildInfoSectionframe, text = "Program(s) you wish your child to participate in .................................... ")
        r = r+1
        label.grid(row = r, column = 0)
            
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatePrograms0())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT HERO_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]

        #Super HEROes Program
        global programs0
        programs0 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Super HEROes Program", variable = programs0).grid(row = r,  column = 1, sticky = W)

        if 'Super HEROes Program' in var:
            programs0.set(1)

        #Bright HEROs Program
        global programs1
        programs1 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Bright HEROs Program", variable = programs1).grid(row = r,  column = 1, sticky = W)

        if 'Bright HEROs Program' in var:
            programs1.set(1)
            
        #Camp High Five
        global programs2
        programs2 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Camp High Five", variable = programs2).grid(row = r,  column = 1, sticky = W)

        if 'Camp High Five' in var:
            programs2.set(1)
            
        #Holiday of HEROs
        global programs3
        programs3 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Holiday of HEROs", variable = programs3).grid(row = r,  column = 1, sticky = W)

        if 'Holiday of HEROs' in var:
            programs3.set(1)
            
        #Transition to Adulthood
        global programs4
        programs4 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Transition to Adulthood", variable = programs4).grid(row = r,  column = 1, sticky = W)

        if 'Transition to Adulthood' in var:
            programs4.set(1)


    #Program(s) you would be interested in your child to participating in
        label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatePrograms1())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT Future_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]
        
        #Healthy HEROs (health curriculum)
        global programs5
        programs5 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Healthy HEROs", variable = programs5).grid(row = r,  column = 1, sticky = SW)

        if 'Healthy HEROs' in var:
            programs5.set(1)

        #Career Development/Job Readiness
        global programs6
        programs6 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Career Development/Job Readiness", variable = programs6).grid(row = r,  column = 1, sticky = W)

        if 'Career Development/Job Readiness' in var:
            programs6.set(1)
            
        #Other
        global programs7
        programs7 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Other", variable = programs7).grid(row = r,  column = 1, sticky = W)

        if 'Other' in var:
            programs7.set(1)

        #if other
        global programs8
        programs8 = Entry(self.ChildInfoSectionframe, width = 19)
        programs8.grid(row = r, column = 1, sticky = E)

        curr.execute("SELECT Future_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        if val is not None:
            programs8.insert(0, val)
        else:
            programs8.insert(0, 'Unanswered')
            
#Referral Needs ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Referral
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updateReferral())
        buttonUpdate.grid(row = r, column = 2)
        
        curr.execute("SELECT Referral FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]
        
        #Food
        global Referral0
        Referral0 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Food", variable = Referral0).grid(row = r,  column = 1, sticky = SW)

        if 'Healthy HEROs' in var:
            Referral0.set(1)

        #Transitional Housing/Shelter
        global Referral1
        Referral1 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Transitional Housing/Shelter", variable = Referral1).grid(row = r,  column = 1, sticky = W)

        if 'Transitional Housing/Shelter' in var:
            Referral1.set(1)

        #Rent/Utilities Assistance
        global Referral2
        Referral2 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Rent/Utilities Assistance", variable = Referral2).grid(row = r,  column = 1, sticky = W)

        if 'Rent/Utilities Assistance' in var:
            Referral2.set(1)

        #Clothing/Furniture
        global Referral3
        Referral3 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Clothing/Furniture", variable = Referral3).grid(row = r,  column = 1, sticky = W)

        if 'Clothing/Furniture' in var:
            Referral3.set(1)

        #Financial/Public Assistance
        global Referral4
        Referral4 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Financial/Public Assistance", variable = Referral4).grid(row = r,  column = 1, sticky = W)

        if 'Financial/Public Assistance' in var:
            Referral4.set(1)

        #Other
        global Referral5
        Referral5 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Other", variable = Referral5).grid(row = r,  column = 1, sticky = W)

        if 'Other' in var:
            Referral5.set(1)

        #if other
        global Referral6
        Referral6 = Entry(self.ChildInfoSectionframe, width = 19)
        Referral6.grid(row = r, column = 1, sticky = E)

        curr.execute("SELECT Referral_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        if val is not None:
            Referral6.insert(0, val)
        else:
            Referral6.insert(0, 'Unanswered')

#Statement of Understanding ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))
       
        #one
        label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... ")
        curr.execute("SELECT Statement_One FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement0
        statement0 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement0, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement0, value=2)

        if val is not None:
            if val is 0:
                statement0.set(2)
            else:
                statement0.set(1)

        r = r+1
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #two
        label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... ")
        curr.execute("SELECT Statement_Two FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement1
        statement1 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement1, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement1, value=2)

        if val is not None:
            if val is 0:
                statement1.set(2)
            else:
                statement1.set(1)
                
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #three
        label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... ")
        curr.execute("SELECT Statement_Three FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement2
        statement2 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement2, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement2, value=2)

        if val is not None:
            if val is 0:
                statement2.set(2)
            else:
                statement2.set(1)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #four
        label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... ")
        curr.execute("SELECT Statement_Four FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement3
        statement3 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement3, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement3, value=2)

        if val is not None:
            if val is 0:
                statement3.set(2)
            else:
                statement3.set(1)
                
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #five
        label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... ")
        curr.execute("SELECT Statement_Five FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement4
        statement4 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement4, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement4, value=2)

        if val is not None:
            if val is 0:
                statement4.set(2)
            else:
                statement4.set(1)
                
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #six
        label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... ")
        curr.execute("SELECT Statement_Six FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement5
        statement5 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement5, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement5, value=2)

        if val is not None:
            if val is 0:
                statement5.set(2)
            else:
                statement5.set(1)
                
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #seven
        label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... ")
        curr.execute("SELECT Statement_Seven FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]

        global statement6
        statement6 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement6, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement6, value=2)

        if val is not None:
            if val is 0:
                statement6.set(2)
            else:
                statement6.set(1)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

 #Signature ************************************************************************************************************************
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSIGNATURE")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. ")
        curr.execute("SELECT Statement_Seven FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        
        global signature
        signature = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = signature, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = signature, value=2)

        if val is not None:
            if val is 0:
                signature.set(2)
            else:
                signature.set(1)

        r = r+1
        buttonUpdate = Button(self.ChildInfoSectionframe, text = "Update", command = lambda:self.updatechildInfo3())
        buttonUpdate.grid(row = r, column = 2)
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
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


#Child Info ************************************************************************************************************************
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
        
        #feedback    
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

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
        
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

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
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

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
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo4(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo5(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_County = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Address_County = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo6(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Childs_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")

            
        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo7(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo7.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Home_Phone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Home_Phone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo8(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo8.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Guardian_Phone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Guardian_Phone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo9(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Guardian_Email = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Guardian_Email = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo10(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo10.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Age = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Childs_Information SET Age = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAge must be only numbers.")

    def updatechildInfo11(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo11.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Birthday = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Childs_Information SET Birthday = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo12(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo12.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Gender = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo13(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo13.get()
        curr.execute("UPDATE Childs_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo14(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo14.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Aware = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo15(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo15.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Why = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Why = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo16(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo16.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Referral_Source = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Referral_Source = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo17(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo17.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET School_attending = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET School_attending = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo18(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo18.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET School_grade_level = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET School_grade_level = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo19(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo19.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Ethnicity = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo20(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo20.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Ethnicity_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Ethnicity_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo21(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo21.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET ADD_ADHD = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo22(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo22.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Learning_Disability = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo23(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo23.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Developmental_Disability = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo24(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo24.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Mental_Health_Issues = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo25(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo25.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Other_Medical_Condition = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo26(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo26.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Victim_of_Abuse = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo27(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo27.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE Childs_Information SET Criminal_Justice_System = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo28(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo28.get()
        if newVal != '':
            curr.execute("UPDATE Childs_Information SET Legal_Custody = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatechildInfo29(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = childInfo29.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Childs_Information SET Custody_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Childs_Information SET Custody_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Parent Info ************************************************************************************************************************

    def updateparentInfo0(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo1(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo2(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Relationship_to_Child = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Relationship_to_Child = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo3(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Age = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Parent_Guardian_Information SET Age = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAge code must be only numbers.")

    def updateparentInfo4(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo4.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo5(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo5.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Adoptive_Parent = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo6(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo6.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Marital_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo7(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo7.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Education_Completed = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo8(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo8.get()
        if newVal != '':
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo9(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Company_Name = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Employment_Company_Name = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo10(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo10.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo11(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo11.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo12(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo12.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo13(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo13.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo14(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo14.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET WorkPhone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET WorkPhone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateparentInfo15(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = parentInfo15.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Parent_Guardian_Information SET Email = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Parent_Guardian_Information SET Email = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Absent Parent Info ************************************************************************************************************************

    def updateabsParentInfo0(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = absParentInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo1(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = absParentInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo2(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = absParentInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Telephone = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Telephone = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo3(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = absParentInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo4(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = absParentInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo5(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = absParentInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_County = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Absent_Parent_Information SET Address_County = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateabsParentInfo6(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = absParentInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Absent_Parent_Information SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")

    def updateabsParentInfo7(self):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = absParentInfo7.get()
        if newVal != '':
            curr.execute("UPDATE Absent_Parent_Information SET HIV_Status = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#Household Info ************************************************************************************************************************

    def updatehouseInfo(self, count):

        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        if count == 1:
            newVal0 = houseInfo10.get()
            newVal1 = houseInfo11.get()
            newVal2 = houseInfo12.get()
            newVal3 = houseInfo13.get()
            newVal4 = houseInfo14.get()

        elif count == 2:
            newVal0 = houseInfo20.get()
            newVal1 = houseInfo21.get()
            newVal2 = houseInfo22.get()
            newVal3 = houseInfo23.get()
            newVal4 = houseInfo24.get()

        elif count == 3:
            newVal0 = houseInfo30.get()
            newVal1 = houseInfo31.get()
            newVal2 = houseInfo32.get()
            newVal3 = houseInfo33.get()
            newVal4 = houseInfo34.get()

        elif count == 4:
            newVal0 = houseInfo40.get()
            newVal1 = houseInfo41.get()
            newVal2 = houseInfo42.get()
            newVal3 = houseInfo43.get()
            newVal4 = houseInfo44.get()

        elif count == 5:
            newVal0 = houseInfo50.get()
            newVal1 = houseInfo51.get()
            newVal2 = houseInfo52.get()
            newVal3 = houseInfo53.get()
            newVal4 = houseInfo54.get()

        elif count == 6:
            newVal0 = houseInfo60.get()
            newVal1 = houseInfo61.get()
            newVal2 = houseInfo62.get()
            newVal3 = houseInfo63.get()
            newVal4 = houseInfo64.get()

        if (newVal0 == 'Unanswered') or (newVal0 == ''):
            newVal0 = None
        
        if (newVal1 == 'Unanswered') or (newVal1 == ''):
            newVal1 = None

        if newVal2 == '':
            newVal2 = None

        goodData = 1
        if (newVal3 == 'Unanswered') or (newVal3 == ''):
            newVal3 = None
        elif (not self.is_number(newVal3)):
            goodData = 0
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nAge must be only numbers.")
            #stop input to database !!!!!!@#@@#!@

        if newVal4 == '':
            newVal4 = None


        if goodData:
            curr.execute("SELECT * FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count,))
            current = curr.fetchall()
            if current is ():
                curr.execute("""INSERT INTO Household_Information VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s);""", 
                    (id, date, count, newVal0, newVal1, newVal2, newVal3, newVal4,))
            else:
                curr.execute("""UPDATE Household_Information 
                    SET Name = %s, Relationship = %s, Sex = %s, Age = %s, HIV_Status = %s 
                    WHERE ID = %s AND Date_Submitted = %s AND Count = %s;""", 
                    (newVal0, newVal1, newVal2, newVal3, newVal4, id, date, count,))

            db.commit()
            
            #feedback
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        
        #Close Database Connection
        curr.close()
        db.close()

    def updatefamIncome0(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = famIncome0.get()
        if newVal != '':
            curr.execute("UPDATE Fam_Annual_Income SET Fam_Annual_Income = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatefamIncome1(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = famIncome1.get()
        if newVal != '':
            curr.execute("UPDATE Source_Fam_Income SET Source_Fam_Income = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatefamIncome2(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = famIncome2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Source_Fam_Income SET Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Source_Fam_Income SET Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

#In Case of Emergency Contact ************************************************************************************************************************
    def updateemergencyInfo0(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo0.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_First = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_First = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateemergencyInfo1(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo1.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_Last = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Name_Last = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateemergencyInfo2(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo2.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Relationship_to_Child = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Relationship_to_Child = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateemergencyInfo3(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo3.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Street = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Street = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateemergencyInfo4(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo4.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_City = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_City = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateemergencyInfo5(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo5.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 


    def updateemergencyInfo6(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo6.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Zip = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            db.commit()
        elif (self.is_number(newVal)):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Address_Zip = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            db.commit()
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nZip code must be only numbers.")

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateemergencyInfo7(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo7.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Home = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Home = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateemergencyInfo8(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo8.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Cell = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Cell = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close() 

    def updateemergencyInfo9(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = emergencyInfo9.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Alt = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE ChildApp_Emergency_Contact SET Phone_Alt = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updatePrograms0(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = ''

        if programs0.get():
            newVal = newVal + 'Super HEROes Program,'

        if programs1.get():
            newVal = newVal + 'Bright HEROs Program,'

        if programs2.get():
            newVal = newVal + 'Camp High Five,'

        if programs3.get():
            newVal = newVal + 'Holiday of HEROs,'

        if programs4.get():
            newVal = newVal + 'Transition to Adulthood,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET HERO_Programs = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET HERO_Programs = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        db.commit()
            
        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()


    def updatePrograms1(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = ''

        if programs5.get():
            newVal = newVal + 'Healthy HEROs,'

        if programs6.get():
            newVal = newVal + 'Career Development/Job Readiness,'

        if programs7.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET Future_Programs = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET Future_Programs = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))

        newValOther = programs8.get()
        if (newValOther == 'Unanswered') or (newValOther == ''):
            curr.execute("UPDATE Child_Application SET Future_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Child_Application SET Future_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newValOther, id, date,))
        
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()

    def updateReferral(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        #Execute
        newVal = ''

        if Referral0.get():
            newVal = newVal + 'Food,'

        if Referral1.get():
            newVal = newVal + 'Transitional Housing/Shelter,'

        if Referral2.get():
            newVal = newVal + 'Rent/Utilities Assistance,'

        if Referral3.get():
            newVal = newVal + 'Clothing/Furniture,'

        if Referral4.get():
            newVal = newVal + 'Financial/Public Assistance,'

        if Referral5.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE Child_Application SET Referral = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE Child_Application SET Referral = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))

        newValOther = Referral6.get()
        if (newValOther == 'Unanswered') or (newValOther == ''):
            curr.execute("UPDATE Child_Application SET Referral_Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            curr.execute("UPDATE Child_Application SET Referral_Other = %s WHERE ID = %s AND Date_Submitted = %s;", (newValOther, id, date,))
        
        db.commit()

        #feedback
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        curr.close()
        db.close()


    #check string entry is a number
    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    #check string entry is a date (YYYY-MM-DD)
    def is_date(self, s):
        if len(s) != 10:
            return False
        if (s[4] != s[7]) or (s[4] != '-') or (not self.is_number(s[0:4])) or (not self.is_number(s[5:7])) or (not self.is_number(s[-2:])):
            return False
        if (1 > int(s[0:4])) or (1 > int(s[5:7])) or (int(s[5:7]) > 12) or (1 > int(s[-2:])):
            return False
        if int(s[5:7]) == 02:
            if (int(s[-2:]) > 29):
                return False
        elif (int(s[5:7]) == 04) or (int(s[5:7]) == 06) or (int(s[5:7]) == 9) or (int(s[5:7]) == 11):
            if (int(s[-2:]) > 30): 
                return False
        elif int(s[-2:]) > 31:
            return False

        return True


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    master=tk.Tk()
    Example(master).pack(side="top", fill="both", expand=True)
    master.mainloop()
