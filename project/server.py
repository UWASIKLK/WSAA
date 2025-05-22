from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from clinic import Clinic

clinic_instance = Clinic()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['CORS_HEADERS'] = 'Content-Type'

# Home route
@app.route('/')
def index():
    return "Welcome to the Clinic API."


## PATIENTS ##

# Route for serving HTML patients
@app.route('/patientsview')
def patients_view():
    return render_template("patients.html")

# GET all patients
@app.route('/api/patients', methods=['GET'])
def get_all_patients():
    patients = clinic_instance.getallpatient()  # Should return list of dicts
    return jsonify(patients)

# GET a single patient by ID
@app.route('/api/patients/<int:patientID>', methods=['GET'])
def get_patient_by_id(patientID):
    result = clinic_instance.findByIDpatient(patientID)
    if result is None:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(result)

# Create a new patient
@app.route('/api/patients', methods=['POST'])
def create_patient():
    patient = request.get_json()
    return jsonify(clinic_instance.createpatient(patient))

# Update an existing patient
@app.route('/api/patients/<int:patientID>', methods=['PUT'])
def update_patient(patientID):
    patient = request.get_json()
    patient["patientID"] = patientID  # Add ID to the payload
    return jsonify(clinic_instance.updatepatient(patient))

#Delete a patient
@app.route('/api/patients/<int:patientID>', methods=['DELETE'])
def delete_patient(patientID):
    return jsonify(clinic_instance.deletepatient(patientID))


## DOCTOR ##

# Route for serving HTML doctor
@app.route('/doctorview')
def doctor_view():
    return render_template("doctor.html")

# GET all doctors
@app.route('/api/doctor', methods=['GET'])
def get_all_doctor():
    doctors = clinic_instance.getalldoctor()  # Should return list of dicts
    return jsonify(doctors)

# GET a single doctor by ID
@app.route('/api/doctor/<int:doctorID>', methods=['GET'])
def get_doctor_by_id(doctorID):
    result = clinic_instance.findByIDdoctor(doctorID)
    if result is None:
        return jsonify({"error": "Doctor not found"}), 404
    return jsonify(result)

# Create a new doctor
@app.route('/api/doctor', methods=['POST'])
def create_doctor():
    newdoctor = request.get_json()
    return jsonify(clinic_instance.createdoctor(newdoctor))

# Update an existing doctor
@app.route('/api/doctor/<int:doctorID>', methods=['PUT'])
def update_doctor(doctorID):
    updoctor = request.get_json()
    updoctor["doctorID"] = doctorID  # Add ID to the payload
    return jsonify(clinic_instance.updatedoctor(updoctor))

#Delete a doctor
@app.route('/api/doctor/<int:doctorID>', methods=['DELETE'])
def delete_doctor(doctorID):
    return jsonify(clinic_instance.deletedoctor(doctorID))

if __name__ == "__main__":
    app.run(debug=True)
