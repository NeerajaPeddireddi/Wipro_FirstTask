from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
patients = [
    {
        "id": 1,
        "name": "Ravi Kumar",
        "age": 35,
        "gender": "Male",
        "contact": "9876543210",
        "disease": "Diabetes",
        "doctor": "Dr. Sharma"
    }
]
@app.route('/')
def home():
    return render_template("register.html")

# GET all patients
@app.route("/api/patients",methods=['GET'])
def getPatients():
    return jsonify(patients)
@app.route("/api/patients/<int:patient_id>",methods=['GET'])
def getPatient(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return jsonify(patient)
    return "Patient not found",404
@app.route("/api/patients",methods=['POST'])
def addPatient():
    if request.is_json:
        data = request.get_json()  # API / Pytest / Postman
    else:
        data = request.form.to_dict()  # HTML form submission
    if not data or "name" not in data or "age" not in data or "gender" not in data or "contact" not in data:
        return "Please provide details",404
    new_patient={
        "id": len(patients) + 1,
        "name": data["name"],
        "age": data["age"],
        "gender": data["gender"],
        "contact": data["contact"],
        "doctor": data["doctor"]
    }
    patients.append(new_patient)
    return jsonify({
        "message": "Patient added successfully",
        "patient": new_patient
    }), 201
@app.route("/api/patients/<int:patient_id>",methods=['PUT'])
def updatePatient(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            patient.update(request.json)
            return jsonify(patient),200
    return "Patient not found",404


if __name__ == '__main__':
    app.run(debug=True)