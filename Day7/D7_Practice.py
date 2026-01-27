#Taking a website apis as reference Restfulapi-dev url from that taking all get,post,put,delete api and checked that using postman
from flask import Flask,request,jsonify

app=Flask(__name__)

users=[
    {
        "id": 1,
        "name": "beem"
    },
    {
        "id": 2,
        "name": "ram"
    },
    {
        "id": 3,
        "name": "Dee"
    }
]
@app.route("/",methods=["GET"])
def home():
    return "Welcome to Flask API"

@app.route("/users",methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>",methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error":"user not found"}),404
    return jsonify(users)
@app.route("/users",methods=["POST"])
def post_user():
    data=request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    new_user = {
        "id":(len(users))+1,
        "name":data.get("name"),
    }
    users.append(new_user)
    return jsonify(new_user),201

@app.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    data=request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name")
            return jsonify(user)
    return jsonify({"error":"user not found"}),404
@app.route("/users/<int:user_id>", methods=["PATCH"])
def update_user_patch(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            if "name" in data:
                user["name"] = data["name"]
            return jsonify(user), 200
    return jsonify({"error": "user not found"}), 404



@app.route("/users/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error":"user not found"}),404@app.route("/users/<int:user_id>", methods=["PATCH"])
# def patch_user(user_id):
#     data = request.get_json()
#     for user in users:
#         if user["id"] == user_id:
#             user.update(data)
#             return jsonify(user), 200
#     return jsonify({"error": "User not found"}), 404



if __name__=="__main__":
    app.run(debug=True)
