# Python script to insert one record to the doctor's table.

import pymysql
import dbconfig as cfg

db = pymysql.connect(
    host= cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password']
    database= cfg.mysql['database'] 
)

cursor = db.cursor()
sql=""" INSERT INTO doctor ( doctorID, firstname, surname, specialization, phone, email) VALUES (%s,%s,%s,%s,%s,%s)"""

values =("3","Paul","Lynch","Consultant Neurology","0087452663","p.lynch@medfit.ie")

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()