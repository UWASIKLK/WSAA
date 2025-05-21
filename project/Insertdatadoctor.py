import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database= "clinic"  
)

cursor = db.cursor()
sql=""" INSERT INTO doctor ( doctorID, firstname, surname, specialization, phone, email) VALUES (%s,%s,%s,%s,%s,%s)"""

values =("3","Paul","Lynch","Consultant Neurology","0087452663","p.lynch@medfit.ie")

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()