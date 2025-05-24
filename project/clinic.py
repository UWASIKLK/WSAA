import pymysql
import dbconfig as cfg

'''I had to use the PyMySQL connector instead of Anaconda's MySQL connector 
(mysql.connector.connect()) because a simple Python script (create database) was crashing silently and 
without throwing an exception, the problem could have been caused by an 
incompatibility in my Anaconda environment. I spent 3 days trying to solve this problem, 
but without the help of ChatGPT, I couldn't move on.'''

# This is a data object class to connect with the database.
class Clinic:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    port =      ''
    database=   ''
    
    # Reads and initializes database credentials from the config file
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    # Setting up connection with database and returns cursor.
    def getcursor(self): 
        self.connection = pymysql.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    # This will generates a dictionary from the results of a query to the patient table.
    def convertToDictionarypatients(self, result):
        columns = ['patientID', 'firstname', 'surname', 'dob', 'address', 'city', 'county', 'eir_code', 'phone', 'email', 'doctorID']
        if result is None:
            return {}
        return dict(zip(columns, result))
    
    # This will generates a dictionary from the results of a query to the doctor table.
    def convertToDictionarydoctor(self, result):
        columns = ['doctorID', 'firstname', 'surname', 'specialization', 'phone', 'email']
        if result is None:
            return {}
        return dict(zip(columns, result))

    # Closing off connection with database and cursor.
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    # Will return all the patients details from database.
    def getallpatient(self):
        cursor = self.getcursor()
        sql= "SELECT * FROM patients"
        cursor.execute(sql)
        results = cursor.fetchall()
        patientslist = []
        
        for result in results:
         
            patientslist.append(self.convertToDictionarypatients(result))
        self.closeAll()
        return patientslist
    
    # Will return all the doctors details from database.
    def getalldoctor(self):
        cursor = self.getcursor()
        sql= "SELECT * FROM doctor"
        cursor.execute(sql)
        results = cursor.fetchall()
        doctorlist = []
        
        for result in results:
            
                doctorlist.append(self.convertToDictionarydoctor(result))
        self.closeAll()
        return doctorlist

    # This will create new patient and insert details to the patient table.
    def createpatient(self, values):
        cursor = self.getcursor()
        sql="""INSERT INTO patients (firstname, surname, dob, address, city, county, eir_code, phone, email, doctorID) 
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        data=(
        values['firstname'], values['surname'], values['dob'], values['address'],
        values['city'], values['county'], values['eir_code'], values['phone'],
        values['email'], values['doctorID'])
        cursor.execute(sql, data)

        
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    # This will create new doctor and insert details to the doctor table.
    def createdoctor(self, values):
        cursor = self.getcursor()
        sql="""INSERT INTO doctor (firstname, surname, specialization, phone, email) 
        values (%s,%s,%s,%s,%s)"""
        
        data=(
        values['firstname'], values['surname'], values['specialization'], 
        values['phone'], values['email'])
        cursor.execute(sql, data)
        
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    # Will get details of the patient by patient ID.
    def findByIDpatient(self, id):
        cursor = self.getcursor()
        sql="SELECT * FROM patients WHERE patientID = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()

        if result is None:
            return None
        
        return self.convertToDictionarypatients(result)
    
    # Will get details of the doctor by doctor ID.
    def findByIDdoctor(self, id):
        cursor = self.getcursor()
        sql="SELECT * FROM doctor WHERE doctorID = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        if result is None:
         return None
    
        return self.convertToDictionarydoctor(result)

    # This will update existing patient details.
    def updatepatient(self, values):
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

    # This will update existing doctor details.   
    def updatedoctor(self, values):
        cursor = self.getcursor()
        
        sql="""UPDATE doctor SET 
        firstname = %s,surname =%s, specialization =%s,         
        phone = %s, email = %s  
        WHERE doctorID = %s"""
        data=(
        values['firstname'], values['surname'], values['specialization'], 
        values['phone'], values['email'], values['doctorID'])
        cursor.execute(sql, data)
        
        self.connection.commit()
        if cursor.rowcount > 0:
            self.closeAll()
            return {'message': 'Doctor updated successfully'}
        
        else:
            self.closeAll()
            return {'message': 'Doctor not found'}, 404
       
    # This will delete patient.
    def deletepatient(self, id):
        cursor = self.getcursor()
        sql1 = "SELECT firstname, surname FROM patients WHERE patientID= %s"
        values1 = (id,)
        cursor.execute(sql1,values1)
        selectedpatient = cursor.fetchone()
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

    # This will delete doctor.
    def deletedoctor(self, id):
        cursor = self.getcursor()
        sql1 = "SELECT firstname, surname FROM doctor WHERE doctorID= %s"
        values1 = (id,)
        cursor.execute(sql1,values1)
        selecteddoctor = cursor.fetchone()
        if selecteddoctor:
            firstname, surname = selecteddoctor
            sql="DELETE FROM doctor WHERE doctorID = %s"
            values = (id,)
            cursor.execute(sql, values)
            self.connection.commit() 
            print(f"Doctor {firstname} {surname} (ID: {id}) has been deleted.")
        else:
            print(f"No doctor found with ID: {id}")
        self.closeAll()
 
clinic = Clinic()
