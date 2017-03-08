/*
  Delete and recreate the database, set the current database to AllianceDb
*/

DROP DATABASE IF EXISTS HERO;
CREATE DATABASE HERO;
USE HERO;

SELECT 'BEGINNING OF SCRIPT'; # Select statements are placed throughout the script and act as a sort of print statement



--Child
DROP TABLE IF EXISTS Child;

CREATE TABLE Child (
	ID MEDIUMINT NOT NULL AUTO_INCREMENT,

	PRIMARY KEY (ID));

/******************************************************************************************************************************************************/

--Child -> Child App
DROP TABLE IF EXISTS Child_Application;

CREATE TABLE Child_Application (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Signeture TINYINT(1),
	Referral SET('Food','Transitional Housing/Shelter',
		'Rent/Utilities Assistance', 'Clothing/Furniture', 'Financial/Public Assistance', 'Other') DEFAULT NULL,
	Referral_Other VARCHAR(30),
	Future_Programs SET('Healthy HEROs', 'Career Development/Job Readiness', 'Other'),
	Future_Other VARCHAR(30),
	HERO_Programs SET('Super HEROes Program', 'Bright HEROs Program', 
		'Camp High Five', 'Holiday of HEROs', 'Transition to Adulthood'),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID), REFERENCES Child(ID) ON DELETE CASCADE );

/******************************************************************************************************************************************************/

SELECT 'CHILD APP'

--
-- Child -> Child Application -> Child's Information
--
CREATE TABLE Childs_Information (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Name_First VARCHAR(30),
  Name_Last VARCHAR(30),
  Name_Nickname VARCHAR(30),
  
  Address_Street VARCHAR(50),
  Address_City VARCHAR(20),
  Address_County VARCHAR(20)
  Address_Zip INT(5),
  
  Home_Phone INT(10),
  Guardian_Phone INT(10),
  Guardian_Email VARCHAR(50),
  
  Birthday DATE,
  Gender ENUM('Male','Female'),
  
  HIV_Status ENUM('HIV Positive','HIV Negative'),
  Aware TINYINT(1),
  Why VARCHAR(100),
  Refferal_Source VARCHAR(70),

  School_attending VARCHAR(50),
  School_grade_level VARCHAR(12),

  Ethnicity ENUM('White/Caucasian','Black/African-American','Hispanic/Latino',
    'Native American','Asian/Pacific Islander/Indian Sub-Continent','Multi-racial','Other'),
  Other VARCHAR(30),

  ADD_ADHD TINYINT(1),
  Learning_Disability TINYINT(1),
  Developmental_Disability TINYINT(1),
  Mental_Health_Issues TINYINT(1),
  Other_Medical_Condition TINYINT(1),
  Victim_of_Abuse TINYINT(1),
  Criminal_Justice_System TINYINT(1),
  Legal_Custody ENUM('Mother','Father','Both Parents','Aunt/Uncle','Grandparent','Pending Court Action','Other'),
  Other VARCHAR(50),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


--
-- Child -> Child Application -> Parent/Guardian Information
--
CREATE TABLE Parent_Guardian_Information (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Name_First VARCHAR(30),
  Name_Last VARCHAR(30),
  Relationship_to_Child VARCHAR(30),
  Age INT,

  HIV_Status ENUM('HIV Positive','HIV Negative'),
  Adoptive_Parent ENUM('Yes','No','Not Applicable'),
  Marital_Status ENUM('Married','Single','Separated','Divorced','Widowed'),
  Education_Completed ENUM('HS','GED','Some College','Associates Degree','Bachelor Degree','Master Degree','Doctorate'),
  Employment_Status ENUM('Full-Time','Part-Time','Unemployed','Disability'),
  Employment_Company_Name VARCHAR(50),

  Address_Street VARCHAR(50),
  Address_City VARCHAR(20),
  Address_State CHAR(2),
  Address_Zip INT(5),

  WorkPhone INT(10),
  Email VARCHAR(50),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


--
-- Child -> Child Application -> Absent Parent Information
--
CREATE TABLE Absent_Parent_Information (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Name_First VARCHAR(30),
  Name_Last VARCHAR(30),
  Telephone INT(10),

  Address_Street VARCHAR(50),
  Address_City VARCHAR(20),
  Address_County VARCHAR(20)
  Address_Zip INT(5),

  HIV_Status ENUM('HIV Positive','HIV Negative','Unknown'),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );



--Chid -> Child App-> Statement of Understanding
DROP TABLE IF EXISTS Statement_Of_Understanding;

CREATE TABLE Statement_Of_Understanding (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Statement_One TINYINT(1),
	Statement_Two TINYINT(1),
	Statement_Three TINYINT(1),
	Statement_Four TINYINT(1),
	Statement_Five TINYINT(1),
	Statement_Six TINYINT(1),
	Statement_Seven TINYINT(1),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );

SELECT 'CAMPER APP'

--Child -> Camper App
DROP TABLE IF EXISTS Camp_Application;

CREATE TABLE Camp_Application (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID) REFERENCES Child(ID) ON DELETE CASCADE );

--Child -> Camper App -> Medical Care Provider -> Medical History
DROP TABLE IF EXISTS Medical_History;

CREATE TABLE Medical_History (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Management VARCHAR(MAX),
	Nutritional_Supplements TINYINT(1),
	Feeding_Care VARCHAR(MAX),
	Formula_Type VARCHAR(50),
	Formula_Enum ENUM('Oral', 'G-tube', 'N-G tube'),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );

--Child -> Camper App -> Medical Care Provider -> Medical History -> Current Diagnosis
DROP TABLE IF EXISTS Curr_Diagnosis;

CREATE TABLE Curr_Diagnosis (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,
	
	Diagnosis VARCHAR(50),

	PRIMARY KEY (ID, Date_Submitted, Diagnosis),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );

--Child -> Camper App -> Medical Care Provider -> Medical History -> Current Diagnosis
--if no allergies, their ID will not appear
DROP TABLE IF EXISTS Allergies_Reactions;

CREATE TABLE Allergies_Reactions (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,
	
	Type ENUM('Food' , 'Eedication', 'Environmental', 'Other'),
	Allergy VARCHAR(30),
	Reaction VARCHAR(250),

	PRIMARY KEY (ID, Date_Submitted, Allergy),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );

--Child -> Camper App -> Medical Care Provider -> Tuberculosis Screening
DROP TABLE IF EXISTS Tuberculosis_Screening;

CREATE TABLE Tuberculosis_Screening (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Type ENUM('Tuberculin Skin Test', 'Quantiferon Testing', 'Chest X-ray'),
	Date_Screened Date,
	Result VARCHAR(20),

	PRIMARY KEY (ID, Date_Submitted, Type),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );

# Child -> CampApp -> Medical Care Provider -> Medications
CREATE TABLE Medications (
  ID INT,
  Date_Submitted DATE,
  Medication_Name VARCHAR(100),
  Amount_Including_Dosage VARCHAR(100),
  Times_To_Give VARCHAR(100)
  PRIMARY KEY (ID, Date_Submitted, Medication_Name),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider (ID, Date_Submitted)
);

# Child -> CampApp -> Medical Care Provider -> Cognitive Development Level
CREATE TABLE Cognitive_Development_Level (
  ID INT,
  Date_Submitted DATE,
  Development_Level ENUM('Age Appropriate', 'Mild Delay', 'Moderate Delay', 'Severe Delay'),
  Other_Psychosocial_Information VARCHAR(MAX),
  PRIMARY KEY (ID, Date_Submitted),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider (ID, Date_Submitted)
);

-- Child -> Camper App -> Parent -> Medications
DROP TABLE IF EXISTS Medications;

CREATE TABLE Medications (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Medication VARCHAR(50),
	Amount VARCHAR(50),
	Time_Instruction VARCHAR(100),

	PRIMARY KEY (ID, Date_Submitted, Medication),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );

# Child -> CampApp -> Parent -> Demographic Information
CREATE TABLE Demographic_Information (
  ID INT,
  Date_Submitted DATE,
  First_Name VARCHAR(100),
  Last_Name VARCHAR(100),
  Middle_Initial VARCHAR(1),
  Date_Of_Birth DATE,
  Age INT, 
  Gender ENUM('Male', 'Female'),
  Race VARCHAR(100),
  Primary_Language VARCHAR(100),
  Address_Street VARCHAR(100),
  Address_City VARCHAR(100),
  Address_State VARCHAR(100),
  Address_Zip INT,
  Address_County VARCHAR(100),
  Cell_Number_Contact_Name VARCHAR(100),
  Cell_Number_Time VARCHAR(100),
  Cell_Number INT,
  Home_Number_Contact_Name VARCHAR(100),
  Home_Number_Time VARCHAR(100),
  Home_Number INT,
  Work_Number_Contact_Name VARCHAR(100),
  Work_Number_Time VARCHAR(100),
  Work_Number INT,
  Camper_Email VARCHAR(100),
  Parent_Email VARCHAR(100),
  Parent_Guardian_Name VARCHAR(100),
  Parent_Guardian_Relationship_With_Camper VARCHAR(100),
  Last_Grade_Completed INT,
  Taking_Special_Ed_Classes TINYINT(1),
  Has_Siblings_Applying_For_Camp TINYINT(1),
  T_Shirt_Size ENUM('Youth S', 'Youth M', 'Youth L', 'Adult S', 'Adult M', 'Adult L', 'Adult XL', 'Adult XXL'),
  Planned_Transportation ENUM('Atlanta bus', 'Augusta bus', 'Albany bus', 'Athens bus', 'Savannah bus', 'Car/drop'),
  PRIMARY KEY (ID, Date_Submitted),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE
);

# Child -> CampApp -> Parent -> Medical_Care_Provider
CREATE TABLE Medical_Care_Provider (
  Child_ID INT,
  Camp_Application_Date_Submitted DATE,
  Provider_Name VARCHAR(100),
  Pharmacy_Name VARCHAR(100),
  Office_Phone_Number INT,
  Pharmacy_Phone_Number INT,
  Restrictions_And_Recommendations VARCHAR(MAX),
  PRIMARY KEY (ID, Date_Submitted),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent (ID, Date_Submitted) ON DELETE CASCADE
);

# Child -> CampApp -> Parent -> Emergency Contact
CREATE TABLE Emergency_Contact (
  ID INT,
  Date_Submitted DATE,
  Name VARCHAR(100),
  Relationship VARCHAR(100),
  Daytime_Phone_Number INT,
  Evening_Phone_Number INT,
  PRIMARY KEY (ID, Date_Submitted, Name),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent (ID, Date_Submitted) ON DELETE CASCADE
);


