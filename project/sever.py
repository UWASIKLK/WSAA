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

## Patients ##

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
    result = clinic_instance.findByID(patientID)
    if result is None:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(result)

# Create a new patient
@app.route('/api/patients', methods=['POST'])
def create_patient():
    patient = request.get_json()
    return jsonify(clinic_instance.create(patient))

# Update an existing patient
@app.route('/api/patients/<int:patientID>', methods=['PUT'])
def update_patient(patientID):
    patient = request.get_json()
    patient["patientID"] = patientID  # Add ID to the payload
    return jsonify(clinic_instance.update(patient))

#Delete a patient
@app.route('/api/patients/<int:patientID>', methods=['DELETE'])
def delete_patient(patientID):
    return jsonify(clinic_instance.delete(patientID))


## Doctor ##

# Route for serving HTML doctor
@app.route('/doctorview')
def doctor_view():
    return render_template("doctor.html")

# GET all patients
@app.route('/api/patients', methods=['GET'])
def get_all_patients():
    patients = clinic_instance.getallpatient()  # Should return list of dicts
    return jsonify(patients)

# GET a single patient by ID
@app.route('/api/patients/<int:patientID>', methods=['GET'])
def get_patient_by_id(patientID):
    result = clinic_instance.findByID(patientID)
    if result is None:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(result)

# Create a new patient
@app.route('/api/patients', methods=['POST'])
def create_patient():
    patient = request.get_json()
    return jsonify(clinic_instance.create(patient))

# Update an existing patient
@app.route('/api/patients/<int:patientID>', methods=['PUT'])
def update_patient(patientID):
    patient = request.get_json()
    patient["patientID"] = patientID  # Add ID to the payload
    return jsonify(clinic_instance.update(patient))

#Delete a patient
@app.route('/api/patients/<int:patientID>', methods=['DELETE'])
def delete_patient(patientID):
    return jsonify(clinic_instance.delete(patientID))

if __name__ == "__main__":
    app.run(debug=True)
