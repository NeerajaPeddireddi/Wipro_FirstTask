import requests
import pytest

def test_getPatients(base_url):
    response = requests.get(f"{base_url}/api/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
# Parametrization
@pytest.mark.parametrize("patient",[
    {
        "name":"ram",
        "age":20,
        "gender":"male",
        "contact": "9999999999",
        "disease": "Fever",
        "doctor": "Dr. Reddy"
    },
{
        "name": "Rahul",
        "age": 45,
        "gender": "Male",
        "contact": "8888888888",
        "disease": "BP",
        "doctor": "Dr. Sharma"
    }
])
def test_addPatient(base_url, patient):
    response = requests.post(
        f"{base_url}/api/patients",
        json=patient,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 201
    # JSON deserialization-->Converts json to python object
    # Accessing values using dict keys
    assert response.json()["name"] == patient["name"]

# Handling negative test cases
@pytest.mark.xfail
def test_invalid_patient(base_url):
    response = requests.post(f"{base_url}/api/patients",json={})
    assert response.status_code == 400

@pytest.mark.skip(reason="Feature not implemented yet")
def test_update_patient():
    pass
