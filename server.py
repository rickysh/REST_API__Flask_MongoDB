from bson import ObjectId
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb+srv://<username>:<password>@cluster0.kuewrfz.mongodb.net/')
db = client['rest_db']
collection = db['rest_col_1']

# GET all documents
@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in collection.find():
        # Convert ObjectId to string for JSON serialization
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users), 200

# GET single document by ID
@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        # Convert ObjectId to string for JSON serialization
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found'}), 404

# POST new document
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = collection.insert_one(data).inserted_id
    return jsonify({'message': 'User created', 'user_id': str(user_id)}), 201

# PUT update document by ID
@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    result = collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'User updated'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

# DELETE document by ID
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
