from flask import Flask,request,jsonify

app=Flask(__name__)

users=[
    {"id":1,
    "name":"John"},
    {
        "id":2,
        "name":"Doe"},
]

@app.route("/",methods=["GET"])
def home():
    return "This is home page"

@app.route("/users",methods=["GET"])
def get_users():
    return jsonify(users)
@app.route("/users/<int:user_id>",methods=["GET"])
def get_user(user_id):
    for user in  users:
        if user["id"] == user_id:
            return jsonify(user)
@app.route("/users",methods=["POST"])
def create_user():
    data=request.get_json()
    if not data or "name" not in data:
        return jsonify({"message":"Please provide a name"}),400
    new_user={"id":len(users)+1,
            "name":data.get("name")
    }
    users.append(new_user)
    return jsonify(new_user),201
@app.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    data=request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"]=data.get("name")
            return jsonify(user)
    return jsonify({"message":"User not found"}),404

@app.route("/users/<int:user_id>",methods=["PATCH"])
def patch_user(user_id):
    data=request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"]=data.get("name")
            return jsonify(user)
    return jsonify({"message":"User not found"}),404


@app.route("/users/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify(user)
    return jsonify({"message":"User not found"}),404

if __name__ == "__main__":
    app.run(debug=False)