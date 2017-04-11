import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
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

        master.title("Detailed Profile")

#size & centering
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        x = (master.winfo_screenwidth() // 2) - (width // 2)
        y = (master.winfo_screenheight() // 2) - (height // 2)
        master.geometry("740x1000")

        self.populate()

    def populate(self):

#Buttons
    #back button frame + back button
        self.buttonframe = Frame(self.frame)
        self.buttonframe.pack(side = "top", fill = "x")

        #fix alignment
        backButton = Button(self.buttonframe, text = "Back", command = self.back)
        backButton.pack(side = "left")

        #edit
        editButton = Button(self.buttonframe, text = "Edit Application", command = self.edit)
        editButton.pack(side = "right")

        #delete
        deleteButton = Button(self.buttonframe, text = "Delete Application", command = self.delete)
        deleteButton.pack(side = "right")

#figure out how to pass in parameters
        id = 1
        date = '2016-11-24'

#Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

#Database dump frame
        self.ChildInfoSectionframe = Frame(self.frame)
        self.ChildInfoSectionframe.pack(fill = 'y', side = 'left') 

#Identifying Info Section    
        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\nIDENTIFYING INFORMATION")
        labelChildInfoSection.pack(fill = "x")
        labelChildInfoSection.config(font=("Helvetica", 20))

        #id
        label = Label(self.ChildInfoSectionframe, text = "\nChild ID.................................................................................................. " + str(id))
        label.pack(anchor = 'w')

        #date
        label = Label(self.ChildInfoSectionframe, text = "\nDate Submitted...................................................................................... " + date)
        label.pack(anchor = 'w')
        
#Child info section
        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nCHILD'S INFORMATION")
        labelChildInfoSection.pack(fill = "x")
        labelChildInfoSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT Name_First FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #last name
        curr.execute("SELECT Name_Last FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name  ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
 
        #nickname
        curr.execute("SELECT Name_Nickname FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #address street
        curr.execute("SELECT Address_Street FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address city
        curr.execute("SELECT Address_City FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address county
        curr.execute("SELECT Address_County FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                
        #address zip
        curr.execute("SELECT Address_Zip FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #home phone
        curr.execute("SELECT Home_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #guardian phone
        curr.execute("SELECT Guardian_Phone FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #guardian email
        curr.execute("SELECT Guardian_Email FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #age
        curr.execute("SELECT Age FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                
        #birthday
        curr.execute("SELECT Birthday FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #gender
        curr.execute("SELECT Gender FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #HIV status
        curr.execute("SELECT HIV_Status FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #aware
        label = Label(self.ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.pack(anchor = 'w')
        curr.execute("SELECT Aware FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... Unanswered')
        label.pack(anchor = 'w')
        
        #why
        label = Label(self.ChildInfoSectionframe, text = "\nIf no,")
        label.pack(anchor = 'w')
        curr.execute("SELECT Why FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "please provide a reason why child is not aware ...................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "please provide a reason why child is not aware ...................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Referral source
        curr.execute("SELECT Referral_Source FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #school attending
        curr.execute("SELECT School_attending FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Grade Level
        curr.execute("SELECT School_grade_level FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Ethnicity
        curr.execute("SELECT Ethnicity_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        ethnicityOther = curr.fetchall()[0][0]
        if ethnicityOther is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... " + ethnicityOther)
        else:
            curr.execute("SELECT Ethnicity FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            ethnicity = curr.fetchall()[0][0]
            if ethnicity is not None:
                label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... " + ethnicity)
            else:
                label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Even been...
        label = Label(self.ChildInfoSectionframe, text = "\nHas your child ever been...")
        label.pack(anchor = 'w')

        #ADD_ADHD
        curr.execute("SELECT ADD_ADHD FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. Unanswered')
        label.pack(anchor = 'w')
        
        #Learning_Disability
        curr.execute("SELECT Learning_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... Unanswered')
        label.pack(anchor = 'w')
        
        #Developmental_Disability
        curr.execute("SELECT Developmental_Disability FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... Unanswered')
        label.pack(anchor = 'w')
        
        #Mental_Health_Issues
        curr.execute("SELECT Mental_Health_Issues FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. Unanswered')
        label.pack(anchor = 'w')
        
        #Other_Medical_Condition
        curr.execute("SELECT Other_Medical_Condition FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... Unanswered')
        label.pack(anchor = 'w')
        
        #Victim_of_Abuse
        curr.execute("SELECT Victim_of_Abuse FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... Unanswered')
        label.pack(anchor = 'w')
        
        #Criminal_Justice_System
        curr.execute("SELECT Criminal_Justice_System FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... Yes')
            else:
                label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... No')
        else:
            label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... Unanswered')
        label.pack(anchor = 'w')
        
        #Custody
        curr.execute("SELECT Custody_Other FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        custodyOther = curr.fetchall()[0][0]
        if custodyOther is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... " + custodyOther)
        else:
            curr.execute("SELECT Legal_Custody FROM Childs_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            custody = curr.fetchall()[0][0]
            if custody is not None:
                label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... " + custody)
            else:
                label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... Unanswered")
        label.pack(anchor = 'w')


#Parent/ Guardian Section
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Last Name
        curr.execute("SELECT Name_Last FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Relationship to child
        curr.execute("SELECT Relationship_to_Child FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Age
        curr.execute("SELECT Age FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #HIV Status
        curr.execute("SELECT HIV_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Adoptive Parent
        curr.execute("SELECT Adoptive_Parent FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... Unanswered")
        label.pack(anchor = 'w')
                
        #Marital Status
        curr.execute("SELECT Marital_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Highest Level of Education Completed
        curr.execute("SELECT Education_Completed FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Employment Status
        curr.execute("SELECT Employment_Status FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Employment Company
        label = Label(self.ChildInfoSectionframe, text = "\nIf employed,")
        label.pack(anchor = 'w')
        
        curr.execute("SELECT Employment_Company_Name FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "please provide Company Name ............................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "please provide Company Name ............................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Address
        curr.execute("SELECT Address_Street FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAddress ................................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAddress ................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #City
        curr.execute("SELECT Address_City FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #State
        curr.execute("SELECT Address_State FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nState .................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nState .................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Zip
        curr.execute("SELECT Address_Zip FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Work Phone
        curr.execute("SELECT WorkPhone FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #E-mail
        curr.execute("SELECT Email FROM Parent_Guardian_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nE-mail ................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nE-mail ................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        

#Absent Parent Info
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Last Name
        curr.execute("SELECT Name_Last FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Telephone
        curr.execute("SELECT Telephone FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nTelephone .............................................................................................. " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nTelephone .............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Home Address
        curr.execute("SELECT Address_Street FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #City
        curr.execute("SELECT Address_City FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #County
        curr.execute("SELECT Address_County FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Zip
        curr.execute("SELECT Address_Zip FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ......................................................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ......................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #HIV Status
        curr.execute("SELECT HIV_Status FROM Absent_Parent_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
#Household Info
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nHOUSEHOLD INFORMATION")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #list all individuals living in the household
        label = Label(self.ChildInfoSectionframe, text = "\nAll Individuals Living in the Household")
        label.pack(anchor = 'w')

        curr.execute("SELECT Count FROM Household_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        countArr = curr.fetchall()
        for count in countArr:
            #Name
            curr.execute("SELECT Name FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... " + val)
            else:
                label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... Unanswered")
            label.pack(anchor = 'w')
                    
            #Relationship to Child
            curr.execute("SELECT Relationship FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. " + val)
            else:
                label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. Unanswered")
            label.pack(anchor = 'w')
                                
            #Sex
            curr.execute("SELECT Sex FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... " + val)
            else:
                label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... Unanswered")
            label.pack(anchor = 'w')
                                
            #Age
            curr.execute("SELECT Age FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... " + str(val))
            else:
                label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... Unanswered")
            label.pack(anchor = 'w')
                    
            #HIV Status
            curr.execute("SELECT HIV_Status FROM Household_Information WHERE ID = %s AND Date_Submitted = %s AND Count = %s;", (id, date, count[0]))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ " + str(val) + "\n")
            else:
                label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ Unanswered\n")
            label.pack(anchor = 'w')
                    
        #Family Annual Income Info
        curr.execute("SELECT Fam_Annual_Income FROM Fam_Annual_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Source of Family Income
        curr.execute("SELECT Other FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        sourceOther = curr.fetchall()[0][0]
        if sourceOther is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... " + sourceOther)
        else:
            curr.execute("SELECT Source_Fam_Income FROM Source_Fam_Income WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            source = curr.fetchall()[0][0]
            if source is not None:
                label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... " + source)
            else:
                label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... Unanswered")
        label.pack(anchor = 'w')

            
 #In Case of Emergency Contact
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #First Name
        curr.execute("SELECT Name_First FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #Last Name
        curr.execute("SELECT Name_Last FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................ " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
        #Relationship to Child
        curr.execute("SELECT Relationship_to_Child FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nRelationship to Child ............................................................................. " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nRelationship to Child ............................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #Home Address
        curr.execute("SELECT Address_Street FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #City
        curr.execute("SELECT Address_City FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #State
        curr.execute("SELECT Address_State FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nState ..................................................................................................... " + val)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nState ..................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Zip
        curr.execute("SELECT Address_Zip FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
        #Home Phone Number
        curr.execute("SELECT Phone_Home FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #Cell Phone Number
        curr.execute("SELECT Phone_Cell FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Alternate Phone Number
        curr.execute("SELECT Phone_Alt FROM ChildApp_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... " + str(val))
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
#H.E.R.O. Programs
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #Program(s) you wish your child to participate in
        curr.execute("SELECT HERO_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        var = curr.fetchall()[0][0]
        if var is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you wish your child to participate in .................................... " + var)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you wish your child to participate in .................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Program(s) you would be interested in your child to participating in
        curr.execute("SELECT Future_Programs FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        programs = curr.fetchall()[0][0]
        curr.execute("SELECT Future_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        otherPrograms = curr.fetchall()[0][0]
        if programs is not None and otherPrograms is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... " + programs + ", " + otherPrograms)
        elif programs is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... " + programs)
        elif otherPrograms is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... " + otherPrograms)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... Unanswered")
        label.pack(anchor = 'w')
                    
#Referral Needs
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #Needs
        curr.execute("SELECT Referral FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        Referral = curr.fetchall()[0][0]
        curr.execute("SELECT Referral_Other FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        otherReferral = curr.fetchall()[0][0]
        if Referral is not None and otherReferral is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... " + Referral + ", " + otherReferral)
        elif Referral is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... " + Referral)
        elif otherReferral is not None:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ........................................................................................ " + otherReferral)
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ........................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
#Statement of Understanding
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))
        
        #one
        curr.execute("SELECT Statement_One FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #two
        curr.execute("SELECT Statement_Two FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #three
        curr.execute("SELECT Statement_Three FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #four
        curr.execute("SELECT Statement_Four FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #five
        curr.execute("SELECT Statement_Five FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #six
        curr.execute("SELECT Statement_Six FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #seven
        curr.execute("SELECT Statement_Seven FROM Statement_Of_Understanding WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
#Signature
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSIGNATURE")
        labelParentInfoSection.pack(fill = "x")
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        curr.execute("SELECT Signature FROM Child_Application WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. Signed")
            else:
                label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. Unsigned")
        else:
            label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
#Close Database Connection
        curr.close()
        db.close()

    def back(self):
        #Go back to 1st level profile page
        self.master.destroy()

    def edit(self):
        #Go to edit profile page
        self.master.destroy()

    def delete(self):
        if askyesno('Verify', 'Really delete?'):
            #Delete application from database

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
            #Delete cancelled
            showinfo('No', 'Delete has been cancelled')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    master=tk.Tk()
    Example(master).pack(side="top", fill="both", expand=True)
    master.mainloop()
