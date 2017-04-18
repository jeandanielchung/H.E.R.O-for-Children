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
        self.DemographicSectionframe = Frame(self.frame)
        self.DemographicSectionframe.pack(fill = 'y', side = 'left') 

#Identifying Info Section    
        #header
        labelDemographicSection = Label(self.DemographicSectionframe, text = "\nIDENTIFYING INFORMATION")
        labelDemographicSection.pack(fill = "x")
        labelDemographicSection.config(font=("Helvetica", 20))

        #id
        label = Label(self.DemographicSectionframe, text = "\nChild ID .................................................................................................. " + str(id))
        label.pack(anchor = 'w')

        #date
        label = Label(self.DemographicSectionframe, text = "\nDate Submitted ...................................................................................... " + date)
        label.pack(anchor = 'w')
        
#Demographic info section
        #header
        labelDemographicSection = Label(self.DemographicSectionframe, text = "\n\nDEMOGRAPHIC INFORMATION")
        labelDemographicSection.pack(fill = "x")
        labelDemographicSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT First_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFirst Name ............................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nFirst Name ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #last name
        curr.execute("SELECT Last_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nLast Name ............................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nLast Name  ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #middle initial
        curr.execute("SELECT Middle_Initial FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMiddle Initial ............................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMiddle Initial  ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #age
        curr.execute("SELECT Age FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAge .......................................................................................................... " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nAge .......................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                
        #birthday
        curr.execute("SELECT Date_Of_Birth FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDate of Birth (YYYY-MM-DD) .............................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nDate of Birth (YYYY-MM-DD) .............................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #gender
        curr.execute("SELECT Gender FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nGender .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nGender .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #race
        curr.execute("SELECT Race FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nRace ...................................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nRace ...................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #language
        curr.execute("SELECT Primary_Language FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPrimary Language ........................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nPrimary Language ........................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #address street
        curr.execute("SELECT Address_Street FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nStreet Address ...................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nStreet Address ...................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address city
        curr.execute("SELECT Address_City FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nCity ....................................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nCity ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address state
        curr.execute("SELECT Address_State FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nState .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nState .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #address county
        curr.execute("SELECT Address_County FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nCounty .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nCounty .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                
        #address zip
        curr.execute("SELECT Address_Zip FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nZip ........................................................................................................ " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nZip ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #camper email
        curr.execute("SELECT Camper_Email FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nCamper Email ............................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nCamper Email ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Parent email
        curr.execute("SELECT Parent_Email FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nParent Email ............................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nParent Email ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Guardian name
        curr.execute("SELECT Guardian_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nGuardian Name .............................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nGuardian Name .............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Guardian Camper Relationship
        curr.execute("SELECT Guardian_Camper_Relationship FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nGuardian Camper Relationship ............................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nGuardian Camper Relationship ............................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Last Grade COmpleted
        curr.execute("SELECT Last_Grade_Completed FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nLast Grade Completed ........................................................................................... " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nLast Grade Completed ........................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Special Ed Classes
        curr.execute("SELECT Special_Ed_Classes FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nSpecial Ed Classes? .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nSpecial Ed Classes? .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nSpecial Ed Classes? .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #siblings applying
        curr.execute("SELECT Siblings_Applying FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nSiblings Applying? .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nSiblings Applying? .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nSiblings Applying? .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #t-shirt size
        curr.execute("SELECT T_Shirt FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nT-Shirt Size ............................................................................................ " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nT-Shirt Size ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Transportation
        curr.execute("SELECT Planned_Transportation FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPlanned Transportation .................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nPlanned Transportation .................................................................. Unanswered")
        label.pack(anchor = 'w')
        
#demographic contacts
        #header
        labelContactsSection = Label(self.DemographicSectionframe, text = "\n\nCONTACT INFORMATION")
        labelContactsSection.pack(fill = "x")
        labelContactsSection.config(font=("Helvetica", 20))

        #type
        curr.execute("SELECT Type FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPhone Number Type .............................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nPhone Number Type .............................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Name
        curr.execute("SELECT Name FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nContact Name ............................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nContact Name ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        

        #time pref
        curr.execute("SELECT Time_Preference FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nTime Preference ............................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nTime Preference ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #phone number
        curr.execute("SELECT Phone_Number FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPhone Number ............................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nPhone Number ............................................................................................. Unanswered")
        label.pack(anchor = 'w')


#Parent/ Guardian Emergency Contact Section
        #header
        labelEmergencySection = Label(self.DemographicSectionframe, text = "\n\nEMERGENCY CONTACT INFORMATION")
        labelEmergencySection.pack(fill = "x")
        labelEmergencySection.config(font=("Helvetica", 20))

        #Name
        curr.execute("SELECT Name FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nEmergency Contact Name .................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nEmergency Contact Name .................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Relationship
        curr.execute("SELECT Relationship FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nRelationship to Camper .................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nRelationship to Camper .................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Daytime Phone
        curr.execute("SELECT Daytime_Phone FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDaytime Phone ............................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nDaytime Phone ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Evening Phone
        curr.execute("SELECT Evening_Phone FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nEvening Phone ............................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nEvening Phone ............................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
#Insurance Info Section
        #header
        labelInsuranceSection = Label(self.DemographicSectionframe, text = "\n\nINSURANCE INFORMATION")
        labelInsuranceSection.pack(fill = "x")
        labelInsuranceSection.config(font=("Helvetica", 20))

        #Insurer
        curr.execute("SELECT Type_of_Health_Insurance FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nHealth Insurance Provider ................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nHealth Insurance Provider ................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Policy Number
        curr.execute("SELECT Policy_Number FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPolicy Number ............................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nPolicy Number ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Group Number
        curr.execute("SELECT Type_of_Health_Insurance FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nGroup Number ............................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nGroup Number ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

#Medical Provider Section
        #header
        labelMedicalSection = Label(self.DemographicSectionframe, text = "\n\nMEDICAL PROVIDER INFORMATION")
        labelMedicalSection.pack(fill = "x")
        labelMedicalSection.config(font=("Helvetica", 20))
                
        #Name
        curr.execute("SELECT Medical_Provider_Name FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMedical Provider Name ...................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedical Provider Name ...................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Office Phone
        curr.execute("SELECT Phone_Office FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMedical Provider Office Phone Number .................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedical Provider Office Phone Number .................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Pharmacy name
        curr.execute("SELECT Pharmacy_Name FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nName of Pharmacy ................................................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nName of Pharmacy ................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Pharmacy Phone Number
        curr.execute("SELECT Phone_Pharmacy FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPharmacy Phone Number ...................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nPharmacy Phone Number ...................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
#Medical Information Section
        #header
        labelMedInfoSection = Label(self.DemographicSectionframe, text = "\n\nMEDICAL INFORMATION")
        labelMedInfoSection.pack(fill = "x")
        labelMedInfoSection.config(font=("Helvetica", 20))

        #Conditions
        curr.execute("SELECT Current_Medical_Conditions FROM Medical_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nCurrent Medical Conditions ............................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nCurrent Medical Conditions ............................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Conditions Explained
        curr.execute("SELECT Medical_Condition_Explanation FROM Medical_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDescription of Medical Conditions ........................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nDescription of Medical Conditions .......................................................... Unanswered")
        label.pack(anchor = 'w')
        
#Allergies Section
        #header
        labelAllergySection = Label(self.DemographicSectionframe, text = "\n\nALLERGY INFORMATION")
        labelAllergySection.pack(fill = "x")
        labelAllergySection.config(font=("Helvetica", 20))

        #Food Allergy
        curr.execute("SELECT Food_Allergy FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nFood Allergies? .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nFood Allergies? .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nFood Allergies? .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Food Allergy Reaction
        curr.execute("SELECT Food_Reaction FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFood Allergy Reaction ..................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nFood Allergy Reaction ..................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Environmental Allergies
        curr.execute("SELECT Env_Allergy FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nEnvironmental Allergies? .................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nEnvironmental Allergies? .................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nEnvironmental Allergies? .................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Environmental Allergy Reaction
        curr.execute("SELECT Env_Reaction FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nEnvironmental Allergy Reaction ........................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nEnvironmental Allergy Reaction ........................................................... Unanswered")
        label.pack(anchor = 'w')

#Dietary Needs Section
        #header
        labelDietarySection = Label(self.DemographicSectionframe, text = "\n\nDIETARY INFORMATION")
        labelDietarySection.pack(fill = "x")
        labelDietarySection.config(font=("Helvetica", 20))

        #Special Dietary Needs
        curr.execute("SELECT Special_Dietary_Needs FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nSpecial Dietary Needs .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nSpecial Dietary Needs .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nSpecial Dietary Needs .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Vegetarian
        curr.execute("SELECT Vegetarian FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nVegetarian .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nVegetarian .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nVegetarian .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Food Restrictions
        curr.execute("SELECT Food_Restrictions FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFood Restrictions ............................................................................ " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nFood Restrictions ............................................................................. Unanswered")
        label.pack(anchor = 'w')

        #G Tube
        curr.execute("SELECT G_Tube FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nG-Tube ..................................................................................................... " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nG-Tube ................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Formula SUpplements
        curr.execute("SELECT Formula_Supplements FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFormula Supplements .......................................................................................... " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nFormula Supplements .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Formula Type
        curr.execute("SELECT Formula_Type FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFormula Type .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nFormula Type .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #cans per day
        curr.execute("SELECT Formula_Cans_Per_Day FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFormula Cans Per Day .......................................................................................... " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nFormula Cans Per Day .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Feeding Pump
        curr.execute("SELECT Feeding_Pump FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFeeding Pump ............................................................................................... " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nFeeding Pump ............................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Feeding schedule
        curr.execute("SELECT Feeding_Schedule FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFeeding Schedule .......................................................................................... " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nFeeding Schedule .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

#General health
        #header
        labelFoodNeedsSection = Label(self.DemographicSectionframe, text = "\n\nGENERAL HEALTH INFORMATION")
        labelFoodNeedsSection.pack(fill = "x")
        labelFoodNeedsSection.config(font=("Helvetica", 20))

        #Physical Limitations
        curr.execute("SELECT Other FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        other = curr.fetchall()[0][0]
        if other is not None:
            label = Label(self.DemographicSectionframe, text = "\nPhysical Limitations ....................................................................... " + other)
        else:
            curr.execute("SELECT Physical_Limitations FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            val = curr.fetchall()[0][0]
            if val is not None:
                label = Label(self.DemographicSectionframe, text = "\nPhysical Limitations ....................................................................... " + val)
            else:
                label = Label(self.DemographicSectionframe, text = "\nPhysical Limitations ....................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Tire Easily
        curr.execute("SELECT Tire_Easily FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nTire Easily .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nTire Easily .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nTire Easily .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Swim
        curr.execute("SELECT Swim FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nCan Swim .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nCan Swim .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nCan Swim .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Chicken Pox
        curr.execute("SELECT Chicken_Pox FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nChicken Pox Vaccinated? .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nChicken Pox Vaccinated? .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nChicken Pox Vaccinated? .......................................................................................... Unanswered")
        label.pack(anchor = 'w')


        #c pox date
        curr.execute("SELECT Chicken_Pox_Date FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nChicken Pox Date ............................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nChicken Pox Date ............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Menstrual Cycle
        curr.execute("SELECT Menstrual_Cycle FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nMenstrual Cycle .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nMenstrual Cycle .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nMenstrual Cycle .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #m cycle difficulties
        curr.execute("SELECT Menstrual_Difficulties FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMenstrual Difficulties ....................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMenstrual Difficulties ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
#Behavior
        #header
        labelBehaviorSection = Label(self.DemographicSectionframe, text = "\n\nBEHAVIORAL INFORMATION")
        labelBehaviorSection.pack(fill = "x")
        labelBehaviorSection.config(font=("Helvetica", 20))

        #Camper knows
        curr.execute("SELECT Time_Camper_Known FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nHow Long has Camper Been Aware of HIV/AIDS Impacting Them? .......................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nHow Long has Camper Been Aware of HIV/AIDS Impacting Them? ..................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Camper experiences
        curr.execute("SELECT Camper_Experiences FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nExperiences of Camper .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nExperiences of Camper .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #medication for hyperactivity
        curr.execute("SELECT Med_Hyper_AttentionProb FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nCamper Takes Medicine for Hyperactivity .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nCamper Takes Medicine for Hyperactivity .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nCamper Takes Medicine for Hyperactivity .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #experience explanation
        curr.execute("SELECT Explanation FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nExplanation of Experiences .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nExplanation of Experiences .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Camper interests
        curr.execute("SELECT Camper_Interests FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nInterests of Camper .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nInterests of Camper .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Recent major events
        curr.execute("SELECT Recent_Major_Events FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nRecent Events for Camper .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nRecent Events for Camper .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        
#Medication Info
        #header
        labelFoodNeedsSection = Label(self.DemographicSectionframe, text = "\n\nMEDICATION INFORMATION")
        labelFoodNeedsSection.pack(fill = "x")
        labelFoodNeedsSection.config(font=("Helvetica", 20))

        #medications
        curr.execute("SELECT Medication FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMedication Taken .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedication Taken .................................................................................................. Unanswered")
        label.pack(anchor = 'w')


        #medications
        curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMedication Amount .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedication Amount .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #medications
        curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMedication Frequency .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedication Frequency .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

            
 #preliminary signatures
        #header
        labelSignatureSection = Label(self.DemographicSectionframe, text = "\n\nPARENTAL CONSENT INFORMATION")
        labelSignatureSection.pack(fill = "x")
        labelSignatureSection.config(font=("Helvetica", 20))

        #parent camper contract
        curr.execute("SELECT Parent_Camper_Contract FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nParental Consent and Release Form Signed .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nParental Consent and Release Form Signed .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nParental Consent and Release Form Signed .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #participation release
        curr.execute("SELECT Partcipation_Consent_Liability_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nParticipation Consent/Liability Release/Disputes Form Signed ............................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nParticipation Consent/Liability Release/Disputes Form Signed .............................................................. No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nParticipation Consent/Liability Release/Disputes Form Signed ................................................................... Unanswered")
        label.pack(anchor = 'w')

                    
        #Media release
        curr.execute("SELECT Media_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nMedia Release Form Signed .................................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nMedia Release Form Signed .................................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedia Release Form Signed .................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #hiv ed waiver
        curr.execute("SELECT Camper_HIV_Education FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nHIV Education Waiver Signed .................................................................................................. Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nHIV Education Waiver Signed .................................................................................................. No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nHIV Education Waiver Signed .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #camp rules form signed
        curr.execute("SELECT Camp_Twin_Lakes_Rules FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nRules Acknowledgement Form Signed .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nRules Acknowledgement Form Signed .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nRules Acknowledgement Form Signed .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #parental consent and release
        curr.execute("SELECT Parental_Consent_And_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nParental Consent and Release Form Signed .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nParental Consent and Release Form Signed .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nParental Consent and Release Form Signed .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                  
 #Medical provider
        #header
        labelMedicalProviderSection = Label(self.DemographicSectionframe, text = "\n\nMEDICAL PROVIDER INFORMATION")
        labelMedicalProviderSection.pack(fill = "x")
        labelMedicalProviderSection.config(font=("Helvetica", 20))

        #medical diagnosis
        curr.execute("SELECT Diagnosis FROM Med_Hist_Diagnosis WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMedical Diagnosis .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedical Diagnosis .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #management
        curr.execute("SELECT Management FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMedical Management Comments ............................................................................ " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedical Management Comments ............................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
        #nutritional supplements
        curr.execute("SELECT Nutritional_Supplements FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nNutritional Supplements Taken? .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nNutritional Supplements Taken? .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nNutritional Supplements Taken? .......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #supplemetn comment
        curr.execute("SELECT Feeding_Care FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFeeding Care Comments ................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nFeeding Care Comments ................................................................................... Unanswered or Not Applicable")
        label.pack(anchor = 'w')
                    
        #formula type
        curr.execute("SELECT Formula_Type FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nFormula Type .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nFormula Type .................................................................................................. Unanswered or Not Applicable")
        label.pack(anchor = 'w')

        #Allergies
        curr.execute("SELECT Type FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAllergy Type .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nAllergy Type .................................................................................................. Unanswered or Not Applicable")
        label.pack(anchor = 'w')

        #a
        curr.execute("SELECT Allergy FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAllergic to .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nAllergic to .................................................................................................. Unanswered or Not Applicable")
        label.pack(anchor = 'w')

        #a r
        curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nReaction .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nReaction .................................................................................................. Unanswered or Not Applicable")
        label.pack(anchor = 'w')


                    
 #physical
        #header
        labelPhysicalSection = Label(self.DemographicSectionframe, text = "\n\nMOST RECENT PHYSICAL INFORMATION")
        labelPhysicalSection.pack(fill = "x")
        labelPhysicalSection.config(font=("Helvetica", 20))

        #date completed
        curr.execute("SELECT Date_Completed FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDate Completed .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nDate Completed .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #height
        curr.execute("SELECT Height FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nHeight .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nHeight .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #weight
        curr.execute("SELECT Height FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nWeight .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nWeight .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #pulse
        curr.execute("SELECT Pulse FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPulse .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nPulse .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #respirations
        curr.execute("SELECT Resperations FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nRespirations .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nRespirations .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #bp
        curr.execute("SELECT Blood_Pressure FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nBlood Pressure .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nBlood Pressure .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #HEENT
        curr.execute("SELECT HEENT FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nHEENT .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nHEENT .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #skin
        curr.execute("SELECT Height FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nSkin .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nSkin .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #cardio
        curr.execute("SELECT Cardiovascular FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nCardiovascular .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nCardiovascular .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #gu gyn
        curr.execute("SELECT GU_GYN FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nGU/GYN .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nGU/GYN .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #pulmonary
        curr.execute("SELECT Pulmonary FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPulmonary .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nPulmonary .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #g ha
        curr.execute("SELECT Glasses_HearingAids_PE FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nGlasses/Contacts/Hearing Aids/PE tubes .................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nGlasses/Contacts/Hearing Aids/PE tubes .................................................... Unanswered")
        label.pack(anchor = 'w')

        #Abdomen
        curr.execute("SELECT Abdomen FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAbdomen .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nAbdomen .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #LN
        curr.execute("SELECT Lymph_Nodes FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nLymph Nodes .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nLymph Nodes .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Extremities
        curr.execute("SELECT Extremities FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nExtremities .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nExtremities .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #spine
        curr.execute("SELECT Spine FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nSpine ......................................................................................................... " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nSpine ......................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Misc
        curr.execute("SELECT Miscellaneous FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMiscellaneous .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMiscellaneous .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #comm
        curr.execute("SELECT Comments FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nComments .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nComments .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
#cognative development level
        #header
        labelCogDevSection = Label(self.DemographicSectionframe, text = "\n\nCOGNITIVE DEVELOPMENT INFORMATION")
        labelCogDevSection.pack(fill = "x")
        labelCogDevSection.config(font=("Helvetica", 20))

        #development level
        curr.execute("SELECT Development_Level FROM Cognitive_Development_Level WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDevelopment Level .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nDevelopment Level .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #other info
        curr.execute("SELECT Other_Psychosocial_Information FROM Cognitive_Development_Level WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nOther Psychosocoal Information .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nOther Psychosocoal Information .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

#tuberculosis screening
        #header
        labelTuberculosisSection = Label(self.DemographicSectionframe, text = "\n\nTUBERCULOSIS SCREENING")
        labelTuberculosisSection.pack(fill = "x")
        labelTuberculosisSection.config(font=("Helvetica", 20))

        #type
        curr.execute("SELECT Type FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nTest Type .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nTest Type .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #date
        curr.execute("SELECT Date_Screened FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nTest Date .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nTest Date .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Result
        curr.execute("SELECT Result FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nTest Results .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nTest Results .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

#medcare provider medications
        #header
        labelMedicineProviderSection = Label(self.DemographicSectionframe, text = "\n\nMEDICAL PROVIDER MEDICATION INFORMATION")
        labelMedicineProviderSection.pack(fill = "x")
        labelMedicineProviderSection.config(font=("Helvetica", 20))

        #medication
        curr.execute("SELECT Medication_Name FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nMedication Name .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nMedication Name .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #amount
        curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAmount and Dosage .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nAmount and Dosage .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #times to give
        curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nTimes to Take Medicine .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nTimes to Take Medicine .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
#medcare provider verification statement
        #header
        labelMedicalStatementSection = Label(self.DemographicSectionframe, text = "\n\nMEDICAL PROVIDER VERIFICATION STATEMENT")
        labelMedicalStatementSection.pack(fill = "x")
        labelMedicalStatementSection.config(font=("Helvetica", 20))

        #signature
        curr.execute("SELECT Signature FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(self.DemographicSectionframe, text = "\nSignature Provided? .......................................................................................... Yes")
            else:
                label = Label(self.DemographicSectionframe, text = "\nSignature Provided? .......................................................................................... No")
        else:
            label = Label(self.DemographicSectionframe, text = "\nSignature Provided? .......................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #sugnature date
        curr.execute("SELECT Sig_Date FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDate .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nDate .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #name
        curr.execute("SELECT Name FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nExaminer Name .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nExaminer Name .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #address street
        curr.execute("SELECT Address_Street FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAddress Street .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nAddress Street .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #address city
        curr.execute("SELECT Address_City FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAddress City .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nAddress City .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #address state
        curr.execute("SELECT Address_State FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAddress State .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nAddress State .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #address zip
        curr.execute("SELECT Address_Zip FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nAddress Zipcode .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nAddress Zipcode .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #phone
        curr.execute("SELECT Phone FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPhone .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nPhone .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #emergency contact
        curr.execute("SELECT Emergency_Contact FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nEmergency Contact .................................................................................................. " + val)
        else:
            label = Label(self.DemographicSectionframe, text = "\nEmergency Contact .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

# #health history
#         #header
#         labelHealthHistorySection = Label(self.DemographicSectionframe, text = "\n\nHEALTH HISTORY INFORMATION FROM HIV PROVIDER")
#         labelHealthHistorySection.pack(fill = "x")
#         labelHealthHistorySection.config(font=("Helvetica", 20))
        
#         #surgical history
#         curr.execute("SELECT Major_Surgical_History FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
#         val = curr.fetchall()[0][0]
#         if val is not None:
#             label = Label(self.DemographicSectionframe, text = "\nMajor Surgical History .................................................................................................. " + val)
#         else:
#             label = Label(self.DemographicSectionframe, text = "\nMajor Surgical History .................................................................................................. Unanswered")
#         label.pack(anchor = 'w')
                    
#         #health history
#         curr.execute("SELECT Health_History FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
#         val = curr.fetchall()[0][0]
#         if val is not None:
#             label = Label(self.DemographicSectionframe, text = "\nMajor Surgical History .................................................................................................. " + val)
#         else:
#             label = Label(self.DemographicSectionframe, text = "\nMajor Surgical History .................................................................................................. Unanswered")
#         label.pack(anchor = 'w')
                    
#         #history of noncompliance
#         curr.execute("SELECT History_of_Noncompliance FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
#         val = curr.fetchall()[0][0]
#         if val is not None:
#             if val:
#                 label = Label(self.DemographicSectionframe, text = "\nHistory of Noncompliance? .......................................................................................... Yes")
#             else:
#                 label = Label(self.DemographicSectionframe, text = "\nHistory of Noncompliance? .......................................................................................... No")
#         else:
#             label = Label(self.DemographicSectionframe, text = "\nHistory of Noncompliance? .......................................................................................... Unanswered")
#         label.pack(anchor = 'w')
                    
#         #explanation
#         curr.execute("SELECT Explanation FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
#         val = curr.fetchall()[0][0]
#         if val is not None:
#             label = Label(self.DemographicSectionframe, text = "\nExplanation of Noncompliance .................................................................................................. " + val)
#         else:
#             label = Label(self.DemographicSectionframe, text = "\nExplanation of Noncompliance .................................................................................................. Unanswered")
#         label.pack(anchor = 'w')
        
#lab data
        #header
        labelHealthHistorySection = Label(self.DemographicSectionframe, text = "\n\nLAB DATA")
        labelHealthHistorySection.pack(fill = "x")
        labelHealthHistorySection.config(font=("Helvetica", 20))
        
        #lab1 date
        curr.execute("SELECT Lab1_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDate of Lab Examination ............................................................................................ " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nDate of Lab Examination ............................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab1 wbc
        curr.execute("SELECT Lab1_WBC FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nWhite Blood Cell Count .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nWhite Blood Cell Count .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab1 hgb
        curr.execute("SELECT Lab1_HGB FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nHemoglobin Level .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nHemoglobin Level .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab1 hct
        curr.execute("SELECT Lab1_HCT FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nHematocrit Level .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nHematocrit Level .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab1 plt
        curr.execute("SELECT Lab1_Plt_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nPlatelet Count .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nPlatelet Count .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab2 date
        curr.execute("SELECT Lab2_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDate of Second Lab Examination .......................................................................... " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nDate of Second Lab Examination .......................................................................... Unanswered")
        label.pack(anchor = 'w')

        #lab2 cd4
        curr.execute("SELECT Lab2_CD4_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nCD4 (T-Cell) Count .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nCD4 (T-Cell) Count .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab2 viral load
        curr.execute("SELECT Lab2_Viral_Load FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nViral Load .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nViral Load .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab3 date
        curr.execute("SELECT Lab3_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nDate of Third Lab Examination ............................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nDate of Third Lab Examination ............................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab3 cd4
        curr.execute("SELECT Lab3_CD4_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nCD4 (T-Cell) Count .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nCD4 (T-Cell) Count .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab3 viral load
        curr.execute("SELECT Lab3_Viral_Load FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(self.DemographicSectionframe, text = "\nViral Load .................................................................................................. " + str(val))
        else:
            label = Label(self.DemographicSectionframe, text = "\nViral Load .................................................................................................. Unanswered")
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
            #Delete cancelled
            showinfo('No', 'Delete has been cancelled')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    master=tk.Tk()
    Example(master).pack(side="top", fill="both", expand=True)
    master.mainloop()