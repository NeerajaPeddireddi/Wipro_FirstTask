#Working with Web & APIs
import requests
get_all_url="https://api.restful-api.dev/objects"
get_all_response=requests.get(get_all_url)
print(get_all_response.status_code)
print(get_all_response.json())

get_one_url="https://api.restful-api.dev/objects/1"
get_one_response=requests.get(get_one_url)
print(get_one_response.status_code)
print(get_one_response.json())

get_list_by_id_url="https://api.restful-api.dev/objects?id=3&id=5&id=10"
get_list_by_id_response=requests.get(get_list_by_id_url)
print(get_list_by_id_response.status_code)
print(get_list_by_id_response.json())

#Post
post_url="https://api.restful-api.dev/objects"
body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
r1=requests.post(post_url,json=body1)
print(r1.status_code)
print(r1.json())
#
#put
put_url="https://api.restful-api.dev/objects/ff8081819782e69e019be3f975e12de0"
body2={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
r2=requests.put(put_url,json=body2)
print(r2.status_code)
print(r2.json())

#patch
patch_url="https://api.restful-api.dev/objects/ff8081819782e69e019be3f975e12de0"
body3={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}
r3=requests.patch(patch_url,json=body3)
print(r3.status_code)
print(r3.json())

#Delete
delete_url="https://api.restful-api.dev/objects/ff8081819782e69e019be3f975e12de0"
r4=requests.delete(delete_url)
print(r4.status_code)
print(r4.json())

# Using Flask server running locally  taking api
import requests
get_url="http://127.0.0.1:5000"
response=requests.get(get_url)
print(response.text)

get_all_users_url="http://127.0.0.1:5000/users"
r1=requests.get(get_all_users_url)
print(r1.status_code)
print(r1.json())

get_single_user_url="http://127.0.0.1:5000/users/1"
r2=requests.get(get_single_user_url)
print(r2.status_code)
print(r2.json())

post_user_url="http://127.0.0.1:5000/users"
body1={"name":"Lee"}
r3=requests.post(post_user_url,json=body1)
print(r3.status_code)
print(r3.json())

put_user_url="http://127.0.0.1:5000/users/4"
body2={"name":"sid"}
r4=requests.put(put_user_url,json=body2)
print(r4.status_code)
print(r4.json())

patch_user_url="http://127.0.0.1:5000/users/4"
body3={"name":"Lee"}
r5=requests.patch(patch_user_url,json=body3)
print(r5.status_code)
print(r5.json())

delete_user_url="http://127.0.0.1:5000/users/4"
r=requests.delete(delete_user_url)
print(r.status_code)
print(r.json())

# -----Output------
# Welcome to Flask API
# 200
# [{'id': 1, 'name': 'beem'}, {'id': 2, 'name': 'ram'}, {'id': 3, 'name': 'Dee'}]
# 200
# {'id': 1, 'name': 'beem'}
# 201
# {'id': 4, 'name': 'Lee'}
# 200
# {'id': 4, 'name': 'sid'}
# 200
# {'id': 4, 'name': 'Lee'}
# 200
# {'message': 'User deleted successfully'}


#--------------Presenation file-----------
import json

from flask import Flask, request, jsonify

# with open("Users.json", "r") as file:

#     users_data = json.load(file)

users_data = [

    {

        "id": 1,

        "name": "Alice Johnson",

        "email": "alice.j@example.com",

        "role": "Admin",

        "active": "True"

    },

    {

        "id": 2,

        "name": "Bob Smith",

        "email": "bob.smith@example.com",

        "role": "User",

        "active": "True"

    },

    {

        "id": 3,

        "name": "Charlie Davis",

        "email": "charlie.d@example.com",

        "role": "User",

        "active": "False"

    },

    {

        "id": 4,

        "name": "Diana Prince",

        "email": "diana.p@example.com",

        "role": "Moderator",

        "active": "True"

    },

    {

        "id": 5,

        "name": "Ethan Hunt",

        "email": "ethan.h@example.com",

        "role": "User",

        "active": "True"

    }

]

app = Flask(__name__)

app.json.sort_keys = False


@app.route("/", methods=["GET"])
def health():
    try:

        return jsonify({

            "Status": "UP",

            "Status": "Flask server is running"

        }), 200

    except Exception as e:

        return jsonify({

            "Message": "Internal server error",

            "error": str(e)

        }), 500


@app.route("/users", methods=["GET"])
def getUsers():
    try:

        print(request.headers)

        if not users_data or len(users_data) == 0:
            return jsonify({

                "message": "No users found"

            }), 200

        return jsonify({

            "message": "Users fetched successfully",

            "data": users_data

        }), 200

    except Exception as e:

        return jsonify({

            "message": "internal server error",

            "error": str(e)

        }), 500


if __name__ == "__main__":
    app.run('0.0.0.0', port=5001, debug=True)

import requests, json

server_url = "http://127.0.0.1:5001"
users_url = "http://127.0.0.1:5001/users"

customHeader = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Client"
}

server_status = requests.get(server_url, headers=customHeader)
print(server_status.status_code)
print(server_status.json())

user_data = requests.get(users_url, customHeader)
print(user_data.status_code)
response_data = user_data.json()
print(response_data['data'])
print(response_data['message'])
try:
    with open("userdump.json", 'w') as file:
        json.dump(response_data['data'], file, indent=4)

except Exception as e:
    print(f"error dumping data into file: {str(e)}")





