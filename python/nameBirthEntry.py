from Tkinter import *
import MySQLdb


    def nameBirthEntryPage(self, childNameDate, camperNameDate, newProgram, entryDate):
        self.master = master
        master.title("Name and Birthday Search Results Page")
        #5 columns at least 3 rows

        nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
        nameHead.grid(row = 1, column = 0)

        progHead = Label(master, text = "Program", font= "Verdana 10 underline")
        progHead.grid(row = 1, column = 1)

        yearHead = Label(master, text = "Year", font= "Verdana 10 underline")
        yearHead.grid(row = 1, column = 2)

        backButton = Button(master, text = "Back")
        #TODO: , command = self.closeWindow)
        backButton.grid(row = 0, column = 0)


        for num in range(len(childNameDate)):
                name = Label(master, text = childNameDate[num][0]+' '+childNameDate[num][1])
                name.grid(row = 2 + num, column = 0)

                prog = Label(master, text = "Child Application")
                prog.grid(row = 2 + num, column = 1)

                year = Label(master, text = childNameDate[num][2])
                year.grid(row = 2 + num, column = 2)

                profBut = Button(master, text = "Profile", command = self.closeWindow)
                profBut.grid(row = 2 + num, column = 3)

        for num in range(len(camperNameDate)):
                name = Label(master, text = camperNameDate[num][0]+' '+camperNameDate[num][1])
                name.grid(row = 2 + num +len(childNameDate), column = 0)

                prog = Label(master, text = "Camper Application")
                prog.grid(row = 2 + num +len(childNameDate), column = 1)

                year = Label(master, text = camperNameDate[num][2])
                year.grid(row = 2 + num +len(childNameDate), column = 2)

                profBut = Button(master, text = "Profile", command = self.closeWindow)
                profBut.grid(row = 2 + num +len(childNameDate), column = 3)

        total = len(childNameDate)+len(camperNameDate)
                
 
        #print total number of matches
        count = Label(master, text = "Total Matches: " + str(total))
        count.grid(row = 0, column = 3)
                    
                    
                    

master = Tk()
my_gui = nameBirthEntryPage(master)
master.mainloop()
