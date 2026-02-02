import requests

def test_book_ticket(base_url):
    data = {
        "movie_id": 101,
        "name":"arjun",
        "tickets": 2
    }
    response = requests.post(f"{base_url}/api/bookings", json=data)
    assert response.status_code == 201

def test_booking_failure(base_url):
    data = {
        "movie_id": 101,
        "tickets": 0
    }
    response = requests.post(f"{base_url}/api/bookings", json=data)
    assert response.status_code == 400
