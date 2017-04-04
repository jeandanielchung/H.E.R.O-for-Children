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
        #header
        self.ChildInfoSectionHeaderframe = Frame(self.frame)
        self.ChildInfoSectionHeaderframe.pack()      
        labelChildInfoSection = Label(self.ChildInfoSectionHeaderframe, text = "\nCHILD'S INFORMATION")
        labelChildInfoSection.pack(fill = "x")
        labelChildInfoSection.config(font=("Helvetica", 20))

        self.ChildInfoSectionframe = Frame(self.frame)
        self.ChildInfoSectionframe.pack(fill = 'y', side = 'left') 

        #first name
        label = Label(self.ChildInfoSectionframe, text = "\nFirst Name ............................................................................................ ")
        global childInfo0
        childInfo0 = Entry(self.ChildInfoSectionframe)

        childInfo0.grid(row = 0, column = 1)
        label.grid(row = 0, column = 0)

        #last name
        label = Label(self.ChildInfoSectionframe, text = "\nLast Name ............................................................................................. ")
        global childInfo1
        childInfo1 = Entry(self.ChildInfoSectionframe)

        childInfo1.grid(row = 1, column = 1)
        label.grid(row = 1, column = 0)

        #nickname
        label = Label(self.ChildInfoSectionframe, text = "\nNickname .............................................................................................. ")
        global childInfo2
        childInfo2 = Entry(self.ChildInfoSectionframe)

        childInfo2.grid(row = 2, column = 1)
        label.grid(row = 2, column = 0)

        #address street
        label = Label(self.ChildInfoSectionframe, text = "\nHome Address ....................................................................................... ")
        global childInfo3
        childInfo3 = Entry(self.ChildInfoSectionframe)

        childInfo3.grid(row = 3, column = 1)
        label.grid(row = 3, column = 0)

        #address city
        label = Label(self.ChildInfoSectionframe, text = "\nCity ....................................................................................................... ")
        global childInfo4
        childInfo4 = Entry(self.ChildInfoSectionframe)

        childInfo4.grid(row = 4, column = 1)
        label.grid(row = 4, column = 0)

        #address county
        label = Label(self.ChildInfoSectionframe, text = "\nCounty .................................................................................................. ")
        global childInfo5
        childInfo5 = Entry(self.ChildInfoSectionframe)

        childInfo5.grid(row = 5, column = 1)
        label.grid(row = 5, column = 0)

        #address zip
        label = Label(self.ChildInfoSectionframe, text = "\nZip ........................................................................................................ ")
        global childInfo6
        childInfo6 = Entry(self.ChildInfoSectionframe)

        childInfo6.grid(row = 6, column = 1)
        label.grid(row = 6, column = 0)

        #home phone
        label = Label(self.ChildInfoSectionframe, text = "\nHome Phone .......................................................................................... ")
        global childInfo7
        childInfo7 = Entry(self.ChildInfoSectionframe)

        childInfo7.grid(row = 7, column = 1)
        label.grid(row = 7, column = 0)

        #guardian phone
        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's Cell Phone ................................................................ ")
        global childInfo8
        childInfo8 = Entry(self.ChildInfoSectionframe)

        childInfo8.grid(row = 8, column = 1)
        label.grid(row = 8, column = 0)

        #guardian email
        label = Label(self.ChildInfoSectionframe, text = "\nParent/Guardian's e-mail address .......................................................... ")
        global childInfo9
        childInfo9 = Entry(self.ChildInfoSectionframe)

        childInfo9.grid(row = 9, column = 1)
        label.grid(row = 9, column = 0)

        #age
        label = Label(self.ChildInfoSectionframe, text = "\nAge ....................................................................................................... ")
        global childInfo10
        childInfo10 = Entry(self.ChildInfoSectionframe)

        childInfo10.grid(row = 10, column = 1)
        label.grid(row = 10, column = 0)

        #birthday
        label = Label(self.ChildInfoSectionframe, text = "\nDate of Birth (Y/M/D) ............................................................................. ")
        global childInfo11
        childInfo11 = Entry(self.ChildInfoSectionframe)

        childInfo11.grid(row = 11, column = 1)
        label.grid(row = 11, column = 0)

        #gender
        label = Label(self.ChildInfoSectionframe, text = "\nGender .................................................................................................. ")
        global childInfo12
        childInfo12 = Entry(self.ChildInfoSectionframe)

        childInfo12.grid(row = 12, column = 1)
        label.grid(row = 12, column = 0)

        #HIV status
        label = Label(self.ChildInfoSectionframe, text = "\nHIV status ............................................................................................. ")
        global childInfo13
        childInfo13 = Entry(self.ChildInfoSectionframe)

        childInfo13.grid(row = 13, column = 1)
        label.grid(row = 13, column = 0)

        #aware
        label = Label(self.ChildInfoSectionframe, text = '\nIs the child aware that he/she is HIV positive or')
        label.grid(row = 14, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = 'that a member of the household is HIV positive? ................................... ')
        global childInfo14
        childInfo14 = Entry(self.ChildInfoSectionframe)

        childInfo14.grid(row = 15, column = 1)
        label.grid(row = 15, column = 0)

        #why
        label = Label(self.ChildInfoSectionframe, text = "\nIf no,")
        label.grid(row = 16, column = 0, sticky = 'w')
        label = Label(self.ChildInfoSectionframe, text = "please provide a reason why child is not aware ...................................... ")
        global childInfo15
        childInfo15 = Entry(self.ChildInfoSectionframe)

        childInfo15.grid(row = 17, column = 1)
        label.grid(row = 17, column = 0)

        #refferal source
        label = Label(self.ChildInfoSectionframe, text = "\nReferral Source ..................................................................................... ")
        global childInfo16
        childInfo16 = Entry(self.ChildInfoSectionframe)

        childInfo16.grid(row = 18, column = 1)
        label.grid(row = 18, column = 0)

        #school attending
        label = Label(self.ChildInfoSectionframe, text = "\nSchool Attending .................................................................................. ")
        global childInfo17
        childInfo17 = Entry(self.ChildInfoSectionframe)

        childInfo17.grid(row = 19, column = 1)
        label.grid(row = 19, column = 0)

        #Grade Level
        label = Label(self.ChildInfoSectionframe, text = "\nGrade Level ........................................................................................... ")
        global childInfo18
        childInfo18 = Entry(self.ChildInfoSectionframe)

        childInfo18.grid(row = 20, column = 1)
        label.grid(row = 20, column = 0)

        #Ethnicity
        label = Label(self.ChildInfoSectionframe, text = "\nEthnicity ............................................................................................... ")
        global childInfo19
        childInfo19 = Entry(self.ChildInfoSectionframe)

        childInfo19.grid(row = 21, column = 1)
        label.grid(row = 21, column = 0)

        #Even been...
        label = Label(self.ChildInfoSectionframe, text = "\nHas your child ever been...")
        label.grid(row = 22, column = 0, sticky = 'w')

        #ADD_ADHD
        label = Label(self.ChildInfoSectionframe, text = 'Diagnosed with ADD/ADHD? ................................................................. ')
        global childInfo20
        childInfo20 = IntVar()

        Yes = Radiobutton(self.ChildInfoSectionframe, text = "Yes", variable = childInfo20, value=1)
        No = Radiobutton(self.ChildInfoSectionframe, text = "No", variable = childInfo20, value=2)

        Yes.grid(row = 23, column = 1, sticky = 'w')
        No.grid(row = 23, column = 1, sticky = 'e')
        label.grid(row = 23, column = 0)

        
#Submit Button
        submitProfileButton = Button(self.ChildInfoSectionframe, text = "Submit Profile", command = lambda:self.submitProfile())
        submitProfileButton.grid(sticky = 'w, e', row = 40, columnspan = 2)

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

        #TODO
            #handle empty string inputs....
            #initial thought = check all of them for == '' right here. Then if true replace with NULL
                #inefficient but would work
            #or just let it be an empty string? idk yet

        #Execute
        try:
            curr.execute("""INSERT INTO ChildApp_Emergency_Contact VALUES
            (%s, %s, %s, 'Smith', 'Grandfather', '318 Goss Street', 'Farmerville', 'LA', '38234', 3188901234, 3185678901, 3182456789);""", (id, date, firstName.get(),))

        except (MySQLdb.IntegrityError) as e:
            tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nA Child application \nSubmitted on: " + date + "\nFor ID number: " + str(id) + " \nAlready exists in the system")
        db.commit()

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
