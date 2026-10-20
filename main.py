from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Drone Detection System API"}), 200

if __name__ == '__main__':
    # Start the system on port 8000 as mentioned in the readme
    app.run(host='0.0.0.0', port=8000, debug=True)
