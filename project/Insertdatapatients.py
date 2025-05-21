import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database= "clinic"  
)

cursor = db.cursor()
sql=""" INSERT INTO patients ( patientID, firstname, surname, dob, address, city, county, eir_code, phone, email, doctorID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

values =("3","Hellen","Morris","1983-07-11","145 Willow Way","Naas", "Co Dublin","D02T452","083526410","helenM@gmail.com","1")

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()