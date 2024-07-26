from flask import Flask, jsonify
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/testbackend', methods=['GET'])
def testbackend():
    return jsonify('Hello from Flask !')


if __name__ == '__main__':
    app.run()