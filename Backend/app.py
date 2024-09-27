from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

# Instantiate the app
app = Flask(__name__)

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/fitness_database'  # Replace 'fitness_database' with your database name
mongo = PyMongo(app)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Replace with your own secret key
jwt = JWTManager(app)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({'message': 'Username, email or password are required'}), 400

    if mongo.db.users.find_one({'email': email}):
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({'username': username, 'email': email,'password': hashed_password})

    return jsonify({'message': 'User registered successfully'}), 201

# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print('Received login data:', data)
    username = data.get('username')
    password = data.get('password')

    user = mongo.db.users.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        # Include user_id in the token
        additional_info = {"user_id": str(user["_id"]), "username": user["username"]}
        access_token = create_access_token(identity=str(user["_id"]),additional_claims=additional_info,expires_delta=timedelta(days=1))
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

# Activity Section Routes

@app.route('/log_activity', methods=['POST'])
@jwt_required()
def log_activity():
    data = request.json
    print('Received activity data:', data)
    mongo.db.activities.insert_one(data)
    return jsonify({'message': 'Activity logged successfully'}), 200

@app.route('/delete_activity', methods=['POST'])
@jwt_required()
def delete_activity():
    data = request.json
    print('Received activity data:', data)
    # delete an activity by id not the whole data
    result = mongo.db.activities.delete_one({'_id': data.get('_id')})
    #result = mongo.db.activities.delete_one(data)
    if result.deleted_count > 0:
        return jsonify({'message': 'Activity deleted successfully'}), 200
    else:
        return jsonify({'message': 'No matching activity found'}), 404

@app.route('/update_activity', methods=['POST'])
@jwt_required()
def update_activity():
    data = request.json
    activity_id = data.get('_id')
    if not activity_id:
        return jsonify({'message': 'Activity ID is required'}), 400
    result = mongo.db.activities.replace_one({'_id': activity_id}, data)
    if result.matched_count > 0:
        return jsonify({'message': 'Activity updated successfully'}), 200
    else:
        return jsonify({'message': 'No matching activity found'}), 404

@app.route('/get_activities', methods=['GET'])
@jwt_required()
def get_activities():
    user_id = get_jwt_identity()  # Get the current user's ID from the toke
    activities = mongo.db.activities.find({"user_id": user_id})
    result = []
    for activity in activities:
        activity['_id'] = str(activity['_id'])  # Convert ObjectId to string
        result.append(activity)
    return jsonify(result)

# Workout Section Routes

@app.route('/log_workout', methods=['POST'])
@jwt_required()
def log_workout():
    data = request.json
    print('Received workout data:', data)
    mongo.db.workouts.insert_one(data)
    return jsonify({'message': 'Workout logged successfully'}), 200

@app.route('/delete_workout', methods=['POST'])
@jwt_required()
def delete_workout():
    data = request.json
    print('Received workout data:', data)
    result = mongo.db.workouts.delete_one(data)
    if result.deleted_count > 0:
        return jsonify({'message': 'Workout deleted successfully'}), 200
    else:
        return jsonify({'message': 'No matching workout found'}), 404

@app.route('/update_workout', methods=['POST'])
@jwt_required()
def update_workout():
    data = request.json
    workout_id = data.get('_id')
    if not workout_id:
        return jsonify({'message': 'Workout ID is required'}), 400
    result = mongo.db.workouts.replace_one({'_id': workout_id}, data)
    if result.matched_count > 0:
        return jsonify({'message': 'Workout updated successfully'}), 200
    else:
        return jsonify({'message': 'No matching workout found'}), 404

@app.route('/get_workouts', methods=['GET'])
@jwt_required()
def get_workouts():
    user_id = get_jwt_identity()  # Get the current user's ID from the toke
    workouts = mongo.db.workouts.find({"user_id": user_id})
    result = []
    for workout in workouts:
        workout['_id'] = str(workout['_id'])  # Convert ObjectId to string
        result.append(workout)
    return jsonify(result)

# Goal Section Routes

@app.route('/log_goal', methods=['POST'])
@jwt_required()
def log_goal():
    data = request.json
    print('Received goal data:', data)
    mongo.db.goals.insert_one(data)
    return jsonify({'message': 'Goal logged successfully'}), 200

@app.route('/delete_goal', methods=['POST'])
@jwt_required()
def delete_goal():
    data = request.json
    print('Received goal data:', data)
    result = mongo.db.goals.delete_one(data)
    if result.deleted_count > 0:
        return jsonify({'message': 'Goal deleted successfully'}), 200
    else:
        return jsonify({'message': 'No matching goal found'}), 404

@app.route('/update_goal', methods=['POST'])
@jwt_required()
def update_goal():
    data = request.json
    goal_id = data.get('_id')
    if not goal_id:
        return jsonify({'message': 'Goal ID is required'}), 400
    result = mongo.db.goals.replace_one({'_id': goal_id}, data)
    if result.matched_count > 0:
        return jsonify({'message': 'Goal updated successfully'}), 200
    else:
        return jsonify({'message': 'No matching goal found'}), 404

@app.route('/get_goals', methods=['GET'])
@jwt_required()
def get_goals():
    user_id = get_jwt_identity()  # Get the current user's ID from the toke
    goals = mongo.db.goals.find({"user_id": user_id})
    result = []
    for goal in goals:
        goal['_id'] = str(goal['_id'])  # Convert ObjectId to string
        result.append(goal)
    return jsonify(result)


# Meal Section Routes

@app.route('/log_meal', methods=['POST'])
@jwt_required()
def log_meal():
    data = request.json
    print('Received meal data:', data)
    mongo.db.meals.insert_one(data)
    return jsonify({'message': 'meal logged successfully'}), 200

@app.route('/delete_meal', methods=['POST'])
@jwt_required()
def delete_meal():
    data = request.json
    print('Received meal data:', data)
    result = mongo.db.meals.delete_one(data)
    if result.deleted_count > 0:
        return jsonify({'message': 'meal deleted successfully'}), 200
    else:
        return jsonify({'message': 'No matching meal found'}), 404

@app.route('/update_meal', methods=['POST'])
@jwt_required()
def update_meal():
    data = request.json
    meal_id = data.get('_id')
    print(meal_id)
    if not meal_id:
        return jsonify({'message': 'meal ID is required'}), 400
    result = mongo.db.meals.replace_one({'_id': meal_id}, data)
    if result.matched_count > 0:
        return jsonify({'message': 'meal updated successfully'}), 200
    else:
        return jsonify({'message': 'No matching meal found'}), 404

@app.route('/get_meals', methods=['GET'])
@jwt_required()
def get_meals():
    user_id = get_jwt_identity()  # Get the current user's ID from the toke
    meals = mongo.db.meals.find({"user_id": user_id})
    result = []
    for meal in meals:
        meal['_id'] = str(meal['_id'])  # Convert ObjectId to string
        result.append(meal)
    return jsonify(result)


# sanity check route
@app.route('/testbackend', methods=['GET'])
def testbackend():
    return jsonify('Hello from Flask!')

if __name__ == '__main__':
    app.run(debug=True)
