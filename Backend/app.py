from flask import Flask, jsonify, request
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Activity

@app.route('/log_activity', methods=['POST','GET'])
def log_activity():
    data = request.json
    print('Received activity data:', data)
    return jsonify({'message': 'Activity logged successfully'}), 200

@app.route('/delete_activity', methods=['POST','GET'])
def delete_activity():
    data = request.json
    print('Received activity data:', data)
    return jsonify({'message': 'Activity deleted successfully'}), 200

#Workout

@app.route('/log_workout', methods=['POST','GET'])
def log_workout():
    data = request.json
    print('Received workout data:', data)
    return jsonify({'message': 'Workout logged successfully'}), 200


@app.route('/delete_workout', methods=['POST','GET'])
def delete_workout():
    data = request.json
    print('Received workout data:', data)
    return jsonify({'message': 'Workout deleted successfully'}), 200
#Goal

@app.route('/log_goal', methods=['POST','GET'])
def log_goal():
    data = request.json
    print('Received goal data:', data)
    return jsonify({'message': 'Goal logged successfully'}), 200

@app.route('/delete_goal', methods=['POST','GET'])
def delete_goal():
    data = request.json
    print('Received goal data:', data)
    return jsonify({'message': 'Goal deleted successfully'}), 200


# sanity check route
@app.route('/testbackend', methods=['GET'])
def testbackend():
    return jsonify('Hello from Flask !')

if __name__ == '__main__':
    app.run(debug=True)