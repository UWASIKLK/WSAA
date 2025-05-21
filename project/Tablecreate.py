import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database= "clinic")

cursor = db.cursor()

sql_doctor = """
    CREATE TABLE doctor (
        doctorID INTEGER AUTO_INCREMENT,
        firstname VARCHAR(50) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        specialization VARCHAR(100),
        phone VARCHAR(25),
        email VARCHAR(50),
        PRIMARY KEY (doctorID)
    )
"""
cursor.execute(sql_doctor)

# Create the patient table
sql_patient = """
    CREATE TABLE patients (
        patientID INTEGER AUTO_INCREMENT,
        firstname VARCHAR(50) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        dob DATE NOT NULL,
        address VARCHAR(100), 
        city VARCHAR(50),
        county VARCHAR(50),
        eir_code VARCHAR(10),
        phone VARCHAR(25),
        email VARCHAR(50),
        doctorID INTEGER,
        PRIMARY KEY (patientID),
        FOREIGN KEY (doctorID) REFERENCES doctor(doctorID)
    )
"""
cursor.execute(sql_patient)

# Close the connection
cursor.close()
db.close()

print("Tables 'doctor' and 'patients' created successfully.")