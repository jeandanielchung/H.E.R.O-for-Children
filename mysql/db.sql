/*
  Delete and recreate the database, set the current database to AllianceDb
*/

DROP DATABASE IF EXISTS HERO;
CREATE DATABASE HERO;
USE HERO;

#User
DROP TABLE IF EXISTS User;

CREATE TABLE User (
  Name VARCHAR(60) NOT NULL,
  Username VARCHAR(25) NOT NULL,
  Password VARCHAR(40) NOT NULL, # needs to be 40 characters for SHA1 encryption
  User_Type ENUM('Administrator', 'Manager', 'Regular'),
  PRIMARY KEY (Username));

#Child
DROP TABLE IF EXISTS Child;

CREATE TABLE Child (
	ID MEDIUMINT NOT NULL AUTO_INCREMENT,

	PRIMARY KEY (ID));

/******************************************************************************************************************************************************/

#Child -> Child App
DROP TABLE IF EXISTS Child_Application;

CREATE TABLE Child_Application (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Signature TINYINT(1),

	Referral SET('Food','Transitional Housing/Shelter',
		'Rent/Utilities Assistance', 'Clothing/Furniture', 'Financial/Public Assistance', 'Other') DEFAULT NULL,
	Referral_Other VARCHAR(30),

	Future_Programs SET('Healthy HEROs', 'Career Development/Job Readiness', 'Other'),
	Future_Other VARCHAR(30),

	HERO_Programs SET('Super HEROes Program', 'Bright HEROs Program',
		'Camp High Five', 'Holiday of HEROs', 'Transition to Adulthood'),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID) REFERENCES Child(ID) ON DELETE CASCADE );

/******************************************************************************************************************************************************/

#
# Child -> Child Application -> Child's Information
#
CREATE TABLE Childs_Information (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Name_First VARCHAR(30),
  Name_Last VARCHAR(30),
  Name_Nickname VARCHAR(30),

  Address_Street VARCHAR(50),
  Address_City VARCHAR(30),
  Address_County VARCHAR(30),
  Address_Zip INT,

  Home_Phone CHAR(10),
  Guardian_Phone CHAR(10),
  Guardian_Email VARCHAR(70),

  Age INT,
  Birthday DATE,
  Gender ENUM('Male','Female'),

  HIV_Status ENUM('HIV Positive','HIV Negative'),
  Aware TINYINT(1),
  Why VARCHAR(100),
  Referral_Source VARCHAR(70),

  School_attending VARCHAR(50),
  School_grade_level VARCHAR(12),

  Ethnicity ENUM('White/Caucasian','Black/African-American','Hispanic/Latino',
    'Native American','Asian/Pacific Islander/Indian Sub-Continent','Multi-racial','Other'),
  Ethnicity_Other VARCHAR(30),

  ADD_ADHD TINYINT(1),
  Learning_Disability TINYINT(1),
  Developmental_Disability TINYINT(1),
  Mental_Health_Issues TINYINT(1),
  Other_Medical_Condition TINYINT(1),
  Victim_of_Abuse TINYINT(1),
  Criminal_Justice_System TINYINT(1),
  Legal_Custody ENUM('Mother','Father','Both Parents','Aunt/Uncle','Grandparent','Pending Court Action','Other'),
  Custody_Other VARCHAR(50),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Child Application -> Parent/Guardian Information
#
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
  Address_City VARCHAR(30),
  Address_State CHAR(2),
  Address_Zip INT,

  WorkPhone CHAR(10),
  Email VARCHAR(70),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Child Application -> Absent Parent Information
#
CREATE TABLE Absent_Parent_Information (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Name_First VARCHAR(30),
  Name_Last VARCHAR(30),
  Telephone CHAR(10),

  Address_Street VARCHAR(50),
  Address_City VARCHAR(30),
  Address_County VARCHAR(30),
  Address_Zip INT,

  HIV_Status ENUM('HIV Positive','HIV Negative','Unknown'),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Child Application -> Household Information
#
CREATE TABLE Household_Information (
  ID MEDIUMINT,
  Date_Submitted DATE,

# Count variable is to distinguish between which line
  Count INT,
  Name VARCHAR(60),






  Relationship VARCHAR(25),
  Sex ENUM('Male', 'Female'),
  Age INT,
  HIV_Status ENUM('HIV Positive','HIV Negative','Unknown'),

  PRIMARY KEY(ID, Date_Submitted, Count),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Child Application -> Household Information
#
CREATE TABLE Fam_Annual_Income (
	ID MEDIUMINT,
	Date_Submitted DATE,

	Fam_Annual_Income ENUM('$0-10,000','$10,001-15,000','$15,001-20,000','$20,000-25,000','$25,001-30,000','$30,001-35,000','$35,001-40,000','$40,001-45,000','$50,000+'),

    PRIMARY KEY(ID, Date_Submitted),
    FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Child Application -> Household Information
# Separate table bc multivaried attribute
#
CREATE TABLE Source_Fam_Income (
  ID MEDIUMINT,
	Date_Submitted DATE,

	Source_Fam_Income SET('Employment','Government Support','Public Assistance', 'Unemployment Benefits','Medicaid','Social Security','Veterans Benefits','Other'),
  Other VARCHAR(30),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


#
#Child -> Child Application -> In Case of Emergency Contact
#
CREATE TABLE ChildApp_Emergency_Contact (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Name_First VARCHAR(30),
  Name_Last VARCHAR (30),
  Relationship_to_Child VARCHAR(25),
  Address_Street VARCHAR(50),
  Address_City VARCHAR(30),
  Address_State CHAR(2),
  Address_Zip INT,

  Phone_Home CHAR(10),
  Phone_Cell CHAR(10),
  Phone_Alt CHAR(10),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Child_Application(ID, Date_Submitted) ON DELETE CASCADE );


#Chid -> Child App-> Statement of Understanding
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

/******************************************************************************************************************************************************/



#Child -> Camper App
DROP TABLE IF EXISTS Camp_Application;

CREATE TABLE Camp_Application (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID) REFERENCES Child(ID) ON DELETE CASCADE );

/******************************************************************************************************************************************************/


#
# Child -> Camper Application -> Parent
#
CREATE TABLE Parent(
  ID MEDIUMINT NOT NULL,
  Date_Submitted DATE,

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Camp_Application(ID, Date_Submitted) ON DELETE CASCADE );

/******************************************************************************************************************************************************/


#
# Child -> Camper Application -> Parent -> Demographic Information
#
CREATE TABLE Demographic_Information (
  ID MEDIUMINT,
  Date_Submitted DATE,

  First_Name VARCHAR(30),
  Last_Name VARCHAR(30),
  Middle_Initial CHAR(1),

  Date_Of_Birth DATE,
  Age INT,
  Gender ENUM('Male', 'Female'),
  Race VARCHAR(20),
  Primary_Language VARCHAR(20),

  Address_Street VARCHAR(50),
  Address_City VARCHAR(30),
  Address_State CHAR(2),
  Address_Zip INT,
  Address_County VARCHAR(30),

  Camper_Email VARCHAR(70),
  Parent_Email VARCHAR(70),

  Guardian_Name VARCHAR(60),
  Guardian_Camper_Relationship VARCHAR(100),
  Last_Grade_Completed INT,
  Special_Ed_Classes TINYINT(1),
  Siblings_Applying TINYINT(1),
  T_Shirt ENUM('Youth S', 'Youth M', 'Youth L', 'Adult S', 'Adult M', 'Adult L', 'Adult XL', 'Adult XXL'),
  Planned_Transportation SET('Atlanta bus', 'Augusta bus', 'Albany bus', 'Athens bus', 'Savannah bus', 'Car/drop'),
  PRIMARY KEY (ID, Date_Submitted),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> CampApp -> Parent -> Demographic Information -> Demographic Contacts
CREATE TABLE Demographic_Contacts (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Type ENUM('Cell', 'Home', 'Work'),
  Name VARCHAR(60),
  Time_Preference SET('Day', 'Evening'),
  Phone_Number CHAR(10),

  PRIMARY KEY (ID, Date_Submitted, Type),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Camper Application -> Parent -> Emergency Contact Info
#


CREATE TABLE Parent_Emergency_Contact (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Name VARCHAR(60),
  Relationship VARCHAR(100),
  Daytime_Phone CHAR(10),
  Evening_Phone CHAR(10),
  PRIMARY KEY (ID, Date_Submitted, Name),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent (ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Camper Application -> Parent -> Insurance Information
#
CREATE TABLE Insurance_Information(
  ID MEDIUMINT,
  Date_Submitted DATE,

  Type_of_Health_Insurance ENUM('Medicaid','PeachCare','Private','None'),
  Private_Insurance_Name VARCHAR(50),
  Policy_Number VARCHAR(30),
  Group_Number VARCHAR(30),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Camper Application -> Parent -> Medical Provider Information
#
CREATE TABLE Medical_Provider_Information (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Medical_Provider_Name VARCHAR(50),
  Phone_Office CHAR(10),
  Pharmacy_Name VARCHAR(50),
  Phone_Pharmacy CHAR(10),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Camper Application -> Parent -> Medical Information
#
CREATE TABLE Medical_Information(
  ID MEDIUMINT,
  Date_Submitted DATE,

  Current_Medical_Conditions SET('HIV','Hepatitis B','Hepatitis C','ADD or ADHD','Sickle Cell Disease','Asthma','Tubes in Ears','Heart Problems','Mental Health Diagnoses','Other'),
  Other VARCHAR(20),

  Medical_Condition_Explanation VARCHAR(500),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> Camp app -> Parent -> Allergies

CREATE TABLE Allergies (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Med_Allergy VARCHAR(20),
	Med_Reaction VARCHAR(100),
	Food_Allergy VARCHAR(20),
	Food_Reaction VARCHAR(100),
	Env_Allergy VARCHAR(20),
	Env_Reaction VARCHAR(100),

	EpiPen TINYINT(1),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Camper Application -> Parent -> Dietary Needs
#
CREATE TABLE Dietary_Needs(
  ID MEDIUMINT,
  Date_Submitted DATE,

  Special_Dietary_Needs TINYINT(1),
  Vegetarian TINYINT(1),
  Food_Restrictions VARCHAR(200),
  G_Tube ENUM('None','Medicine','Formula','Both'),
  Formula_Supplements ENUM('None','By Mouth','By G-Tube'),
  Formula_Type VARCHAR(30),
  Formula_Cans_Per_Day INT,
  Feeding_Pump TINYINT(1),
  Pump_Type VARCHAR(30),
  Feeding_Schedule VARCHAR(200),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Camper Application -> Parent -> General Health
#
CREATE TABLE General_Health(
  ID MEDIUMINT,
  Date_Submitted DATE,

  Physical_Limitations SET('Dressing','Showering','Eating','Toileting','Walking/Balance','Braces','Casts','Walker','Wheelchair','Other'),
  Other VARCHAR(50),

  Tire_Easily TINYINT(1),
  Swim TINYINT(1),
  Chicken_Pox TINYINT(1),
  Chicken_Pox_Date VARCHAR(20),

# this section is for females only
  Menstrual_Cycle TINYINT(1),
  Menstrual_Difficulties VARCHAR(300),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> Camp app -> Parent -> Pyschosocial and Behavioral Information

CREATE TABLE Pyschosocial_and_Behavioral_info (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Camper_Knows TINYINT(1),
	Time_Camper_Known ENUM('less than 6 months', 'less than 1 year', 'a few years', 'always'),
	Camper_Experiences SET('Anxiety', 'Fear of dark', 'Homesickness', 'Sleeps with night light', 'Fights easily',
		'School suspension due to behavior', 'Bedwetting', 'Sleeps with comfort item', 'Hyperactivity or problems with attention',
		'History of trauma or sexual abuse'),
	Med_Hyper_AttentionProb TINYINT(1),
	Explanation VARCHAR(600),
	Camper_Interests SET('Reading', 'Music', 'Swimming', 'Dance', 'Sports', 'Arts/Crafts', 'Fishing', 'Boating',
		'Archery', 'Golf', 'Bicycling', 'Animals', 'Nature'),
	Recent_Major_Events VARCHAR(500),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


# Child -> Camper App -> Parent -> Medications
DROP TABLE IF EXISTS Medications;

CREATE TABLE Parent_Medications (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Medication VARCHAR(50),
	Amount VARCHAR(50),
	Time_Instruction VARCHAR(100),

	PRIMARY KEY (ID, Date_Submitted, Medication),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> Camp app -> Parent -> Camp high five release forms signed

CREATE TABLE Release_Forms_Signed (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Parent_Camper_Contract TINYINT(1),
	Partcipation_Consent_Liability_Release TINYINT(1),
	Media_Release TINYINT(1),
	Camper_HIV_Education TINYINT(1),
	Camp_Twin_Lakes_Rules TINYINT(1),
	Parental_Consent_and_Release TINYINT(1),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Parent(ID, Date_Submitted) ON DELETE CASCADE );

/******************************************************************************************************************************************************/


#Child -> Camper App -> Medical Care Provider
CREATE TABLE Medical_Care_Provider (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Restrictions_And_Recommendations VARCHAR(1000),

  PRIMARY KEY (ID, Date_Submitted),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Camp_Application(ID, Date_Submitted) ON DELETE CASCADE );


/******************************************************************************************************************************************************/


#Child -> Camper App -> Medical Care Provider -> Medical History
DROP TABLE IF EXISTS Medical_History;

CREATE TABLE Medical_History (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Management VARCHAR(500),
	Nutritional_Supplements TINYINT(1),
	Feeding_Care VARCHAR(500),
	Formula_Type VARCHAR(50),
	Formula_Enum ENUM('Oral', 'G-tube', 'N-G tube'),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> Camper App -> Medical Care Provider -> Medical History -> Current Diagnosis
DROP TABLE IF EXISTS Curr_Diagnosis;

CREATE TABLE Med_Hist_Diagnosis (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Diagnosis VARCHAR(100),

	PRIMARY KEY (ID, Date_Submitted, Diagnosis),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );

#Child -> Camper App -> Medical Care Provider -> Medical History -> Current Diagnosis
#if no allergies, their ID will not appear
DROP TABLE IF EXISTS Allergies_Reactions;

CREATE TABLE Med_Hist_Allergies (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Type ENUM('Food' , 'Medication', 'Environmental', 'Other'),
	Allergy VARCHAR(30),
	Reaction VARCHAR(250),

	PRIMARY KEY (ID, Date_Submitted, Allergy),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );


#Child ->  Camp app -> medical care provider -> physical exam date
CREATE TABLE Physical_Exam (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Date_Completed DATE NOT NULL,
	Height VARCHAR(7),	# format #' ##''
	Weight INT,
	Pulse INT,
	Resperations INT,
	Blood_Pressure INT,
	HEENT VARCHAR(100),
	Skin VARCHAR(100),
	Cardiovascular VARCHAR(100),
	GU_GYN VARCHAR(100),
	Pulmonary VARCHAR(100),
	Glasses_HearingAids_PE VARCHAR(100),
	Abdomen VARCHAR(100),
	Lymph_Nodes VARCHAR(100),
	Extremities VARCHAR(100),
	Spine VARCHAR(100),
	Miscellaneous VARCHAR(500),
	Comments VARCHAR(500),


 PRIMARY KEY (ID, Date_Submitted),
 FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> Camper App -> Medical Care Provider -> Cognitive/ Development Level
CREATE TABLE Cognitive_Development_Level (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Development_Level ENUM('Age Appropriate', 'Mild Delay', 'Moderate Delay', 'Severe Delay'),
  Other_Psychosocial_Information VARCHAR(1000),

  PRIMARY KEY (ID, Date_Submitted),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> Camper App -> Medical Care Provider -> Immunization Record FILE I/O !!


#Child -> Camper App -> Medical Care Provider -> Tuberculosis Screening
DROP TABLE IF EXISTS Tuberculosis_Screening;

CREATE TABLE Tuberculosis_Screening (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Type ENUM('Tuberculin Skin Test', 'Quantiferon Testing', 'Chest X-ray'),
	Date_Screened Date,
	Result VARCHAR(70),

	PRIMARY KEY (ID, Date_Submitted, Type),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> Camper App -> Medical Care Provider -> Medications
CREATE TABLE MedCareProvider_Medications (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Medication_Name VARCHAR(100),
  Amount_Including_Dosage VARCHAR(100),
  Times_To_Give VARCHAR(100),

  PRIMARY KEY (ID, Date_Submitted, Medication_Name),
  FOREIGN KEY (ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );


#
# Child -> Camper Application -> Medical Provider -> Verification Statement
#
CREATE TABLE Medical_Provider_Verification_Statement (
  ID MEDIUMINT,
  Date_Submitted DATE,

  Signature TINYINT(1),
  Sig_Date DATE,
  Name VARCHAR(40),
  Address_Street VARCHAR(50),
  Address_City VARCHAR(30),
  Address_State CHAR(2),
  Address_Zip INT,
  Phone CHAR(10),
  Emergency_Contact VARCHAR(50),

  PRIMARY KEY(ID, Date_Submitted),
  FOREIGN KEY(ID, Date_Submitted) REFERENCES Medical_Care_Provider(ID, Date_Submitted) ON DELETE CASCADE );


/******************************************************************************************************************************************************/

#Child -> Camp App-> HIV Provider

CREATE TABLE HIV_Provider (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES Camp_Application(ID, Date_Submitted) ON DELETE CASCADE );

/******************************************************************************************************************************************************/


#Child -> Camp App -> HIV Provider -> heath history
CREATE TABLE Heatlh_History (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Major_Surgical_History VARCHAR(500),
	Health_History SET('HIV', 'Hepatitis B', 'Hepatitis C', 'Poor growth', 'Bleeding disorders', 'Asthma',
		'Pulmonary Disease', 'Chronic Cough', 'ADD or ADHD', 'Renal Disease', 'Sickle Cell disease', 'Congenital Heart Disease',
		'Hypertension', 'Cryptosporidium', 'Chronic diarrhea', 'Seizures', 'Diabetes', 'Other'),
	Other VARCHAR(20),
	History_of_Noncompliance TINYINT(1),
	Explanation VARCHAR(500),


	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES HIV_Provider(ID, Date_Submitted) ON DELETE CASCADE );


#Child -> Camp App ->HIV Provider -> Lab data
CREATE TABLE Lab_Data (
	ID MEDIUMINT NOT NULL,
	Date_Submitted DATE,

	Lab1_Date DATE,
	Lab1_WBC VARCHAR(6),
	Lab1_HGB VARCHAR(4),
	Lab1_HCT VARCHAR(3),
	Lab1_Plt_Count VARCHAR(6),

	Lab2_Date DATE,
	Lab2_CD4_Count VARCHAR(4),
	Lab2_Viral_Load VARCHAR(5),

	Lab3_Date DATE,
	Lab3_CD4_Count VARCHAR(4),
	Lab3_Viral_Load VARCHAR(5),

	PRIMARY KEY (ID, Date_Submitted),
	FOREIGN KEY (ID, Date_Submitted) REFERENCES HIV_Provider(ID, Date_Submitted) ON DELETE CASCADE );
