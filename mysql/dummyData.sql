
INSERT INTO Child VALUES ();
INSERT INTO Child VALUES ();
/*
INSERT INTO Childs_Information 
(ID, Date_Submitted, 
	Name_First, Name_Last, Name_Nickname,
	Address_Street, Address_City, Address_County, Address_Zip,
	Home_Phone, Guardian_Phone, Guardian_Email,
	Age, Birthday, Gender, HIV_Status, Aware, Why, Refferal_Source,
	School_attending, School_grade_level,
	Ethnicity, Ethnicity_Other, ADD_ADHD, Learning_Disability,
	Developmental_Disability, Mental_Health_Issues,
	Other_Medical_Condition, Victim_of_Abuse)
VALUES 
(1, '2016-11-24', 
  'Sonika', 'Finch', 'Son', 
  '123 Techwood Drive', 'Atlanta', 'Fulton', 30308, 
  1234567890, 0987654321, 'guardian@gmail.com', 21,
  '1997-01-02', 'Female',
  'HIV Negative', 1, 'idk why', 'no refferal',
  'Gatech', 'Junior',
  ('Other,Multi-racial'), 'idk lol',
  0, 1, 0, 1, 0, 1);
*/
INSERT INTO Child_Application (ID,Date_Submitted,  Signature, Referral, Future_Programs, HERO_Programs) VALUES
	(1,'2016-11-24', 1, 'Clothing/Furniture', 'Healthy HEROs', 'Camp High Five');

INSERT INTO Child_Application (ID,Date_Submitted, Signature, Referral, Future_Programs, HERO_Programs) VALUES
	(2,'2016-12-12', 0, 'Food', 'Other', 'Holiday of HEROs');


INSERT INTO Childs_Information (ID, Date_Submitted, Name_First, Name_Last, Name_Nickname, Address_Street, Address_City,Address_County,Address_Zip, Home_Phone, Guardian_Phone, Guardian_Email, Birthday, Gender, HIV_Status, Aware, Why, Refferal_Source,School_attending,School_grade_level,Ethnicity,ADD_ADHD,Learning_Disability,Developmental_Disability,Mental_Health_Issues,Other_Medical_Condition,Victim_of_Abuse,Criminal_Justice_System,Legal_Custody)	VALUES
	(1,'2016-11-24', 'John', 'Osman', 'Johnny Boy', '3567 Clubland Drive', 'Marietta', 'Cobb County', 30068,7709736653, 4044083543, 'osmangirls@bellsouth.net', '1958-11-24', 'Male','HIV Negative', 1,'Because he asked', 'His doctor', 'Langley High School', '9','White/Caucasian', 0, 1, 0,1, 0, 0,1, 'Mother');


INSERT INTO Childs_Information (ID, Date_Submitted, Name_First, Name_Last, Name_Nickname, Address_Street, Address_City,Address_County,Address_Zip, Home_Phone, Guardian_Phone, Guardian_Email, Birthday, Gender, HIV_Status, Aware, Why, Refferal_Source,School_attending,School_grade_level,Ethnicity,ADD_ADHD,Learning_Disability,Developmental_Disability,Mental_Health_Issues,Other_Medical_Condition,Victim_of_Abuse,Criminal_Justice_System,Legal_Custody,Custody_Other) VALUES
	(2,'2016-12-12', 'Claire', 'Kennedy', 'ID', '123 Dumb Street', 'Monroe', 'Lincoln Parish', 12345, 3182345678, 3183456789,'imkarmenkenneday@gmail.com', '2007-12-12', 'Female', 'HIV Positive', 0, 'She is too dumb', 'Her doctor', 'Good Hope Elementary School','3rd grade', 'White/Caucasian', 1, 1, 1, 1, 0, 0,1, 'Both Parents', 'She is really annoying');



INSERT INTO Parent_Guardian_Information (ID,Date_Submitted,Name_First,Name_Last,Relationship_to_Child,Age,HIV_Status, Adoptive_Parent, Marital_Status, Education_Completed, Employment_Status, Employment_Company_Name, Address_Street, Address_City, Address_State, Address_Zip, WorkPhone, Email) VALUES
	(1,'2016-11-24', 'Karla', 'Osman', 'Mother', 57, 'HIV Positive', 'Yes', 'Widowed', 'Some College', 'Part-Time', 'Cobb County Youth Museum','3567 Clubland Drive', 'Marietta', 'GA', 30068, 4044083543, 'osmangirls@bellsouth.net');
INSERT INTO Parent_Guardian_Information (ID,Date_Submitted,Name_First,Name_Last,Relationship_to_Child,Age,HIV_Status, Adoptive_Parent, Marital_Status, Education_Completed, Employment_Status, Employment_Company_Name, Address_Street, Address_City, Address_State, Address_Zip, WorkPhone, Email) VALUES
	(2,'2016-12-12', 'Karmen', 'Kennedy', 'Mother', 43, 'HIV Positive', 'No', 'Married', 'HS', 'Part-Time', 'Dentist Office','123 Dumb Street', 'Monroe', 'LA', 12345, 3183456789, 'imkarmenkenneday@gmail.com');


INSERT INTO Absent_Parent_Information (ID, Date_Submitted, Name_First, Name_Last, Telephone) VALUES
	(1,'2016-11-24', 'Joe', 'Smith',1234567890);
INSERT INTO Absent_Parent_Information (ID, Date_Submitted, Name_First, Name_Last, Telephone, Address_Street, Address_City, Address_County, Address_Zip, HIV_Status) VALUES
	(2,'2016-12-12', 'John', 'Kennedy', 3185678901, '345 Really Dumb Street', 'Monroe', 'Lincoln Parish', 12345, 'HIV Positive');


INSERT INTO Household_Information (ID, Date_Submitted, Count, Name, Relationship, Sex, Age, HIV_Status) VALUES
	(1,'2016-11-24', 3, 'Karla Osman', 'Mom', 'Female', 56, 'HIV Negative');
INSERT INTO Household_Information (ID, Date_Submitted, Count, Name, Relationship, Sex, Age, HIV_Status) VALUES
	(2,'2016-12-12', 3, 'Karmen Kenneday', 'Mom', 'Female', 42, 'HIV Positive');


INSERT INTO Fam_Annual_Income (ID, Date_Submitted, Fam_Annual_Income) VALUES
	(1,'2016-11-24', '$15,001-20,000'), (2,'2016-12-12', '$0-10,000');


INSERT INTO Source_Fam_Income (ID,Date_Submitted, Source_Fam_Income) VALUES
	(1,'2016-11-24', 'Employment'), (2,'2016-12-12', 'Social Security');

INSERT INTO ChildApp_Emergency_Contact (ID, Date_Submitted, Name_First, Name_Last, Relationship_to_Child, Address_Street, Address_City, Address_State, Address_Zip, Phone_Home, Phone_Cell,Phone_Alt) VALUES
	(1,'2016-11-24', 'Karla', 'Osman', 'Mom', '3567 Clubland Drive', 'Marietta', 'GA', 30068, 7709736653, 4044083543, 6784776905), (2,'2016-12-12', 'Ted', 'Lamprich', 'Grandfather', '318 Goss Street', 'Farmerville', 'LA', '38234', 3188901234, 3185678901, 3182456789);


INSERT INTO Statement_Of_Understanding (ID, Date_Submitted, Statement_One, Statement_Two, Statement_Three, Statement_Four, Statement_Five, Statement_Six, Statement_Seven)VALUES
	(1,'2016-11-24',1,1,1,1,1,1,1),(2,'2016-12-12', 0,0,0,0,0,0,0);


INSERT INTO Camp_Application(ID, Date_Submitted) VALUES (1,'2016-11-24'), (2,'2016-12-12');


INSERT INTO Parent (ID, Date_Submitted) VALUES
	(1,'2016-11-24'), (2,'2016-12-12');


INSERT INTO Demographic_Information (ID, Date_Submitted, First_Name, Last_Name, Middle_Initial, Date_Of_Birth, Age, Gender, Race, Primary_Language, Address_Street, Address_City, Address_State, Address_Zip, Address_County, Camper_Email, Parent_Email, Guardian_Name, Guardian_Camper_Relationship, Last_Grade_Completed, Special_Ed_Classes, Siblings_Applying, T_Shirt, Planned_Transportation) VALUES
(1,'2016-11-24', 'John', 'Osman', 'E', '1958-11-24', 58, 'Male', 'White', 'English', '3567 Clubland Drive', 'Marietta', 'GA', 30068, 'Cobb County','josmanassociate@att.net', 'osmangirls@bellsouth.net', 'Karla Osman', 'Mom', '10', 0, 0, 'Youth L', 'Atlanta bus'),
(2,'2016-12-12', 'Claire', 'Kennedy', 'E', '2007-12-12', 10, 'Female','White', 'English', '123 Dumb Street', 'LA','CA', 12345, 'Lincoln Parish','that@this.com', 'something@whatever.com', 'Karmen Kennedy','Mom', 4, 1, 1, 'Adult L', 'Albany bus');


INSERT INTO Demographic_Contacts (ID, Date_Submitted, Type, Name, Time_Preference, Phone_Number) VALUES
	(1,'2016-11-24', 'Home', 'Karla Osman', 'Evening', 7709736653),
	(2,'2016-12-12', 'Cell', 'Ted Lamprich', 'Day', 3188901234);


INSERT INTO Parent_Emergency_Contact (ID, Date_Submitted, Name, Relationship, Daytime_Phone, Evening_Phone) VALUES
	(1,'2016-11-24', 'Karla Osman','mom', 7709736653, 4044083543),
	(2,'2016-12-12', 'Ted Lamprich','dad', 3188901234, 3187893456);


INSERT INTO Insurance_Information (ID, Date_Submitted, Type_of_Health_Insurance, Policy_Number, Group_Number) VALUES
	(1,'2016-11-24', 'Medicaid', '123456789', '3456'), (2,'2016-12-12','PeachCare', '234567890', '2345');


INSERT INTO Medical_Provider_Information (ID, Date_Submitted, Medical_Provider_Name, Phone_Office, Pharmacy_Name, Phone_Pharmacy) VALUES
	(1,'2016-11-24', 'Dr. Locata', 6781234556, 'Publix Pharmacy', 7701234567),
	(2,'2016-12-12', 'Dr. Pickles', 3184567890, 'Kroger Pharmacy', 3182344455);


INSERT INTO Medical_Information (ID, Date_Submitted, Current_Medical_Conditions, Medical_Condition_Explanation) VALUES
	(1,'2016-11-24', 'Asthma', 'He is old and doesn"t breathe well'),
	(2,'2016-12-12', 'HIV','She is young and hyperactive');


INSERT INTO Allergies (ID,Date_Submitted, Food_Allergy, Food_Reaction, Env_Allergy, Env_Reaction) VALUES (1,'2016-11-24', 'Cheese', 'Poops smell bad', 'Grass', 'Gets an uncomfortable rash, but will not die');
INSERT INTO Allergies (ID,Date_Submitted, Env_Allergy, Env_Reaction) VALUES (2,'2016-12-12', 'Bees', 'Swelling, but won"t die');



INSERT INTO Dietary_Needs (ID, Date_Submitted, Special_Dietary_Needs, Vegetarian, Food_Restrictions, G_Tube, Formula_Supplements, Formula_Type, Formula_Cans_Per_Day, Feeding_Pump, Feeding_Schedule) VALUES
	(1,'2016-11-24', 1, 0, 'No cheese, but can have milk and yogurt', 'None', 'None', 'None', 0, 0, 'Breakfast, Lunch, and Dinner with some snacks'),
	(2,'2016-12-12', 0, 1, 'Sugar makes her ADD worse', 'Medicine', 'By Mouth', 'Growth suppliments', 10, 0, 'Only breakfast and lunch, we do not want her to eat carbs late in the day');



INSERT INTO General_Health (ID, Date_Submitted, Physical_Limitations, Other, Tire_Easily,Swim, Chicken_Pox, Chicken_Pox_Date, Menstrual_Cycle, Menstrual_Difficulties) VALUES
	(1,'2016-11-24', 'Other', 'bending over', 1, 0, 0, NULL, 0, 'Man'),
	(2,'2016-12-12', 'Showering',NULL, 1, 1, 0, NULL, 1, 'She still does not understand what it is');



INSERT INTO Pyschosocial_and_Behavioral_info (ID, Date_Submitted, Camper_Knows, Time_Camper_Known, Camper_Experiences, Med_Hyper_AttentionProb, Explanation, Camper_Interests, Recent_Major_Events) VALUES
	(1,'2016-11-24', 1, 'always', 'Fear of dark', 0, NULL, 'Golf', 'He got a hole in 1!'),
	(2,'2016-12-12', 1, 'less than 6 months','Bedwetting', 1, 'she has ADD', 'Swimming', 'she can finally swim with her head not above the water');


INSERT INTO Parent_Medications (ID, Date_Submitted, Medication, Amount, Time_Instruction) VALUES
	(1,'2016-11-24', 'Allegra', 'One tablet', 'At night'),
	(2,'2016-12-12', 'Tums', '4 tablets', 'After every meal');


INSERT INTO Release_Forms_Signed (ID, Date_Submitted, Parent_Camper_Contract, Partcipation_Consent_Liability_Release, Media_Release, Camper_HIV_Education, Camp_Twin_Lakes_Rules, Parental_Consent_and_Release) VALUES
	(1,'2016-11-24', 1, 0, 1, 1, 0, 1),
	(2,'2016-12-12', 1, 1, 1, 0, 0, 0);



INSERT INTO Medical_Care_Provider(ID, Date_Submitted,Restrictions_And_Recommendations) VALUES
	(1,'2016-11-24', 'Still just the arthritis and some asthma'),
	(2,'2016-12-12', 'Still ADD and cannot have sugar');



INSERT INTO Medical_History (ID, Date_Submitted, Management, Nutritional_Supplements, Feeding_Care, Formula_Type, Formula_Enum) VALUES
	(1,'2016-11-24', 'He is a lot to manage', 1, 'He needs a lot of fiber', 'Apples and oatmeal, preferably together', 'Oral');
INSERT INTO Medical_History VALUES
	(2,'2016-12-12', 'She needs a lot of supervision', 1, 'She cannot have sugar', 'Low sugar', 'G-tube');




INSERT INTO Med_Hist_Diagnosis (ID, Date_Submitted, Diagnosis) VALUES
	(1,'2016-11-24', 'He has bad arthritis, because he is old');
INSERT INTO Med_Hist_Diagnosis (ID, Date_Submitted, Diagnosis) VALUES
	(2,'2016-12-12', 'She has attention problems and is very self-centered');



INSERT INTO Med_Hist_Allergies (ID, Date_Submitted, Type, Allergy, Reaction) VALUES
	(1,'2016-11-24', 'Environmental', 'Grass', 'Gets a bad rash'),
	(2,'2016-12-12', 'Environmental', 'Bees', 'Stung area swells up');



INSERT INTO Physical_Exam (ID, Date_Submitted, Date_Completed, Height, Weight, Pulse, Resperations, Blood_Pressure, HEENT, Skin, Cardiovascular, GU_GYN, Pulmonary, Glasses_HearingAids_PE, Abdomen, Lymph_Nodes, Extremities,Spine, Miscellaneous, Comments) VALUES
	(1,'2016-11-24', '2016-10-31', '5" 6""', 140, 59, 30, 145, 'I do not remember what this is', 'Pale', 'Heart pumping', 'Doing great',
		'No problems here', 'Has reading and near sighted glasses and hearing aids', 'Ripped abs', 'they are nodin', 'Arthritis in extremities',
		'strong spine', 'graying hair and balding', 'overall doing great, just aging'),
	(2,'2016-12-12', '2016-05-20', '4" 5"', 98, 68, 20, 130, 'Who knows', 'Tan, watch out for skin cancer', 'Heart is doing the thing', 'So good', 'really cool pulmonary', 'No glasses or hearing aids', 'flabby tummy', 'not as nodin as John', 'weak arms', 'spine is aight','really nice hair', 'is overall doing well');


INSERT INTO Cognitive_Development_Level (ID, Date_Submitted, Development_Level, Other_Psychosocial_Information) VALUES (1,'2016-11-24',NULL,NULL), (2,'2016-12-12',NULL,NULL);


INSERT INTO Tuberculosis_Screening (ID, Date_Submitted, Type, Date_Screened, Result) VALUES
	(1,'2016-11-24', 'Chest X-ray', '2016-02-15', 'No Tuberculosis here'),
	(2,'2016-12-12', 'Tuberculin Skin Test', '2016-05-20', 'May have tuberculosis should test again');


INSERT INTO MedCareProvider_Medications (ID, Date_Submitted, Medication_Name, Amount_Including_Dosage, Times_To_Give) VALUES
	(1,'2016-11-24', 'Allegra', '30mg', 'before bed'),
	(2,'2016-12-12', 'Tums', '4 tablets', 'after every meal');


INSERT INTO Medical_Provider_Verification_Statement (ID, Date_Submitted, Signature,Sig_Date, Name, Address_Street, Address_City, Address_State, Address_Zip,Phone, Emergency_Contact) VALUES
	(1,'2016-11-24', 1, '2015-03-04', 'Dr. John Smith', '123 Georgia Tech Station', 'Atlanta', 'GA', 12345, 7701234567, 'No emergency contact'),
	(2,'2016-12-12', 1, '2015-04-11', 'Dr. Joe Tan', '123 ULM Station', 'Monroe', 'LA', 34567, 3184567890, 'Grandfather');


INSERT INTO HIV_Provider(ID, Date_Submitted) VALUES
	(1,'2016-11-24'), (2,'2016-12-12');


INSERT INTO Heatlh_History (ID, Date_Submitted, Major_Surgical_History, Health_History, History_of_Noncompliance, Explanation) VALUES
	(1,'2016-11-24','I aint been operated on', 'Chronic Cough', 0, 'He complies pretty well'),
	(2,'2016-12-12', 'some people call me the terminator','ADD or ADHD', 1, 'She is rude and is not compliant');


INSERT INTO Lab_Data (ID, Date_Submitted, Lab1_Date,Lab1_WBC,Lab1_HGB, Lab1_HCT, Lab1_Plt_Count, Lab2_Date, Lab2_CD4_Count, Lab2_Viral_Load, Lab3_Date, Lab3_CD4_Count, Lab3_Viral_Load) VALUES
	(1,'2016-11-24', '2015-10-31', 1345, 345, 23, 12345, '2016-01-20', 456, 2345, '2016-04-23', 567, 1234),
	(2,'2016-12-12', '2015-04-11', 3471, 347, 45, 7892, '2015-09-16', 347, 2342, '2016-02-14', 214, 1240);
