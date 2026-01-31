import requests

from Day8.D8_Practice import body1

get_url="http://127.0.0.1:5000/users"
get_response=requests.get(get_url)
print(get_response.json())

body1={
    "name": "Anjali",
}
post_url="http://127.0.0.1:5000/users"
post_response=requests.post(post_url,json=body1)
print(post_response.json())
print(post_response.status_code)