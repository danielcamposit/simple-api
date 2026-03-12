from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Daniel"},
    {"id": 2, "name": "Maria"}
]

@app.route("/")
def home():
    return "Simple API is running"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"})

@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user)

if __name__ == "__main__":
    app.run(debug=True)