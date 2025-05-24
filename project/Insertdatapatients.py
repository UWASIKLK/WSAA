# Python script to insert one record to the patient's table.

import pymysql
import dbconfig as cfg

db = pymysql.connect(
    host= cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database= cfg.mysql['database'] 
)

cursor = db.cursor()
sql=""" INSERT INTO patients ( patientID, firstname, surname, dob, address, city, county, eir_code, phone, email, doctorID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

values =("11","Trevor","Cuffe","1875-07-11","63 Hollywell","Greystones", "Co Wicklow","G45M122","08545310","trevor.cuffe@gmail.com","2")

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()