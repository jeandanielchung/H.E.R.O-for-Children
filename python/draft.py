#ready to go

    	if goodData:

#Parent section
	        try:
		        curr.execute("""INSERT INTO Parent VALUES (
		    	%s, %s);""",
		        (id, date,))

	        except (MySQLdb.Error) as e:
	            success = 0

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

    #Demographic_Contacts
            try:
                curr.execute("""INSERT INTO Demographic_Contacts VALUES (%s, %s, %s, %s, %s);""",
                    (id, date, 
                        demContactInfo0, demContactInfo1, demContactInfoTime, demContactInfo2
                        ,))

            except (MySQLdb.Error) as e:
                success = 0

    #Parent_Emergency_Contact
            try:
                curr.execute("""INSERT INTO Parent_Emergency_Contact VALUES (%s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        emergencyInfo0, emergencyInfo1, emergencyInfo2, emergencyInfo3
                        ,))

            except (MySQLdb.Error) as e:
                success = 0

    #Insurance_Information
            try:
                curr.execute("""INSERT INTO Insurance_Information VALUES (%s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        insuranceInfo0, insuranceInfo1, insuranceInfo2, insuranceInfo3
                        ,))

            except (MySQLdb.Error) as e:
                success = 0

    #Medical_Provider_Information
            try:
                curr.execute("""INSERT INTO Medical_Provider_Information VALUES (%s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        medProviderInfo0, medProviderInfo1, medProviderInfo2, medProviderInfo3
                        ,))

            except (MySQLdb.Error) as e:
                success = 0

    #Medical_Information
    		try:
                curr.execute("""INSERT INTO Medical_Information VALUES (%s, %s, %s, %s, %s);""",
                    (id, date, 
                        medInfoCurr, medInfo0, medInfo1
                        ,))

            except (MySQLdb.Error) as e:
                success = 0

    #Allergies
            try:
                curr.execute("""INSERT INTO Allergies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                        allergyInfo0, allergyInfo1, allergyInfo2, allergyInfo3, allergyInfo4, allergyInfo5, allergyInfo6
                        ,))

            except (MySQLdb.Error) as e:
                success = 0

    #Dietary_Needs
            try:
                curr.execute("""INSERT INTO Dietary_Needs VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                    	dietaryNeedsInfo0, dietaryNeedsInfo1, dietaryNeedsInfo2, dietaryNeedsInfo3, dietaryNeedsInfo4,
                        dietaryNeedsHowInfo, dietaryNeedsInfo5, dietaryNeedsInfo6, dietaryNeedsInfo7, dietaryNeedsInfo8, dietaryNeedsInfo9
                        ,))

            except (MySQLdb.Error) as e:
                success = 0

    #General_Health
            try:
                curr.execute("""INSERT INTO General_Health VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                    	genHealthLimit, genHealth0, genHealth1, genHealth2, genHealth3, genHealth4, genHealth5, genHealth6
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

    #Pyschosocial_and_Behavioral
            try:
                curr.execute("""INSERT INTO Pyschosocial_and_Behavioral_info VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date, 
                    	behavior0, behavior1, behaviorExperiances, behavior2, behavior3, behaviorInterests, behavior4
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

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

    #Release_Forms_Signed
            try:
                curr.execute("""INSERT INTO Release_Forms_Signed VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                    	parentSig0, parentSig1, parentSig2, parentSig3, parentSig4, parentSig5
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

#Medical_Care_Provider section
            try:
                curr.execute("""INSERT INTO Medical_Care_Provider VALUES (%s, %s, %s);""",
                    (id, date,
                    	restrictionsRec
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

    #Medical_History
            try:
                curr.execute("""INSERT INTO Medical_History VALUES (%s, %s, %s, %s, %s, %s);""",
                    (id, date,
                    	medProvider5, medProvider6, medProvider7, medProvider8
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

    #Med_Hist_Diagnosis
            try:
            	i = 0
            	while i < len(medHistDiagnosis)
	                if medHistDiagnosis[i] is None:
	                	break
	                curr.execute("""INSERT INTO Med_Hist_Diagnosis VALUES (%s, %s, %s);""",
	                    (id, date,
	                    	medHistDiagnosis[i]
	                    	,))
	                i += 1

            except (MySQLdb.Error) as e:
                success = 0

    #Med_Hist_Allergies
            try:
                i = 0
                while i < len(foodAllergies)
                	if foodAllergies[i] is None:
                		break
	                curr.execute("""INSERT INTO Med_Hist_Allergies VALUES (%s, %s, %s, %s, %s);""",
	                    (id, date,
	                    	'Food', foodAllergies[i], foodAllergies[i + 1]
	                    	,))
	                i += 2

                i = 0
                while i < len(medAllergies)
                	if medAllergies[i] is None:
                		break
	                curr.execute("""INSERT INTO Med_Hist_Allergies VALUES (%s, %s, %s, %s, %s);""",
	                    (id, date,
	                    	'Medication', medAllergies[i], medAllergies[i + 1]
	                    	,))
	                i += 2

                i = 0
                while i < len(envAllergies)
                	if envAllergies[i] is None:
                		break
	                curr.execute("""INSERT INTO Med_Hist_Allergies VALUES (%s, %s, %s, %s, %s);""",
	                    (id, date,
	                    	'Environmental', envAllergies[i], envAllergies[i + 1]
	                    	,))
	                i += 2

            except (MySQLdb.Error) as e:
                success = 0

    #Physical_Exam
            try:
                curr.execute("""INSERT INTO Physical_Exam VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                    	physical0, physical1, physical2, physical3, physical4, physical5, physical6, physical7, physical8, physical9,
                    	physical10, physical11, physical12, physical13, physical14, physical15, physical16, physical17
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

    #Cognitive_Development_Level
            try:
                curr.execute("""INSERT INTO Cognitive_Development_Level VALUES (%s, %s, %s, %s);""",
                    (id, date,
                    	cogDev0, cogDev1
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

    #Varicella_Screening
            try:
                curr.execute("""INSERT INTO Varicella_Screening VALUES (%s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                    	varicella0, varicella1, varicella2, varicella3, varicella4
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

	#tuberculosis screening
            try:
                curr.execute("""INSERT INTO Tuberculosis_Screening VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                    	tuberculosis10, tuberculosis11, tuberculosis20, tuberculosis21, tuberculosis30, tuberculosis31
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

	#medcare provider medications
            try:
                i = 0
                while i < len(medProMedications)
                	if medProMedications[i] is None:
                		break
	                curr.execute("""INSERT INTO MedCareProvider_Medications VALUES (%s, %s, %s, %s, %s);""",
	                    (id, date,
	                    	medProMedications[i], medProMedications[i + 1], medProMedications[i + 2]
	                    	,))
	                i += 3

            except (MySQLdb.Error) as e:
                success = 0

	#medcare provider verification statement
            try:
                curr.execute("""INSERT INTO Medical_Provider_Verification_Statement VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                    	medProvVerState0, medProvVerState1, medProvVerState2, medProvVerState3, medProvVerState4, medProvVerState5, medProvVerState6, medProvVerState7, medProvVerState8
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

#HIV_Provider section
            try:
                curr.execute("""INSERT INTO HIV_Provider VALUES (%s, %s);""",
                    (id, date,))

            except (MySQLdb.Error) as e:
                success = 0

	#health history
            try:
                curr.execute("""INSERT INTO Health_History VALUES (%s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                    	healthHistory0, healthHistory, healthHistory19, healthHistory20, healthHistory21
                    	,))

            except (MySQLdb.Error) as e:
                success = 0

	#lab data
            try:
                curr.execute("""INSERT INTO Lab_Data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                    (id, date,
                    	lab0, lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9, lab10
                    	,))

            except (MySQLdb.Error) as e:
                success = 0


#last stuff
            db.commit()

            if success:
                tkMessageBox.showinfo("New Profile", "Submission Sucessful!")
            else:
                tkMessageBox.showinfo("New Profile", "Submission Unsucessful\n\nA Camper application \nSubmitted on: " + date + "\nFor ID number: " + str(id) + " \nAlready exists in the system")
