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

        master.title("New Applicaion")

#size & centering
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        x = (master.winfo_screenwidth() // 2) - (width // 2)
        y = (master.winfo_screenheight() // 2) - (height // 2)
        master.geometry("850x1000")

#TODO
    #figure out how to pass in parameters
        global id
        global date
        id = 2
        date = '2016-12-12'
        
#Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()
        
#Top Buttons
    #back button frame + back button
        self.buttonframe = Frame(self.frame)
        self.buttonframe.pack(side = "top", fill = "x")

        #fix alignment
        backButton = Button(self.buttonframe, text = "Back", command = self.back)
        backButton.pack(side = "left")

#Child info section
        self.ChildInfoSectionframe = Frame(self.frame)
        self.ChildInfoSectionframe.pack(fill = 'y', side = 'left') 
        r = 0

        #header
        labelChildInfoSection = Label(self.ChildInfoSectionframe, text = "\nCHILD'S INFORMATION")
        labelChildInfoSection.grid(row = r, column = 0)
        labelChildInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global childInfo0
        childInfo0 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global childInfo1
        childInfo1 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #nickname
        label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. ")
        global childInfo2
        childInfo2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global childInfo3
        childInfo3 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global childInfo4
        childInfo4 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global childInfo5
        childInfo5 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global childInfo6
        childInfo6 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #home phone
        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... ")
        global childInfo7
        childInfo7 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian phone
        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ ")
        global childInfo8
        childInfo8 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #guardian email
        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... ")
        global childInfo9
        childInfo9 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global childInfo10
        childInfo10 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #birthday
        label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ................................................................ ")
        global childInfo11
        childInfo11 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. ")
        global childInfo12
        childInfo12 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo12, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")
        global childInfo13
        childInfo13 = StringVar()
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo13, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #aware
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... ')
        global childInfo14
        childInfo14 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo14, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo14, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #why
        label = Label(self.ChildInfoSectionframe, text = "If no, please provide a reason why child is not aware .............................. ")
        global childInfo15
        childInfo15 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Referral source
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... ")
        global childInfo16
        childInfo16 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #school attending
        label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. ")
        global childInfo17
        childInfo17 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Grade Level
        label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... ")
        global childInfo18
        childInfo18 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo18.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Ethnicity
        label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... ")
        global childInfo19
        childInfo19 = StringVar()
        choices = ['White/Caucasian','Black/African-American','Hispanic/Latino',
        'Native American','Asian/Pacific Islander/Indian Sub-Continent','Multi-racial','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo19, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Ethnicity Other
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global childInfo20
        childInfo20 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Even been...
        label = Label(self.ChildInfoSectionframe, text = "\nHas your child ever been...")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #ADD_ADHD
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. ')
        global childInfo21
        childInfo21 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo21, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo21, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)
        
        #Learning_Disability
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a learning disability? .................................................... ')
        global childInfo22
        childInfo22 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo22, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo22, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Developmental_Disability
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with a developmental disability? .......................................... ')
        global childInfo23
        childInfo23 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo23, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo23, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Mental_Health_Issues
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with any mental health issues? ............................................. ')
        global childInfo24
        childInfo24 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo24, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo24, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Other_Medical_Condition
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed or suffered from any other medical condition? ..................... ')
        global childInfo25
        childInfo25 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo25, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo25, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Victim_of_Abuse
        label = Label(self.ChildInfoSectionframe, text = 'A victim of sexual abuse, physical or emotional abuse? ......................... ')
        global childInfo26
        childInfo26 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo26, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo26, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Criminal_Justice_System
        label = Label(self.ChildInfoSectionframe, text = 'Part of the criminal justice system? ...................................................... ')
        global childInfo27
        childInfo27 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo27, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo27, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Custody
        label = Label(self.ChildInfoSectionframe, text = "\nWho has legal custody of the child? ...................................................... ")
        global childInfo28
        childInfo28 = StringVar()
        choices = ['Mother','Father','Both Parents','Aunt/Uncle','Grandparent','Pending Court Action','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, childInfo28, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Custody Other
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global childInfo29
        childInfo29 = Entry(self.ChildInfoSectionframe)

        r = r+1
        childInfo29.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Section
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nPARENT/GUARDIAN INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global parentInfo0
        parentInfo0 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global parentInfo1
        parentInfo1 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global parentInfo2
        parentInfo2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Age
        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global parentInfo3
        parentInfo3 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)       
        
        #HIV Status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ ")
        global parentInfo4
        parentInfo4 =  StringVar()
        choices = ['HIV Positive','HIV Negative']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo4, *choices)
        
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Adoptive Parent
        label = Label(self.ChildInfoSectionframe, text = "\nAdoptive Parent ..................................................................................... ")
        global parentInfo5
        parentInfo5 = StringVar()
        choices = ['Yes','No','Not Applicable']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo5, *choices)
        
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Marital Status
        label = Label(self.ChildInfoSectionframe, text = "\nMarital Status ...................................................................................... ")
        global parentInfo6
        parentInfo6 = StringVar()
        choices = ['Married','Single','Separated','Divorced','Widowed']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo6, *choices)
        
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Highest Level of Education Completed
        label = Label(self.ChildInfoSectionframe, text = "\nHighest Level of Education Completed .................................................. ")
        global parentInfo7
        parentInfo7 = StringVar()
        choices = ['HS','GED','Some College','Associates Degree','Bachelor Degree','Master Degree','Doctorate']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo7, *choices)
        
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Status
        label = Label(self.ChildInfoSectionframe, text = "\nEmployment Status ............................................................................... ")
        global parentInfo8
        parentInfo8 = StringVar()
        choices = ['Full-Time','Part-Time','Unemployed','Disability']
        option = tk.OptionMenu(self.ChildInfoSectionframe, parentInfo8, *choices)
        
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Employment Company
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = "\nIf employed,")
        label.grid(row = r, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = "please provide Company Name ............................................................. ")
        global parentInfo9
        parentInfo9 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Address
        label = Label(self.ChildInfoSectionframe, text = "\nAddress ................................................................................................ ")
        global parentInfo10
        parentInfo10 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global parentInfo11
        parentInfo11 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        label = Label(self.ChildInfoSectionframe, text = "\nState .................................................................................................... ")
        global parentInfo12
        parentInfo12 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global parentInfo13
        parentInfo13 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Work Phone
        label = Label(self.ChildInfoSectionframe, text = "\nWork Phone .......................................................................................... ")
        global parentInfo14
        parentInfo14 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #E-mail
        label = Label(self.ChildInfoSectionframe, text = "\nE-mail ................................................................................................... ")
        global parentInfo15
        parentInfo15 = Entry(self.ChildInfoSectionframe)

        r = r+1
        parentInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Absent Parent Info
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nABSENT PARENT INFORMATION")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global absParentInfo0
        absParentInfo0 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global absParentInfo1
        absParentInfo1 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Telephone
        label = Label(self.ChildInfoSectionframe, text = "\nTelephone .............................................................................................. ")
        global absParentInfo2
        absParentInfo2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global absParentInfo3
        absParentInfo3 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global absParentInfo4
        absParentInfo4 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #County
        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global absParentInfo5
        absParentInfo5 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ......................................................................................................... ")
        global absParentInfo6
        absParentInfo6 = Entry(self.ChildInfoSectionframe)

        r = r+1
        absParentInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV Status ............................................................................................ ")
        global absParentInfo7
        absParentInfo7 =  StringVar()
        choices = ['HIV Positive','HIV Negative', 'Unkown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, absParentInfo7, *choices)
        
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

#Household Info
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
        
        #Name1
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo10
        houseInfo10 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child1
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo11
        houseInfo11 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex1
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo12
        houseInfo12 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo12, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age1
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo13
        houseInfo13 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status1
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo14
        houseInfo14 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo14, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person2
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 2')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name2
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo20
        houseInfo20 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child2
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo21
        houseInfo21 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex2
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo22
        houseInfo22 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo22, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age2
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo23
        houseInfo23 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status2
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo24
        houseInfo24 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo24, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person3
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 3')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name3
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo30
        houseInfo30 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child3
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo31
        houseInfo31 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex3
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo32
        houseInfo32 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo32, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age3
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo33
        houseInfo33 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo33.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status3
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo34
        houseInfo34 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo34, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person4
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 4')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name4
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo40
        houseInfo40 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo40.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child4
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo41
        houseInfo41 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex4
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo42
        houseInfo42 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo42, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age4
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo43
        houseInfo43 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo43.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status4
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo44
        houseInfo44 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo44, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0) 


    #person5
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 5')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name5
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo50
        houseInfo50 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo50.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child5
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo51
        houseInfo51 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex5
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo52
        houseInfo52 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo52, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age5
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo53
        houseInfo53 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo53.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status5
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo54
        houseInfo54 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo54, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)


    #person6
        r = r+1
        label = Label(self.ChildInfoSectionframe, text = '\nPerson 6')
        label.grid(row = r, column = 0, sticky = 'w')
        
        #Name6
        label = Label(self.ChildInfoSectionframe, text = "Name .................................................................................................... ")
        global houseInfo60
        houseInfo60 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo60.grid(row = r, column = 1)
        label.grid(row = r, column = 0)        

        #Relationship to Child6
        label = Label(self.ChildInfoSectionframe, text = "Relationship to Child ............................................................................. ")
        global houseInfo61
        houseInfo61 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Sex6
        label = Label(self.ChildInfoSectionframe, text = "Sex ....................................................................................................... ")
        global houseInfo62
        houseInfo62 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo62, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Age6
        label = Label(self.ChildInfoSectionframe, text = "Age ....................................................................................................... ")
        global houseInfo63
        houseInfo63 = Entry(self.ChildInfoSectionframe)

        r = r+1
        houseInfo63.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HIV Status6
        label = Label(self.ChildInfoSectionframe, text = "HIV Status ............................................................................................ ")
        global houseInfo64
        houseInfo64 = StringVar()
        choices = ['HIV Positive','HIV Negative','Unknown']
        option = tk.OptionMenu(self.ChildInfoSectionframe, houseInfo64, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Family Annual Income Info
        label = Label(self.ChildInfoSectionframe, text = "\nFamily Annual Income Information ......................................................... ")
        global famIncome0
        famIncome0 = StringVar()
        choices = ['$0-10,000','$10,001-15,000','$15,001-20,000','$20,000-25,000','$25,001-30,000','$30,001-35,000','$35,001-40,000','$40,001-45,000','$50,000+']
        option = tk.OptionMenu(self.ChildInfoSectionframe, famIncome0, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income
        label = Label(self.ChildInfoSectionframe, text = "\nSource of Family Income ....................................................................... ")
        global famIncome1
        famIncome1 = StringVar()
        choices = ['Employment','Government Support','Public Assistance', 'Unemployment Benefits','Medicaid','Social Security','Veterans Benefits','Other']
        option = tk.OptionMenu(self.ChildInfoSectionframe, famIncome1, *choices)

        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Source of Family Income Other
        label = Label(self.ChildInfoSectionframe, text = "If Other ................................................................................................. ")
        global famIncome2
        famIncome2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        famIncome2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#In Case of Emergency Contact
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nIN CASE OF EMERGENCY CONTACT")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global emergencyInfo0
        emergencyInfo0 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global emergencyInfo1
        emergencyInfo1 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship to child
        label = Label(self.ChildInfoSectionframe, text = "\nRelationship to child ............................................................................. ")
        global emergencyInfo2
        emergencyInfo2 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Address
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global emergencyInfo3
        emergencyInfo3 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #City
        label = Label(self.ChildInfoSectionframe, text = "\nCity ...................................................................................................... ")
        global emergencyInfo4
        emergencyInfo4 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #State
        label = Label(self.ChildInfoSectionframe, text = "\nState ..................................................................................................... ")
        global emergencyInfo5
        emergencyInfo5 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global emergencyInfo6
        emergencyInfo6 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Home Phone Number
        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone Number ............................................................................. ")
        global emergencyInfo7
        emergencyInfo7 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Cell Phone Number
        label = Label(self.ChildInfoSectionframe, text = "\nCell Phone Number ............................................................................... ")
        global emergencyInfo8
        emergencyInfo8 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Alternate Phone Number
        label = Label(self.ChildInfoSectionframe, text = "\nAlternate Phone Number ....................................................................... ")
        global emergencyInfo9
        emergencyInfo9 = Entry(self.ChildInfoSectionframe)

        r = r+1
        emergencyInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#H.E.R.O. Programs
        #header               
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nH.E.R.O. FOR CHILDREN PROGRAMS\n")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Program(s) you wish your child to participate in
        label = Label(self.ChildInfoSectionframe, text = "Program(s) you wish your child to participate in .................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Super HEROes Program
        global programs0
        programs0 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Super HEROes Program", variable = programs0).grid(row = r,  column = 1, sticky = W)

        #Bright HEROs Program
        global programs1
        programs1 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Bright HEROs Program", variable = programs1).grid(row = r,  column = 1, sticky = W)

        #Camp High Five
        global programs2
        programs2 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Camp High Five", variable = programs2).grid(row = r,  column = 1, sticky = W)

        #Holiday of HEROs
        global programs3
        programs3 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Holiday of HEROs", variable = programs3).grid(row = r,  column = 1, sticky = W)

        #Transition to Adulthood
        global programs4
        programs4 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Transition to Adulthood", variable = programs4).grid(row = r,  column = 1, sticky = W)

    #Program(s) you would be interested in your child to participating in
        label = Label(self.ChildInfoSectionframe, text = "\nProgram(s) you would be interested in your child to participating in ...... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Healthy HEROs (health curriculum)
        global programs5
        programs5 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Healthy HEROs", variable = programs5).grid(row = r,  column = 1, sticky = SW)

        #Career Development/Job Readiness
        global programs6
        programs6 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Career Development/Job Readiness", variable = programs6).grid(row = r,  column = 1, sticky = W)

        #Other
        global programs7
        programs7 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Other", variable = programs7).grid(row = r,  column = 1, sticky = W)

        global programs8
        programs8 = Entry(self.ChildInfoSectionframe, width = 19)
        programs8.grid(row = r, column = 1, sticky = E)

#Referral Needs
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nREFERRAL NEEDS")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

    #Referral
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Needs ....................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Food
        global Referral0
        Referral0 = IntVar()
        Checkbutton(self.ChildInfoSectionframe, text="Food", variable = Referral0).grid(row = r,  column = 1, sticky = SW)

        #Transitional Housing/Shelter
        global Referral1
        Referral1 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Transitional Housing/Shelter", variable = Referral1).grid(row = r,  column = 1, sticky = W)

        #Rent/Utilities Assistance
        global Referral2
        Referral2 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Rent/Utilities Assistance", variable = Referral2).grid(row = r,  column = 1, sticky = W)

        #Clothing/Furniture
        global Referral3
        Referral3 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Clothing/Furniture", variable = Referral3).grid(row = r,  column = 1, sticky = W)

        #Financial/Public Assistance
        global Referral4
        Referral4 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Financial/Public Assistance", variable = Referral4).grid(row = r,  column = 1, sticky = W)

        #Other
        global Referral5
        Referral5 = IntVar()
        r = r+1
        Checkbutton(self.ChildInfoSectionframe, text="Other", variable = Referral5).grid(row = r,  column = 1, sticky = W)
        
        global Referral6
        Referral6 = Entry(self.ChildInfoSectionframe, width = 19)
        Referral6.grid(row = r, column = 1, sticky = E)

#Statement of Understanding
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSTATEMENT OF UNDERSTANDING")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #one
        label = Label(self.ChildInfoSectionframe, text = "Statement 1 ........................................................................................... ")
        global statement0
        statement0 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement0, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement0, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #two
        label = Label(self.ChildInfoSectionframe, text = "Statement 2 .......................................................................................... ")
        global statement1
        statement1 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement1, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement1, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #three
        label = Label(self.ChildInfoSectionframe, text = "Statement 3 .......................................................................................... ")
        global statement2
        statement2 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement2, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement2, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #four
        label = Label(self.ChildInfoSectionframe, text = "Statement 4 .......................................................................................... ")
        global statement3
        statement3 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement3, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement3, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #five
        label = Label(self.ChildInfoSectionframe, text = "Statement 5 .......................................................................................... ")
        global statement4
        statement4 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement4, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement4, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #six
        label = Label(self.ChildInfoSectionframe, text = "Statement 6 .......................................................................................... ")
        global statement5
        statement5 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement5, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement5, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #seven
        label = Label(self.ChildInfoSectionframe, text = "Statement 7 .......................................................................................... ")
        global statement6
        statement6 = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = statement6, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = statement6, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#Signature
        #header
        labelParentInfoSection = Label(self.ChildInfoSectionframe, text = "\n\nSIGNATURE")
        r = r+1
        labelParentInfoSection.grid(row = r, column = 0)
        labelParentInfoSection.config(font=("Helvetica", 20))

        #signature completed
        label = Label(self.ChildInfoSectionframe, text = "\nSignature .............................................................................................. ")
        global signature
        signature = IntVar()
        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = signature, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = signature, value=2)

        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)



#Submit Button
        r = r+1
        submitProfileButton = Button(self.ChildInfoSectionframe, text = "Submit Profile", command = lambda:self.submitProfile())
        submitProfileButton.grid(sticky = 'w, e', row = r, columnspan = 2)

#Close Database Connection
        curr.close()
        db.close()

#Button Definitions
    def back(self):
        if askyesno('Verify', '\nAre you sure you want to leave this page?\nYour work will not be saved.'):
            #Go back to 1st level profile page (call back if you can)
            self.master.destroy()


    def submitProfile(self):
        #Open Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", passwd="Darling", db="HERO" )
        curr = db.cursor()

        success = 1
        goodData = 1

#adapt for database

#Child App
        
        #wish
        programsA = ''

        if programs0.get():
            programsA = programsA + 'Super HEROes Program,'

        if programs1.get():
            programsA = programsA + 'Bright HEROs Program,'

        if programs2.get():
            programsA = programsA + 'Camp High Five,'

        if programs3.get():
            programsA = programsA + 'Holiday of HEROs,'

        if programs4.get():
            programsA = programsA + 'Transition to Adulthood,'

        if programsA == '':
            programsA = None
        else:
            programsA = programsA[:-1]

        #future
        programsB = ''

        if programs5.get():
            programsB = programsB + 'Healthy HEROs,'

        if programs6.get():
            programsB = programsB + 'Career Development/Job Readiness,'

        if programs7.get():
            programsB = programsB + 'Other,'

        if programsB == '':
            programsB = None
        else:
            programsB = programsB[:-1]


        programsOther = programs8.get()
        if programsOther == '':
            programsOther = None


        #Referral 
        programsC = ''

        if Referral0.get():
            programsC = programsC + 'Food,'

        if Referral1.get():
            programsC = programsC + 'Transitional Housing/Shelter,'

        if Referral2.get():
            programsC = programsC + 'Rent/Utilities Assistance,'

        if Referral3.get():
            programsC = programsC + 'Clothing/Furniture,'

        if Referral4.get():
            programsC = programsC + 'Financial/Public Assistance,'

        if Referral5.get():
            programsC = programsC + 'Other,'

        if programsC == '':
            programsC = None
        else:
            programsC = programsC[:-1]

        ReferralOther = Referral6.get()
        if ReferralOther == '':
            ReferralOther = None

        #Signature
        sig = signature.get()
        if sig == 0:
            sig = None
        elif sig == 2:
            sig = 0
   
#Child's Information

        cI0 = childInfo0.get()
        if cI0 == '':
            cI0 = None

        cI1 = childInfo1.get()
        if cI1 == '':
            cI1 = None

        cI2 = childInfo2.get()
        if cI2 == '':
            cI2 = None        

        cI3 = childInfo3.get()
        if cI3 == '':
            cI3 = None

        cI4 = childInfo4.get()
        if cI4 == '':
            cI4 = None

        cI5 = childInfo5.get()
        if cI5 == '':
            cI5 = None

        cI6 = childInfo6.get()
        if cI6 != '':
            if self.is_number(cI6):
                cI6 = int(cI6)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Child's Information\n\nZip code must be only numbers.")
                goodData = 0
        else:
            cI6 = None


        cI7 = childInfo7.get()
        if cI7 == '':
            cI7 = None

        cI8 = childInfo8.get()
        if cI8 == '':
            cI8 = None
            
        cI9 = childInfo9.get()
        if cI9 == '':
            cI9 = None

        cI10 = childInfo10.get()
        if cI10 != '':
            if self.is_number(cI10):
                cI10 = int(cI10)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Child's Information\n\nAge must be only numbers.")
                goodData = 0
        else:
            cI10 = None

        cI11 = childInfo11.get()
        if cI11 != '':
            if not self.is_date(cI11):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Child's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            cI11 = None

        cI12 = childInfo12.get()
        if cI12 == '':
            cI12 = None

        cI13 = childInfo13.get()
        if cI13 == '':
            cI13 = None

        cI14 = childInfo14.get()
        if cI14 == 0:
            cI14 = None
        elif cI14 == 2:
            cI14 = 0

        cI15 = childInfo15.get()
        if cI15 == '':
            cI15 = None

        cI16 = childInfo16.get()
        if cI16 == '':
            cI16 = None

        cI17 = childInfo17.get()
        if cI17 == '':
            cI17 = None

        cI18 = childInfo18.get()
        if cI18 == '':
            cI18 = None

        cI19 = childInfo19.get()
        if cI19 == '':
            cI19 = None

        cI20 = childInfo20.get()
        if cI20 == '':
            cI20 = None

        cI21 = childInfo21.get()
        if cI21 == 0:
            cI21 = None
        elif cI21 == 2:
            cI21 = 0

        cI22 = childInfo22.get()
        if cI22 == 0:
            cI22 = None
        elif cI22 == 2:
            cI22 = 0

        cI23 = childInfo23.get()
        if cI23 == 0:
            cI23 = None
        elif cI23 == 2:
            cI23 = 0

        cI24 = childInfo24.get()
        if cI24 == 0:
            cI24 = None
        elif cI24 == 2:
            cI24 = 0

        cI25 = childInfo25.get()
        if cI25 == 0:
            cI25 = None
        elif cI25 == 2:
            cI25 = 0

        cI26 = childInfo26.get()
        if cI26 == 0:
            cI26 = None
        elif cI26 == 2:
            cI26 = 0

        cI27 = childInfo27.get()
        if cI27 == 0:
            cI27 = None
        elif cI27 == 2:
            cI27 = 0

        cI28 = childInfo28.get()
        if cI28 == '':
            cI28 = None

        cI29 = childInfo29.get()
        if cI29 == '':
            cI29 = None

#Parent/ Guardian's Information
        #adapt for database

        pI0 = parentInfo0.get()
        if pI0 == '':
            pI0 = None

        pI1 = parentInfo1.get()
        if pI1 == '':
            pI1 = None

        pI2 = parentInfo2.get()
        if pI2 == '':
            pI2 = None

        pI3 = parentInfo3.get()
        if pI3 != '':
            if self.is_number(pI3):
                pI3 = int(pI3)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Parent/Guardian Information\n\nAge must be only numbers.")
                goodData = 0
        else:
            pI3 = None

        pI4 = parentInfo4.get()
        if pI4 == '':
            pI4 = None

        pI5 = parentInfo5.get()
        if pI5 == '':
            pI5 = None

        pI6 = parentInfo6.get()
        if pI6 == '':
            pI6 = None

        pI7 = parentInfo7.get()
        if pI7 == '':
            pI7 = None

        pI8 = parentInfo8.get()
        if pI8 == '':
            pI8 = None

        pI9 = parentInfo9.get()
        if pI9 == '':
            pI9 = None

        pI10 = parentInfo10.get()
        if pI10 == '':
            pI10 = None

        pI11 = parentInfo11.get()
        if pI11 == '':
            pI11 = None

        pI12 = parentInfo12.get()
        if pI12 == '':
            pI12 = None

        pI13 = parentInfo13.get()
        if pI13 != '':
            if self.is_number(pI13):
                pI13 = int(pI13)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Parent/Guardian Information\n\nZip must be only numbers.")
                goodData = 0
        else:
            pI13 = None

        pI14 = parentInfo14.get()
        if pI14 == '':
            pI14 = None

        pI15 = parentInfo15.get()
        if pI15 == '':
            pI15 = None
        

#Absent Parent's Information
        #adapt for database

        abs0 = absParentInfo0.get()
        if abs0 == '':
            abs0 = None

        abs1 = absParentInfo1.get()
        if abs1 == '':
            abs1 = None            

        abs2 = absParentInfo2.get()
        if abs2 == '':
            abs2 = None  

        abs3 = absParentInfo3.get()
        if abs3 == '':
            abs3 = None

        abs4 = absParentInfo4.get()
        if abs4 == '':
            abs4 = None  

        abs5 = absParentInfo5.get()
        if abs5 == '':
            abs5 = None  

        abs6 = absParentInfo6.get()
        if abs6 != '':
            if self.is_number(abs6):
                abs6 = int(abs6)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Absent Parent Information\n\nZip must be only numbers.")
                goodData = 0
        else:
            abs6 = None

        abs7 = absParentInfo7.get()
        if abs7 == '':
            abs7 = None  


#Household Information
        #adapt for database
        person1 = 0
        person2 = 0
        person3 = 0
        person4 = 0
        person5 = 0
        person6 = 0

        #person 1
        house10 = houseInfo10.get()
        if house10 != '':
            person1 = 1

            house11 = houseInfo11.get()
            if house11 == '':
                house11 = None  
            
            house12 = houseInfo12.get()
            if house12 == '':
                house12 = None  
            
            house13 = houseInfo13.get()
            if house13 != '':
                if self.is_number(house13):
                    house13 = int(house13)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house13 = None
            
            house14 = houseInfo14.get()
            if house14 == '':
                house14 = None 

        #person 2
        house20 = houseInfo20.get()
        if house20 != '':
            person2 = 1

            house21 = houseInfo21.get()
            if house21 == '':
                house21 = None  
            
            house22 = houseInfo22.get()
            if house22 == '':
                house22 = None  
            
            house23 = houseInfo23.get()
            if house23 != '':
                if self.is_number(house23):
                    house23 = int(house23)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house23 = None
            
            house24 = houseInfo24.get()
            if house24 == '':
                house24 = None 

        #person 3
        house30 = houseInfo30.get()
        if house30 != '':
            person3 = 1

            house31 = houseInfo31.get()
            if house31 == '':
                house31 = None  
            
            house32 = houseInfo32.get()
            if house32 == '':
                house32 = None  
            
            house33 = houseInfo33.get()
            if house33 != '':
                if self.is_number(house33):
                    house33 = int(house33)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house33 = None
            
            house34 = houseInfo34.get()
            if house34 == '':
                house34 = None 

        #person 4
        house40 = houseInfo40.get()
        if house40 != '':
            person4 = 1

            house41 = houseInfo41.get()
            if house41 == '':
                house41 = None  
            
            house42 = houseInfo42.get()
            if house42 == '':
                house42 = None  
            
            house43 = houseInfo43.get()
            if house43 != '':
                if self.is_number(house43):
                    house43 = int(house43)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house43 = None
            
            house44 = houseInfo44.get()
            if house44 == '':
                house44 = None 

        #person 5
        house50 = houseInfo50.get()
        if house50 != '':
            person5 = 1

            house51 = houseInfo51.get()
            if house51 == '':
                house51 = None  
            
            house52 = houseInfo52.get()
            if house52 == '':
                house52 = None  
            
            house53 = houseInfo53.get()
            if house53 != '':
                if self.is_number(house53):
                    house53 = int(house53)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house53 = None
            
            house54 = houseInfo54.get()
            if house54 == '':
                house54 = None 

        #person 6
        house60 = houseInfo60.get()
        if house60 != '':
            person6 = 1

            house61 = houseInfo61.get()
            if house61 == '':
                house61 = None  
            
            house62 = houseInfo62.get()
            if house62 == '':
                house62 = None  
            
            house63 = houseInfo63.get()
            if house63 != '':
                if self.is_number(house63):
                    house63 = int(house63)
                else:
                    tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Household Information\n\nAge must be only numbers.")
                    goodData = 0
            else:
                house63 = None
            
            house64 = houseInfo64.get()
            if house64 == '':
                house64 = None 

#Family Annual Income Info
        #adapt for database
        
        income = famIncome0.get()
        if income == '':
            income = None

#Source of Family Income
        #adapt for database

        source0 = famIncome1.get()
        if source0 == '':
            source0 = None

        source1 = famIncome2.get()
        if source1 == '':
            source1 = None

#In Case of Emergency Contact
        #adapt for database

        emergency0 = emergencyInfo0.get()
        if emergency0 == '':
            emergency0 = None

        emergency1 = emergencyInfo1.get()
        if emergency1 == '':
            emergency1 = None

        emergency2 = emergencyInfo2.get()
        if emergency2 == '':
            emergency2 = None

        emergency3 = emergencyInfo3.get()
        if emergency3 == '':
            emergency3 = None

        emergency4 = emergencyInfo4.get()
        if emergency4 == '':
            emergency4 = None

        emergency5 = emergencyInfo5.get()
        if emergency5 == '':
            emergency5 = None

        emergency6 = emergencyInfo6.get()
        if emergency6 != '':
            if self.is_number(emergency6):
                emergency6 = int(emergency6)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in In Case of Emergency Contact\n\nZip must be only numbers.")
                goodData = 0
        else:
            emergency6 = None

        emergency7 = emergencyInfo7.get()
        if emergency7 == '':
            emergency7 = None

        emergency8 = emergencyInfo8.get()
        if emergency8 == '':
            emergency8 = None

        emergency9 = emergencyInfo9.get()
        if emergency9 == '':
            emergency9 = None

#statements of understanding
        #adapt for database

        s0 = statement0.get()
        if s0 == 0:
            s0 = None
        elif s0 == 2:
            s0 = 0

        s1 = statement1.get()
        if s1 == 0:
            s1 = None
        elif s1 == 2:
            s1 = 0

        s2 = statement2.get()
        if s2 == 0:
            s2 = None
        elif s2 == 2:
            s2 = 0

        s3 = statement3.get()
        if s3 == 0:
            s3 = None
        elif s3 == 2:
            s3 = 0

        s4 = statement4.get()
        if s4 == 0:
            s4 = None
        elif s4 == 2:
            s4 = 0

        s5 = statement5.get()
        if s5 == 0:
            s5 = None
        elif s5 == 2:
            s5 = 0

        s6 = statement6.get()
        if s6 == 0:
            s6 = None
        elif s6 == 2:
            s6 = 0


#Insert into DB
        if goodData:
            try:
                curr.execute("""DELETE FROM Child_Application WHERE ID = 2;""")
                db.commit()

                curr.execute("""INSERT INTO Child_Application VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, sig, programsC, ReferralOther, programsB, programsOther, programsA,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM Childs_Information WHERE ID = 2;""")
                db.commit()

                curr.execute("""INSERT INTO Childs_Information VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                             (id, date, cI0, cI1, cI2, cI3, cI4, cI5, cI6, cI7, cI8, cI9, cI10, cI11, cI12, cI13, cI14, cI15, cI16,
                                 cI17, cI18, cI19, cI20, cI21, cI22, cI23, cI24, cI25, cI26, cI27, cI28, cI29,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM Parent_Guardian_Information WHERE ID = 2;""")
                db.commit()

                curr.execute("""INSERT INTO Parent_Guardian_Information VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                             (id, date, pI0, pI1, pI2, pI3, pI4, pI5, pI6, pI7, pI8, pI9, pI10, pI11,
                                 pI12, pI13, pI14, pI15,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM Absent_Parent_Information WHERE ID = 2;""")
                db.commit()

                curr.execute("""INSERT INTO Absent_Parent_Information VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                                 (id, date, abs0, abs1, abs2, abs3, abs4, abs5, abs6, abs7,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            if person1:
                try:
                    count = 1
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 1;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house10, house11, house12, house13, house14,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person2:
                try:
                    count = 2
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 2;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house20, house21, house22, house23, house24,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person3:
                try:
                    count = 3
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 3;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house30, house31, house32, house33, house34,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person4:
                try:
                    count = 4
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 4;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house40, house41, house42, house43, house44,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person5:
                try:
                    count = 5
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 5;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house50, house51, house52, house53, house54,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            if person6:
                try:
                    count = 6
                    curr.execute("""DELETE FROM Household_Information WHERE ID = 2 AND Count = 6;""")
                    db.commit()

                    curr.execute("""INSERT INTO Household_Information VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s);""",
                                     (id, date, count, house60, house61, house62, house63, house64,))

                except (MySQLdb.IntegrityError) as e:
                    success = 0

            try:
                curr.execute("""DELETE FROM Fam_Annual_Income WHERE ID = 2;""")
                db.commit()

                curr.execute("""INSERT INTO Fam_Annual_Income VALUES
                    (%s, %s, %s);""",
                    (id, date, income,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM Source_Fam_Income WHERE ID = 2;""")
                db.commit()

                curr.execute("""INSERT INTO Source_Fam_Income VALUES
                    (%s, %s, %s, %s);""",
                    (id, date, source0, source1,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""DELETE FROM ChildApp_Emergency_Contact WHERE ID = 2;""")
                db.commit()

                curr.execute("""INSERT INTO ChildApp_Emergency_Contact VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, emergency0, emergency1, emergency2, emergency3, emergency4, emergency5, emergency6,
                         emergency7, emergency8, emergency9,))

            except (MySQLdb.IntegrityError) as e:
                success = 0

            try:
                curr.execute("""INSERT INTO Statement_Of_Understanding VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, s0, s1, s2, s3, s4, s5, s6,))

            except (MySQLdb.IntegrityError) as e:
                success = 0
            

            db.commit()

            if success:
                tkMessageBox.showinfo("New Profile", "Submission Sucessful!")
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nA Child application \nSubmitted on: " + date + "\nFor ID number: " + str(id) + " \nAlready exists in the system")




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


