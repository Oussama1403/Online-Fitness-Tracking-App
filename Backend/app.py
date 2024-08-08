from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo

# Instantiate the app
app = Flask(__name__)

# Configure MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/fitness_database'  # Replace 'fitness_database' with your database name
mongo = PyMongo(app)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Activity

@app.route('/log_activity', methods=['POST'])
def log_activity():
    data = request.json
    print('Received activity data:', data)
    mongo.db.activities.insert_one(data)
    return jsonify({'message': 'Activity logged successfully'}), 200

@app.route('/delete_activity', methods=['POST'])
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
def get_activities():
    activities = mongo.db.activities.find()
    result = []
    for activity in activities:
        activity['_id'] = str(activity['_id'])  # Convert ObjectId to string
        result.append(activity)
    return jsonify(result)

# Workout

@app.route('/log_workout', methods=['POST'])
def log_workout():
    data = request.json
    print('Received workout data:', data)
    mongo.db.workouts.insert_one(data)
    return jsonify({'message': 'Workout logged successfully'}), 200

@app.route('/delete_workout', methods=['POST'])
def delete_workout():
    data = request.json
    print('Received workout data:', data)
    result = mongo.db.workouts.delete_one(data)
    if result.deleted_count > 0:
        return jsonify({'message': 'Workout deleted successfully'}), 200
    else:
        return jsonify({'message': 'No matching workout found'}), 404

@app.route('/update_workout', methods=['POST'])
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
def get_workouts():
    workouts = mongo.db.workouts.find()
    result = []
    for workout in workouts:
        workout['_id'] = str(workout['_id'])  # Convert ObjectId to string
        result.append(workout)
    return jsonify(result)

# Goal

@app.route('/log_goal', methods=['POST'])
def log_goal():
    data = request.json
    print('Received goal data:', data)
    mongo.db.goals.insert_one(data)
    return jsonify({'message': 'Goal logged successfully'}), 200

@app.route('/delete_goal', methods=['POST'])
def delete_goal():
    data = request.json
    print('Received goal data:', data)
    result = mongo.db.goals.delete_one(data)
    if result.deleted_count > 0:
        return jsonify({'message': 'Goal deleted successfully'}), 200
    else:
        return jsonify({'message': 'No matching goal found'}), 404

@app.route('/update_goal', methods=['POST'])
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
def get_goals():
    goals = mongo.db.goals.find()
    result = []
    for goal in goals:
        goal['_id'] = str(goal['_id'])  # Convert ObjectId to string
        result.append(goal)
    return jsonify(result)

# sanity check route
@app.route('/testbackend', methods=['GET'])
def testbackend():
    return jsonify('Hello from Flask!')

if __name__ == '__main__':
    app.run(debug=True)
