import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import MySQLdb

#TODO: Immunization PDF
#TODO: deal with demographic contacts!!!

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
        master.geometry("1000x1000")


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
        DemographicSectionframe = Frame(self.frame)
        DemographicSectionframe.pack(fill = 'y', side = 'left') 

#Identifying Info Section 
        #header
        labelDemographicSection = Label(DemographicSectionframe, text = "\nIDENTIFYING INFORMATION")
        labelDemographicSection.pack(fill = "x")
        labelDemographicSection.config(font=("Helvetica", 20))

        #id
        label = Label(DemographicSectionframe, text = "\nChild ID ...................................................................................................................................... " + str(id))
        label.pack(anchor = 'w')

        #date
        label = Label(DemographicSectionframe, text = "\nDate Submitted .......................................................................................................................... " + date)
        label.pack(anchor = 'w')

#
#Parent sections
#

#Demographic info section
        #header
        labelDemographicSection = Label(DemographicSectionframe, text = "\n\nDEMOGRAPHIC INFORMATION")
        labelDemographicSection.pack(fill = "x")
        labelDemographicSection.config(font=("Helvetica", 20))

        #first name
        curr.execute("SELECT First_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFirst Name ................................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nFirst Name ................................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #last name
        curr.execute("SELECT Last_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nLast Name ................................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nLast Name  ................................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #middle initial
        curr.execute("SELECT Middle_Initial FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nMiddle Initial .............................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nMiddle Initial .............................................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #age
        curr.execute("SELECT Age FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nAge ............................................................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nAge ............................................................................................................................................ Unanswered")
        label.pack(anchor = 'w')
                
        #birthday
        curr.execute("SELECT Date_Of_Birth FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ..................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nDate of Birth (YYYY-MM-DD) ..................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #gender
        curr.execute("SELECT Gender FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nGender ...................................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nGender ...................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #race
        curr.execute("SELECT Race FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nRace .......................................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nRace .......................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #language
        curr.execute("SELECT Primary_Language FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nPrimary Language ...................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nPrimary Language ...................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #address street
        curr.execute("SELECT Address_Street FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nStreet Address ........................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nStreet Address ........................................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address city
        curr.execute("SELECT Address_City FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nCity ........................................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nCity ........................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #address state
        curr.execute("SELECT Address_State FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nState ......................................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nState ......................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #address county
        curr.execute("SELECT Address_County FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nCounty ...................................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nCounty ...................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                
        #address zip
        curr.execute("SELECT Address_Zip FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nZip ............................................................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nZip ............................................................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #camper email
        curr.execute("SELECT Camper_Email FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nCamper Email ............................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nCamper Email ............................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Parent email
        curr.execute("SELECT Parent_Email FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nParent Email .............................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nParent Email ............................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Guardian name
        curr.execute("SELECT Guardian_Name FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nGuardian Name .......................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nGuardian Name .......................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Guardian Camper Relationship
        curr.execute("SELECT Guardian_Camper_Relationship FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nGuardian Camper Relationship ................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nGuardian Camper Relationship ................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Last Grade Completed
        curr.execute("SELECT Last_Grade_Completed FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nLast Grade Completed ............................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nLast Grade Completed ............................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Special Ed Classes
        curr.execute("SELECT Special_Ed_Classes FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nSpecial Ed Classes? ................................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nSpecial Ed Classes? ................................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nSpecial Ed Classes? ................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #siblings applying
        curr.execute("SELECT Siblings_Applying FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nSiblings Applying? ..................................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nSiblings Applying? ..................................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nSiblings Applying? ..................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #t-shirt size
        curr.execute("SELECT T_Shirt FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nT-Shirt Size ............................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nT-Shirt Size ............................................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Transportation
        curr.execute("SELECT Planned_Transportation FROM Demographic_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nPlanned Transportation ............................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nPlanned Transportation .................................................................. Unanswered")
        label.pack(anchor = 'w')
        
#demographic contacts
        #header
        labelContactsSection = Label(DemographicSectionframe, text = "\n\nCONTACT INFORMATION")
        labelContactsSection.pack(fill = "x")
        labelContactsSection.config(font=("Helvetica", 20))

        curr.execute("SELECT Type FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        contactTypes = curr.fetchall()
        if contactTypes is not ():
            for cType in contactTypes:
                #type
                label = Label(DemographicSectionframe, text = "\nPhone Number Type ................................................................................................................... " + cType[0])
                label.pack(anchor = 'w')

                #Name
                curr.execute("SELECT Name FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, cType[0],))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "Contact Name ............................................................................................................................ " + val)
                else:
                    label = Label(DemographicSectionframe, text = "Contact Name ............................................................................................................................ Unanswered")
                label.pack(anchor = 'w')

                #time pref
                curr.execute("SELECT Time_Preference FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, cType[0],))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "Time Preference ......................................................................................................................... " + val)
                else:
                    label = Label(DemographicSectionframe, text = "Time Preference ......................................................................................................................... Unanswered")
                label.pack(anchor = 'w')

                #phone number
                curr.execute("SELECT Phone_Number FROM Demographic_Contacts WHERE ID = %s AND Date_Submitted = %s AND Type = %s;", (id, date, cType[0],))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "Phone Number ............................................................................................................................ " + val)
                else:
                    label = Label(DemographicSectionframe, text = "Phone Number ............................................................................................................................ Unanswered")
                label.pack(anchor = 'w')
        else:
            label = Label(DemographicSectionframe, text = "\nPhone Number Type ................................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nContact Name ............................................................................................................................ Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nTime Preference ......................................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nPhone Number ............................................................................................................................ Unanswered")
            label.pack(anchor = 'w')

#Parent/ Guardian Emergency Contact Section
        #header
        labelEmergencySection = Label(DemographicSectionframe, text = "\n\nEMERGENCY CONTACT INFORMATION")
        labelEmergencySection.pack(fill = "x")
        labelEmergencySection.config(font=("Helvetica", 20))


        #contacts
        curr.execute("SELECT Name FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        emergencyContacts = curr.fetchall()
        contactNum = 0
        if emergencyContacts is not ():
            for contact in emergencyContacts:
                contactNum += 1

                #taken
                label = Label(DemographicSectionframe, text = "\nEmergency Contact Name " + str(contactNum) + " ....................................................................................................... " + contact[0])
                label.pack(anchor = 'w')

                #Relationship
                curr.execute("SELECT Relationship FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, contact[0]))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. " + val)
                else:
                    label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. Unanswered")
                label.pack(anchor = 'w')
                            
                #Daytime Phone
                curr.execute("SELECT Daytime_Phone FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, contact[0]))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... " + val)
                else:
                    label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... Unanswered")
                label.pack(anchor = 'w')
                
                #Evening Phone
                curr.execute("SELECT Evening_Phone FROM Parent_Emergency_Contact WHERE ID = %s AND Date_Submitted = %s AND Name = %s;", (id, date, contact[0]))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... " + val)
                else:
                    label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... Unanswered")
                label.pack(anchor = 'w')
        
        if contactNum < 1:
            label = Label(DemographicSectionframe, text = "\nEmergency Contact Name 1 ....................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... Unanswered")
            label.pack(anchor = 'w')

        if contactNum < 2:
            label = Label(DemographicSectionframe, text = "\nEmergency Contact Name 2 ....................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "Relationship to Camper .............................................................................................................. Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "Daytime Phone ........................................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "Evening Phone ........................................................................................................................... Unanswered")
            label.pack(anchor = 'w')

#Insurance Info Section
        #header
        labelInsuranceSection = Label(DemographicSectionframe, text = "\n\nINSURANCE INFORMATION")
        labelInsuranceSection.pack(fill = "x")
        labelInsuranceSection.config(font=("Helvetica", 20))

        #Insurer
        curr.execute("SELECT Type_of_Health_Insurance FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nHealth Insurance Provider .......................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nHealth Insurance Provider .......................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Private Insurer Name
        curr.execute("SELECT Private_Insurance_Name FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nIf Private, Insurance Provider Name ........................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nIf Private, Insurance Provider Name ........................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Policy Number
        curr.execute("SELECT Policy_Number FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nPolicy Number ........................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nPolicy Number ........................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Group Number
        curr.execute("SELECT Group_Number FROM Insurance_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nGroup Number ........................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nGroup Number ........................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

#Medical Provider Section
        #header
        labelMedicalSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER INFORMATION")
        labelMedicalSection.pack(fill = "x")
        labelMedicalSection.config(font=("Helvetica", 20))
                
        #Name
        curr.execute("SELECT Medical_Provider_Name FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nMedical Provider Name .............................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nMedical Provider Name ............................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Office Phone
        curr.execute("SELECT Phone_Office FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nMedical Provider Office Phone Number ...................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nMedical Provider Office Phone Number ....................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Pharmacy name
        curr.execute("SELECT Pharmacy_Name FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nName of Pharmacy ..................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nName of Pharmacy ...................................................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Pharmacy Phone Number
        curr.execute("SELECT Phone_Pharmacy FROM Medical_Provider_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nPharmacy Phone Number ........................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nPharmacy Phone Number ...................................................................................... Unanswered")
        label.pack(anchor = 'w')

#Medical Information Section
        #header
        labelMedInfoSection = Label(DemographicSectionframe, text = "\n\nMEDICAL INFORMATION")
        labelMedInfoSection.pack(fill = "x")
        labelMedInfoSection.config(font=("Helvetica", 20))

        #Conditions + Other
        curr.execute("SELECT Current_Medical_Conditions FROM Medical_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        conditions = curr.fetchall()[0][0]
        curr.execute("SELECT Other FROM Medical_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        other = curr.fetchall()[0][0]
        if conditions is not None and other is not None:
            label = Label(DemographicSectionframe, text = "\nCurrent Medical Conditions ........................................................................................................ " + conditions + ": " + other)
        elif conditions is not None:
            label = Label(DemographicSectionframe, text = "\nCurrent Medical Conditions ........................................................................................................ " + conditions)
        else:
            label = Label(DemographicSectionframe, text = "\nCurrent Medical Conditions ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Conditions Explained
        curr.execute("SELECT Medical_Condition_Explanation FROM Medical_Information WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nDescription of Medical Conditions .............................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nDescription of Medical Conditions .............................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
#Allergies Section
        #header
        labelAllergySection = Label(DemographicSectionframe, text = "\n\nALLERGY INFORMATION")
        labelAllergySection.pack(fill = "x")
        labelAllergySection.config(font=("Helvetica", 20))

        #Med Allergy
        curr.execute("SELECT Med_Allergy FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nMedical Allergies? ...................................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nMedical Allergies? ...................................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nMedical Allergies? ...................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Med Allergy Reaction
        curr.execute("SELECT Med_Reaction FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nMedical Allergy Reaction ............................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nMedical Allergy Reaction ............................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Food Allergy
        curr.execute("SELECT Food_Allergy FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nFood Allergies? .......................................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nFood Allergies? .......................................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nFood Allergies? .......................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Food Allergy Reaction
        curr.execute("SELECT Food_Reaction FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFood Allergy Reaction ................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nFood Allergy Reaction ................................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Environmental Allergies
        curr.execute("SELECT Env_Allergy FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nEnvironmental Allergies? ............................................................................................................ Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nEnvironmental Allergies? ............................................................................................................ No")
        else:
            label = Label(DemographicSectionframe, text = "\nEnvironmental Allergies? ............................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Environmental Allergy Reaction
        curr.execute("SELECT Env_Reaction FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nEnvironmental Allergy Reaction .................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nEnvironmental Allergy Reaction .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Epi Pen
        curr.execute("SELECT EpiPen FROM Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nEpiPen for any of the above allergies? ........................................................................................ Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nEpiPen for any of the above allergies? ........................................................................................ No")
        else:
            label = Label(DemographicSectionframe, text = "\nEpiPen for any of the above allergies? ........................................................................................ Unanswered")
        label.pack(anchor = 'w')

#Dietary Needs Section
        #header
        labelDietarySection = Label(DemographicSectionframe, text = "\n\nDIETARY INFORMATION")
        labelDietarySection.pack(fill = "x")
        labelDietarySection.config(font=("Helvetica", 20))

        #Special Dietary Needs
        curr.execute("SELECT Special_Dietary_Needs FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nSpecial Dietary Needs ................................................................................................................ Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nSpecial Dietary Needs ................................................................................................................ No")
        else:
            label = Label(DemographicSectionframe, text = "\nSpecial Dietary Needs ................................................................................................................ Unanswered")
        label.pack(anchor = 'w')
        
        #Vegetarian
        curr.execute("SELECT Vegetarian FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nVegetarian ................................................................................................................................. Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nVegetarian ................................................................................................................................. No")
        else:
            label = Label(DemographicSectionframe, text = "\nVegetarian ................................................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Food Restrictions
        curr.execute("SELECT Food_Restrictions FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFood Restrictions ....................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nFood Restrictions ....................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #G Tube
        curr.execute("SELECT G_Tube FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nG-Tube ...................................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nG-Tube ...................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Formula Supplements
        curr.execute("SELECT Formula_Supplement FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nFormula Supplements ................................................................................................................ Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nFormula Supplements ................................................................................................................ No")
        else:
            label = Label(DemographicSectionframe, text = "\nFormula Supplements ................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Formula Supplements How
        curr.execute("SELECT Formula_Supplement_How FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFormula Supplements How? ....................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nFormula Supplements How? ....................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Formula Type
        curr.execute("SELECT Formula_Type FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFormula Type ............................................................................................................................. " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nFormula Type ............................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #cans per day
        curr.execute("SELECT Formula_Cans_Per_Day FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFormula Cans Per Day ................................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nFormula Cans Per Day ................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Feeding Pump
        curr.execute("SELECT Feeding_Pump FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nFeeding Pump ............................................................................................................................ Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nFeeding Pump ............................................................................................................................ No")
        else:
            label = Label(DemographicSectionframe, text = "\nFeeding Pump ............................................................................................................................ Unanswered")
        label.pack(anchor = 'w')


        #Feeding Pump Type
        curr.execute("SELECT Pump_Type FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nPump Type ................................................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nPump Type ................................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Feeding schedule
        curr.execute("SELECT Feeding_Schedule FROM Dietary_Needs WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFeeding Schedule ...................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nFeeding Schedule ...................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

#General health
        #header
        labelFoodNeedsSection = Label(DemographicSectionframe, text = "\n\nGENERAL HEALTH INFORMATION")
        labelFoodNeedsSection.pack(fill = "x")
        labelFoodNeedsSection.config(font=("Helvetica", 20))

        #Physical Limitations + Other
        curr.execute("SELECT Physical_Limitations FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        physLimit = curr.fetchall()[0][0]
        curr.execute("SELECT Other FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        other = curr.fetchall()[0][0]
        if physLimit is not None and other is not None:
            label = Label(DemographicSectionframe, text = "\nPhysical Limitations ................................................................................................................... " + physLimit + ": " + other)
        elif physLimit is not None:
            label = Label(DemographicSectionframe, text = "\nPhysical Limitations ................................................................................................................... " + physLimit)
        else:
            label = Label(DemographicSectionframe, text = "\nPhysical Limitations ................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Tire Easily
        curr.execute("SELECT Tire_Easily FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nTire Easily .................................................................................................................................. Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nTire Easily .................................................................................................................................. No")
        else:
            label = Label(DemographicSectionframe, text = "\nTire Easily .................................................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Swim
        curr.execute("SELECT Swim FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nCan Swim ................................................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nCan Swim ................................................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nCan Swim ................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Chicken Pox
        curr.execute("SELECT Chicken_Pox FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nChicken Pox Vaccinated? ............................................................................................................ Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nChicken Pox Vaccinated? ............................................................................................................ No")
        else:
            label = Label(DemographicSectionframe, text = "\nChicken Pox Vaccinated? ............................................................................................................ Unanswered")
        label.pack(anchor = 'w')


        #c pox date
        curr.execute("SELECT Chicken_Pox_Date FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nChicken Pox Date (YYYY-MM-DD) ............................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nChicken Pox Date (YYYY-MM-DD) ............................................................................................... Unanswered")
        label.pack(anchor = 'w')
        
        #Menstrual Cycle
        curr.execute("SELECT Menstrual_Cycle FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nMenstrual Cycle ......................................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nMenstrual Cycle ......................................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nMenstrual Cycle ......................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #m cycle difficulties
        curr.execute("SELECT Menstrual_Difficulties FROM General_Health WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nMenstrual Difficulties ................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nMenstrual Difficulties ................................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
#Behavior
        #header
        labelBehaviorSection = Label(DemographicSectionframe, text = "\n\nBEHAVIORAL INFORMATION")
        labelBehaviorSection.pack(fill = "x")
        labelBehaviorSection.config(font=("Helvetica", 20))

        #Camper knows
        curr.execute("SELECT Camper_Knows FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nCamper knows that someone in his/her family has HIV/AIDS ...................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nCamper knows that someone in his/her family has HIV/AIDS ...................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nCamper knows that someone in his/her family has HIV/AIDS ...................................................... Unanswered")
        label.pack(anchor = 'w')

        #How long Camper known
        curr.execute("SELECT Time_Camper_Known FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nHow Long has Camper Been Aware of HIV/AIDS Impacting Them? .............................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nHow Long has Camper Been Aware of HIV/AIDS Impacting Them? .............................................. Unanswered")
        label.pack(anchor = 'w')
        
        #Camper experiences
        curr.execute("SELECT Camper_Experiences FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nExperiences of Camper .............................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nExperiences of Camper .............................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
        #medication for hyperactivity
        curr.execute("SELECT Med_Hyper_AttentionProb FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nCamper Takes Medicine for Hyperactivity ................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nCamper Takes Medicine for Hyperactivity ................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nCamper Takes Medicine for Hyperactivity ................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #experience explanation
        curr.execute("SELECT Explanation FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nExplanation of Experiences ........................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nExplanation of Experiences ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Camper interests
        curr.execute("SELECT Camper_Interests FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nInterests of Camper ................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nInterests of Camper ................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Recent major events
        curr.execute("SELECT Recent_Major_Events FROM Pyschosocial_and_Behavioral_info WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nRecent Events for Camper .......................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nRecent Events for Camper .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
    
#Medication Info
        #header
        labelFoodNeedsSection = Label(DemographicSectionframe, text = "\n\nMEDICATION INFORMATION")
        labelFoodNeedsSection.pack(fill = "x")
        labelFoodNeedsSection.config(font=("Helvetica", 20))

        #medications
        curr.execute("SELECT Medication FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        medArr = curr.fetchall()
        if medArr is not ():
            for med in medArr:

                #taken
                label = Label(DemographicSectionframe, text = "\nMedication Taken ....................................................................................................................... " + med[0])
                label.pack(anchor = 'w')

                #amount
                curr.execute("SELECT Amount FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, med[0],))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "\nMedication Amount .................................................................................................................... " + val)
                else:
                    label = Label(DemographicSectionframe, text = "\nMedication Amount .................................................................................................................... Unanswered")
                label.pack(anchor = 'w')
                            
                #frequency
                curr.execute("SELECT Time_Instruction FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, med[0],))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "\nMedication Frequency ................................................................................................................ " + val + "\n")
                else:
                    label = Label(DemographicSectionframe, text = "\nMedication Frequency .................................................................................................. Unanswered\n")
                label.pack(anchor = 'w')
        else:
            label = Label(DemographicSectionframe, text = "\nMedication Taken ....................................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nMedication Amount .................................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nMedication Frequency .................................................................................................. Unanswered")
            label.pack(anchor = 'w')

#Preliminary signatures
        #header
        labelSignatureSection = Label(DemographicSectionframe, text = "\n\nPARENTAL CONSENT INFORMATION")
        labelSignatureSection.pack(fill = "x")
        labelSignatureSection.config(font=("Helvetica", 20))

        #parent camper contract
        curr.execute("SELECT Parent_Camper_Contract FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nParent Camper Contract ............................................................................................................. Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nParent Camper Contract ............................................................................................................. No")
        else:
            label = Label(DemographicSectionframe, text = "\nParent Camper Contract ............................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #participation release
        curr.execute("SELECT Partcipation_Consent_Liability_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nParticipation Consent/Liability Release/Disputes Form Signed .................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nParticipation Consent/Liability Release/Disputes Form Signed .................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nParticipation Consent/Liability Release/Disputes Form Signed .................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #Media release
        curr.execute("SELECT Media_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nMedia Release Form Signed ........................................................................................................ Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nMedia Release Form Signed ........................................................................................................ No")
        else:
            label = Label(DemographicSectionframe, text = "\nMedia Release Form Signed ........................................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
        #hiv ed waiver
        curr.execute("SELECT Camper_HIV_Education FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nHIV Education Waiver Signed ...................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nHIV Education Waiver Signed ...................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nHIV Education Waiver Signed ...................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #camp rules form signed
        curr.execute("SELECT Camp_Twin_Lakes_Rules FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nRules Acknowledgement Form Signed ......................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nRules Acknowledgement Form Signed ......................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nRules Acknowledgement Form Signed ......................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #parental consent and release
        curr.execute("SELECT Parental_Consent_And_Release FROM Release_Forms_Signed WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nParental Consent and Release Form Signed ................................................................................. Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nParental Consent and Release Form Signed ................................................................................. No")
        else:
            label = Label(DemographicSectionframe, text = "\nParental Consent and Release Form Signed ................................................................................. Unanswered")
        label.pack(anchor = 'w')

#                  
#Medical provider sections
#

#medical history
        #header
        labelMedicalProviderSection = Label(DemographicSectionframe, text = "\n\nMEDICAL HISTORY")
        labelMedicalProviderSection.pack(fill = "x")
        labelMedicalProviderSection.config(font=("Helvetica", 20))

        #medical diagnosises
        curr.execute("SELECT Diagnosis FROM Med_Hist_Diagnosis WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        diagnosisArr = curr.fetchall()
        if diagnosisArr is not ():
            diganosisCount = 0
            for diagnosis in diagnosisArr:
                diganosisCount = 1 + diganosisCount
                label = Label(DemographicSectionframe, text = "\nMedical Diagnosis " + str(diganosisCount) + " ................................................................................................................... " + diagnosis[0])
                label.pack(anchor = 'w')        
        else:    
            label = Label(DemographicSectionframe, text = "\nMedical Diagnosis ...................................................................................................................... Unanswered")
            label.pack(anchor = 'w')

        #management
        curr.execute("SELECT Management FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nMedical Management Comments ................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nMedical Management Comments ................................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
        #nutritional supplements
        curr.execute("SELECT Nutritional_Supplements FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nNutritional Supplements Taken? ................................................................................................. Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nNutritional Supplements Taken? ................................................................................................. No")
        else:
            label = Label(DemographicSectionframe, text = "\nNutritional Supplements Taken? ................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
        #supplement comment
        curr.execute("SELECT Feeding_Care FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFeeding Care Comments ............................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nFeeding Care Comments ............................................................................................................ Unanswered or Not Applicable")
        label.pack(anchor = 'w')
                    
        #formula type
        curr.execute("SELECT Formula_Type FROM Medical_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nFormula Type ............................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nFormula Type ............................................................................................................................. Unanswered or Not Applicable")
        label.pack(anchor = 'w')

        #allergies
        curr.execute("SELECT Allergy FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        allergyArr = curr.fetchall()
        if allergyArr is not ():
            for allergy in allergyArr:

                #type
                curr.execute("SELECT Type FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s;", (id, date, allergy[0],))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "\n\nAllergy Type ............................................................................................................................... " + val)
                else:
                    label = Label(DemographicSectionframe, text = "\n\nAllergy Type ............................................................................................................................... Unanswered or Not Applicable")
                label.pack(anchor = 'w')

                #allergy
                label = Label(DemographicSectionframe, text = "\nAllergic to .................................................................................................................................. " + allergy[0])
                label.pack(anchor = 'w')

                #reaction
                curr.execute("SELECT Reaction FROM Med_Hist_Allergies WHERE ID = %s AND Date_Submitted = %s AND Allergy = %s;", (id, date, allergy[0],))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "\nReaction .................................................................................................................................... " + val)
                else:
                    label = Label(DemographicSectionframe, text = "\nReaction .................................................................................................................................... Unanswered or Not Applicable")
                label.pack(anchor = 'w')
        else:
            label = Label(DemographicSectionframe, text = "\nAllergy Type ............................................................................................................................... Unanswered or Not Applicable")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nAllergic to .................................................................................................................................. Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nReaction .................................................................................................................................... Unanswered or Not Applicable")
            label.pack(anchor = 'w')

#physical
        #header
        labelPhysicalSection = Label(DemographicSectionframe, text = "\n\nMOST RECENT PHYSICAL INFORMATION")
        labelPhysicalSection.pack(fill = "x")
        labelPhysicalSection.config(font=("Helvetica", 20))

        #date completed
        curr.execute("SELECT Date_Completed FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nDate Completed (YYY-MM-DD) ................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nDate Completed (YYY-MM-DD) ................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #height
        curr.execute("SELECT Height FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nHeight ........................................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nHeight ........................................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #weight
        curr.execute("SELECT Weight FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nWeight (lb) ................................................................................................................................. " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nWeight (lb) ................................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #pulse
        curr.execute("SELECT Pulse FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nPulse (bpm) ................................................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nPulse (bpm) ................................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #respirations
        curr.execute("SELECT Resperations FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nRespirations ............................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nRespirations ............................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #bp
        curr.execute("SELECT Blood_Pressure FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nBlood Pressure ........................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nBlood Pressure ........................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #HEENT
        curr.execute("SELECT HEENT FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nHEENT ........................................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nHEENT ........................................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #skin
        curr.execute("SELECT Skin FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nSkin ............................................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nSkin ............................................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #cardio
        curr.execute("SELECT Cardiovascular FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nCardiovascular ........................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nCardiovascular ........................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #gu gyn
        curr.execute("SELECT GU_GYN FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nGU/GYN ...................................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nGU/GYN ...................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #pulmonary
        curr.execute("SELECT Pulmonary FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nPulmonary .................................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nPulmonary .................................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #g ha
        curr.execute("SELECT Glasses_HearingAids_PE FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nGlasses/Contacts/Hearing Aids/PE tubes .................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nGlasses/Contacts/Hearing Aids/PE tubes .................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Abdomen
        curr.execute("SELECT Abdomen FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nAbdomen ................................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nAbdomen ................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #LN
        curr.execute("SELECT Lymph_Nodes FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nLymph Nodes ............................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nLymph Nodes ............................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Extremities
        curr.execute("SELECT Extremities FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nExtremities ................................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nExtremities ................................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #spine
        curr.execute("SELECT Spine FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nSpine ......................................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nSpine ......................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Misc
        curr.execute("SELECT Miscellaneous FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nMiscellaneous ............................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nMiscellaneous ............................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #comm
        curr.execute("SELECT Comments FROM Physical_Exam WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nComments .................................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nComments .................................................................................................................................. Unanswered")
        label.pack(anchor = 'w')
                    
#cognative development level
        #header
        labelCogDevSection = Label(DemographicSectionframe, text = "\n\nCOGNITIVE DEVELOPMENT INFORMATION")
        labelCogDevSection.pack(fill = "x")
        labelCogDevSection.config(font=("Helvetica", 20))

        #development level
        curr.execute("SELECT Development_Level FROM Cognitive_Development_Level WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nDevelopment Level ..................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nDevelopment Level ..................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #other info
        curr.execute("SELECT Other_Psychosocial_Information FROM Cognitive_Development_Level WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nOther Psychosocoal Information ................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nOther Psychosocoal Information ................................................................................................. Unanswered")
        label.pack(anchor = 'w')

#Varicella screening
        #header
        labelTuberculosisSection = Label(DemographicSectionframe, text = "\n\nVARICELLA SCREENING")
        labelTuberculosisSection.pack(fill = "x")
        labelTuberculosisSection.config(font=("Helvetica", 20))

        #Two_Doses
        curr.execute("SELECT Two_Doses FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nTwo doses of vaccine ................................................................................................................. Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nTwo doses of vaccine ................................................................................................................. No")
        else:
            label = Label(DemographicSectionframe, text = "\nTwo doses of vaccine ................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #Chicken_Pox
        curr.execute("SELECT Chicken_Pox FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nHistory of chicken pox or shingles? ............................................................................................ Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nHistory of chicken pox or shingles? ............................................................................................ No")
        else:
            label = Label(DemographicSectionframe, text = "\nHistory of chicken pox or shingles? ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Chicken_Pox_Date
        curr.execute("SELECT Chicken_Pox_Date FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nChicken pox/ shingles date (YYYY-MM-DD) ................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nChicken pox/ shingles date (YYYY-MM-DD) ................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Varicella_Antibody
        curr.execute("SELECT Varicella_Antibody FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nVaricella antibody ....................................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nVaricella antibody ....................................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nVaricella antibody ....................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #Varicella_Antibody_Date
        curr.execute("SELECT Varicella_Antibody_Date FROM Varicella_Screening WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nVaricella antibody date (YYYY-MM-DD) ...................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nVaricella antibody date (YYYY-MM-DD) ...................................................................................... Unanswered")
        label.pack(anchor = 'w')

#tuberculosis screening
        #header
        labelTuberculosisSection = Label(DemographicSectionframe, text = "\n\nTUBERCULOSIS SCREENING")
        labelTuberculosisSection.pack(fill = "x")
        labelTuberculosisSection.config(font=("Helvetica", 20))

        #Tuberculin Skin Test
        label = Label(DemographicSectionframe, text = "\nTuberculin Skin Test")
        label.pack(anchor = 'w')

        #date
        curr.execute("SELECT Date_Screened FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Tuberculin Skin Test';", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Result
        curr.execute("SELECT Result FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Tuberculin Skin Test';", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... Unanswered")
        label.pack(anchor = 'w')
 
        #Quantiferon Testing
        label = Label(DemographicSectionframe, text = "\nQuantiferon Testing")
        label.pack(anchor = 'w')

        #date
        curr.execute("SELECT Date_Screened FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Quantiferon Testing';", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Result
        curr.execute("SELECT Result FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Quantiferon Testing';", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... Unanswered")
        label.pack(anchor = 'w')
 
        #Chest X-ray
        label = Label(DemographicSectionframe, text = "\nChest X-ray")
        label.pack(anchor = 'w')

        #date
        curr.execute("SELECT Date_Screened FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Chest X-ray';", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "Test Date (YYY-MM-DD) ............................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #Result
        curr.execute("SELECT Result FROM Tuberculosis_Screening WHERE ID = %s AND Date_Submitted = %s AND Type = 'Chest X-ray';", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "Test Results ............................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

#Restrictions_And_Recommendations
        #header
        labelTuberculosisSection = Label(DemographicSectionframe, text = "\n\nRESTRICTIONS AND RECOMMENDATIONS")
        labelTuberculosisSection.pack(fill = "x")
        labelTuberculosisSection.config(font=("Helvetica", 20))

        #Restrictions and recommendations
        curr.execute("SELECT Restrictions_And_Recommendations FROM Medical_Care_Provider WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nRestrictions and recommendations ............................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nRestrictions and recommendations ............................................................................................ Unanswered")
        label.pack(anchor = 'w')

#medcare provider medications
        #header
        labelMedicineProviderSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER MEDICATION INFORMATION")
        labelMedicineProviderSection.pack(fill = "x")
        labelMedicineProviderSection.config(font=("Helvetica", 20))

        #medications
        curr.execute("SELECT Medication_Name FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        nameArr = curr.fetchall()
        if nameArr is not ():
            count = len(nameArr)
            for medName in nameArr:
                count -= 1

                #medication
                label = Label(DemographicSectionframe, text = "\nMedication Name ....................................................................................................................... " + medName[0])
                label.pack(anchor = 'w')

                #amount
                curr.execute("SELECT Amount_Including_Dosage FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, medName,))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "\nAmount and Dosage ................................................................................................................... " + val)
                else:
                    label = Label(DemographicSectionframe, text = "\nAmount and Dosage ................................................................................................................... Unanswered")
                label.pack(anchor = 'w')

                #times to give
                curr.execute("SELECT Times_To_Give FROM MedCareProvider_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication_Name = %s;", (id, date, medName,))
                val = curr.fetchall()[0][0]
                if val is not None:
                    label = Label(DemographicSectionframe, text = "\nTimes to Take Medicine .............................................................................................................. " + val)
                else:
                    label = Label(DemographicSectionframe, text = "\nTimes to Take Medicine .................................................................................................. Unanswered")
                label.pack(anchor = 'w')
                
                #spacing
                if count != 0:
                    label = Label(DemographicSectionframe).pack(anchor = 'w')
        else:
            label = Label(DemographicSectionframe, text = "\nMedication Name ....................................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nAmount and Dosage ................................................................................................................... Unanswered")
            label.pack(anchor = 'w')
            label = Label(DemographicSectionframe, text = "\nTimes to Take Medicine .................................................................................................. Unanswered")
            label.pack(anchor = 'w')

#medcare provider verification statement
        #header
        labelMedicalStatementSection = Label(DemographicSectionframe, text = "\n\nMEDICAL PROVIDER VERIFICATION STATEMENT")
        labelMedicalStatementSection.pack(fill = "x")
        labelMedicalStatementSection.config(font=("Helvetica", 20))

        #signature
        curr.execute("SELECT Signature FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nSignature Provided? ................................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nSignature Provided? ................................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nSignature Provided? ................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #signature date
        curr.execute("SELECT Sig_Date FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nDate (YYYY-MM-DD) .................................................................................................................. " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nDate (YYYY-MM-DD) .................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #name
        curr.execute("SELECT Name FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nExaminer Name .......................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nExaminer Name .......................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #address street
        curr.execute("SELECT Address_Street FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nAddress Street ........................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nAddress Street ........................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #address city
        curr.execute("SELECT Address_City FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nAddress City .............................................................................................................................. " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nAddress City .............................................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #address state
        curr.execute("SELECT Address_State FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nAddress State ............................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nAddress State ............................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #address zip
        curr.execute("SELECT Address_Zip FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nAddress Zipcode ........................................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nAddress Zipcode ........................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #phone
        curr.execute("SELECT Phone FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nPhone ........................................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nPhone ........................................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #emergency contact
        curr.execute("SELECT Emergency_Contact FROM Medical_Provider_Verification_Statement WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nEmergency Contact .................................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nEmergency Contact .................................................................................................. Unanswered")
        label.pack(anchor = 'w')

#
#hiv provider sections
#

#health history
        #header
        labelHealthHistorySection = Label(DemographicSectionframe, text = "\n\nHEALTH HISTORY INFORMATION FROM HIV PROVIDER")
        labelHealthHistorySection.pack(fill = "x")
        labelHealthHistorySection.config(font=("Helvetica", 20))
        
        #surgical history
        curr.execute("SELECT Major_Surgical_History FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nMajor Surgical History ................................................................................................................ " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nMajor Surgical History ................................................................................................................ Unanswered")
        label.pack(anchor = 'w')
                    
        #health history
        curr.execute("SELECT Health_History FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        History = curr.fetchall()[0][0]
        curr.execute("SELECT Other FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        other = curr.fetchall()[0][0]
        if History is not None and other is not None:
            label = Label(DemographicSectionframe, text = "\nHealth History ............................................................................................................................ " + History + ": " + other)
        elif History is not None:
            label = Label(DemographicSectionframe, text = "\nHealth History ............................................................................................................................ " + History)
        else:
            label = Label(DemographicSectionframe, text = "\nHealth History ............................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #history of noncompliance
        curr.execute("SELECT History_of_Noncompliance FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            if val:
                label = Label(DemographicSectionframe, text = "\nHistory of Noncompliance? ......................................................................................................... Yes")
            else:
                label = Label(DemographicSectionframe, text = "\nHistory of Noncompliance? ......................................................................................................... No")
        else:
            label = Label(DemographicSectionframe, text = "\nHistory of Noncompliance? ......................................................................................................... Unanswered")
        label.pack(anchor = 'w')
                    
        #explanation
        curr.execute("SELECT Explanation FROM Health_History WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nExplanation of Noncompliance .................................................................................................... " + val)
        else:
            label = Label(DemographicSectionframe, text = "\nExplanation of Noncompliance .................................................................................................. Unanswered")
        label.pack(anchor = 'w')
        
#lab data
        #header
        labelHealthHistorySection = Label(DemographicSectionframe, text = "\n\nLAB DATA")
        labelHealthHistorySection.pack(fill = "x")
        labelHealthHistorySection.config(font=("Helvetica", 20))
        
        #lab1 date
        curr.execute("SELECT Lab1_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nDate of First Lab Examination (YYYY-MM-DD) ............................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nDate of First Lab Examination (YYYY-MM-DD) ............................................................................ Unanswered")
        label.pack(anchor = 'w')

        #lab1 wbc
        curr.execute("SELECT Lab1_WBC FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "White Blood Cell Count .............................................................................................................. " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "White Blood Cell Count .............................................................................................................. Unanswered")
        label.pack(anchor = 'w')

        #lab1 hgb
        curr.execute("SELECT Lab1_HGB FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Hemoglobin Level ....................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "Hemoglobin Level ....................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #lab1 hct
        curr.execute("SELECT Lab1_HCT FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Hematocrit Level ........................................................................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "Hematocrit Level ........................................................................................................................ Unanswered")
        label.pack(anchor = 'w')

        #lab1 plt
        curr.execute("SELECT Lab1_Plt_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Plt Count .................................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "Plt Count .................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #spacing
        label = Label(DemographicSectionframe).pack(anchor = 'w')

        #lab2 date
        curr.execute("SELECT Lab2_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nDate of Second Lab Examination (YYYY-MM-DD) ........................................................................ " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nDate of Second Lab Examination (YYYY-MM-DD) ........................................................................ Unanswered")
        label.pack(anchor = 'w')

        #lab2 cd4
        curr.execute("SELECT Lab2_CD4_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "CD4 (T-Cell) Count ..................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "CD4 (T-Cell) Count ..................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #lab2 viral load
        curr.execute("SELECT Lab2_Viral_Load FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Viral Load ................................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "Viral Load ................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #spacing
        label = Label(DemographicSectionframe).pack(anchor = 'w')

        #lab3 date
        curr.execute("SELECT Lab3_Date FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "\nDate of Third Lab Examination (YYYY-MM-DD) ........................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "\nDate of Third Lab Examination (YYYY-MM-DD) ........................................................................... Unanswered")
        label.pack(anchor = 'w')

        #lab3 cd4
        curr.execute("SELECT Lab3_CD4_Count FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "CD4 (T-Cell) Count ..................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "CD4 (T-Cell) Count ..................................................................................................................... Unanswered")
        label.pack(anchor = 'w')

        #lab3 viral load
        curr.execute("SELECT Lab3_Viral_Load FROM Lab_Data WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        val = curr.fetchall()[0][0]
        if val is not None:
            label = Label(DemographicSectionframe, text = "Viral Load ................................................................................................................................... " + str(val))
        else:
            label = Label(DemographicSectionframe, text = "Viral Load ................................................................................................................................... Unanswered")
        label.pack(anchor = 'w')



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