    

    def updateLab0(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Lab_Data SET Lab1_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab1(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_WBC = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 6):
            curr.execute("UPDATE Lab_Data SET Lab1_WBC = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 6 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab2(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_HGB = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 4):
            curr.execute("UPDATE Lab_Data SET Lab1_HGB = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 4 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab3(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_HCT = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 3):
            curr.execute("UPDATE Lab_Data SET Lab1_HCT = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 3 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab4(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab1_Plt_Count = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 6):
            curr.execute("UPDATE Lab_Data SET Lab1_Plt_Count = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 6 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab5(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab2_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Lab_Data SET Lab2_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab6(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab2_CD4_Count = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 4):
            curr.execute("UPDATE Lab_Data SET Lab2_CD4_Count = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 4 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab7(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab2_Viral_Load = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 5):
            curr.execute("UPDATE Lab_Data SET Lab2_Viral_Load = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 5 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab8(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab3_Date = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (self.is_date(newVal)):
            curr.execute("UPDATE Lab_Data SET Lab3_Date = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Sucessful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nDate must be if YYYY-MM-DD format\nAnd must be a real date.")
            
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab9(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab3_CD4_Count = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 4):
            curr.execute("UPDATE Lab_Data SET Lab3_CD4_Count = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 4 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

    def updateLab10(self, newWidget, id, date):
        #Database Connection
        db = self.connect()
        curr = db.cursor()

        #Execute
        newVal = newWidget.get()
        if (newVal == 'Unanswered') or (newVal == ''):
            curr.execute("UPDATE Lab_Data SET Lab3_Viral_Load = NULL WHERE ID = %s AND Date_Submitted = %s;", (id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        elif (len(newVal) <= 5):
            curr.execute("UPDATE Lab_Data SET Lab3_Viral_Load = %s WHERE ID = %s AND Date_Submitted = %s;", (newVal, id, date,))
            tkMessageBox.showinfo("Edit Profile", "Update Successful!")
        else:
            tkMessageBox.showinfo("Edit Profile", "Update Unsucessful\n\nMaximum length is 5 characters.")        
                
        #Close Database Connection
        db.commit()
        curr.close()
        db.close()

