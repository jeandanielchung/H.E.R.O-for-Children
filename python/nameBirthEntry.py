from Tkinter import *
import MySQLdb


class nameBirthEntryPage:
        def __init__(self, master):
                self.master = master
                master.title("Name and Birthday Search Results Page")
                #5 columns at least 3 rows

                nameHead = Label(master, text = "Name", font= "Verdana 10 underline")
                nameHead.grid(row = 1, column = 0)

                progHead = Label(master, text = "Program", font= "Verdana 10 underline")
                progHead.grid(row = 1, column = 1)

                yearHead = Label(master, text = "Year", font= "Verdana 10 underline")
                yearHead.grid(row = 1, column = 2)

                self.back = Button(master, text = "Back", command = self.closeWindow)
                self.back.grid(row = 0, column = 0)

                ###
                ID = 2 ##get this ID from another page
                ###
                program = "Child Application" #get me too!
                ###
                
                db = MySQLdb.connect( host = "localhost",
                                      user="root",
                                      passwd="Darling",
                                      db="HERO" )
                curr = db.cursor()

                #selects all instances of specified ID in child and camper applications
                curr.execute("SELECT Name_First,Name_Last,Year(Date_Submitted) FROM Childs_Information WHERE ID = %s;",(ID,))
                childNameDate = curr.fetchall()
                curr.execute("SELECT First_Name,Last_Name,Year(Date_Submitted) FROM Demographic_Information WHERE ID = %s;",(ID,))
                camperNameDate = curr.fetchall()


 

                if program == 'none':
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
                        
                elif program == 'Child Application':
                        for num in range(len(childNameDate)):
                                if (childNameDate[num][0] is not None) and (childNameDate[num][1] is not None):
                                        name = Label(master, text = childNameDate[num][0]+' '+childNameDate[num][1])
                                        name.grid(row = 2 + num, column = 0)
                                elif childNameDate[num][0] is not None:
                                        name = Label(master, text = childNameDate[num][0])
                                        name.grid(row = 2 + num, column = 0)
                                elif childNameDate[num][1] is not None:
                                        name = Label(master, text = childNameDate[num][1])
                                        name.grid(row = 2 + num, column = 0)
                                
                                prog = Label(master, text = "Child Application")
                                prog.grid(row = 2 + num, column = 1)

                                year = Label(master, text = childNameDate[num][2])
                                year.grid(row = 2 + num, column = 2)

                                profBut = Button(master, text = "Profile", command = self.closeWindow)
                        total = len(childNameDate)
                        
                else:
                        for num in range(len(camperNameDate)):
                                if (camperNameDate[num][0] is not None) and (camperNameDate[num][1] is not None):
                                        name = Label(master, text = camperNameDate[num][0]+' '+camperNameDate[num][1])
                                        name.grid(row = 2 + num, column = 0)
                                elif camperNameDate[num][0] is not None:
                                        name = Label(master, text = camperNameDate[num][0])
                                        name.grid(row = 2 + num, column = 0)
                                elif camperNameDate[num][1] is not None:
                                        name = Label(master, text = camperNameDate[num][1])
                                        name.grid(row = 2 + num, column = 0)



                                prog = Label(master, text = "Camper Application")
                                prog.grid(row = 2 + num, column = 1)

                                year = Label(master, text = camperNameDate[num][2])
                                year.grid(row = 2 + num, column = 2)

                                profBut = Button(master, text = "Profile", command = self.closeWindow)
                                profBut.grid(row = 2 + num, column = 3)
                        total = len(camperNameDate)


                #print total number of matches
                count = Label(master, text = "Total Matches: " + str(total))
                count.grid(row = 0, column = 3)
                        
                        
                        
                        






                #possibly add a back button
        def closeWindow(self):
                self.master.destroy()

master = Tk()
my_gui = nameBirthEntryPage(master)
master.mainloop()
