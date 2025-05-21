import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="root"  
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS clinic")

cursor.close()
db.close()

print("Database 'clinic' created or already exists.")
