import requests
import pytest
def test_get_movies(base_url):
    try:
        response = requests.get(f"{base_url}/api/movies")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    except Exception as e:
        pytest.fail(f"Test failed due to exception: {e}")
def test_add_movie(base_url):
    data={
    "id":102,
    "duration": "3h 49m",
    "language": "Hindi",
    "movie_name": "Tare jameen par",
    "price": 250
    }
    response = requests.post(f"{base_url}/api/movies", json=data)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Tare jameen par"

@pytest.mark.parametrize("movie_id,status", [
    (101, 200),

])
def test_get_movie_by_id(base_url, movie_id, status):
    response = requests.get(f"{base_url}/api/movies/{movie_id}")
    assert response.status_code == status
