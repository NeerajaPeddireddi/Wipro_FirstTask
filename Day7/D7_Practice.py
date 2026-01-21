#Simple message printing creating api using flask api
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to Flask API"

if __name__ == '__main__':
    app.run(debug=True)

#Get users and get single user
from flask import Flask,request,jsonify

app= Flask(__name__)

users=[
    {
        "id":1,
        "name":"John",
    },
    {
        "id":2,
        "name":"Doe", }

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


# if __name__ == '__main__':
#     app.run(debug=True)
