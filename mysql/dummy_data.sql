#Insert Child
INSERT INTO Child VALUES (); 
INSERT INTO Child VALUES ();
INSERT INTO Child VALUES ();
INSERT INTO Child VALUES ();
INSERT INTO Child VALUES ();

#Insert into Child Application
INSERT INTO Child_Application (ID, Date_Submitted, Signature, Referral, Future_Programs, HERO_Programs) 
	VALUES 
	(1, '2016-11-24', 1, 'Clothing/Furniture', 'Healthy HEROs', 'Camp High Five');

INSERT INTO Child_Application VALUES 
	(1, '2016-12-12', 1, 'Other', 'Mental Health', 'Other', 'College Scholarship', 'Camp High Five');

INSERT INTO Child_Application (ID MEDIUMINT, Date_Submitted, Referral, Future_Programs, HERO_Programs) VALUES 
	(1, '2016-05-20', 1, 'Rent/Utlities Assistance', 'Career Development/Job Readiness', 
		'Transition to Adulthood'), 
	(1, '2016-02-18', 1, 'Food', 'Healthy HEROs', 'Bright HEROs Program'), 
	(1, '2016-07-06', 1, 'Clothing/Furniture', 'Healthy HEROs', 'Camp High Five');


#Insert into Childs Information
INSERT INTO Childs_Information VALUES
	('2016-11-24', 'John', 'Osman', 'Johnny Boy', '3567 Clubland Drive', 'Marietta', 'Cobb County', 30068, 
		7709736653, 4044083543, 'osmangirls@bellsouth.net', '1958-11-24', 'Male', 'HIV Negative', 'Y', 
		'Because he asked', 'His doctor', 'Langley High School', '9', 'White/Caucasian', 'He"s so white' 'N', 'Y', 'N', 
		'Y', 'N', 'N', 'Mother', 'He has arthritis'); 

INSERT INTO Childs_Information VALUES
	('2016-12-12', 'Claire', 'Kennedy', 'ID', '123 Dumb Street', 'Monroe', 'Lincoln Parish', 12345, 3182345678, 3183456789, 
		'imkarmenkenneday@gmail.com', '2007-12-12', 'Female', 'HIV Positive', 'N', 'She is too dumb', 'Her doctor', 'Good Hope Elementary School', 
		'3rd grade', 'White/Caucasian', 'Cajun', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'Both Parents', 'She is really annoying');

INSERT INTO Childs_Information VALUES 
	('2016-05-20', 'Elizabeth', 'Osman', 'Lizard', '3567 Clubland Drive', 'Marietta', 'Cobb County', 30068, 7709736653, 4044083543, 
		'osmangirls@bellsouth.net', '1996-05-20', 'Female', 'HIV Positive', 1, 'Mother has HIV', 'Brother in HERO programs', 
		'Walton High School', '9th grade', 'White/Caucasian', 1, 0, 0, 1, 0, 0, 1, 'Both Parents'),
	('2016-07-06', 'Eli', 'Lind', 'E', '256 Chestnut Springs Ct', 'Marietta', 'Cobb County', 30062, 7705673456, 7705673456, 
		'immyla@gmail.com', '1997-07-06', 'Male', 'HIV_Negative', 1, 'Had to explain to him that he was not HIV Positive', 'Girlfriend in HERO programs', 
		'Walton High School', '9th grade', 'Asian/Pacific Islander/Indian Sub-Continent', 1, 0, 1, 1, 0, 1, 0, 'Both Parents');

INSERT INTO Childs_Information (Name_First, Name_Last, Name_Nickname, Address_Street, Address_City, Address_County, Address_Zip, 
	Home_Phone, Guardian_Phone, Guardian_Email, Birthday, Gender, HIV_Status, Aware, Why, Referral_Source, School_attending, School_grade_level, 
	Ethnicity, Ethnicity_Other, ADD_ADHD, Learning_Disability, Developmental_Disability, Mental_Health_Issues, Other_Medical_Condition, Victim_of_Abuse, Criminal_Justice_System, 
	Legal_Custoday) VALUES
	('2016-02-08', 'Layla', 'Goodman', 'Lala', '456 Fulton St', 'Johns Creek', 'Fulton County', 30022, 6789031234, 4044443456, 
		'immsgoodman@gmail.com', '1997-01-21', 'Female', 'HIV_Positive', 0, 'She refuses to accept it', 'Referred by friend in HERO programs', 
		'Johns Creek High School', '10th grade', 'Other', 'Iranian', 1, 0, 1, 1, 0, 1, 0, 'Mother');

#Insert into Parent_Guardian Information
INSERT INTO Parent_Guardian_Information VALUES
	('2016-11-24', 'Karla', 'Osman', 'Mother', 57, 'HIV Positive', 'Yes', 'Widowed', 'Some College', 'Part-Time', 'Cobb County Youth Museum', 
		'3567 Clubland Drive', 'Marietta', 'GA', 30068, 4044083543, 'osmangirls@bellsouth.net');

INSERT INTO Parent_Guardian_Information VALUES
	('2016-12-12', 'Karmen', 'Kennedy', 'Mother', 43, 'HIV Positive', 'No', 'Married', 'HS', 'Part-Time', 'Dentist Office', 
		'123 Dumb Street', 'Monroe', 'LA', 12345, 3183456789, 'imkarmenkenneday@gmail.com');
INSERT INTO Parent_Guardian_Information VALUES
	('2016-11-24', 'Macy', 'Osman', 'Mother', 56, 'HIV Negative', 'No', 'Single', 'HS', 'Full-Time', 'DPM Fragrances', '3567 Clubland Drive', 
		'Marietta', 'GA', 30068, 4048976789, 'macyatwork@gmail.com'),
	('2016-02-08', 'Venus', 'Goodman', 'Mother', 48, 'HIV Positive', 'No', 'Separated', 'Doctorate', 'Part-Time', 'Neiman Marcus', '456 Fulton St', 
		'Johns Creek', 'GA', 30022, 7704561234, 'venusatwork@gmail.com'), 
	('2016-07-06', 'Gary', 'Lind', 'Father', 52, 'HIV Positive', 'No', 'Married', 'Bachelor Degree', 'Full-Time', 'Waffle House', '256 Chestnut Springs Ct', 
		'Marietta', 'GA', 20062, 7708905678, 'garyatwork@gmail.com');

#Insert into Absent_Parent_Information
INSERT INTO Absent_Parent_Information (Date_Submitted, Name_First, Name_Last) VALUES 
	('2016-11-24', 'Joe', 'Smith');

INSERT INTO Absent_Parent_Information VALUES
	('2016-12-12', 'John', 'Kennedy', '3185678901', '345 Really Dumb Street', 'Monroe', 'Lincoln Parish', 12345, 'HIV Positive'),
	('2016-02-08', 'Mohammad', 'Goodman', 8904493214, '456 Cowboy St', 'Jackson', 'WY', 45689, 'HIV Negative');

INSERT INTO Absent_Parent_Information (Date_Submitted, Name_First, Name_Last, HIV_Status) VALUES 
	('2016-05-20', 'Calvin', 'Young', 'Unknown');


#Insert into Household_Information
INSERT INTO Household_Information VALUES 
	('2016-11-24', 3, 'Karla Osman', 'Mom', 'Female', 56, 'HIV Negative';

INSERT INTO Household_Information VALUES 
	('2016-12-12', 3, 'Karmen Kenneday', 'Mom', 'Female', 42, 'HIV Positive'), 
	('2016-05-20', 3, 'Macy Osman', 'Mom', 'Female', 56, 'HIV Positive'), 
	('2016-02-08', 3, 'Venus Goodman', 'Mom', 'Female', 48, 'HIV Positive'), 
	('2016-07-06', 3, 'Gary Lind', 'Dad', 'Male', 52, 'HIV Positive');


#Insert into Fam_Annual_Income
INSERT INTO Fam_Annual_Income VALUES
	('2016-11-24', '$15,001-20,000'), 
	('2016-12-12', '$0-10,000'), 
	('2016-05-20', '$0-10,000'), 
	('2016-02-08', '$10,001-15,000'), 
	('2016-07-06', '$25,001-30,000');

#Source_Fam_Income
INSERT INTO Source_Fam_Income VALUES Date_Submitted, Source_Fam_Income
	('2016-11-24', 'Employment'),
	('2016-12-12', 'Social Security')
	('2016-05-20', 'Government Support'), 
	('2016-02-08', 'Social Security'), 
	('2016-07-06', 'Employment');


#ChildApp_Emergency_Contact
INSERT INTO ChildApp_Emergency_Contact VALUES 
	('2016-11-24', 'Karla', 'Osman', 'Mom', '3567 Clubland Drive', 'Marietta', 'GA', 30068, 7709736653, 4044083543, 6784776905),
	('2016-12-12', 'Ted', 'Lamprich', 'Grandfather', '318 Goss Street', 'Farmerville', 'LA', '38234', 3188901234, 3185678901, 3182456789), 
	('2016-05-20', 'Karla', 'Osman' 'Grandmother', '3567 Clubalnd Drive', 'Marietta', 'GA', 30068, 7709736653, 4044083543, 6784776905), 
	('2016-02-08', 'Carl', 'Feelings', 'Friend', '128 Telker Dr', 'Marietta', 'GA', 30067, 7708876789, 4043453456, 7701234567), 
	('2016-07-06', 'Myla', 'Lind', 'Mom', '256 Chestnut Springs Ct', 'Marietta', 'GA', 30062, 7709877890, 4044563456, 4042341235);

#Insert into Statement_Of_Understanding 
INSERT INTO Statement_Of_Understanding VALUES
	('2016-11-24', 1, 1, 1, 1, 1, 1, 1);
INSERT INTO Statement_Of_Understanding VALUES 
	('2016-12-12', 0, 0, 0, 0, 0, 0, 0);
INSERT INTO Statement_Of_Understanding VALUES
	('2016-05-20', 1, 1, 0, 0, 1, 1, 1), 
	('2016-02-08', 1, 1, 1, 1, 1, 1, 1), 
	('2016-07-06', 0, 0, 0, 1, 1, 1, 0);

#Insert into Camp_Application
INSERT INTO Camp_Application VALUES
	('2016-11-24');
INSERT INTO Camp_Application VALUES
	('2016-12-12'), 
	('2016-05-20'),
	('2016-02-08'), 
	('2016-07-06');

#Parent Application (Parent)
INSERT INTO Parent VALUES
	('2016-11-24'), 
	('2016-12-12'), 
	('2016-05-20'), 
	('2016-02-08'), 
	('2016-07-06');

#Demographic_Information (Parent)
INSERT INTO Demographic_Information VALUES 
	('2016-11-24', 'John', 'Osman', 'E', '1958-11-24', '58', 'Male', 'White', 'English', '3567 Clubland Drive', 'Marietta', 'GA', 30068, 'Cobb County', 
		'josmanassociate@att.net', 'osmangirls@bellsouth.net', 'Karla Osman', 'Mom', '10', 'N', 'N', 'Youth L', 'Atlanta bus'), 
	('2016-12-12', 'Claire', 'Kennedy', 'E', '2007-12-12', 10, 'White', 'English', '123 Dumb Street', 'LA', 12345, 'Lincoln Parish', 'Karmen Kennedy', 
		'Mom', '4', 'Y', 'Y', 'Adult L', 'Albany bus'), 
	('2016-05-20', 'Elizabeth', 'Osman', 'N', '1996-05-20', 20, 'Female', 'White', 'English', '3567 Clubland Drive', 'Marietta', 'GA', 30068, 
		'Cobb County', 'eosman7@gatech.edu', 'osmangirls@bellsouth.net', 'Macy Osman', 'Mom', 9, 0, 0, 'Adult M', 'Atlanta bus'), 
	('2016-02-08', 'Layla', 'Goodman', 'A' ,'1997-01-21', 20, 'Female', 'Persian', 'English and Persian', '456 Fulton St', 'Johns Creek', 'GA', 30022, 'Fulton County', 
		'imlayla@gmail.com', 'msgoodmanatwork@gmail.com', 'Venus Goodman', 'Mom', 10, 0, 0, 'Adult XXL', 'Savannah bus'), 
	('2016-07-06', 'Eli', 'Lind', 'A', '1997-07-06', 19, 'Male', 'Asian', 'Chinese', '256 Chestnut Springs Ct', 'Marietta', 'GA', 30062, 'Cobb County', 
		'spiderflu@gmail.com', 'imgary@gmail.com', 'Gary Lind', 'Father', 9, 1, 0, 'Adult L');

#Demographic_Contacts (Parent)
INSERT INTO Demographic_Contacts VALUES
	('2016-11-24', 'Home', 'Karla Osman', 'Evening', 7709736653), 
	('2016-12-12', 'Cell', 'Ted Lamprich', 'Day', 3188901234)
	('2016-05-20', 'Home', 'Macy Osman', 'Evening', 7709736653), 
	('2016-02-08', 'Cell', 'Venus Goodman', 'Day', 6784563456), 
	('2016-07-06', 'Work', 'Gary Lind', 'Day', 7702325432);

#Parent_Emergency_Contact (Parent)
INSERT INTO Parent_Emergency_Contact VALUES
	('2016-11-24', 'Karla Osman', 'Mom', 7709736653, 4044083543), 
	('2016-12-12', 'Ted Lamprich', 'Grandfather' ,3188901234, 3187893456)
	('2016-05-20', 'Karla Osman', 'Grandmother', 7709736653, 4044083543), 
	('2016-02-08', 'Karla Osman', 'Family Friend', 7709736653, 4044083543), 
	('2016-07-06', 'Myla Lind', 'Mother', 6784562345, 4043450987);

#Insurance_Information (Parent)
INSERT INTO Insurance_Information VALUES
	('2016-11-24', 'Medicaid', 123456789, 3456, 789), 
	('2016-12-12','PeachCare', 234567890, 2345, 678), 
	('2016-05-20', 'Medicaid', 345678901, 4567, 456), 
	('2016-07-06', 'Private', 456789012, 1234, 789);
INSERT INTO Insurance_Information (Date_Submitted, Type_of_Health_Insurance) VALUES
	('2016-02-08', 'None');

#Medical_Provider_Information (Parent)
INSERT INTO Medical_Provider_Information VALUES
	('2016-11-24', 'Dr. Locata', 6781234556, 'Publix Pharmacy', 7701234567), 
	('2016-12-12', 'Dr. Pickles', 3184567890, 'Kroger Pharmacy', 3182344455)
	('2016-05-20', 'Dr. Locata', 6781234556, 'CVS Pharmacy', 6788900009), 
	('2016-02-08', 'Dr. Fang', 7703452234, 'GT Pharmacy', 7709887766),
	('2016-07-06', 'Dr. Bonaig', 6784456676, 'Wellstar Pharmacy', 6781233221);

#Medical_Information (Parent)
INSERT INTO Medical_Information VALUES
	('2016-11-24', 'Asthma', 'Arthritis', 'He is old and doesn"t breathe well'), 
	('2016-12-12', 'HIV', 'ADD', 'She is young and hyperactive')
	('2016-05-20', 'Other', 'Chronic Strep Throat', 'She is incredibly susceptible to contracting Strep Throat'), 
	('2016-02-08', 'HIV', 'Depression and Anxiety', 'Mental health problems caused by HIV diagnosis');
INSERT INTO Medical_Information (Date_Submitted, Current_Medical_Conditions) VALUES
	('2016-07-06', 'ADD or ADHD');

#Allergies (parent)
INSERT INTO Allergies (Date_Submitted, Food_Allergy, Food_Reaction, Env_Allergy, Env_Reaction) VALUES 
	('2016-11-24', 'Cheese', 'Poops smell bad', 'Grass', 'Gets an uncomfortable rash but not detrimental');
INSERT INTO Allergies (Date_Submitted, Env_Allergy, Env_Reaction) VALUES 
	('2016-12-12', 'Bees', 'Swelling, but won"t die'), 
	('2016-05-20', 'Yellow Jackets and Hornets', 'Will go into shock');
INSERT INTO Allergies (Date_Submitted, Food_Allergy, Food_Reaction) VALUES 
	('2016-02-08', 'Chocolate', 'Tongue will swell');

#Dietary_Needs (parent)
INSERT INTO Dietary_Needs VALUES 
	('2016-11-24', 1, 0,  'No cheese, but can have milk and yogurt', 'None', 'None', 'None', 0, 0, 'None', 'Breakfast, Lunch, and Dinner with some snacks'),
	('2016-12-12', 1, 0,'Sugar makes her, ADD worse', 'None', 'None', 'Growth suppliments', 10, 0, 'No pump', 'Only breakfast and lunch, we do not want her to eat carbs late in the day'),
	('2016-02-08', 1, 1, 'No meat but can eat fish', 'None', 'By Mouth', 'Growth suppliments and vitamins', 1, 0, 'No pump', 'Takes suppliments and vitamins before bed');
INSERT INTO Dietary_Needs (Date_Submitted, Special_Dietary_Needs, Vegetarian, Food_Restrictions, G_Tube, Formula_Supplments, Feeding_Pump) VALUES
	('2016-05-20', 1, 1, 'Cannot eat meat including seafood', 'None', 'None', 0);
INSERT INTO Dietary_Needs (Date_Submitted, Special_Dietary_Needs, Vegetarian, Feeding_Pump) VALUES
	('2016-07-06', 0, 0, 0);

#General_Health (parent)
INSERT INTO General_Health VALUES
	('2016-12-12', 'Showering', 'Has weak arms, do not ask her to carry things she will be embarrassed', 1, 1, 0, 'NA', 1, 'She still does not understand what it is'), 
	('2016-05-20', 'Dressing', 'Hard time balancing to get on pants', 1, 0, 0, 'NA', 1, 'Can handle flow well'), 
	('2016-02-08', 'Eating', 'She needs to be told what she is eating, she cannot handle options', 0, 1, 0, 'NA', 0, 'She still hasn"t gotten hers yet'); 
INSERT INTO General_Health (Date_Submitted, Physical_Limitations, Other, Tire_Easily, Swim, Chicken_Pox, Chicken Pox_Date) VALUES
	('2016-07-06', 'Dressing', 'He will come with a list of what he should wear everyday', 1, 1, 1, '2001-10-24'),
	('2016-11-24', 'Other', 'Cannot bend over easily to tie shoes', 1, 0, 0, 'NA');

#Pyschosocial_and_Behavioral_info (parent)
INSERT INTO Pyschosocial_and_Behavioral_info VALUES 
	('2016-02-08', 1, 'a few years', 'Sleeps with comfort item', 1, 'Take medication once a day in the morning', 'Nature', 'She went on a hike in Peru'),
	('2016-12-12', 1, 'less than 6 months','Bedwetting', 1, 'she has ADD', 'Swimming', 'she can finally swim with her head not above the water');
INSERT INTO Pyschosocial_and_Behavioral_info (Date_Submitted, Camper_Knows, Time_Camper_Known, Camper_Experiences, Med_Hyper_AttentionProb, Camper_Interests, Recent_Major_Events) VALUES
	('2016-05-20', 1, 'less than 6 months', 'Anxiety', 0, 'Bicycling', 'She doesn"t need training wheels anymore!'), 
	('2016-11-24', 1, 'always', 'Fear of dark', 0, 'Golf', 'He got a hole in 1!'), 
	('2016-07-06', 1, 'always', 'Fights easily', 0, 'Sports', 'Recently got interested in weightlifting');


#Parent_Medications (parent)
INSERT INTO Parent_Medications VALUES
	('2016-11-24', 'Allegra', 'One tablet', 'At night'), 
	('2016-12-12', 'Tums', '4 tablets', 'After every meal'), 
	('2016-05-20', 'Spironolactone', '1 tablet', 'At night before bed'), 
	('2016-02-08', 'Growth suppliments and vitamins', '5 total tablets', 'At night'), 
	('2016-07-06', 'Allegra', '1 tablet', 'In the morning');

#Release_Forms_Signed (parent)
INSERT INTO Release_Forms_Signed VALUES
	('2016-11-24', 1, 1, 1, 1, 1, 1), 
	('2016-12-12', 1, 1, 1, 0, 0, 0), 
	('2016-05-20', 1, 1, 1, 1, 1, 1), 
	('2016-02-08', 1, 1, 0, 0, 1, 1), 
	('2016-07-08', 1, 1, 1, 1, 1, 1);

#Medical Care Provider (medical)
INSERT INTO Medical_Care_Provider VALUES
	('2016-11-24', 'Still just the arthritis and some asthma'), 
	('2016-12-12', 'Still ADD and cannot have sugar'), 
	('2016-05-20', 'Recommended that she takes naps throughout the day since she tires easily'), 
	('2016-02-08', 'Sometimes she needs moments to herself to calm down when she becomes too stimulated'), 
	('2016-07-06', 'He is extremely introverted and enjoys being alone. Allow him time by himself or he will not enjoy himself');

#Insert into Medical_History (medical)
INSERT INTO Medical_History VALUES 
	('2016-11-24', 'He is a lot to manage', 1, 'He needs a lot of fiber', 'Apples and oatmeal, preferably together', 'Oral');
INSERT INTO Medical_History VALUES 
	('2016-12-12', 'She needs a lot of supervision', 1, 'She cannot have sugar', 'Low sugar', 'G-tube'), 
	('2016-02-08', 'She needs a lot of attention', 1, 'Vegetarian', 'Protein suppliments', 'Oral');
INSERT INTO Medical_History (Date_Submitted, Management, Nutritional_Supplements, Feeding_Care) VALUES
	('2016-05-20', 'Very calm and easy to manage', 0, 'Vegetarian'), 
	('2016-07-06', 'Easy to manage', 0, 'Will eat basically anything you give to him');

#Insert into Curr_Diagnosis (medical)
INSERT INTO Curr_Diagnosis VALUES
	('2016-11-24', 'He has bad arthritis, because he is old');
INSERT INTO Curr_Diagnosis VALUES
	('2016-12-12', 'She has attention problems and is very self-centered'), 
	('2016-05-20', 'She has chronic strep throat'), 
	('2016-02-08', 'Severe anxiety and depression, feels better when around others, but sometimes needs a break from activities'), 
	('2016-07-06', 'Shoulder problems');

#Med_Hist_Allergies (medical)
INSERT INTO Med_Hist_Allergies VALUES
	('2016-11-24', 'Environmental', 'Grass', 'Gets a bad rash'), 
	('2016-12-12', 'Environmental', 'Bees', 'Stung area swells up'), 
	('2016-05-20', 'Environmental', 'Yellow Jackets and Hornets', 'She will go into shock'), 
	('2016-02-08', 'Food', 'Chocolate', 'Tongue will swell'), 
	('2016-05-20', 'Medication', 'Penicillin', 'She will break out in hives');

#Physical_Exam
INSERT INTO Physical_Exam VALUES 
	('2016-11-24', '2016-10-31', '5" 6""', 140, 59, 30, 145, 'I do not remember what this is', 'Pale', 'Heart pumping', 'Doing great', 
		'No problems here', 'Has reading and near sighted glasses and hearing aids', 'Ripped abs', 'they are nodin', 'Arthritis in extremities', 
		'strong spine', 'graying hair and balding', 'overall doing great, just aging'), 
	('2016-12-12', '2016-05-20', '4" 5""', 98, 68, 20, 130, 'Who knows', 'Tan, watch out for skin cancer', 'Heart is doing the thing', 'So good', 
		'so good', 'really cool pulmonary', 'No glasses or hearing aids', 'flabby tummy', 'not as nodin as John', 'weak arms', 'spine is aight', 
		'really nice hair', 'is overall doing well')
	('2016-05-20', '2016-02-10', '5" 1""', 125, 60, 25, 130, 'Who knows', 'Prone to sunburn', 'Heart going well', 'So good', 'No problems', 'Wears glasses', 
		'Flabby tummy', 'Strep throat common', 'weak arms', 'Spine strong, but poor posture', 'She has soft hair', 'She could be doing better'), 
	('2016-02-08', '2015-12-26', '5" 5""', 120, 48, 26, 143, 'So good', 'Tans easily', 'Heart pumping'. 'Could be better', 'No problems', 'Needs to wear contacts', 
		'Ripped abs', 'Really strong legs from running', 'Poor posture', 'Pretty hair', 'She"s doing pretty well'), 
	('2016-07-06', '2016-05-24', '5" 8""', 150, 65, 29, 147, 'Pretty good', 'Olive complexion', 'Pumpin away', 'Pretty good', 'Good!', 'Must wear glasses', 
		'Lil tummy', 'Just nodin', 'Really strong legs and arms','Extremely good posture', 'Really good hugs', 'Can open most jars');

INSERT INTO Cognitive_Development_Level (Date_Submitted, Development_Level) VALUES 
('2016-11-24', 'Age Appropriate'), 
('2016-12-12', 'Severe Delay'), 
('2016-05-20', 'Mild Delay'), 
('2016-02-08', 'Moderate Delay'), 
('2016-07-06', 'Mild Delay');

#Tuberculosis_Screening (medical)
INSERT INTO Tuberculosis_Screening VALUES
	('2016-11-24', 'Chest X-ray', '2016-20-31', 'No Tuberculosis here'), 
	('2016-12-12', 'Tuberculin Skin Test', '2016-05-20', 'May have tuberculosis should test again')
	('2016-05-20', 'Quantiferon Testing', '2016-04-20', 'She is clean'), 
	('2016-02-08', 'Tuberculin Skin Test', '2016-01-30', 'Should use another test, results inconclusive'), 
	('2016-07-06', 'Chest X-ray', '2016-06-07', 'No Tuberculosis');

#MedCareProvider_Medications (medical)
INSERT INTO MedCareProvider_Medications VALUES
	('2016-11-24', 'Allegra', '30mg', 'before bed'), 
	('2016-12-12', 'Tums', '4 tablets', 'after every meal')
	('2016-05-20', 'Spironolactone', '1 tablet', 'before bed'), 
	('2016-02-08', 'Growth supplements and vitamins', 'taken before bed'), 
	('2016-07-06', 'Allegra', '30 mg', 'taken in morning');

#Medical_Provider_Verification_Statement (medical)
INSERT INTO Medical_Provider_Verification_Statement VALUES
	('2016-11-24', 1, '2015-03-04', 'Dr. John Smith', '123 Georgia Tech Station', 'Atlanta', 'GA', 12345, 7701234567, 'No emergency contact'), 
	('2016-12-12', 1, '2015-04-11', 'Dr. Joe Tan', '123 ULM Station', 'Monroe', 'LA', 34567, 3184567890, 'Grandfather'), 
	('2016-05-20', 1, '2016-04-20', 'Dr. John Smith', '123 Georgia Tech Station', 'Atlanta', 'GA', 12345, 7701234567, 'Karla Osman'), 
	('2016-02-08', 1, '2016-01-30', 'Dr. Fang', '345 Cool St', 'Johns Creek', 'GA', 30022, 4045675566, 'Venus Goodman'), 
	('2016-07-06', 1, '2016-06-07', 'Dr. Locata', '367 Gucci Ct', 'Marietta', 'GA', 30062, 7708812345, 'Myla Lind');

#HIV_Provider (hiv)
INSERT INTO HIV_Provider VALUES
	('2016-11-24'), 
	('2016-12-12'), 
	('2016-05-20'), 
	('2016-02-08'), 
	('2016-07-06');

#Heatlh_History (hiv)
INSERT INTO Heatlh_History VALUES
	('2016-11-24', 'Appendix removed', 'Chronic Cough', 'Arthritis', 0, 'He complies pretty well'), 
	('2016-12-12', 'Tubes inserted in ears','ADD or ADHD', 'Weak arms', 1, 'She is rude and is not compliant'), 
	('2016-05-20', 'Tonsils removed', 'Other', 'Chronic Strep Throat', 0, 'She is calm'), 
	('2016-02-08', 'Nose reconstructed after being broken', 'Poor growth', 'Mental health problems', 1, 'She can be difficult to work with'), 
	('2016-07-06', 'Shoulder surgery to fix mobility problems', 'Chronic diarrhea', 'Chronic migranes', 0, 'He is not bothered by medical procedures');

#Lab_Data (hiv)
INSERT INTO Lab_Data VALUES
	('2016-11-24', '2015-10-31', 1345, 345, 23, 12345, '2016-01-20', 456, 2345, '2016-04-23', 567, 1234), 
	('2016-12-12', '2015-04-11', 3471, 347, 45, 7892, '2015-09-16', 347, 2342, '2016-02-14', 214, 1240), 
	('2016-05-20', '2015-05-28', 2345, 367, 34, 8909, '2015-09-29', 453, 2434, '2016-10-05', 432, 1078), 
	('2016-02-08', '2015-06-09', 2098, 387, 32, 9081, '2015-10-19', 398, 2561, '2016-01-20', 390, 1209), 
	('2016-07-06', '2016-02-16', 1999, 342, 29, 1067, '2016-03-17', 420, 2290, '2016-05-26', 479, 1197);

