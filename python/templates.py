
    def genHealthLimit(self, genHealthLimit0, genHealthLimit1, genHealthLimit2, genHealthLimit3, genHealthLimit4,
            genHealthLimit5, genHealthLimit6, genHealthLimit7, genHealthLimit8, genHealthLimit9, genHealthLimit10, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = ''
        if genHealthLimit0.get():
            newVal = newVal + 'Dressing,'

        if genHealthLimit1.get():
            newVal = newVal + 'Showering,'

        if genHealthLimit9.get():
            newVal = newVal + 'Other,'

        if newVal == '':
            curr.execute("UPDATE General_Health SET Physical_Limitations = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        else:
            newVal = newVal[:-1]
            curr.execute("UPDATE General_Health SET Physical_Limitations = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))

        other = genHealthLimit10.get()
        if (other == 'Unanswered') or (other == ''):
            curr.execute("UPDATE General_Health SET Other = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(other) <= 50):
            curr.execute("UPDATE General_Health SET Other = %s WHERE ID = %s AND Date_Submitted = %s;", (other, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()


    def updateGenHealth2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != 0:
            if newVal == 2:
                newVal = 0
            curr.execute("UPDATE General_Health SET Swim = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE General_Health SET Chicken_Pox_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE General_Health SET Chicken_Pox_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateGenHealth6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE General_Health SET Menstrual_Difficulties = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 300):
            curr.execute("UPDATE General_Health SET Menstrual_Difficulties = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 300 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()
    
    def updateMed0(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Medication FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldName = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldName = arr[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                if askyesno('Verify', '\nDeleting the name of a medication will delete all of the information for that medication.\nAre you sure you want to delete?'):
                    curr.execute("DELETE FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, oldName,))
                    tkMessageBox.showinfo("Edit Profile", "Update Successful!")
                else:
                    tkMessageBox.showinfo("Edit Profile", "Update Canceled")
        elif (len(newVal) <= 50):
            if oldName is not None:
                curr.execute("UPDATE Parent_Medications SET Medication = %s WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (newVal, id, date, oldName,))
            else:
                curr.execute("INSERT INTO Parent_Medications (Medication, ID, Date_Submitted) VALUES (%s, %s, %s);", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateMed1(self, newWidget, count, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        curr.execute("SELECT Medication FROM Parent_Medications WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
        arr = curr.fetchall()
        if len(arr) > 0 and count is 1:
            oldName = arr[0][0]
        elif len(arr) > 1 and count is 2:
            oldName = arr[1][0]
        else:
            oldName = None;

        if (newVal == 'Unanswered') or (newVal == ''):
            if oldName is not None:
                curr.execute("UPDATE Parent_Medications SET Amount = NULL WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (id, date, oldName,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 50):
            if oldName is not None:
                curr.execute("UPDATE Parent_Medications SET Amount = %s WHERE ID = %s AND Date_Submitted = %s AND Medication = %s;", (newVal, id, date, oldName,))
                tkMessageBox.showinfo("Edit Profile", "Update Successful!")
            else:
                tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMedication must have a name.")        
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 50 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo5(self, newWidget, id, date):
        #Open Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if newVal != '':
            curr.execute("UPDATE Demographic_Information SET Gender = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
        tkMessageBox.showinfo("Edit Profile", "Update Successful!")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDietaryNeedsInfo7(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Dietary_Needs SET Formula_Cans_Per_Day = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_number(newVal)):
            curr.execute("UPDATE Dietary_Needs SET Formula_Cans_Per_Day = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMust be only numbers.")

        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateDemInfo10(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Demographic_Information SET Address_State = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) is 2):
            curr.execute("UPDATE Demographic_Information SET Address_State = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nLength must be 2 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()


