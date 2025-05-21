import pymysql
from datetime import datetime
import dbconfig as cfg

class Clinic:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    port =      ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = pymysql.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def convertToDictionary(self, result):
        columns = ['patientID', 'firstname', 'surname', 'dob', 'address', 'city', 'county', 'eir_code', 'phone', 'email', 'doctorID']
        if result is None:
            return {}
        return dict(zip(columns, result))

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def getallpatient(self):
        cursor = self.getcursor()
        sql= "SELECT * FROM patients"
        cursor.execute(sql)
        results = cursor.fetchall()
        patientslist = []
        #print(results)
        for result in results:
          #print(result)
            patientslist.append(self.convertToDictionary(result))
        self.closeAll()
        return patientslist
    
    def getalldoctor(self):
        cursor = self.getcursor()
        sql= "SELECT * FROM doctor"
        cursor.execute(sql)
        results = cursor.fetchall()
        doctorlist = []
        #print(results)
        for result in results:
            #print(result)
                doctorlist.append(self.convertToDictionary(result))
        self.closeAll()
        return doctorlist

    def create(self, values):
        cursor = self.getcursor()
        sql="""INSERT INTO patients (firstname, surname, dob, address, city, county, eir_code, phone, email, doctorID) 
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        data=(
        values['firstname'], values['surname'], values['dob'], values['address'],
        values['city'], values['county'], values['eir_code'], values['phone'],
        values['email'], values['doctorID'])
        cursor.execute(sql, data)

        #cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def findByID(self, id):
        cursor = self.getcursor()
        sql="SELECT * FROM patients WHERE patientID = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()

        if result is None:
            return None
        
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.getcursor()

        sql="""UPDATE patients SET 
        firstname = %s,surname =%s, dob = %s, address = %s,  
        city = %s, county = %s, eir_code = %s, 
        phone = %s, email = %s, doctorID = %s  
        WHERE patientID = %s"""

        data=(
        values['firstname'], values['surname'], values['dob'], values['address'],
        values['city'], values['county'], values['eir_code'], values['phone'],
        values['email'], values['doctorID'], values['patientID'])
        cursor.execute(sql, data)

        self.connection.commit()
        if cursor.rowcount > 0:
            self.closeAll()
            return {'message': 'Patient updated successfully'}
        else:
            self.closeAll()
            return {'message': 'Patient not found'}, 404
       
        

    def delete(self, id):
        cursor = self.getcursor()
        sql1 = "SELECT firstname, surname FROM patients WHERE patientID= %s"
        values1 = (id,)
        cursor.execute(sql1,values1)
        selectedpatient = cursor.fetchone()
        #cursor.execute("SELECT firstname, surname FROM patient WHERE id= %s", (id,))
        #selectedpatient = cursor.fetchone()
        if selectedpatient:
            firstname, surname = selectedpatient
            sql="DELETE FROM patients WHERE patientID = %s"
            values = (id,)
            cursor.execute(sql, values)
            self.connection.commit() 
            print(f"Patient {firstname} {surname} (ID: {id}) has been deleted.")
        else:
            print(f"No patient found with ID: {id}")
        self.closeAll()


 
clinic = Clinic()
