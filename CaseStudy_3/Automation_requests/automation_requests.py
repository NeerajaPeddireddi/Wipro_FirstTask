import requests
get_patients_url="http://127.0.0.1:5000/api/patients"
get_patients_response=requests.get(get_patients_url)
print("Status Code:",get_patients_response.status_code)
print("Response JSON:",get_patients_response.json())

get_patient_url="http://127.0.0.1:5000/api/patients/1"
get_patient_response=requests.get(get_patient_url)
print("Status Code:",get_patient_response.status_code)
print("Response JSON:",get_patient_response.json())

post_url = "http://127.0.0.1:5000/api/patients"

headers = {
    "Content-Type": "application/json"
}

body = {
    "name": "Anita",
    "age": 30,
    "gender": "Female",
    "contact": "9999999999",
    "disease": "Fever",
    "doctor": "Dr. Reddy"
}

post_response = requests.post(
    post_url,
    json=body,
    headers=headers
)

print("Status Code:", post_response.status_code)
print("Created Patient:", post_response.json())

response_data = post_response.json()

if post_response.status_code == 201:
    print("Patient created successfully")

else:
    print("Patient creation failed"
# Negative Validation
invalid_body = {}

negative_response = requests.post(
    post_url,
    json=invalid_body,
    headers=headers
)
try:
    error_data = negative_response.json()
    print("Error Response:", error_data)
except ValueError:
    print("Error Response: No JSON body returned from server")