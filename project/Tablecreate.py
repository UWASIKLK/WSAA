# Python script to which will created doctor and patients table.

import pymysql
from pymysql import Error
import dbconfig as cfg

try:
    db = pymysql.connect(
    host= cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password']
)

    cursor = db.cursor()

    sql_doctor = """
        CREATE TABLE IF NOT EXISTS doctor (
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

    sql_patient = """
        CREATE TABLE IF NOT EXISTS patients (
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

    print("Tables 'doctor' and 'patients' created (or already exist).")

except Error as e:
    print("Error while creating tables:", e)

cursor.close()
db.close()
