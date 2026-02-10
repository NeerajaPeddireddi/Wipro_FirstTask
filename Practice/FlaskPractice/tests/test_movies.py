import pytest
import requests


def test_get_movies(base_url):
    response=requests.get(f"{base_url}/api/movies")
    assert response.status_code == 200
def test_add_movie(base_url):
    body={
    "duration": "2h 49m",
    "language": "Hindi",
    "movie_name": "Dil bechara",
    "price": 260
}
    response=requests.post(f"{base_url}/api/movies",json=body)
    assert response.status_code == 201

def test_add_booking(base_url):
    body1={
    "movie_name": "Wak up sid",
    "name":"ram",
    "tickets":1
    }
    response=requests.post(f"{base_url}/api/bookings",json=body1)
    assert response.status_code == 201

def test_failure_booing(base_url):
    body2={
    "movie_name": "Wak up sid",
    }
    response=requests.post(f"{base_url}/api/bookings",json=body2)
    assert response.status_code == 400
