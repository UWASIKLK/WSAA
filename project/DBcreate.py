import pymysql
from pymysql import Error
import dbconfig as cfg

#trying connection to MySQL database
try:
    print("Connecting to MySQL...")

    db = pymysql.connect(
        host= cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password']
    )

#once connected, will create database if doesn't exist, if exist already will confirm.
    print("Connected!")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS clinic")
    print("Database 'clinic' created or already exists.")
    cursor.close()
    db.close()

except Error as e:
    print("Error:", e)
