import pymysql
from pymysql import Error

try:
    print("Connecting to MySQL...")

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="root"
    )

    print("Connected!")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS clinic")
    print("Database 'clinic' created or already exists.")
    cursor.close()
    db.close()

except Error as e:
    print("Error:", e)
