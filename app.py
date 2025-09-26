from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory user store
users = {}

# Home route (renders HTML)
@app.route('/')
def home():
    return render_template("index.html", users=users)

# API Endpoints
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"message": "User created", "user_id": user_id}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id].update(data)
    return jsonify({"message": "User updated", "user_id": user_id})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted", "user_id": user_id})

if __name__ == "__main__":
    app.run(debug=True)
