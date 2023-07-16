import json

from pymongo import MongoClient

from models import user_schema

client = MongoClient("mongodb://localhost:27017/")
db = client['backend-database']
user_collection = db['users']


def validate_user_schema(data):
    for key, value_type in user_schema.items():
        if key not in data or not isinstance(data[key], value_type):
            return False
    return True


def register(request_body):
    # Validate if the request has a JSON in its body as the same structure as the User Schema
    try:
        payload = json.loads(request_body)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON payload"}, 400

    # Validate JSON payload against user schema
    if not validate_user_schema(payload):
        return {"error": "Invalid user data"}, 400

    # Validate if the username already exits in the database
    if user_collection.find_one({"username": payload["username"]}):
        return {"error": "User already Registered"}, 409

    # Insert the document into the user collection and validate
    result = user_collection.insert_one(payload)

    if not result.acknowledged:
        return {"error": "User not Registered"}, 500

    return {"message": "User Successfully registered"}, 201
