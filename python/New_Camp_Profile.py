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
        master.geometry("1000x1000")

#TODO: Pass in parameters
#parameters
        global id
        global date
        id = 4
        date = '2014-09-12'
        
#Buttons
        #frame
        buttonframe = Frame(self.frame)
        buttonframe.pack(side = "top", fill = "x")

        #back
        backButton = Button(buttonframe, text = "Back", command = lambda:self.backNewChildProfilePage(id, date))
        backButton.pack(side = "left")

#Database dump frame
        DemographicSectionframe = Frame(self.frame)
        DemographicSectionframe.pack(fill = 'y', side = 'left') 
        r = 0

#Demographic info section
        #header
        labelDemographicSection = Label(DemographicSectionframe, text = "\n\nDEMOGRAPHIC INFORMATION")
        labelDemographicSection.grid(row = r, columnspan = 2)
        labelDemographicSection.config(font=("Helvetica", 20))

        #first name
        label = Label(DemographicSectionframe, text = "\nFirst Name ................................................................................................................................. ")
        demInfo0 = Entry(DemographicSectionframe)
        r = r+1
        demInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #last name
        label = Label(DemographicSectionframe, text = "\nLast Name ................................................................................................................................. ")
        demInfo1 = Entry(DemographicSectionframe)
        r = r+1
        demInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #middle initial
        label = Label(DemographicSectionframe, text = "\nMiddle Initial .............................................................................................................................. ")
        demInfo2 = Entry(DemographicSectionframe)
        r = r+1
        demInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #age
        label = Label(DemographicSectionframe, text = "\nAge ............................................................................................................................................ ")
        demInfo3 = Entry(DemographicSectionframe)
        r = r+1
        demInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #birthday
        label = Label(DemographicSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ..................................................................................................... ")
        demInfo4 = Entry(DemographicSectionframe)
        r = r+1
        demInfo4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gender
        label = Label(DemographicSectionframe, text = "\nGender ...................................................................................................................................... ")
        demInfo5 = StringVar()
        choices = ['Male','Female']
        option = tk.OptionMenu(DemographicSectionframe, demInfo5, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #race
        label = Label(DemographicSectionframe, text = "\nRace .......................................................................................................................................... ")
        demInfo6 = Entry(DemographicSectionframe)
        r = r+1
        demInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #language
        label = Label(DemographicSectionframe, text = "\nPrimary Language ...................................................................................................................... ")
        demInfo7 = Entry(DemographicSectionframe)
        r = r+1
        demInfo7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        label = Label(DemographicSectionframe, text = "\nStreet Address ........................................................................................................................... ")
        demInfo8 = Entry(DemographicSectionframe)
        r = r+1
        demInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        label = Label(DemographicSectionframe, text = "\nCity ........................................................................................................................................... ")
        demInfo9 = Entry(DemographicSectionframe)
        r = r+1
        demInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address state
        label = Label(DemographicSectionframe, text = "\nState ......................................................................................................................................... ")
        demInfo10 = Entry(DemographicSectionframe)
        r = r+1
        demInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address county
        label = Label(DemographicSectionframe, text = "\nCounty ...................................................................................................................................... ")
        demInfo11 = Entry(DemographicSectionframe)
        r = r+1
        demInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        label = Label(DemographicSectionframe, text = "\nZip ............................................................................................................................................ ")
        demInfo12 = Entry(DemographicSectionframe)
        r = r+1
        demInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #camper email
        label = Label(DemographicSectionframe, text = "\nCamper Email ............................................................................................................................ ")
        demInfo13 = Entry(DemographicSectionframe)
        r = r+1
        demInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Parent email
        label = Label(DemographicSectionframe, text = "\nParent Email .............................................................................................................................. ")
        demInfo14 = Entry(DemographicSectionframe)
        r = r+1
        demInfo14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Guardian name
        label = Label(DemographicSectionframe, text = "\nGuardian Name .......................................................................................................................... ")
        demInfo15 = Entry(DemographicSectionframe)
        r = r+1
        demInfo15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Guardian Camper Relationship
        label = Label(DemographicSectionframe, text = "\nGuardian Camper Relationship ................................................................................................... ")
        demInfo16 = Entry(DemographicSectionframe)
        r = r+1
        demInfo16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Last Grade Completed
        label = Label(DemographicSectionframe, text = "\nLast Grade Completed ............................................................................................................... ")
        demInfo17 = Entry(DemographicSectionframe)
        r = r+1
        demInfo17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Special Ed Classes
        label = Label(DemographicSectionframe, text = '\nSpecial Ed Classes? ................................................................................................................... ')
        demInfo18 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = demInfo18, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = demInfo18, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #siblings applying
        label = Label(DemographicSectionframe, text = "\nSiblings Applying? ..................................................................................................................... ")
        demInfo19 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = demInfo19, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = demInfo19, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #t-shirt size
        label = Label(DemographicSectionframe, text = "\nT-Shirt Size ............................................................................................................................... ")
        demInfo20 = StringVar()
        choices = ['Youth S', 'Youth M', 'Youth L', 'Adult S', 'Adult M', 'Adult L', 'Adult XL', 'Adult XXL']
        option = tk.OptionMenu(DemographicSectionframe, demInfo20, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Transportation
        label = Label(DemographicSectionframe, text = "\nPlanned Transportation ............................................................................................................. ")
        r = r+1
        label.grid(row = r, column = 0)

        #ATL bus
        demInfoTransport0 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'Atlanta bus', variable = demInfoTransport0).grid(row = r,  column = 1, sticky = W)

        #Augusta bus
        demInfoTransport1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Augusta bus', variable = demInfoTransport1).grid(row = r,  column = 1, sticky = W)

        #Albany bus
        demInfoTransport2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Albany bus', variable = demInfoTransport2).grid(row = r,  column = 1, sticky = W)

        #Athens bus
        demInfoTransport3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Athens bus', variable = demInfoTransport3).grid(row = r,  column = 1, sticky = W)

        #Savannah bus
        demInfoTransport4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Savannah bus', variable = demInfoTransport4).grid(row = r,  column = 1, sticky = W)

        #Car/drop
        demInfoTransport5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Car/drop', variable = demInfoTransport5).grid(row = r,  column = 1, sticky = W)

#demographic contacts
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
        label = Label(DemographicSectionframe, text = "Contact Name ............................................................................................................................ ")
        demContactInfo10 = Entry(DemographicSectionframe)
        r = r+1
        demContactInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #time pref
        label = Label(DemographicSectionframe, text = "Time Preference ......................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Day
        demContactInfoTime10 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'Day', variable = demContactInfoTime10).grid(row = r,  column = 1, sticky = W)

        #Evening
        demContactInfoTime11 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Evening', variable = demContactInfoTime11).grid(row = r,  column = 1, sticky = W)

        #phone number
        label = Label(DemographicSectionframe, text = "Phone Number ............................................................................................................................ ")
        demContactInfo11 = Entry(DemographicSectionframe)
        r = r+1
        demContactInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HOME
        #type
        label = Label(DemographicSectionframe, text = "\nHome Number")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #Name
        label = Label(DemographicSectionframe, text = "Contact Name ............................................................................................................................ ")
        demContactInfo20 = Entry(DemographicSectionframe)
        r = r+1
        demContactInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #time pref
        label = Label(DemographicSectionframe, text = "Time Preference ......................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Day
        demContactInfoTime20 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'Day', variable = demContactInfoTime20).grid(row = r,  column = 1, sticky = W)

        #Evening
        demContactInfoTime21 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Evening', variable = demContactInfoTime21).grid(row = r,  column = 1, sticky = W)

        #phone number
        label = Label(DemographicSectionframe, text = "Phone Number ............................................................................................................................ ")
        demContactInfo21 = Entry(DemographicSectionframe)
        r = r+1
        demContactInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #WORK
        #type
        label = Label(DemographicSectionframe, text = "\nWork Number")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #Name
        label = Label(DemographicSectionframe, text = "Contact Name ............................................................................................................................ ")
        demContactInfo30 = Entry(DemographicSectionframe)
        r = r+1
        demContactInfo30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #time pref
        label = Label(DemographicSectionframe, text = "Time Preference ......................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Day
        demContactInfoTime30 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'Day', variable = demContactInfoTime30).grid(row = r,  column = 1, sticky = W)

        #Evening
        demContactInfoTime31 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Evening', variable = demContactInfoTime31).grid(row = r,  column = 1, sticky = W)

        #phone number
        label = Label(DemographicSectionframe, text = "Phone Number ............................................................................................................................ ")
        demContactInfo31 = Entry(DemographicSectionframe)
        r = r+1
        demContactInfo31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Parent/ Guardian Emergency Contact Section
        #header
        labelEmergencySection = Label(DemographicSectionframe, text = "\n\nEMERGENCY CONTACT INFORMATION")
        r = r+1
        labelEmergencySection.grid(row = r, columnspan = 2)
        labelEmergencySection.config(font=("Helvetica", 20))

        #Name
        label = Label(DemographicSectionframe, text = "\nEmergency Contact Name 1 ....................................................................................................... ")
        emergencyInfo10 = Entry(DemographicSectionframe)
        r = r+1
        emergencyInfo10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship
        label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. ")
        emergencyInfo11 = Entry(DemographicSectionframe)
        r = r+1
        emergencyInfo11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Daytime Phone
        label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... ")
        emergencyInfo12 = Entry(DemographicSectionframe)
        r = r+1
        emergencyInfo12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Evening Phone
        label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... ")
        emergencyInfo13 = Entry(DemographicSectionframe)
        r = r+1
        emergencyInfo13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Name
        label = Label(DemographicSectionframe, text = "\nEmergency Contact Name 2 ....................................................................................................... ")
        emergencyInfo20 = Entry(DemographicSectionframe)
        r = r+1
        emergencyInfo20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Relationship
        label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. ")
        emergencyInfo21 = Entry(DemographicSectionframe)
        r = r+1
        emergencyInfo21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Daytime Phone
        label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... ")
        emergencyInfo22 = Entry(DemographicSectionframe)
        r = r+1
        emergencyInfo22.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Evening Phone
        label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... ")
        emergencyInfo23 = Entry(DemographicSectionframe)
        r = r+1
        emergencyInfo23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Insurance Info Section
        #header
        labelInsuranceSection = Label(DemographicSectionframe, text = "\n\nINSURANCE INFORMATION")
        r = r+1
        labelInsuranceSection.grid(row = r, columnspan = 2)
        labelInsuranceSection.config(font=("Helvetica", 20))

        #Insurer
        label = Label(DemographicSectionframe, text = "\nHealth Insurance Provider .......................................................................................................... ")
        insuranceInfo0 = StringVar()
        choices = ['Medicaid','PeachCare','Private','None']
        option = tk.OptionMenu(DemographicSectionframe, insuranceInfo0, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Private Insurer Name
        label = Label(DemographicSectionframe, text = "\nIf Private, Insurance Provider Name ........................................................................................... ")
        insuranceInfo1 = Entry(DemographicSectionframe)
        r = r+1
        insuranceInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Policy Number
        label = Label(DemographicSectionframe, text = "\nPolicy Number ........................................................................................................................... ")
        insuranceInfo2 = Entry(DemographicSectionframe)
        r = r+1
        insuranceInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Group Number
        label = Label(DemographicSectionframe, text = "\nGroup Number ........................................................................................................................... ")
        insuranceInfo3 = Entry(DemographicSectionframe)
        r = r+1
        insuranceInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Medical Provider Section
        #header
        labelMedicalSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER INFORMATION")
        r = r+1
        labelMedicalSection.grid(row = r, columnspan = 2)
        labelMedicalSection.config(font=("Helvetica", 20))
                
        #Name
        label = Label(DemographicSectionframe, text = "\nMedical Provider Name .............................................................................................................. ")
        medProviderInfo0 = Entry(DemographicSectionframe)
        r = r+1
        medProviderInfo0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Office Phone
        label = Label(DemographicSectionframe, text = "\nMedical Provider Office Phone Number ...................................................................................... ")
        medProviderInfo1 = Entry(DemographicSectionframe)
        r = r+1
        medProviderInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Pharmacy name
        label = Label(DemographicSectionframe, text = "\nName of Pharmacy ..................................................................................................................... ")
        medProviderInfo2 = Entry(DemographicSectionframe)
        r = r+1
        medProviderInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
        
        #Pharmacy Phone Number
        label = Label(DemographicSectionframe, text = "\nPharmacy Phone Number ........................................................................................................... ")
        medProviderInfo3 = Entry(DemographicSectionframe)
        r = r+1
        medProviderInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Medical Information Section
        #header
        labelMedInfoSection = Label(DemographicSectionframe, text = "\n\nMEDICAL INFORMATION")
        r = r+1
        labelMedInfoSection.grid(row = r, columnspan = 2)
        labelMedInfoSection.config(font=("Helvetica", 20))

        #Conditions
        label = Label(DemographicSectionframe, text = "\nCurrent Medical Conditions ........................................................................................................ ")
        r = r+1
        label.grid(row = r, column = 0)

        #HIV
        medInfoCurr0 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'HIV', variable = medInfoCurr0).grid(row = r,  column = 1, sticky = W)

        #Hepatitis B
        medInfoCurr1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Hepatitis B', variable = medInfoCurr1).grid(row = r,  column = 1, sticky = W)

        #Hepatitis C
        medInfoCurr2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Hepatitis C', variable = medInfoCurr2).grid(row = r,  column = 1, sticky = W)

        #ADD or ADHD
        medInfoCurr3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'ADD or ADHD', variable = medInfoCurr3).grid(row = r,  column = 1, sticky = W)

        #Sickle Cell Disease
        medInfoCurr4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Sickle Cell Disease', variable = medInfoCurr4).grid(row = r,  column = 1, sticky = W)

        #Asthma
        medInfoCurr5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Asthma', variable = medInfoCurr5).grid(row = r,  column = 1, sticky = W)

        #Tubes in Ears
        medInfoCurr6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Tubes in Ears', variable = medInfoCurr6).grid(row = r,  column = 1, sticky = W)

        #Heart Problems
        medInfoCurr7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Heart Problems', variable = medInfoCurr7).grid(row = r,  column = 1, sticky = W)

        #Mental Health Diagnoses
        medInfoCurr8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Mental Health Diagnoses', variable = medInfoCurr8).grid(row = r,  column = 1, sticky = W)

        #Other
        medInfoCurr9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Other', variable = medInfoCurr9).grid(row = r,  column = 1, sticky = W)

        #If other
        medInfo0 = Entry(DemographicSectionframe, width = 19)
        medInfo0.grid(row = r, column = 1, sticky = E)

        #Conditions Explained
        label = Label(DemographicSectionframe, text = "\nDescription of Medical Conditions .............................................................................................. ")
        medInfo1 = Entry(DemographicSectionframe)
        r = r+1
        medInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Allergies Section
        #header
        labelAllergySection = Label(DemographicSectionframe, text = "\n\nALLERGY INFORMATION")
        r = r+1
        labelAllergySection.grid(row = r, columnspan = 2)
        labelAllergySection.config(font=("Helvetica", 20))

        #Med Allergies
        label = Label(DemographicSectionframe, text = "\nMedical Allergies? ...................................................................................................................... ")
        allergyInfo0 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = allergyInfo0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = allergyInfo0, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Med Allergy Reaction
        label = Label(DemographicSectionframe, text = "\nMedical Allergy Reaction ............................................................................................................ ")
        allergyInfo1 = Entry(DemographicSectionframe)
        r = r+1
        allergyInfo1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Food Allergy
        label = Label(DemographicSectionframe, text = "\nFood Allergies? .......................................................................................................................... ")
        allergyInfo2 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = allergyInfo2, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = allergyInfo2, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Food Allergy Reaction
        label = Label(DemographicSectionframe, text = "\nFood Allergy Reaction ................................................................................................................ ")
        allergyInfo3 = Entry(DemographicSectionframe)
        r = r+1
        allergyInfo3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Environmental Allergies
        label = Label(DemographicSectionframe, text = "\nEnvironmental Allergies? ............................................................................................................ ")
        allergyInfo4 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = allergyInfo4, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = allergyInfo4, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Environmental Allergy Reaction
        label = Label(DemographicSectionframe, text = "\nEnvironmental Allergy Reaction .................................................................................................. ")
        allergyInfo5 = Entry(DemographicSectionframe)
        r = r+1
        allergyInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Epi Pen
        label = Label(DemographicSectionframe, text = "\nEpiPen for any of the above allergies? ........................................................................................ ")
        allergyInfo6 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = allergyInfo6, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = allergyInfo6, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#Dietary Needs Section
        #header
        labelDietarySection = Label(DemographicSectionframe, text = "\n\nDIETARY INFORMATION")
        r = r+1
        labelDietarySection.grid(row = r, columnspan = 2)
        labelDietarySection.config(font=("Helvetica", 20))

        #Special Dietary Needs
        label = Label(DemographicSectionframe, text = "\nSpecial Dietary Needs ................................................................................................................ ")
        dietaryNeedsInfo0 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = dietaryNeedsInfo0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = dietaryNeedsInfo0, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Vegetarian
        label = Label(DemographicSectionframe, text = "\nVegetarian ................................................................................................................................. ")
        dietaryNeedsInfo1 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = dietaryNeedsInfo1, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = dietaryNeedsInfo1, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Food Restrictions
        label = Label(DemographicSectionframe, text = "\nFood Restrictions ....................................................................................................................... ")
        dietaryNeedsInfo2 = Entry(DemographicSectionframe)
        r = r+1
        dietaryNeedsInfo2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #G Tube
        label = Label(DemographicSectionframe, text = "\nG-Tube ...................................................................................................................................... ")
        dietaryNeedsInfo3 = StringVar()
        choices = ['None','Medicine','Formula','Both']
        option = tk.OptionMenu(DemographicSectionframe, dietaryNeedsInfo3, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Formula Supplements
        label = Label(DemographicSectionframe, text = "\nFormula Supplements ................................................................................................................ ")
        dietaryNeedsInfo4 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = dietaryNeedsInfo4, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = dietaryNeedsInfo4, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Formula Supplements How
        label = Label(DemographicSectionframe, text = "\nFormula Supplements How? ....................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #By Mouth
        dietaryNeedsHowInfo0 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'By Mouth', variable = dietaryNeedsHowInfo0).grid(row = r,  column = 1, sticky = W)

        #By G-Tube
        dietaryNeedsHowInfo1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'By G-Tube', variable = dietaryNeedsHowInfo1).grid(row = r,  column = 1, sticky = W)

        #Formula Type
        label = Label(DemographicSectionframe, text = "\nFormula Type ............................................................................................................................. ")
        dietaryNeedsInfo5 = Entry(DemographicSectionframe)
        r = r+1
        dietaryNeedsInfo5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #cans per day
        label = Label(DemographicSectionframe, text = "\nFormula Cans Per Day ................................................................................................................ ")
        dietaryNeedsInfo6 = Entry(DemographicSectionframe)
        r = r+1
        dietaryNeedsInfo6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Feeding Pump
        label = Label(DemographicSectionframe, text = "\nFeeding Pump ............................................................................................................................ ")
        dietaryNeedsInfo7 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = dietaryNeedsInfo7, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = dietaryNeedsInfo7, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Feeding Pump Type
        label = Label(DemographicSectionframe, text = "\nPump Type ................................................................................................................................ ")
        dietaryNeedsInfo8 = Entry(DemographicSectionframe)
        r = r+1
        dietaryNeedsInfo8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Feeding schedule
        label = Label(DemographicSectionframe, text = "\nFeeding Schedule ...................................................................................................................... ")
        dietaryNeedsInfo9 = Entry(DemographicSectionframe)
        r = r+1
        dietaryNeedsInfo9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#General health
        #header
        labelFoodNeedsSection = Label(DemographicSectionframe, text = "\n\nGENERAL HEALTH INFORMATION")
        r = r+1
        labelFoodNeedsSection.grid(row = r, columnspan = 2)
        labelFoodNeedsSection.config(font=("Helvetica", 20))

        #Physical Limitations
        label = Label(DemographicSectionframe, text = "\nPhysical Limitations ................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Dressing
        genHealthLimit0 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'Dressing', variable = genHealthLimit0).grid(row = r,  column = 1, sticky = W)

        #Showering
        genHealthLimit1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Showering', variable = genHealthLimit1).grid(row = r,  column = 1, sticky = W)

        #Eating
        genHealthLimit2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Eating', variable = genHealthLimit2).grid(row = r,  column = 1, sticky = W)

        #Toileting
        genHealthLimit3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Toileting', variable = genHealthLimit3).grid(row = r,  column = 1, sticky = W)

        #Walking/Balance
        genHealthLimit4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Walking/Balance', variable = genHealthLimit4).grid(row = r,  column = 1, sticky = W)

        #Braces
        genHealthLimit5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Braces', variable = genHealthLimit5).grid(row = r,  column = 1, sticky = W)

        #Casts
        genHealthLimit6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Casts', variable = genHealthLimit6).grid(row = r,  column = 1, sticky = W)

        #Walker
        genHealthLimit7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Walker', variable = genHealthLimit7).grid(row = r,  column = 1, sticky = W)

        #Wheelchair
        genHealthLimit8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Wheelchair', variable = genHealthLimit8).grid(row = r,  column = 1, sticky = W)

        #Other
        genHealthLimit9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Other', variable = genHealthLimit9).grid(row = r,  column = 1, sticky = W)

        #If other
        genHealth0 = Entry(DemographicSectionframe, width = 19)
        genHealth0.grid(row = r, column = 1, sticky = E)

        #Tire Easily
        label = Label(DemographicSectionframe, text = "\nTire Easily .................................................................................................................................. ")
        genHealth1 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth1, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth1, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Swim
        label = Label(DemographicSectionframe, text = "\nCan Swim ................................................................................................................................... ")
        genHealth2 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth2, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth2, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Chicken Pox
        label = Label(DemographicSectionframe, text = "\nChicken Pox Vaccinated? ............................................................................................................ ")
        genHealth3 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth3, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth3, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #c pox date
        label = Label(DemographicSectionframe, text = "\nChicken Pox Date (YYYY-MM-DD) ............................................................................................... ")
        genHealth4 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth4, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth4, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Menstrual Cycle
        label = Label(DemographicSectionframe, text = "\nMenstrual Cycle ......................................................................................................................... ")
        genHealth5 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = genHealth5, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = genHealth5, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #m cycle difficulties
        label = Label(DemographicSectionframe, text = "\nMenstrual Difficulties ................................................................................................................. ")
        genHealth6 = Entry(DemographicSectionframe)
        r = r+1
        genHealth6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Behavior
        #header
        labelBehaviorSection = Label(DemographicSectionframe, text = "\n\nBEHAVIORAL INFORMATION")
        r = r+1
        labelBehaviorSection.grid(row = r, columnspan = 2)
        labelBehaviorSection.config(font=("Helvetica", 20))

        #How long Camper known
        label = Label(DemographicSectionframe, text = "\nCamper knows that someone in his/her family has HIV/AIDS ...................................................... ")
        behavior0 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = behavior0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = behavior0, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #How long Camper known
        label = Label(DemographicSectionframe, text = "\nHow Long has Camper Been Aware of HIV/AIDS Impacting Them? .............................................. ")
        behavior1 = StringVar()
        choices = ['less than 6 months', 'less than 1 year', 'a few years', 'always']
        option = tk.OptionMenu(DemographicSectionframe, behavior1, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #Camper experiences
        label = Label(DemographicSectionframe, text = "\nExperiences of Camper .............................................................................................................. ")
        r = r+1
        label.grid(row = r, column = 0)

        #Anxiety
        behaviorExperiances0 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'Anxiety', variable = behaviorExperiances0).grid(row = r,  column = 1, sticky = W)

        #Fear of dark
        behaviorExperiances1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Fear of dark', variable = behaviorExperiances1).grid(row = r,  column = 1, sticky = W)

        #Homesickness
        behaviorExperiances2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Homesickness', variable = behaviorExperiances2).grid(row = r,  column = 1, sticky = W)

        #Sleeps with night light
        behaviorExperiances3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Sleeps with night light', variable = behaviorExperiances3).grid(row = r,  column = 1, sticky = W)

        #Fights easily
        behaviorExperiances4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Fights easily', variable = behaviorExperiances4).grid(row = r,  column = 1, sticky = W)

        #School suspension due to behavior
        behaviorExperiances5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'School suspension due to behavior', variable = behaviorExperiances5).grid(row = r,  column = 1, sticky = W)

        #Bedwetting
        behaviorExperiances6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Bedwetting', variable = behaviorExperiances6).grid(row = r,  column = 1, sticky = W)

        #Sleeps with comfort item
        behaviorExperiances7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Sleeps with comfort item', variable = behaviorExperiances7).grid(row = r,  column = 1, sticky = W)

        #Hyperactivity or problems with attention
        behaviorExperiances8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Hyperactivity or problems with attention', variable = behaviorExperiances8).grid(row = r,  column = 1, sticky = W)

        #History of trauma or sexual abuse
        behaviorExperiances9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'History of trauma or sexual abuse', variable = behaviorExperiances9).grid(row = r,  column = 1, sticky = W)

        #medication for hyperactivity
        label = Label(DemographicSectionframe, text = "\nCamper Takes Medicine for Hyperactivity ................................................................................... ")
        behavior2 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = behavior2, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = behavior2, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #experience explanation
        label = Label(DemographicSectionframe, text = "\nExplanation of Experiences ........................................................................................................ ")
        behavior3 = Entry(DemographicSectionframe)
        r = r+1
        behavior3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Camper interests
        label = Label(DemographicSectionframe, text = "\nInterests of Camper ................................................................................................................... ")
        r = r+1
        label.grid(row = r, column = 0)

        #Reading
        behaviorInterests0 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'Reading', variable = behaviorInterests0).grid(row = r,  column = 1, sticky = W)

        #Music
        behaviorInterests1 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Music', variable = behaviorInterests1).grid(row = r,  column = 1, sticky = W)

        #Swimming
        behaviorInterests2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Swimming', variable = behaviorInterests2).grid(row = r,  column = 1, sticky = W)

        #Dance
        behaviorInterests3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Dance', variable = behaviorInterests3).grid(row = r,  column = 1, sticky = W)

        #Sports
        behaviorInterests4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Sports', variable = behaviorInterests4).grid(row = r,  column = 1, sticky = W)

        #Arts/Crafts
        behaviorInterests5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Arts/Crafts', variable = behaviorInterests5).grid(row = r,  column = 1, sticky = W)

        #Fishing
        behaviorInterests6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Fishing', variable = behaviorInterests6).grid(row = r,  column = 1, sticky = W)

        #Boating
        behaviorInterests7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Boating', variable = behaviorInterests7).grid(row = r,  column = 1, sticky = W)

        #Archery
        behaviorInterests8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Archery', variable = behaviorInterests8).grid(row = r,  column = 1, sticky = W)

        #Golf
        behaviorInterests9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Golf', variable = behaviorInterests9).grid(row = r,  column = 1, sticky = W)

        #Bicycling
        behaviorInterests10 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Bicycling', variable = behaviorInterests7).grid(row = r,  column = 1, sticky = W)

        #Animals
        behaviorInterests11 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Animals', variable = behaviorInterests8).grid(row = r,  column = 1, sticky = W)

        #Nature
        behaviorInterests12 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Nature', variable = behaviorInterests9).grid(row = r,  column = 1, sticky = W)

        #Recent major events
        label = Label(DemographicSectionframe, text = "\nRecent Events for Camper .......................................................................................................... ")
        behavior4 = Entry(DemographicSectionframe)
        r = r+1
        behavior4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Medication Info
        #header
        labelFoodNeedsSection = Label(DemographicSectionframe, text = "\n\nMEDICATION INFORMATION")
        r = r+1
        labelFoodNeedsSection.grid(row = r, columnspan = 2)
        labelFoodNeedsSection.config(font=("Helvetica", 20))

        #med 1
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 1')
        label.grid(row = r, column = 0, sticky = 'w')
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med10 = Entry(DemographicSectionframe)
        r = r+1
        med10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med11 = Entry(DemographicSectionframe)
        r = r+1
        med11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med12 = Entry(DemographicSectionframe)
        r = r+1
        med12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 2
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 2')
        label.grid(row = r, column = 0, sticky = 'w')
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med20 = Entry(DemographicSectionframe)
        r = r+1
        med20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med21 = Entry(DemographicSectionframe)
        r = r+1
        med21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med22 = Entry(DemographicSectionframe)
        r = r+1
        med22.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 3
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 3')
        label.grid(row = r, column = 0, sticky = 'w')        
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med30 = Entry(DemographicSectionframe)
        r = r+1
        med30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med31 = Entry(DemographicSectionframe)
        r = r+1
        med31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med32 = Entry(DemographicSectionframe)
        r = r+1
        med32.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 4
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 4')
        label.grid(row = r, column = 0, sticky = 'w')
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med40 = Entry(DemographicSectionframe)
        r = r+1
        med40.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med41 = Entry(DemographicSectionframe)
        r = r+1
        med41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med42 = Entry(DemographicSectionframe)
        r = r+1
        med42.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 5
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 5')
        label.grid(row = r, column = 0, sticky = 'w') 
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med50 = Entry(DemographicSectionframe)
        r = r+1
        med50.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med51 = Entry(DemographicSectionframe)
        r = r+1
        med51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med52 = Entry(DemographicSectionframe)
        r = r+1
        med52.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 6
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 6')
        label.grid(row = r, column = 0, sticky = 'w') 
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med60 = Entry(DemographicSectionframe)
        r = r+1
        med60.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med61 = Entry(DemographicSectionframe)
        r = r+1
        med61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med62 = Entry(DemographicSectionframe)
        r = r+1
        med62.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 7
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 7')
        label.grid(row = r, column = 0, sticky = 'w')        
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med70 = Entry(DemographicSectionframe)
        r = r+1
        med70.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med71 = Entry(DemographicSectionframe)
        r = r+1
        med71.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med72 = Entry(DemographicSectionframe)
        r = r+1
        med72.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 8
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 8')
        label.grid(row = r, column = 0, sticky = 'w')         
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med80 = Entry(DemographicSectionframe)
        r = r+1
        med80.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med81 = Entry(DemographicSectionframe)
        r = r+1
        med81.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med82 = Entry(DemographicSectionframe)
        r = r+1
        med82.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 9
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 9')
        label.grid(row = r, column = 0, sticky = 'w')        
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med90 = Entry(DemographicSectionframe)
        r = r+1
        med90.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med91 = Entry(DemographicSectionframe)
        r = r+1
        med91.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med92 = Entry(DemographicSectionframe)
        r = r+1
        med92.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 10
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 10')
        label.grid(row = r, column = 0, sticky = 'w')        
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med100 = Entry(DemographicSectionframe)
        r = r+1
        med100.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med101 = Entry(DemographicSectionframe)
        r = r+1
        med101.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med102 = Entry(DemographicSectionframe)
        r = r+1
        med102.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 11
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 11')
        label.grid(row = r, column = 0, sticky = 'w')        
        #taken
        label = Label(DemographicSectionframe, text = "Medication Taken ....................................................................................................................... ")
        med110 = Entry(DemographicSectionframe)
        r = r+1
        med110.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Medication Amount .................................................................................................................... ")
        med111 = Entry(DemographicSectionframe)
        r = r+1
        med111.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #frequency
        label = Label(DemographicSectionframe, text = "Medication Frequency ................................................................................................................ ")
        med112 = Entry(DemographicSectionframe)
        r = r+1
        med112.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Preliminary signatures
        #header
        labelSignatureSection = Label(DemographicSectionframe, text = "\n\nPARENTAL CONSENT INFORMATION")
        r = r+1
        labelSignatureSection.grid(row = r, columnspan = 2)
        labelSignatureSection.config(font=("Helvetica", 20))

        #parent camper contract
        label = Label(DemographicSectionframe, text = "\nParent Camper Contract ............................................................................................................. ")
        parentSig0 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig0, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #participation release
        label = Label(DemographicSectionframe, text = "\nParticipation Consent/Liability Release/Disputes Form Signed .................................................... ")
        parentSig1 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig1, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig1, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Media release
        label = Label(DemographicSectionframe, text = "\nMedia Release Form Signed ........................................................................................................ ")
        parentSig2 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig2, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig2, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #hiv ed waiver
        label = Label(DemographicSectionframe, text = "\nHIV Education Waiver Signed ...................................................................................................... ")
        parentSig3 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig3, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig3, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #camp rules form signed
        label = Label(DemographicSectionframe, text = "\nRules Acknowledgement Form Signed ......................................................................................... ")
        parentSig4 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig4, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig4, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #parental consent and release
        label = Label(DemographicSectionframe, text = "\nParental Consent and Release Form Signed ................................................................................. ")
        parentSig5 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = parentSig5, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = parentSig5, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

#Medical provider
        #header
        labelMedicalProviderSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER INFORMATION")
        r = r+1
        labelMedicalProviderSection.grid(row = r, columnspan = 2)
        labelMedicalProviderSection.config(font=("Helvetica", 20))

        #Diagnosis 1
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 1 ................................................................................................................... ")
        medProvider0 = Entry(DemographicSectionframe)
        r = r+1
        medProvider0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Diagnosis 2
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 2 ................................................................................................................... ")
        medProvider1= Entry(DemographicSectionframe)
        r = r+1
        medProvider1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Diagnosis 3
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 3 ................................................................................................................... ")
        medProvider2 = Entry(DemographicSectionframe)
        r = r+1
        medProvider2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Diagnosis 4
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 4 ................................................................................................................... ")
        medProvider3 = Entry(DemographicSectionframe)
        r = r+1
        medProvider3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Diagnosis 5
        label = Label(DemographicSectionframe, text = "\nMedical Diagnosis 5 ................................................................................................................... ")
        medProvider4 = Entry(DemographicSectionframe)
        r = r+1
        medProvider4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #management
        label = Label(DemographicSectionframe, text = "\nMedical Management Comments ................................................................................................ ")
        medProvider5 = Entry(DemographicSectionframe)
        r = r+1
        medProvider5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #nutritional supplements
        label = Label(DemographicSectionframe, text = "\nNutritional Supplements Taken? ................................................................................................. ")
        medProvider6 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = medProvider6, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = medProvider6, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #supplement comment
        label = Label(DemographicSectionframe, text = "\nFeeding Care Comments ............................................................................................................ ")
        medProvider7 = Entry(DemographicSectionframe)
        r = r+1
        medProvider7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #formula type
        label = Label(DemographicSectionframe, text = "\nFormula Type ............................................................................................................................. ")
        medProvider8 = StringVar()
        choices = ['Oral', 'G-tube', 'N-G tube']
        option = tk.OptionMenu(DemographicSectionframe, medProvider8, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #type
        label = Label(DemographicSectionframe, text = "\nFood Allergy")
        r = r+1
        label.grid(row = r, column = 0)

        #allergy1
        label = Label(DemographicSectionframe, text = "\nAllergy 1 .................................................................................................................................... ")
        foodAllergy1 = Entry(DemographicSectionframe)
        r = r+1
        foodAllergy1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction1
        label = Label(DemographicSectionframe, text = "\nReaction 1 .................................................................................................................................. ")
        foodReaction1 = Entry(DemographicSectionframe)
        r = r+1
        foodReaction1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy2
        label = Label(DemographicSectionframe, text = "\n\nAllergy 2 .................................................................................................................................... ")
        foodAllergy2 = Entry(DemographicSectionframe)
        r = r+1
        foodAllergy2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction2
        label = Label(DemographicSectionframe, text = "\nReaction 2 .................................................................................................................................. ")
        foodReaction2 = Entry(DemographicSectionframe)
        r = r+1
        foodReaction2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy3
        label = Label(DemographicSectionframe, text = "\n\nAllergy 3 .................................................................................................................................... ")
        foodAllergy3 = Entry(DemographicSectionframe)
        r = r+1
        foodAllergy3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction3
        label = Label(DemographicSectionframe, text = "\nReaction 3 .................................................................................................................................. ")
        foodReaction3 = Entry(DemographicSectionframe)
        r = r+1
        foodReaction3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy4
        label = Label(DemographicSectionframe, text = "\n\nAllergy 4 .................................................................................................................................... ")
        foodAllergy4 = Entry(DemographicSectionframe)
        r = r+1
        foodAllergy4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction4
        label = Label(DemographicSectionframe, text = "\nReaction 4 .................................................................................................................................. ")
        foodReaction4 = Entry(DemographicSectionframe)
        r = r+1
        foodReaction4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy5
        label = Label(DemographicSectionframe, text = "\n\nAllergy 5 .................................................................................................................................... ")
        foodAllergy5 = Entry(DemographicSectionframe)
        r = r+1
        foodAllergy5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction5
        label = Label(DemographicSectionframe, text = "\nReaction 5 .................................................................................................................................. ")
        foodReaction5 = Entry(DemographicSectionframe)
        r = r+1
        foodReaction5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #type
        label = Label(DemographicSectionframe, text = "\nMedical Allergy")
        r = r+1
        label.grid(row = r, column = 0)

        #allergy1
        label = Label(DemographicSectionframe, text = "\nAllergy 1 .................................................................................................................................... ")
        medAllergy1 = Entry(DemographicSectionframe)
        r = r+1
        medAllergy1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction1
        label = Label(DemographicSectionframe, text = "\nReaction 1 .................................................................................................................................. ")
        medReaction1 = Entry(DemographicSectionframe)
        r = r+1
        medReaction1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy2
        label = Label(DemographicSectionframe, text = "\n\nAllergy 2 .................................................................................................................................... ")
        medAllergy2 = Entry(DemographicSectionframe)
        r = r+1
        medAllergy2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction2
        label = Label(DemographicSectionframe, text = "\nReaction 2 .................................................................................................................................. ")
        medReaction2 = Entry(DemographicSectionframe)
        r = r+1
        medReaction2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy3
        label = Label(DemographicSectionframe, text = "\n\nAllergy 3 .................................................................................................................................... ")
        medAllergy3 = Entry(DemographicSectionframe)
        r = r+1
        medAllergy3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction3
        label = Label(DemographicSectionframe, text = "\nReaction 3 .................................................................................................................................. ")
        medReaction3 = Entry(DemographicSectionframe)
        r = r+1
        medReaction3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy4
        label = Label(DemographicSectionframe, text = "\n\nAllergy 4 .................................................................................................................................... ")
        medAllergy4 = Entry(DemographicSectionframe)
        r = r+1
        medAllergy4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction4
        label = Label(DemographicSectionframe, text = "\nReaction 4 .................................................................................................................................. ")
        medReaction4 = Entry(DemographicSectionframe)
        r = r+1
        medReaction4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy5
        label = Label(DemographicSectionframe, text = "\n\nAllergy 5 .................................................................................................................................... ")
        medAllergy5 = Entry(DemographicSectionframe)
        r = r+1
        medAllergy5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction5
        label = Label(DemographicSectionframe, text = "\nReaction 5 .................................................................................................................................. ")
        medReaction5 = Entry(DemographicSectionframe)
        r = r+1
        medReaction5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #type
        label = Label(DemographicSectionframe, text = "\nEnvironmental Allergy")
        r = r+1
        label.grid(row = r, column = 0)

        #allergy1
        label = Label(DemographicSectionframe, text = "\nAllergy 1 .................................................................................................................................... ")
        envAllergy1 = Entry(DemographicSectionframe)
        r = r+1
        envAllergy1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction1
        label = Label(DemographicSectionframe, text = "\nReaction 1 .................................................................................................................................. ")
        envReaction1 = Entry(DemographicSectionframe)
        r = r+1
        envReaction1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy2
        label = Label(DemographicSectionframe, text = "\n\nAllergy 2 .................................................................................................................................... ")
        envAllergy2 = Entry(DemographicSectionframe)
        r = r+1
        envAllergy2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction2
        label = Label(DemographicSectionframe, text = "\nReaction 2 .................................................................................................................................. ")
        envReaction2 = Entry(DemographicSectionframe)
        r = r+1
        envReaction2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy3
        label = Label(DemographicSectionframe, text = "\n\nAllergy 3 .................................................................................................................................... ")
        envAllergy3 = Entry(DemographicSectionframe)
        r = r+1
        envAllergy3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction3
        label = Label(DemographicSectionframe, text = "\nReaction 3 .................................................................................................................................. ")
        envReaction3 = Entry(DemographicSectionframe)
        r = r+1
        envReaction3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy4
        label = Label(DemographicSectionframe, text = "\n\nAllergy 4 .................................................................................................................................... ")
        envAllergy4 = Entry(DemographicSectionframe)
        r = r+1
        envAllergy4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction4
        label = Label(DemographicSectionframe, text = "\nReaction 4 .................................................................................................................................. ")
        envReaction4 = Entry(DemographicSectionframe)
        r = r+1
        envReaction4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #allergy5
        label = Label(DemographicSectionframe, text = "\n\nAllergy 5 .................................................................................................................................... ")
        envAllergy5 = Entry(DemographicSectionframe)
        r = r+1
        envAllergy5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #reaction5
        label = Label(DemographicSectionframe, text = "\nReaction 5 .................................................................................................................................. ")
        envReaction5 = Entry(DemographicSectionframe)
        r = r+1
        envReaction5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#physical
        #header
        labelPhysicalSection = Label(DemographicSectionframe, text = "\n\nMOST RECENT PHYSICAL INFORMATION")
        r = r+1
        labelPhysicalSection.grid(row = r, columnspan = 2)
        labelPhysicalSection.config(font=("Helvetica", 20))

        #date completed
        label = Label(DemographicSectionframe, text = "\nDate Completed (YYY-MM-DD) ................................................................................................... ")
        physical0 = Entry(DemographicSectionframe)
        r = r+1
        physical0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)
                    
        #height
        label = Label(DemographicSectionframe, text = "\nHeight ........................................................................................................................................ ")
        physical1 = Entry(DemographicSectionframe)
        r = r+1
        physical1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #weight
        label = Label(DemographicSectionframe, text = "\nWeight (lb) ................................................................................................................................. ")
        physical2 = Entry(DemographicSectionframe)
        r = r+1
        physical2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #pulse
        label = Label(DemographicSectionframe, text = "\nPulse (bpm) ................................................................................................................................ ")
        physical3 = Entry(DemographicSectionframe)
        r = r+1
        physical3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #respirations
        label = Label(DemographicSectionframe, text = "\nRespirations ............................................................................................................................... ")
        physical4 = Entry(DemographicSectionframe)
        r = r+1
        physical4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #bp
        label = Label(DemographicSectionframe, text = "\nBlood Pressure ........................................................................................................................... ")
        physical5 = Entry(DemographicSectionframe)
        r = r+1
        physical5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #HEENT
        label = Label(DemographicSectionframe, text = "\nHEENT ........................................................................................................................................ ")
        physical6 = Entry(DemographicSectionframe)
        r = r+1
        physical6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #skin
        label = Label(DemographicSectionframe, text = "\nSkin ............................................................................................................................................ ")
        physical7 = Entry(DemographicSectionframe)
        r = r+1
        physical7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #cardio
        label = Label(DemographicSectionframe, text = "\nCardiovascular ........................................................................................................................... ")
        physical8 = Entry(DemographicSectionframe)
        r = r+1
        physical8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #gu gyn
        label = Label(DemographicSectionframe, text = "\nGU/GYN ...................................................................................................................................... ")
        physical9 = Entry(DemographicSectionframe)
        r = r+1
        physical9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #pulmonary
        label = Label(DemographicSectionframe, text = "\nPulmonary .................................................................................................................................. ")
        physical10 = Entry(DemographicSectionframe)
        r = r+1
        physical10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #g ha
        label = Label(DemographicSectionframe, text = "\nGlasses/Contacts/Hearing Aids/PE tubes .................................................................................... ")
        physical11 = Entry(DemographicSectionframe)
        r = r+1
        physical11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Abdomen
        label = Label(DemographicSectionframe, text = "\nAbdomen ................................................................................................................................... ")
        physical12 = Entry(DemographicSectionframe)
        r = r+1
        physical12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #LN
        label = Label(DemographicSectionframe, text = "\nLymph Nodes ............................................................................................................................. ")
        physical13 = Entry(DemographicSectionframe)
        r = r+1
        physical13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Extremities
        label = Label(DemographicSectionframe, text = "\nExtremities ................................................................................................................................. ")
        physical14 = Entry(DemographicSectionframe)
        r = r+1
        physical14.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #spine
        label = Label(DemographicSectionframe, text = "\nSpine ......................................................................................................................................... ")
        physical15 = Entry(DemographicSectionframe)
        r = r+1
        physical15.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Misc
        label = Label(DemographicSectionframe, text = "\nMiscellaneous ............................................................................................................................ ")
        physical16 = Entry(DemographicSectionframe)
        r = r+1
        physical16.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #comm
        label = Label(DemographicSectionframe, text = "\nComments .................................................................................................................................. ")
        physical17 = Entry(DemographicSectionframe)
        r = r+1
        physical17.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#cognative development level
        #header
        labelCogDevSection = Label(DemographicSectionframe, text = "\n\nCOGNITIVE DEVELOPMENT INFORMATION")
        r = r+1
        labelCogDevSection.grid(row = r, columnspan = 2)
        labelCogDevSection.config(font=("Helvetica", 20))

        #development level
        label = Label(DemographicSectionframe, text = "\nDevelopment Level ..................................................................................................................... ")
        cogDev0 = StringVar()
        choices = ['Age Appropriate', 'Mild Delay', 'Moderate Delay', 'Severe Delay']
        option = tk.OptionMenu(DemographicSectionframe, cogDev0, *choices)
        r = r+1
        option.grid(row = r, column = 1, ipadx = 70)
        label.grid(row = r, column = 0)

        #other info
        label = Label(DemographicSectionframe, text = "\nOther Psychosocoal Information ................................................................................................. ")
        cogDev1 = Entry(DemographicSectionframe)
        r = r+1
        cogDev1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Varicella screening
        #header
        labelTuberculosisSection = Label(DemographicSectionframe, text = "\n\nVARICELLA SCREENING")
        r = r+1
        labelTuberculosisSection.grid(row = r, columnspan = 2)
        labelTuberculosisSection.config(font=("Helvetica", 20))

        #Two_Doses
        label = Label(DemographicSectionframe, text = "\nTwo doses of vaccine ................................................................................................................. ")
        varicella0 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = varicella0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = varicella0, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Chicken_Pox
        label = Label(DemographicSectionframe, text = "\nHistory of chicken pox or shingles? ............................................................................................ ")
        varicella1 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = varicella1, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = varicella1, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Chicken_Pox_Date
        label = Label(DemographicSectionframe, text = "\nChicken pox/ shingles date (YYYY-MM-DD) ................................................................................ ")
        varicella2 = Entry(DemographicSectionframe)
        r = r+1
        varicella2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Varicella_Antibody
        label = Label(DemographicSectionframe, text = "\nVaricella antibody ....................................................................................................................... ")
        varicella3 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Neg", variable = varicella3, value=1)
        No = Radiobutton(DemographicSectionframe, text = "Pos", variable = varicella3, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #Varicella_Antibody_Date
        label = Label(DemographicSectionframe, text = "\nVaricella antibody date (YYYY-MM-DD) ...................................................................................... ")
        varicella4 = Entry(DemographicSectionframe)
        r = r+1
        varicella4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#tuberculosis screening
        #header
        labelTuberculosisSection = Label(DemographicSectionframe, text = "\n\nTUBERCULOSIS SCREENING")
        r = r+1
        labelTuberculosisSection.grid(row = r, columnspan = 2)
        labelTuberculosisSection.config(font=("Helvetica", 20))

        #Tuberculin Skin Test
        label = Label(DemographicSectionframe, text = "\nTuberculin Skin Test")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #date
        label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................. ")
        tuberculosis10 = Entry(DemographicSectionframe)
        r = r+1
        tuberculosis10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Result
        label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... ")
        tuberculosis11 = Entry(DemographicSectionframe)
        r = r+1
        tuberculosis11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Quantiferon Testing
        label = Label(DemographicSectionframe, text = "\nQuantiferon Testing")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #date
        label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................. ")
        tuberculosis20 = Entry(DemographicSectionframe)
        r = r+1
        tuberculosis20.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Result
        label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... ")
        tuberculosis21 = Entry(DemographicSectionframe)
        r = r+1
        tuberculosis21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Chest X-ray
        label = Label(DemographicSectionframe, text = "\nChest X-ray")
        r = r+1
        label.grid(row = r, column = 0, sticky = 'w')

        #date
        label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................. ")
        tuberculosis30 = Entry(DemographicSectionframe)
        r = r+1
        tuberculosis30.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #Result
        label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... ")
        tuberculosis31 = Entry(DemographicSectionframe)
        r = r+1
        tuberculosis31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Restrictions_And_Recommendations
        #header
        labelTuberculosisSection = Label(DemographicSectionframe, text = "\n\nRESTRICTIONS AND RECOMMENDATIONS")
        r = r+1
        labelTuberculosisSection.grid(row = r, columnspan = 2)
        labelTuberculosisSection.config(font=("Helvetica", 20))

        #Restrictions and recommendations
        label = Label(DemographicSectionframe, text = "\nRestrictions and recommendations ............................................................................................ ")
        restrictionsRec = Entry(DemographicSectionframe)
        r = r+1
        restrictionsRec.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#medcare provider medications
        #header
        labelMedicineProviderSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER MEDICATION INFORMATION")
        r = r+1
        labelMedicineProviderSection.grid(row = r, columnspan = 2)
        labelMedicineProviderSection.config(font=("Helvetica", 20))

        #med 1
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 1')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed11 = Entry(DemographicSectionframe)
        r = r+1
        medProMed11.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed12 = Entry(DemographicSectionframe)
        r = r+1
        medProMed12.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed13 = Entry(DemographicSectionframe)
        r = r+1
        medProMed13.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 2
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 2')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed21 = Entry(DemographicSectionframe)
        r = r+1
        medProMed21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed22 = Entry(DemographicSectionframe)
        r = r+1
        medProMed22.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed23 = Entry(DemographicSectionframe)
        r = r+1
        medProMed23.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 3
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 3')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed31 = Entry(DemographicSectionframe)
        r = r+1
        medProMed31.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed32 = Entry(DemographicSectionframe)
        r = r+1
        medProMed32.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed33 = Entry(DemographicSectionframe)
        r = r+1
        medProMed33.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 4
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 4')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed41 = Entry(DemographicSectionframe)
        r = r+1
        medProMed41.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed42 = Entry(DemographicSectionframe)
        r = r+1
        medProMed42.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed43 = Entry(DemographicSectionframe)
        r = r+1
        medProMed43.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 5
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 5')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed51 = Entry(DemographicSectionframe)
        r = r+1
        medProMed51.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed52 = Entry(DemographicSectionframe)
        r = r+1
        medProMed52.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed53 = Entry(DemographicSectionframe)
        r = r+1
        medProMed53.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 6
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 6')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed61 = Entry(DemographicSectionframe)
        r = r+1
        medProMed61.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed62 = Entry(DemographicSectionframe)
        r = r+1
        medProMed62.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed63 = Entry(DemographicSectionframe)
        r = r+1
        medProMed63.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 7
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 7')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed71 = Entry(DemographicSectionframe)
        r = r+1
        medProMed71.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed72 = Entry(DemographicSectionframe)
        r = r+1
        medProMed72.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed73 = Entry(DemographicSectionframe)
        r = r+1
        medProMed73.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 8
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 8')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed81 = Entry(DemographicSectionframe)
        r = r+1
        medProMed81.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed82 = Entry(DemographicSectionframe)
        r = r+1
        medProMed82.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed83 = Entry(DemographicSectionframe)
        r = r+1
        medProMed83.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 9
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 9')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed91 = Entry(DemographicSectionframe)
        r = r+1
        medProMed91.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed92 = Entry(DemographicSectionframe)
        r = r+1
        medProMed92.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed93 = Entry(DemographicSectionframe)
        r = r+1
        medProMed93.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #med 10
        r = r+1
        label = Label(DemographicSectionframe, text = '\nMedication 10')
        label.grid(row = r, column = 0, sticky = 'w')
        #medication10
        label = Label(DemographicSectionframe, text = "Medication Name ....................................................................................................................... ")
        medProMed101 = Entry(DemographicSectionframe)
        r = r+1
        medProMed101.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #amount
        label = Label(DemographicSectionframe, text = "Amount and Dosage ................................................................................................................... ")
        medProMed102 = Entry(DemographicSectionframe)
        r = r+1
        medProMed102.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #times to give
        label = Label(DemographicSectionframe, text = "Times to Take Medicine .............................................................................................................. ")
        medProMed103 = Entry(DemographicSectionframe)
        r = r+1
        medProMed103.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#medcare provider verification statement
        #header
        labelMedicalStatementSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER VERIFICATION STATEMENT")
        r = r+1
        labelMedicalStatementSection.grid(row = r, columnspan = 2)
        labelMedicalStatementSection.config(font=("Helvetica", 20))

        #signature
        label = Label(DemographicSectionframe, text = "\nSignature Provided? ................................................................................................................... ")
        medProvVerState0 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = medProvVerState0, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = medProvVerState0, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #signature date
        label = Label(DemographicSectionframe, text = "\nDate (YYYY-MM-DD) .................................................................................................................. ")
        medProvVerState1 = Entry(DemographicSectionframe)
        r = r+1
        medProvVerState1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #name
        label = Label(DemographicSectionframe, text = "\nExaminer Name .......................................................................................................................... ")
        medProvVerState2 = Entry(DemographicSectionframe)
        r = r+1
        medProvVerState2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address street
        label = Label(DemographicSectionframe, text = "\nAddress Street ........................................................................................................................... ")
        medProvVerState3 = Entry(DemographicSectionframe)
        r = r+1
        medProvVerState3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address city
        label = Label(DemographicSectionframe, text = "\nAddress City .............................................................................................................................. ")
        medProvVerState4 = Entry(DemographicSectionframe)
        r = r+1
        medProvVerState4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address state
        label = Label(DemographicSectionframe, text = "\nAddress State ............................................................................................................................ ")
        medProvVerState5 = Entry(DemographicSectionframe)
        r = r+1
        medProvVerState5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #address zip
        label = Label(DemographicSectionframe, text = "\nAddress Zipcode ........................................................................................................................ ")
        medProvVerState6 = Entry(DemographicSectionframe)
        r = r+1
        medProvVerState6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #phone
        label = Label(DemographicSectionframe, text = "\nPhone ........................................................................................................................................ ")
        medProvVerState7 = Entry(DemographicSectionframe)
        r = r+1
        medProvVerState7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #emergency contact
        label = Label(DemographicSectionframe, text = "\nEmergency Contact .................................................................................................................... ")
        medProvVerState8 = Entry(DemographicSectionframe)
        r = r+1
        medProvVerState8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#health history
        #header
        labelHealthHistorySection = Label(DemographicSectionframe, text = "\n\nHEALTH HISTORY INFORMATION FROM HIV PROVIDER")
        r = r+1
        labelHealthHistorySection.grid(row = r, columnspan = 2)
        labelHealthHistorySection.config(font=("Helvetica", 20))
        
        #surgical history
        label = Label(DemographicSectionframe, text = "\nMajor Surgical History ................................................................................................................ ")
        healthHistory0 = Entry(DemographicSectionframe)
        r = r+1
        healthHistory0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #health history
        label = Label(DemographicSectionframe, text = "\nHealth History ............................................................................................................................ ")
        r = r+1
        label.grid(row = r, column = 0)

        #HIV
        healthHistory1 = IntVar()
        Checkbutton(DemographicSectionframe, text = 'HIV', variable = healthHistory1).grid(row = r,  column = 1, sticky = W)

        #Hepatitis B
        healthHistory2 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Hepatitis B', variable = healthHistory2).grid(row = r,  column = 1, sticky = W)

        #Hepatitis C
        healthHistory3 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Hepatitis C', variable = healthHistory3).grid(row = r,  column = 1, sticky = W)

        #Poor growth
        healthHistory4 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Poor growth', variable = healthHistory4).grid(row = r,  column = 1, sticky = W)

        #Bleeding disorders
        healthHistory5 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Bleeding disorders', variable = healthHistory5).grid(row = r,  column = 1, sticky = W)

        #Asthma
        healthHistory6 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Asthma', variable = healthHistory6).grid(row = r,  column = 1, sticky = W)

        #Pulmonary Disease
        healthHistory7 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Pulmonary Disease', variable = healthHistory7).grid(row = r,  column = 1, sticky = W)

        #Chronic Cough
        healthHistory8 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Chronic Cough', variable = healthHistory8).grid(row = r,  column = 1, sticky = W)

        #ADD or ADHD
        healthHistory9 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'ADD or ADHD', variable = healthHistory9).grid(row = r,  column = 1, sticky = W)

        #Renal Disease
        healthHistory10 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Renal Disease', variable = healthHistory10).grid(row = r,  column = 1, sticky = W)

        #Sickle Cell disease
        healthHistory11 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Sickle Cell disease', variable = healthHistory11).grid(row = r,  column = 1, sticky = W)

        #Congenital Heart Disease
        healthHistory12 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Congenital Heart Disease', variable = healthHistory12).grid(row = r,  column = 1, sticky = W)

        #Hypertension
        healthHistory13 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Hypertension', variable = healthHistory13).grid(row = r,  column = 1, sticky = W)

        #Cryptosporidium
        healthHistory14 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Cryptosporidium', variable = healthHistory14).grid(row = r,  column = 1, sticky = W)

        #Chronic diarrhea
        healthHistory15 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Chronic diarrhea', variable = healthHistory15).grid(row = r,  column = 1, sticky = W)

        #Seizures
        healthHistory16 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Seizures', variable = healthHistory16).grid(row = r,  column = 1, sticky = W)

        #Diabetes
        healthHistory17 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Diabetes', variable = healthHistory17).grid(row = r,  column = 1, sticky = W)

        #Other
        healthHistory18 = IntVar()
        r = r+1
        Checkbutton(DemographicSectionframe, text = 'Other', variable = healthHistory18).grid(row = r,  column = 1, sticky = W)

        #If other
        healthHistory19 = Entry(DemographicSectionframe, width = 19)
        healthHistory19.grid(row = r, column = 1, sticky = E)

        #history of noncompliance
        label = Label(DemographicSectionframe, text = "\nHistory of Noncompliance? ......................................................................................................... ")
        healthHistory20 = IntVar()
        Yes = Radiobutton(DemographicSectionframe, text = "Yes", variable = healthHistory20, value=1)
        No = Radiobutton(DemographicSectionframe, text = "No", variable = healthHistory20, value=2)
        r = r+1
        Yes.grid(row = r, column = 1, sticky = 'w')
        No.grid(row = r, column = 1, sticky = 'e')
        label.grid(row = r, column = 0)

        #explanation
        label = Label(DemographicSectionframe, text = "\nExplanation of Noncompliance .................................................................................................... ")
        healthHistory21 = Entry(DemographicSectionframe)
        r = r+1
        healthHistory21.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#lab data
        #header
        labelHealthHistorySection = Label(DemographicSectionframe, text = "\n\nLAB DATA")
        r = r+1
        labelHealthHistorySection.grid(row = r, columnspan = 2)
        labelHealthHistorySection.config(font=("Helvetica", 20))
        
        #lab1 date
        label = Label(DemographicSectionframe, text = "\nDate of First Lab Examination (YYYY-MM-DD) ............................................................................ ")
        lab0 = Entry(DemographicSectionframe)
        r = r+1
        lab0.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab1 wbc
        label = Label(DemographicSectionframe, text = "White Blood Cell Count .............................................................................................................. ")
        lab1 = Entry(DemographicSectionframe)
        r = r+1
        lab1.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab1 hgb
        label = Label(DemographicSectionframe, text = "Hemoglobin Level ....................................................................................................................... ")
        lab2 = Entry(DemographicSectionframe)
        r = r+1
        lab2.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab1 hct
        label = Label(DemographicSectionframe, text = "Hematocrit Level ........................................................................................................................ ")
        lab3 = Entry(DemographicSectionframe)
        r = r+1
        lab3.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab1 plt
        label = Label(DemographicSectionframe, text = "Plt Count .................................................................................................................................... ")
        lab4 = Entry(DemographicSectionframe)
        r = r+1
        lab4.grid(row = r, column = 1)
        label.grid(row = r, column = 0)


        #lab2 date
        label = Label(DemographicSectionframe, text = "\nDate of Second Lab Examination (YYYY-MM-DD) ........................................................................ ")
        lab5 = Entry(DemographicSectionframe)
        r = r+1
        lab5.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab2 cd4
        label = Label(DemographicSectionframe, text = "CD4 (T-Cell) Count ..................................................................................................................... ")
        lab6 = Entry(DemographicSectionframe)
        r = r+1
        lab6.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab2 viral load
        label = Label(DemographicSectionframe, text = "Viral Load ................................................................................................................................... ")
        lab7 = Entry(DemographicSectionframe)
        r = r+1
        lab7.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab3 date
        label = Label(DemographicSectionframe, text = "\nDate of Third Lab Examination (YYYY-MM-DD) ........................................................................... ")
        lab8 = Entry(DemographicSectionframe)
        r = r+1
        lab8.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab3 cd4
        label = Label(DemographicSectionframe, text = "CD4 (T-Cell) Count ..................................................................................................................... ")
        lab9 = Entry(DemographicSectionframe)
        r = r+1
        lab9.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

        #lab3 viral load
        label = Label(DemographicSectionframe, text = "Viral Load ................................................................................................................................... ")
        lab10 = Entry(DemographicSectionframe)
        r = r+1
        lab10.grid(row = r, column = 1)
        label.grid(row = r, column = 0)

#Submit arrays
        demInfoArr = [demInfo0, demInfo1, demInfo2, demInfo3, demInfo4, demInfo5, demInfo6, demInfo7, demInfo8, demInfo9,
        demInfo10, demInfo11, demInfo12, demInfo13, demInfo14, demInfo15, demInfo16, demInfo17, demInfo18, demInfo19, demInfo20]
        demInfoTransportArr = [demInfoTransport0, demInfoTransport1, demInfoTransport2, demInfoTransport3, demInfoTransport4, demInfoTransport5]
        demContactInfoArr = [demContactInfo10, demContactInfoTime10, demContactInfoTime11, demContactInfo11,
        demContactInfo20, demContactInfoTime20, demContactInfoTime21, demContactInfo21,
        demContactInfo30, demContactInfoTime30, demContactInfoTime31, demContactInfo31]
        emergencyInfoArr = [emergencyInfo10, emergencyInfo11, emergencyInfo12, emergencyInfo13, emergencyInfo20, emergencyInfo21, emergencyInfo22, emergencyInfo23]
        insuranceInfoArr = [insuranceInfo0, insuranceInfo1, insuranceInfo2, insuranceInfo3]
        medProviderInfoArr = [medProviderInfo0, medProviderInfo1, medProviderInfo2, medProviderInfo3]
        medInfoCurrArr = [medInfoCurr0, medInfoCurr1, medInfoCurr2, medInfoCurr3, medInfoCurr4, medInfoCurr5, medInfoCurr6, medInfoCurr7, medInfoCurr8, medInfoCurr9]
        medInfoArr = [medInfo0, medInfo1]
        allergyInfoArr = [allergyInfo0, allergyInfo1, allergyInfo2, allergyInfo3, allergyInfo4, allergyInfo5, allergyInfo6]
        dietaryNeedsInfoArr = [dietaryNeedsInfo0, dietaryNeedsInfo1, dietaryNeedsInfo2, dietaryNeedsInfo3, dietaryNeedsInfo4,
        dietaryNeedsInfo5, dietaryNeedsInfo6, dietaryNeedsInfo7, dietaryNeedsInfo8, dietaryNeedsInfo9]
        dietaryNeedsHowInfoArr = [dietaryNeedsHowInfo0, dietaryNeedsHowInfo1]
        genHealthLimitArr = [genHealthLimit0, genHealthLimit1, genHealthLimit2, genHealthLimit3, genHealthLimit4, genHealthLimit5, genHealthLimit6, genHealthLimit7, genHealthLimit8, genHealthLimit9]
        genHealthArr = [genHealth0, genHealth1, genHealth2, genHealth3, genHealth4, genHealth5, genHealth6]
        behaviorArr = [behavior0, behavior1, behavior2, behavior3, behavior4]
        behaviorExperiancesArr = [behaviorExperiances0, behaviorExperiances1, behaviorExperiances2, behaviorExperiances3, behaviorExperiances4, behaviorExperiances5, behaviorExperiances6, behaviorExperiances7, behaviorExperiances8, behaviorExperiances9]
        behaviorInterestsArr = [behaviorInterests0, behaviorInterests1, behaviorInterests2, behaviorInterests3, behaviorInterests4, behaviorInterests5, behaviorInterests6, behaviorInterests7, behaviorInterests8, behaviorInterests9,
        behaviorInterests10, behaviorInterests11, behaviorInterests12]
        medArr = [med10, med11, med12, med20, med21, med22, med30, med31, med32, med40, med41, med42, med50, med51, med52, med60, med61, med62, med70, med71, med72,
        med80, med81, med82, med90, med91, med92, med100, med101, med102, med110, med111, med112]
        parentSigArr = [parentSig0, parentSig1, parentSig2, parentSig3, parentSig4, parentSig5]
        medProviderArr = [medProvider0, medProvider1, medProvider2, medProvider3, medProvider4, medProvider5, medProvider6, medProvider7, medProvider8]
        foodAlergyArr = [foodAllergy1, foodReaction1, foodAllergy2, foodReaction2, foodAllergy3, foodReaction3, foodAllergy4, foodReaction4, foodAllergy5, foodReaction5]
        medAlergyArr = [medAllergy1, medReaction1, medAllergy2, medReaction2, medAllergy3, medReaction3, medAllergy4, medReaction4, medAllergy5, medReaction5]
        envAlergyArr = [envAllergy1, envReaction1, envAllergy2, envReaction2, envAllergy3, envReaction3, envAllergy4, envReaction4,  envAllergy5, envReaction5]
        physicalArr = [physical0, physical1, physical2, physical3, physical4, physical5, physical6, physical7, physical8, physical9,
        physical10, physical11, physical12, physical13, physical14, physical15, physical16, physical17]
        cogDevArr = [cogDev0, cogDev1]
        varicellaArr = [varicella0, varicella1, varicella2, varicella3, varicella4]
        tuberculosisArr = [tuberculosis10, tuberculosis11, tuberculosis20, tuberculosis21, tuberculosis30, tuberculosis31]
        medProMedArr = [medProMed11, medProMed12, medProMed13, medProMed21, medProMed22, medProMed23, medProMed31, medProMed32, medProMed33, medProMed41, medProMed42, medProMed43,
        medProMed51, medProMed52, medProMed53, medProMed61, medProMed62, medProMed63, medProMed71, medProMed72, medProMed73, medProMed81, medProMed82, medProMed83,
        medProMed91, medProMed92, medProMed93, medProMed101, medProMed102, medProMed103]
        medProvVerStateArr = [medProvVerState0, medProvVerState1, medProvVerState2, medProvVerState3, medProvVerState4, medProvVerState5, medProvVerState6, medProvVerState7, medProvVerState8]
        healthHistoryArr = [healthHistory0, healthHistory1, healthHistory2, healthHistory3, healthHistory4, healthHistory5, healthHistory6, healthHistory7, healthHistory8, healthHistory9,
        healthHistory10, healthHistory11, healthHistory12, healthHistory13, healthHistory14, healthHistory15, healthHistory16, healthHistory17, healthHistory18,
        healthHistory19, healthHistory20, healthHistory21]
        labArr = [lab0, lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9, lab10]

#Submit
        r = r+1
        submitProfileButton = Button(DemographicSectionframe, text = "Submit Profile", 
            command = lambda:self.submitProfile(
        demInfoArr, demInfoTransportArr, demContactInfoArr, emergencyInfoArr, insuranceInfoArr, medProviderInfoArr, medInfoCurrArr, medInfoArr,
        allergyInfoArr, dietaryNeedsInfoArr, dietaryNeedsHowInfoArr, genHealthLimitArr, genHealthArr, behaviorArr, behaviorExperiancesArr,
        behaviorInterestsArr, medArr, parentSigArr, medProviderArr, foodAlergyArr, medAlergyArr, envAlergyArr, physicalArr, cogDevArr, varicellaArr,
        tuberculosisArr, restrictionsRec, medProMedArr, medProvVerStateArr, healthHistoryArr, labArr))


        submitProfileButton.grid(sticky = 'w, e', row = r, columnspan = 2)

    def submitProfile(self,
        demInfoArr, demInfoTransportArr, demContactInfoArr, emergencyInfoArr, insuranceInfoArr, medProviderInfoArr, medInfoCurrArr, medInfoArr,
        allergyInfoArr, dietaryNeedsInfoArr, dietaryNeedsHowInfoArr, genHealthLimitArr, genHealthArr, behaviorArr, behaviorExperiancesArr,
        behaviorInterestsArr, medArr, parentSigArr, medProviderArr, foodAlergyArr, medAlergyArr, envAlergyArr, physicalArr, cogDevArr, varicellaArr,
        tuberculosisArr, restrictionsRec, medProMedArr, medProvVerStateArr, healthHistoryArr, labArr):

        success = 1
        goodData = 1

#adapt for database

#Demographic info section
        demInfo0 = demInfoArr[0].get()
        if demInfo0 == '':
            demInfo0 = None
        
        demInfo1 = demInfoArr[1].get()
        if demInfo1 == '':
            demInfo1 = None

        demInfo2 = demInfoArr[2].get()
        if demInfo2 == '':
            demInfo2 = None

        demInfo3 = demInfoArr[3].get()
        if demInfo3 != '':
            if self.is_number(demInfo3):
                demInfo3 = int(demInfo3)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nAge must be only numbers.")
                goodData = 0
        else:
            demInfo3 = None

        demInfo4 = demInfoArr[4].get()
        if demInfo4 != '':
            if not self.is_date(demInfo4):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            demInfo4 = None

        demInfo5 = demInfoArr[5].get()
        if demInfo5 == '':
            demInfo5 = None

        demInfo6 = demInfoArr[6].get()
        if demInfo6 == '':
            demInfo6 = None

        demInfo7 = demInfoArr[7].get()
        if demInfo7 == '':
            demInfo7 = None

        demInfo8 = demInfoArr[8].get()
        if demInfo8 == '':
            demInfo8 = None

        demInfo9 = demInfoArr[9].get()
        if demInfo9 == '':
            demInfo9 = None

        demInfo10 = demInfoArr[10].get()
        if demInfo10 == '':
            demInfo10 = None

        demInfo11 = demInfoArr[11].get()
        if demInfo11 == '':
            demInfo11 = None

        demInfo12 = demInfoArr[12].get()
        if demInfo12 != '':
            if self.is_number(demInfo12):
                demInfo12 = int(demInfo12)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nZip must be only numbers.")
                goodData = 0
        else:
            demInfo12 = None

        demInfo13 = demInfoArr[13].get()
        if demInfo13 == '':
            demInfo13 = None

        demInfo14 = demInfoArr[14].get()
        if demInfo14 == '':
            demInfo14 = None

        demInfo15 = demInfoArr[15].get()
        if demInfo15 == '':
            demInfo15 = None

        demInfo16 = demInfoArr[16].get()
        if demInfo16 == '':
            demInfo16 = None

        demInfo17 = demInfoArr[17].get()
        if demInfo17 != '':
            if self.is_number(demInfo17):
                demInfo17 = int(demInfo17)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nGrade level must be only numbers.")
                goodData = 0
        else:
            demInfo17 = None

        demInfo18 = demInfoArr[18].get()
        if demInfo18 == 0:
            demInfo18 = None
        elif demInfo18 == 2:
            demInfo18 = 0

        demInfo19 = demInfoArr[19].get()
        if demInfo19 == 0:
            demInfo19 = None
        elif demInfo19 == 2:
            demInfo19 = 0

        demInfo20 = demInfoArr[20].get()
        if demInfo20 == '':
            demInfo20 = None

        demInfoTransport = ''

        if demInfoTransportArr[0].get():
            demInfoTransport = demInfoTransport + 'Atlanta bus,'

        if demInfoTransportArr[1].get():
            demInfoTransport = demInfoTransport + 'Augusta bus,'

        if demInfoTransportArr[2].get():
            demInfoTransport = demInfoTransport + 'Albany bus,'

        if demInfoTransportArr[3].get():
            demInfoTransport = demInfoTransport + 'Athens bus,'

        if demInfoTransportArr[4].get():
            demInfoTransport = demInfoTransport + 'Savannah bus,'

        if demInfoTransportArr[5].get():
            demInfoTransport = demInfoTransport + 'Car/drop,'

        if demInfoTransport == '':
            demInfoTransport = None
        else:
            demInfoTransport = demInfoTransport[:-1]

#demographic contacts
        #cell
        demContactInfo10 = demContactInfoArr[0].get()
        if demContactInfo10 == '':
            demContactInfo10 = None

        demContactInfoTime1 = ''

        if demContactInfoArr[1].get():
            demContactInfoTime1 = demContactInfoTime1 + 'Day'

        if demContactInfoArr[2].get():
            demContactInfoTime1 = demContactInfoTime1 + 'Evening'

        if demContactInfoTime1 == '':
            demContactInfoTime1 = None

        demContactInfo11 = demContactInfoArr[3].get()
        if demContactInfo11 == '':
            demContactInfo11 = None

        #home
        demContactInfo20 = demContactInfoArr[4].get()
        if demContactInfo20 == '':
            demContactInfo20 = None

        demContactInfoTime2 = ''

        if demContactInfoArr[5].get():
            demContactInfoTime2 = demContactInfoTime2 + 'Day'

        if demContactInfoArr[6].get():
            demContactInfoTime2 = demContactInfoTime2 + 'Evening'

        if demContactInfoTime2 == '':
            demContactInfoTime2 = None

        demContactInfo21 = demContactInfoArr[7].get()
        if demContactInfo21 == '':
            demContactInfo21 = None

        #work
        demContactInfo30 = demContactInfoArr[8].get()
        if demContactInfo30 == '':
            demContactInfo30 = None

        demContactInfoTime3 = ''

        if demContactInfoArr[9].get():
            demContactInfoTime3 = demContactInfoTime3 + 'Day'

        if demContactInfoArr[10].get():
            demContactInfoTime3 = demContactInfoTime3 + 'Evening'

        if demContactInfoTime3 == '':
            demContactInfoTime3 = None

        demContactInfo31 = demContactInfoArr[11].get()
        if demContactInfo31 == '':
            demContactInfo31 = None

#Parent/ Guardian Emergency Contact Section
        emergencyInfo10 = emergencyInfoArr[0].get()
        if emergencyInfo10 == '':
            emergencyInfo10 = None

        emergencyInfo11 = emergencyInfoArr[1].get()
        if emergencyInfo11 == '':
            emergencyInfo11 = None

        emergencyInfo12 = emergencyInfoArr[2].get()
        if emergencyInfo12 == '':
            emergencyInfo12 = None

        emergencyInfo13 = emergencyInfoArr[3].get()
        if emergencyInfo13 == '':
            emergencyInfo13 = None
        
        emergencyInfo20 = emergencyInfoArr[4].get()
        if emergencyInfo20 == '':
            emergencyInfo20 = None

        emergencyInfo21 = emergencyInfoArr[5].get()
        if emergencyInfo21 == '':
            emergencyInfo21 = None

        emergencyInfo22 = emergencyInfoArr[6].get()
        if emergencyInfo22 == '':
            emergencyInfo22 = None

        emergencyInfo23 = emergencyInfoArr[7].get()
        if emergencyInfo23 == '':
            emergencyInfo23 = None

#Insurance Info Section
        insuranceInfo0 = insuranceInfoArr[0].get()
        if insuranceInfo0 == '':
            insuranceInfo0 = None

        insuranceInfo1 = insuranceInfoArr[1].get()
        if insuranceInfo1 == '':
            insuranceInfo1 = None

        insuranceInfo2 = insuranceInfoArr[2].get()
        if insuranceInfo2 == '':
            insuranceInfo2 = None

        insuranceInfo3 = insuranceInfoArr[3].get()
        if insuranceInfo3 == '':
            insuranceInfo3 = None

#Medical Provider Section
        medProviderInfo0 = medProviderInfoArr[0].get()
        if medProviderInfo0 == '':
            medProviderInfo0 = None

        medProviderInfo1 = medProviderInfoArr[1].get()
        if medProviderInfo1 == '':
            medProviderInfo1 = None

        medProviderInfo2 = medProviderInfoArr[2].get()
        if medProviderInfo2 == '':
            medProviderInfo2 = None

        medProviderInfo3 = medProviderInfoArr[3].get()
        if medProviderInfo3 == '':
            medProviderInfo3 = None

#Medical Information Section
        medInfoCurr = ''

        if medInfoCurrArr[0].get():
            medInfoCurr = medInfoCurr + 'HIV,'

        if medInfoCurrArr[1].get():
            medInfoCurr = medInfoCurr + 'Hepatitis B,'

        if medInfoCurrArr[2].get():
            medInfoCurr = medInfoCurr + 'Hepatitis C,'

        if medInfoCurrArr[3].get():
            medInfoCurr = medInfoCurr + 'ADD or ADHD,'

        if medInfoCurrArr[4].get():
            medInfoCurr = medInfoCurr + 'Sickle Cell Disease,'

        if medInfoCurrArr[5].get():
            medInfoCurr = medInfoCurr + 'Asthma,'

        if medInfoCurrArr[6].get():
            medInfoCurr = medInfoCurr + 'Tubes in Ears,'

        if medInfoCurrArr[7].get():
            medInfoCurr = medInfoCurr + 'Heart Problems,'

        if medInfoCurrArr[8].get():
            medInfoCurr = medInfoCurr + 'Mental Health Diagnoses,'

        if medInfoCurrArr[9].get():
            medInfoCurr = medInfoCurr + 'Other,'

        if medInfoCurr == '':
            medInfoCurr = None
        else:
            medInfoCurr = medInfoCurr[:-1]

        medInfo0 = medInfoArr[0].get()
        if medInfo0 == '':
            medInfo0 = None

        medInfo1 = medInfoArr[1].get()
        if medInfo1 == '':
            medInfo1 = None

#Allergies Section
        allergyInfo0 = allergyInfoArr[0].get()
        if allergyInfo0 == 0:
            allergyInfo0 = None
        elif allergyInfo0 == 2:
            allergyInfo0 = 0

        allergyInfo1 = allergyInfoArr[1].get()
        if allergyInfo1 == '':
            allergyInfo1 = None

        allergyInfo2 = allergyInfoArr[2].get()
        if allergyInfo2 == 0:
            allergyInfo2 = None
        elif allergyInfo2 == 2:
            allergyInfo2 = 0

        allergyInfo3 = allergyInfoArr[3].get()
        if allergyInfo3 == '':
            allergyInfo3 = None

        allergyInfo4 = allergyInfoArr[4].get()
        if allergyInfo4 == 0:
            allergyInfo4 = None
        elif allergyInfo4 == 2:
            allergyInfo4 = 0

        allergyInfo5 = allergyInfoArr[5].get()
        if allergyInfo5 == '':
            allergyInfo5 = None

        allergyInfo6 = allergyInfoArr[6].get()
        if allergyInfo6 == 0:
            allergyInfo6 = None
        elif allergyInfo6 == 2:
            allergyInfo6 = 0

#Dietary Needs Section
        dietaryNeedsInfo0 = dietaryNeedsInfoArr[0].get()
        if dietaryNeedsInfo0 == 0:
            dietaryNeedsInfo0 = None
        elif dietaryNeedsInfo0 == 2:
            dietaryNeedsInfo0 = 0

        dietaryNeedsInfo1 = dietaryNeedsInfoArr[1].get()
        if dietaryNeedsInfo1 == 0:
            dietaryNeedsInfo1 = None
        elif dietaryNeedsInfo1 == 2:
            dietaryNeedsInfo1 = 0

        dietaryNeedsInfo2 = dietaryNeedsInfoArr[2].get()
        if dietaryNeedsInfo2 == '':
            dietaryNeedsInfo2 = None

        dietaryNeedsInfo3 = dietaryNeedsInfoArr[3].get()
        if dietaryNeedsInfo3 == '':
            dietaryNeedsInfo3 = None

        dietaryNeedsInfo4 = dietaryNeedsInfoArr[4].get()
        if dietaryNeedsInfo4 == 0:
            dietaryNeedsInfo4 = None
        elif dietaryNeedsInfo4 == 2:
            dietaryNeedsInfo4 = 0

        dietaryNeedsHowInfo = ''

        if dietaryNeedsHowInfoArr[0].get():
            dietaryNeedsHowInfo = dietaryNeedsHowInfo + 'By Mouth,'

        if dietaryNeedsHowInfoArr[1].get():
            dietaryNeedsHowInfo = dietaryNeedsHowInfo + 'By G-Tube,'

        if dietaryNeedsHowInfo == '':
            dietaryNeedsHowInfo = None
        else:
            dietaryNeedsHowInfo = dietaryNeedsHowInfo[:-1]

        dietaryNeedsInfo5 = dietaryNeedsInfoArr[5].get()
        if dietaryNeedsInfo5 == '':
            dietaryNeedsInfo5 = None

        dietaryNeedsInfo6 = demInfoArr[6].get()
        if dietaryNeedsInfo6 != '':
            if self.is_number(dietaryNeedsInfo6):
                dietaryNeedsInfo6 = int(dietaryNeedsInfo6)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nFormula cans per day must be only numbers.")
                goodData = 0
        else:
            dietaryNeedsInfo6 = None

        dietaryNeedsInfo7 = dietaryNeedsInfoArr[7].get()
        if dietaryNeedsInfo7 == 0:
            dietaryNeedsInfo7 = None
        elif dietaryNeedsInfo7 == 2:
            dietaryNeedsInfo7 = 0

        dietaryNeedsInfo8 = dietaryNeedsInfoArr[8].get()
        if dietaryNeedsInfo8 == '':
            dietaryNeedsInfo8 = None

        dietaryNeedsInfo9 = dietaryNeedsInfoArr[9].get()
        if dietaryNeedsInfo9 == '':
            dietaryNeedsInfo9 = None

#General health
        genHealthLimit = ''

        if genHealthLimitArr[0].get():
            genHealthLimit = genHealthLimit + 'Dressing,'

        if genHealthLimitArr[1].get():
            genHealthLimit = genHealthLimit + 'Showering,'

        if genHealthLimitArr[2].get():
            genHealthLimit = genHealthLimit + 'Eating,'

        if genHealthLimitArr[3].get():
            genHealthLimit = genHealthLimit + 'Toileting,'

        if genHealthLimitArr[4].get():
            genHealthLimit = genHealthLimit + 'Walking/Balance,'

        if genHealthLimitArr[5].get():
            genHealthLimit = genHealthLimit + 'Braces,'

        if genHealthLimitArr[6].get():
            genHealthLimit = genHealthLimit + 'Casts,'

        if genHealthLimitArr[7].get():
            genHealthLimit = genHealthLimit + 'Walker,'

        if genHealthLimitArr[8].get():
            genHealthLimit = genHealthLimit + 'Wheelchair,'

        if genHealthLimitArr[9].get():
            genHealthLimit = genHealthLimit + 'Other,'

        if genHealthLimit == '':
            genHealthLimit = None
        else:
            genHealthLimit = genHealthLimit[:-1]

        genHealth0 = genHealthArr[0].get()
        if genHealth0 == '':
            genHealth0 = None

        genHealth1 = genHealthArr[1].get()
        if genHealth1 == 0:
            genHealth1 = None
        elif genHealth1 == 2:
            genHealth1 = 0

        genHealth2 = genHealthArr[2].get()
        if genHealth2 == 0:
            genHealth2 = None
        elif genHealth2 == 2:
            genHealth2 = 0

        genHealth3 = genHealthArr[3].get()
        if genHealth3 == 0:
            genHealth3 = None
        elif genHealth3 == 2:
            genHealth3 = 0

        genHealth4 = genHealthArr[4].get()
        if genHealth4 == 0:
            genHealth4 = None
        elif genHealth4 == 2:
            genHealth4 = 0

        genHealth5 = genHealthArr[5].get()
        if genHealth5 == 0:
            genHealth5 = None
        elif genHealth5 == 2:
            genHealth5 = 0

        genHealth6 = genHealthArr[6].get()
        if genHealth6 == '':
            genHealth6 = None

#Behavior
        behavior0 = behaviorArr[0].get()
        if behavior0 == 0:
            behavior0 = None
        elif behavior0 == 2:
            behavior0 = 0

        behavior1 = behaviorArr[1].get()
        if behavior1 == '':
            behavior1 = None

        behaviorExperiances = ''

        if behaviorExperiancesArr[0].get():
            behaviorExperiances = behaviorExperiances + 'Anxiety,'

        if behaviorExperiancesArr[1].get():
            behaviorExperiances = behaviorExperiances + 'Fear of dark,'

        if behaviorExperiancesArr[2].get():
            behaviorExperiances = behaviorExperiances + 'Homesickness,'

        if behaviorExperiancesArr[3].get():
            behaviorExperiances = behaviorExperiances + 'Sleeps with night light,'

        if behaviorExperiancesArr[4].get():
            behaviorExperiances = behaviorExperiances + 'Fights easily,'

        if behaviorExperiancesArr[5].get():
            behaviorExperiances = behaviorExperiances + 'School suspension due to behavior,'

        if behaviorExperiancesArr[6].get():
            behaviorExperiances = behaviorExperiances + 'Bedwetting,'

        if behaviorExperiancesArr[7].get():
            behaviorExperiances = behaviorExperiances + 'Sleeps with comfort item,'

        if behaviorExperiancesArr[8].get():
            behaviorExperiances = behaviorExperiances + 'Hyperactivity or problems with attention,'

        if behaviorExperiancesArr[9].get():
            behaviorExperiances = behaviorExperiances + 'History of trauma or sexual abuse,'

        if behaviorExperiances == '':
            behaviorExperiances = None
        else:
            behaviorExperiances = behaviorExperiances[:-1]

        behavior2 = behaviorArr[2].get()
        if behavior2 == 0:
            behavior2 = None
        elif behavior2 == 2:
            behavior2 = 0

        behavior3 = behaviorArr[3].get()
        if behavior3 == 0:
            behavior3 = None
        elif behavior3 == 2:
            behavior3 = 0

        behaviorInterests = ''

        if behaviorInterestsArr[0].get():
            behaviorInterests = behaviorInterests + 'Reading,'

        if behaviorInterestsArr[1].get():
            behaviorInterests = behaviorInterests + 'Music,'

        if behaviorInterestsArr[2].get():
            behaviorInterests = behaviorInterests + 'Swimming,'

        if behaviorInterestsArr[3].get():
            behaviorInterests = behaviorInterests + 'Dance,'

        if behaviorInterestsArr[4].get():
            behaviorInterests = behaviorInterests + 'Sports,'

        if behaviorInterestsArr[5].get():
            behaviorInterests = behaviorInterests + 'Arts/Crafts,'

        if behaviorInterestsArr[6].get():
            behaviorInterests = behaviorInterests + 'Fishing,'

        if behaviorInterestsArr[7].get():
            behaviorInterests = behaviorInterests + 'Boating,'

        if behaviorInterestsArr[8].get():
            behaviorInterests = behaviorInterests + 'Archery,'

        if behaviorInterestsArr[9].get():
            behaviorInterests = behaviorInterests + 'Golf,'

        if behaviorInterestsArr[10].get():
            behaviorInterests = behaviorInterests + 'Bicycling,'

        if behaviorInterestsArr[11].get():
            behaviorInterests = behaviorInterests + 'Animals,'

        if behaviorInterestsArr[12].get():
            behaviorInterests = behaviorInterests + 'Nature,'

        if behaviorInterests == '':
            behaviorInterests = None
        else:
            behaviorInterests = behaviorInterests[:-1]

        behavior4 = behaviorArr[4].get()
        if behavior4 == '':
            behavior4 = None

#Medication Info

        med10 = medArr[0].get()
        if med10 == '':
            med10 = None

        med11 = medArr[1].get()
        if med11 == '':
            med11 = None

        med12 = medArr[2].get()
        if med12 == '':
            med12 = None

        med20 = medArr[3].get()
        if med20 == '':
            med20 = None

        med21 = medArr[4].get()
        if med21 == '':
            med21 = None

        med22 = medArr[5].get()
        if med22 == '':
            med22 = None

        med30 = medArr[6].get()
        if med30 == '':
            med30 = None

        med31 = medArr[7].get()
        if med31 == '':
            med31 = None

        med32 = medArr[8].get()
        if med32 == '':
            med32 = None

        med40 = medArr[9].get()
        if med40 == '':
            med40 = None

        med41 = medArr[10].get()
        if med41 == '':
            med41 = None

        med42 = medArr[11].get()
        if med42 == '':
            med42 = None

        med50 = medArr[12].get()
        if med50 == '':
            med50 = None

        med51 = medArr[13].get()
        if med51 == '':
            med51 = None

        med52 = medArr[14].get()
        if med52 == '':
            med52 = None

        med60 = medArr[15].get()
        if med60 == '':
            med60 = None

        med61 = medArr[16].get()
        if med61 == '':
            med61 = None

        med62 = medArr[17].get()
        if med62 == '':
            med62 = None

        med70 = medArr[18].get()
        if med70 == '':
            med70 = None

        med71 = medArr[19].get()
        if med71 == '':
            med71 = None

        med72 = medArr[20].get()
        if med72 == '':
            med72 = None

        med80 = medArr[21].get()
        if med80 == '':
            med80 = None

        med81 = medArr[22].get()
        if med81 == '':
            med81 = None

        med82 = medArr[23].get()
        if med82 == '':
            med82 = None

        med90 = medArr[24].get()
        if med90 == '':
            med90 = None

        med91 = medArr[25].get()
        if med91 == '':
            med91 = None

        med92 = medArr[26].get()
        if med92 == '':
            med92 = None

        med100 = medArr[27].get()
        if med100 == '':
            med100 = None

        med101 = medArr[28].get()
        if med101 == '':
            med101 = None

        med102 = medArr[29].get()
        if med102 == '':
            med102 = None

        med110 = medArr[30].get()
        if med110 == '':
            med110 = None

        med111 = medArr[31].get()
        if med111 == '':
            med111 = None

        med112 = medArr[32].get()
        if med112 == '':
            med112 = None

        parentMeds = [med10, med11, med12, med20, med21, med22, med30, med31, med32,
        med40, med41, med42, med50, med51, med52, med60, med61, med62, med70, med71, med72,
        med80, med81, med82, med90, med91, med92, med100, med101, med102, med110, med111, med112]

#Preliminary signatures
        parentSig0 = parentSigArr[0].get()
        if parentSig0 == 0:
            parentSig0 = None
        elif parentSig0 == 2:
            parentSig0 = 0

        parentSig1 = parentSigArr[1].get()
        if parentSig1 == 0:
            parentSig1 = None
        elif parentSig1 == 2:
            parentSig1 = 0

        parentSig2 = parentSigArr[2].get()
        if parentSig2 == 0:
            parentSig2 = None
        elif parentSig2 == 2:
            parentSig2 = 0

        parentSig3 = parentSigArr[3].get()
        if parentSig3 == 0:
            parentSig3 = None
        elif parentSig3 == 2:
            parentSig3 = 0

        parentSig4 = parentSigArr[4].get()
        if parentSig4 == 0:
            parentSig4 = None
        elif parentSig4 == 2:
            parentSig4 = 0

        parentSig5 = parentSigArr[5].get()
        if parentSig5 == 0:
            parentSig5 = None
        elif parentSig5 == 2:
            parentSig5 = 0

#Medical provider
        medProvider0 = medProviderArr[0].get()
        if medProvider0 == '':
            medProvider0 = None
        
        medProvider1 = medProviderArr[1].get()
        if medProvider1 == '':
            medProvider1 = None
        
        medProvider2 = medProviderArr[2].get()
        if medProvider2 == '':
            medProvider2 = None
        
        medProvider3 = medProviderArr[3].get()
        if medProvider3 == '':
            medProvider3 = None
        
        medProvider4 = medProviderArr[4].get()
        if medProvider4 == '':
            medProvider4 = None

        medHistDiagnosis = [medProvider0, medProvider1, medProvider2, medProvider3, medProvider4]

        medProvider5 = medProviderArr[5].get()
        if medProvider5 == '':
            medProvider5 = None

        medProvider6 = medProviderArr[6].get()
        if medProvider6 == 0:
            medProvider6 = None
        elif medProvider6 == 2:
            medProvider6 = 0

        medProvider7 = medProviderArr[7].get()
        if medProvider7 == '':
            medProvider7 = None

        medProvider8 = medProviderArr[8].get()
        if medProvider8 == '':
            medProvider8 = None

        foodAllergy1 = foodAlergyArr[0].get()
        if foodAllergy1 == '':
            foodAllergy1 = None

        foodReaction1 = foodAlergyArr[1].get()
        if foodReaction1 == '':
            foodReaction1 = None

        foodAllergy2 = foodAlergyArr[2].get()
        if foodAllergy2 == '':
            foodAllergy2 = None

        foodReaction2 = foodAlergyArr[3].get()
        if foodReaction2 == '':
            foodReaction2 = None

        foodAllergy3 = foodAlergyArr[4].get()
        if foodAllergy3 == '':
            foodAllergy3 = None

        foodReaction3 = foodAlergyArr[5].get()
        if foodReaction3 == '':
            foodReaction3 = None

        foodAllergy4 = foodAlergyArr[6].get()
        if foodAllergy4 == '':
            foodAllergy4 = None

        foodReaction4 = foodAlergyArr[7].get()
        if foodReaction4 == '':
            foodReaction4 = None

        foodAllergy5 = foodAlergyArr[8].get()
        if foodAllergy5 == '':
            foodAllergy5 = None

        foodReaction5 = foodAlergyArr[9].get()
        if foodReaction5 == '':
            foodReaction5 = None

        foodAllergies = [foodAllergy1, foodReaction1, foodAllergy2, foodReaction2, foodAllergy3, foodReaction3,
        foodAllergy4, foodReaction4, foodAllergy5, foodReaction5]

        medAllergy1 = medAlergyArr[0].get()
        if medAllergy1 == '':
            medAllergy1 = None

        medReaction1 = medAlergyArr[1].get()
        if medReaction1 == '':
            medReaction1 = None

        medAllergy2 = medAlergyArr[2].get()
        if medAllergy2 == '':
            medAllergy2 = None

        medReaction2 = medAlergyArr[3].get()
        if medReaction2 == '':
            medReaction2 = None

        medAllergy3 = medAlergyArr[4].get()
        if medAllergy3 == '':
            medAllergy3 = None

        medReaction3 = medAlergyArr[5].get()
        if medReaction3 == '':
            medReaction3 = None

        medAllergy4 = medAlergyArr[6].get()
        if medAllergy4 == '':
            medAllergy4 = None

        medReaction4 = medAlergyArr[7].get()
        if medReaction4 == '':
            medReaction4 = None

        medAllergy5 = medAlergyArr[8].get()
        if medAllergy5 == '':
            medAllergy5 = None

        medReaction5 = medAlergyArr[9].get()
        if medReaction5 == '':
            medReaction5 = None

        medAllergies = [medAllergy1, medReaction1, medAllergy2, medReaction2, medAllergy3, medReaction3,
        medAllergy4, medReaction4, medAllergy5, medReaction5]

        envAllergy1 = envAlergyArr[0].get()
        if envAllergy1 == '':
            envAllergy1 = None

        envReaction1 = envAlergyArr[1].get()
        if envReaction1 == '':
            envReaction1 = None

        envAllergy2 = envAlergyArr[2].get()
        if envAllergy2 == '':
            envAllergy2 = None

        envReaction2 = envAlergyArr[3].get()
        if envReaction2 == '':
            envReaction2 = None

        envAllergy3 = envAlergyArr[4].get()
        if envAllergy3 == '':
            envAllergy3 = None

        envReaction3 = envAlergyArr[5].get()
        if envReaction3 == '':
            envReaction3 = None

        envAllergy4 = envAlergyArr[6].get()
        if envAllergy4 == '':
            envAllergy4 = None

        envReaction4 = envAlergyArr[7].get()
        if envReaction4 == '':
            envReaction4 = None

        envAllergy5 = envAlergyArr[8].get()
        if envAllergy5 == '':
            envAllergy5 = None

        envReaction5 = envAlergyArr[9].get()
        if envReaction5 == '':
            envReaction5 = None

        envAllergies = [envAllergy1, envReaction1, envAllergy2, envReaction2, envAllergy3, envReaction3,
        envAllergy4, envReaction4, envAllergy5, envReaction5]

#physical
        physical0 = physicalArr[0].get()
        if physical0 != '':
            if not self.is_date(physical0):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            physical0 = None
        
        physical1 = physicalArr[1].get()
        if physical1 == '':
            physical1 = None
        
        physical2 = physicalArr[2].get()
        if physical2 != '':
            if self.is_number(physical2):
                physical2 = int(physical2)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nWeight must be only numbers.")
                goodData = 0
        else:
            physical2 = None
        
        physical3 = physicalArr[3].get()
        if physical3 != '':
            if self.is_number(physical3):
                physical3 = int(physical3)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nPulse must be only numbers.")
                goodData = 0
        else:
            physical3 = None
        
        physical4 = physicalArr[4].get()
        if physical4 != '':
            if self.is_number(physical4):
                physical4 = int(physical4)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nResperations must be only numbers.")
                goodData = 0
        else:
            physical4 = None
        
        physical5 = physicalArr[5].get()
        if physical5 == '':
            physical5 = None
        
        physical6 = physicalArr[6].get()
        if physical6 == '':
            physical6 = None
        
        physical7 = physicalArr[7].get()
        if physical7 == '':
            physical7 = None
        
        physical8 = physicalArr[8].get()
        if physical8 == '':
            physical8 = None
        
        physical9 = physicalArr[9].get()
        if physical9 == '':
            physical9 = None
        
        physical10 = physicalArr[10].get()
        if physical10 == '':
            physical10 = None
        
        physical11 = physicalArr[11].get()
        if physical11 == '':
            physical11 = None
        
        physical12 = physicalArr[12].get()
        if physical12 == '':
            physical12 = None
        
        physical13 = physicalArr[13].get()
        if physical13 == '':
            physical13 = None
        
        physical14 = physicalArr[14].get()
        if physical14 == '':
            physical14 = None
        
        physical15 = physicalArr[15].get()
        if physical15 == '':
            physical15 = None
        
        physical16 = physicalArr[16].get()
        if physical16 == '':
            physical16 = None
        
        physical17 = physicalArr[17].get()
        if physical17 == '':
            physical17 = None

#cognative development level
        cogDev0 = cogDevArr[0].get()
        if cogDev0 == '':
            cogDev0 = None

        cogDev1 = cogDevArr[1].get()
        if cogDev1 == '':
            cogDev1 = None

#Varicella screening
        varicella0 = varicellaArr[0].get()
        if varicella0 == 0:
            varicella0 = None
        elif varicella0 == 2:
            varicella0 = 0

        varicella1 = varicellaArr[1].get()
        if varicella1 == 0:
            varicella1 = None
        elif varicella1 == 2:
            varicella1 = 0

        varicella2 = varicellaArr[2].get()
        if varicella2 != '':
            if not self.is_date(varicella2):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            varicella2 = None

        varicella3 = varicellaArr[3].get()
        if varicella3 == 0:
            varicella3 = None
        elif varicella3 == 2:
            varicella3 = 0

        varicella4 = varicellaArr[4].get()
        if varicella4 != '':
            if not self.is_date(varicella4):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            varicella4 = None

#tuberculosis screening
        tuberculosis10 = tuberculosisArr[0].get()
        if tuberculosis10 != '':
            if not self.is_date(tuberculosis10):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            tuberculosis10 = None

        tuberculosis11 = tuberculosisArr[1].get()
        if tuberculosis11 == '':
            tuberculosis11 = None

        tuberculosis20 = tuberculosisArr[2].get()
        if tuberculosis20 != '':
            if not self.is_date(tuberculosis20):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            tuberculosis20 = None

        tuberculosis21 = tuberculosisArr[3].get()
        if tuberculosis21 == '':
            tuberculosis21 = None

        tuberculosis30 = tuberculosisArr[4].get()
        if tuberculosis30 != '':
            if not self.is_date(tuberculosis30):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            tuberculosis30 = None

        tuberculosis31 = tuberculosisArr[5].get()
        if tuberculosis31 == '':
            tuberculosis31 = None

#Restrictions_And_Recommendations
        if restrictionsRec == '':
            restrictionsRec = None

#medcare provider medications
        medProMed11 = medProMedArr[0].get()
        if medProMed11 == '':
            medProMed11 = None

        medProMed12 = medProMedArr[1].get()
        if medProMed12 == '':
            medProMed12 = None
        
        medProMed13 = medProMedArr[2].get()
        if medProMed13 == '':
            medProMed13 = None

        medProMed21 = medProMedArr[3].get()
        if medProMed21 == '':
            medProMed21 = None

        medProMed22 = medProMedArr[4].get()
        if medProMed22 == '':
            medProMed22 = None

        medProMed23 = medProMedArr[5].get()
        if medProMed23 == '':
            medProMed23 = None

        medProMed31 = medProMedArr[6].get()
        if medProMed31 == '':
            medProMed31 = None

        medProMed32 = medProMedArr[7].get()
        if medProMed32 == '':
            medProMed32 = None

        medProMed33 = medProMedArr[8].get()
        if medProMed33 == '':
            medProMed33 = None

        medProMed41 = medProMedArr[9].get()
        if medProMed41 == '':
            medProMed41 = None

        medProMed42 = medProMedArr[10].get()
        if medProMed42 == '':
            medProMed42 = None

        medProMed43 = medProMedArr[11].get()
        if medProMed43 == '':
            medProMed43 = None

        medProMed51 = medProMedArr[12].get()
        if medProMed51 == '':
            medProMed51 = None

        medProMed52 = medProMedArr[13].get()
        if medProMed52 == '':
            medProMed52 = None

        medProMed53 = medProMedArr[14].get()
        if medProMed53 == '':
            medProMed53 = None

        medProMed61 = medProMedArr[15].get()
        if medProMed61 == '':
            medProMed61 = None

        medProMed62 = medProMedArr[16].get()
        if medProMed62 == '':
            medProMed62 = None

        medProMed63 = medProMedArr[17].get()
        if medProMed63 == '':
            medProMed63 = None

        medProMed71 = medProMedArr[18].get()
        if medProMed71 == '':
            medProMed71 = None

        medProMed72 = medProMedArr[19].get()
        if medProMed72 == '':
            medProMed72 = None

        medProMed73 = medProMedArr[20].get()
        if medProMed73 == '':
            medProMed73 = None

        medProMed81 = medProMedArr[21].get()
        if medProMed81 == '':
            medProMed81 = None

        medProMed82 = medProMedArr[22].get()
        if medProMed82 == '':
            medProMed82 = None

        medProMed83 = medProMedArr[23].get()
        if medProMed83 == '':
            medProMed83 = None

        medProMed91 = medProMedArr[24].get()
        if medProMed91 == '':
            medProMed91 = None

        medProMed92 = medProMedArr[25].get()
        if medProMed92 == '':
            medProMed92 = None

        medProMed93 = medProMedArr[26].get()
        if medProMed93 == '':
            medProMed93 = None

        medProMed101 = medProMedArr[27].get()
        if medProMed101 == '':
            medProMed101 = None

        medProMed102 = medProMedArr[28].get()
        if medProMed102 == '':
            medProMed102 = None

        medProMed103 = medProMedArr[29].get()
        if medProMed103 == '':
            medProMed103 = None

        medProMedications = [medProMed11, medProMed12, medProMed13, medProMed21, medProMed22, medProMed23, medProMed31, medProMed32, medProMed33, medProMed41, medProMed42, medProMed43,
        medProMed51, medProMed52, medProMed53, medProMed61, medProMed62, medProMed63, medProMed71, medProMed72, medProMed73, medProMed81, medProMed82, medProMed83,
        medProMed91, medProMed92, medProMed93, medProMed101, medProMed102, medProMed103]

#medcare provider verification statement
        medProvVerState0 = medProvVerStateArr[0].get()
        if medProvVerState0 == 0:
            medProvVerState0 = None
        elif medProvVerState0 == 2:
            medProvVerState0 = 0

        medProvVerState1 = medProvVerStateArr[1].get()
        if medProvVerState1 != '':
            if not self.is_date(medProvVerState1):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            medProvVerState1 = None

        medProvVerState2 = medProvVerStateArr[2].get()
        if medProvVerState2 == '':
            medProvVerState2 = None

        medProvVerState3 = medProvVerStateArr[3].get()
        if medProvVerState3 == '':
            medProvVerState3 = None

        medProvVerState4 = medProvVerStateArr[4].get()
        if medProvVerState4 == '':
            medProvVerState4 = None

        medProvVerState5 = medProvVerStateArr[5].get()
        if medProvVerState5 == '':
            medProvVerState5 = None

        medProvVerState6 = medProvVerStateArr[6].get()
        if medProvVerState6 != '':
            if self.is_number(medProvVerState6):
                medProvVerState6 = int(medProvVerState6)
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nZip must be only numbers.")
                goodData = 0
        else:
            medProvVerState6 = None

        medProvVerState7 = medProvVerStateArr[7].get()
        if medProvVerState7 == '':
            medProvVerState7 = None

        medProvVerState8 = medProvVerStateArr[8].get()
        if medProvVerState8 == '':
            medProvVerState8 = None

#health history
        healthHistory0 = healthHistoryArr[0].get()
        if healthHistory0 == '':
            healthHistory0 = None

        healthHistory = ''

        if healthHistoryArr[1].get():
            healthHistory = healthHistory + 'HIV,'

        if healthHistoryArr[2].get():
            healthHistory = healthHistory + 'Hepatitis B,'

        if healthHistoryArr[3].get():
            healthHistory = healthHistory + 'Hepatitis C,'

        if healthHistoryArr[4].get():
            healthHistory = healthHistory + 'Poor growth,'

        if healthHistoryArr[5].get():
            healthHistory = healthHistory + 'Bleeding disorders,'

        if healthHistoryArr[6].get():
            healthHistory = healthHistory + 'Asthma,'

        if healthHistoryArr[7].get():
            healthHistory = healthHistory + 'Pulmonary Disease,'

        if healthHistoryArr[8].get():
            healthHistory = healthHistory + 'Chronic Cough,'

        if healthHistoryArr[9].get():
            healthHistory = healthHistory + 'ADD or ADHD,'

        if healthHistoryArr[10].get():
            healthHistory = healthHistory + 'Renal Disease,'

        if healthHistoryArr[11].get():
            healthHistory = healthHistory + 'Sickle Cell disease,'

        if healthHistoryArr[12].get():
            healthHistory = healthHistory + 'Congenital Heart Disease,'

        if healthHistoryArr[13].get():
            healthHistory = healthHistory + 'Hypertension,'

        if healthHistoryArr[14].get():
            healthHistory = healthHistory + 'Cryptosporidium,'

        if healthHistoryArr[15].get():
            healthHistory = healthHistory + 'Chronic diarrhea,'

        if healthHistoryArr[16].get():
            healthHistory = healthHistory + 'Seizures,'

        if healthHistoryArr[17].get():
            healthHistory = healthHistory + 'Diabetes,'

        if healthHistoryArr[18].get():
            healthHistory = healthHistory + 'Other,'

        if healthHistory == '':
            healthHistory = None
        else:
            healthHistory = healthHistory[:-1]

        healthHistory19 = healthHistoryArr[19].get()
        if healthHistory19 == '':
            healthHistory19 = None

        healthHistory20 = healthHistoryArr[20].get()
        if healthHistory20 == 0:
            healthHistory20 = None
        elif healthHistory20 == 2:
            healthHistory20 = 0

        healthHistory21 = healthHistoryArr[21].get()
        if healthHistory21 == '':
            healthHistory21 = None

#lab data
        lab0 = labArr[0].get()
        if lab0 == '':
            lab0 = None

        lab1 = labArr[1].get()
        if lab1 != '':
            if not self.is_date(lab1):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            lab1 = None

        lab2 = labArr[2].get()
        if lab2 == '':
            lab2 = None

        lab3 = labArr[3].get()
        if lab3 == '':
            lab3 = None

        lab4 = labArr[4].get()
        if lab4 == '':
            lab4 = None

        lab5 = labArr[5].get()
        if lab5 != '':
            if not self.is_date(lab5):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            lab5 = None

        lab6 = labArr[6].get()
        if lab6 == '':
            lab6 = None

        lab7 = labArr[7].get()
        if lab7 == '':
            lab7 = None

        lab8 = labArr[8].get()
        if lab8 != '':
            if not self.is_date(lab8):
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nIncompatible entry in Camper's Information\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
                goodData = 0
        else:
            lab8 = None

        lab9 = labArr[9].get()
        if lab9 == '':
            lab9 = None

        lab10 = labArr[10].get()
        if lab10 == '':
            lab10 = None

#Database Connection
        db = self.connect()
        curr = db.cursor()

#Insert into DB
        if goodData:


#TODO: delete this!!!

            curr.execute("""DELETE FROM Camp_Application WHERE ID = %s AND Date_Submitted = %s;""", (id, date,))


            errorCode = 0

#camp application
            try:
                curr.execute("""INSERT INTO Camp_Application VALUES (
                %s, %s);""",
                (id, date,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 1
                print e
                print errorCode

#Parent section
            try:
                curr.execute("""INSERT INTO Parent VALUES (
                %s, %s);""",
                (id, date,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 2
                print e
                print errorCode

   #Demographic_Information
            try:
                curr.execute("""INSERT INTO Demographic_Information VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        demInfo0, demInfo1, demInfo2, demInfo3, demInfo4, demInfo5, demInfo6, demInfo7, demInfo8, demInfo9, demInfo10, demInfo11,
                        demInfo12, demInfo13, demInfo14, demInfo15, demInfo16, demInfo17, demInfo18, demInfo19, demInfo20, demInfoTransport
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 3
                print e
                print errorCode

    #Demographic_Contacts
            try:
                curr.execute("""INSERT INTO Demographic_Contacts VALUES (%s, %s, 'Cell', %s, %s, %s);""",
                    (id, date,
                        demContactInfo10, demContactInfoTime1, demContactInfo11
                        ,))

                curr.execute("""INSERT INTO Demographic_Contacts VALUES (%s, %s, 'Home', %s, %s, %s);""",
                    (id, date,
                        demContactInfo20, demContactInfoTime2, demContactInfo21
                        ,))

                curr.execute("""INSERT INTO Demographic_Contacts VALUES (%s, %s, 'Work', %s, %s, %s);""",
                    (id, date,
                        demContactInfo30, demContactInfoTime3, demContactInfo31
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 4
                print e
                print errorCode

    #Parent_Emergency_Contact
            try:
                if emergencyInfo10 is not None:
                    curr.execute("""INSERT INTO Parent_Emergency_Contact VALUES (%s, %s, %s, %s, %s, %s);""",
                        (id, date, 
                            emergencyInfo10, emergencyInfo11, emergencyInfo12, emergencyInfo13
                            ,))
                
                if emergencyInfo20 is not None:
                    curr.execute("""INSERT INTO Parent_Emergency_Contact VALUES (%s, %s, %s, %s, %s, %s);""",
                        (id, date, 
                            emergencyInfo20, emergencyInfo21, emergencyInfo22, emergencyInfo23
                            ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 5
                print e
                print errorCode

    #Insurance_Information
            try:
                curr.execute("""INSERT INTO Insurance_Information VALUES (%s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        insuranceInfo0, insuranceInfo1, insuranceInfo2, insuranceInfo3
                        ,))

            except (MySQLdb.Error) as e:
                errorCode = 6
                print e
                print errorCode

    #Medical_Provider_Information
            try:
                curr.execute("""INSERT INTO Medical_Provider_Information VALUES (%s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        medProviderInfo0, medProviderInfo1, medProviderInfo2, medProviderInfo3
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 7
                print e
                print errorCode

    #Medical_Information
            try:
                curr.execute("""INSERT INTO Medical_Information VALUES (%s, %s, %s, %s, %s);""",
                    (id, date, 
                        medInfoCurr, medInfo0, medInfo1
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 8
                print e
                print errorCode

    #Allergies
            try:
                curr.execute("""INSERT INTO Allergies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        allergyInfo0, allergyInfo1, allergyInfo2, allergyInfo3, allergyInfo4, allergyInfo5, allergyInfo6
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 9
                print e
                print errorCode

    #Dietary_Needs
            try:
                curr.execute("""INSERT INTO Dietary_Needs VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        dietaryNeedsInfo0, dietaryNeedsInfo1, dietaryNeedsInfo2, dietaryNeedsInfo3, dietaryNeedsInfo4,
                        dietaryNeedsHowInfo, dietaryNeedsInfo5, dietaryNeedsInfo6, dietaryNeedsInfo7, dietaryNeedsInfo8, dietaryNeedsInfo9
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 10
                print e
                print errorCode

    #General_Health
            try:
                curr.execute("""INSERT INTO General_Health VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        genHealthLimit, genHealth0, genHealth1, genHealth2, genHealth3, genHealth4, genHealth5, genHealth6
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 11
                print e
                print errorCode

    #Pyschosocial_and_Behavioral
            try:
                curr.execute("""INSERT INTO Pyschosocial_and_Behavioral_info VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        behavior0, behavior1, behaviorExperiances, behavior2, behavior3, behaviorInterests, behavior4
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 12
                print e
                print errorCode

    #Parent_Medical
            try:
                i = 0
                while i < len(parentMeds):
                    if parentMeds[i] is None:
                        break
                    curr.execute("""INSERT INTO Parent_Medications VALUES (%s, %s, %s, %s, %s);""",
                        (id, date, 
                            parentMeds[i], parentMeds[i + 1], parentMeds[i + 2]
                            ,))
                    i += 3

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 13
                print e
                print errorCode

    #Release_Forms_Signed
            try:
                curr.execute("""INSERT INTO Release_Forms_Signed VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                        parentSig0, parentSig1, parentSig2, parentSig3, parentSig4, parentSig5
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 14
                print e
                print errorCode

#Medical_Care_Provider section
            try:
                curr.execute("""INSERT INTO Medical_Care_Provider VALUES (%s, %s, %s);""",
                    (id, date,
                        restrictionsRec
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 15
                print e
                print errorCode

    #Medical_History
            try:
                curr.execute("""INSERT INTO Medical_History VALUES (%s, %s, %s, %s, %s, %s);""",
                    (id, date,
                        medProvider5, medProvider6, medProvider7, medProvider8
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 16
                print e
                print errorCode

    #Med_Hist_Diagnosis
            try:
                i = 0
                while i < len(medHistDiagnosis):
                    if medHistDiagnosis[i] is None:
                        break
                    curr.execute("""INSERT INTO Med_Hist_Diagnosis VALUES (%s, %s, %s);""",
                        (id, date,
                            medHistDiagnosis[i]
                            ,))
                    i += 1

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 17
                print e
                print errorCode

    #Med_Hist_Allergies
            try:
                i = 0
                while i < len(foodAllergies):
                    if foodAllergies[i] is None:
                        break
                    curr.execute("""INSERT INTO Med_Hist_Allergies VALUES (%s, %s, %s, %s, %s);""",
                        (id, date,
                            'Food', foodAllergies[i], foodAllergies[i + 1]
                            ,))
                    i += 2

                i = 0
                while i < len(medAllergies):
                    if medAllergies[i] is None:
                        break
                    curr.execute("""INSERT INTO Med_Hist_Allergies VALUES (%s, %s, %s, %s, %s);""",
                        (id, date,
                            'Medication', medAllergies[i], medAllergies[i + 1]
                            ,))
                    i += 2

                i = 0
                while i < len(envAllergies):
                    if envAllergies[i] is None:
                        break
                    curr.execute("""INSERT INTO Med_Hist_Allergies VALUES (%s, %s, %s, %s, %s);""",
                        (id, date,
                            'Environmental', envAllergies[i], envAllergies[i + 1]
                            ,))
                    i += 2

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 18
                print e
                print errorCode

    #Physical_Exam
            try:
                curr.execute("""INSERT INTO Physical_Exam VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                        physical0, physical1, physical2, physical3, physical4, physical5, physical6, physical7, physical8, physical9,
                        physical10, physical11, physical12, physical13, physical14, physical15, physical16, physical17
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 19
                print e
                print errorCode

    #Cognitive_Development_Level
            try:
                curr.execute("""INSERT INTO Cognitive_Development_Level VALUES (%s, %s, %s, %s);""",
                    (id, date,
                        cogDev0, cogDev1
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 20
                print e
                print errorCode

    #Varicella_Screening
            try:
                curr.execute("""INSERT INTO Varicella_Screening VALUES (%s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                        varicella0, varicella1, varicella2, varicella3, varicella4
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 21
                print e
                print errorCode

    #tuberculosis screening
            try:
                curr.execute("""INSERT INTO Tuberculosis_Screening VALUES (%s, %s, 'Tuberculin Skin Test', %s, %s);""",
                    (id, date,
                        tuberculosis10, tuberculosis11
                        ,))
                
                curr.execute("""INSERT INTO Tuberculosis_Screening VALUES (%s, %s, 'Quantiferon Testing', %s, %s);""",
                    (id, date,
                        tuberculosis20, tuberculosis21
                        ,))
                
                curr.execute("""INSERT INTO Tuberculosis_Screening VALUES (%s, %s, 'Chest X-ray', %s, %s);""",
                    (id, date,
                        tuberculosis30, tuberculosis31
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 22
                print e
                print errorCode

    #medcare provider medications
            try:
                i = 0
                while i < len(medProMedications):
                    if medProMedications[i] is None:
                        break
                    curr.execute("""INSERT INTO MedCareProvider_Medications VALUES (%s, %s, %s, %s, %s);""",
                        (id, date,
                            medProMedications[i], medProMedications[i + 1], medProMedications[i + 2]
                            ,))
                    i += 3

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 23
                print e
                print errorCode

    #medcare provider verification statement
            try:
                curr.execute("""INSERT INTO Medical_Provider_Verification_Statement VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                        medProvVerState0, medProvVerState1, medProvVerState2, medProvVerState3, medProvVerState4, medProvVerState5, medProvVerState6, medProvVerState7, medProvVerState8
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 24
                print e
                print errorCode

#HIV_Provider section
            try:
                curr.execute("""INSERT INTO HIV_Provider VALUES (%s, %s);""",
                    (id, date,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 25
                print e
                print errorCode

    #health history
            try:
                curr.execute("""INSERT INTO Health_History VALUES (%s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                        healthHistory0, healthHistory, healthHistory19, healthHistory20, healthHistory21
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 26
                print e
                print errorCode

    #lab data
            try:
                curr.execute("""INSERT INTO Lab_Data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                        lab0, lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9, lab10
                        ,))

            except (MySQLdb.Error) as e:
                success = 0
                errorCode = 28
                print e
                print errorCode


#last stuff
            db.commit()

            if success:
                tkMessageBox.showinfo("New Profile", "Submission Sucessful!")
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nA Camper application \nSubmitted on: " + date + "\nFor ID number: " + str(id) + " \nAlready exists in the system.")


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


if __name__ == "__main__":
    master=tk.Tk()
    Example(master).pack(side="top", fill="both", expand=True)
    master.mainloop()
