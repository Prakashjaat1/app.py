!pip install flask flask-cors
# Import necessary libraries        

from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

# In-memory data stores (for prototype use)
users = {}
modules = {}
progress_submissions = {}

# Route: Register user (mentor or learner)
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user_id = str(uuid.uuid4())
    users[user_id] = {
        'name': data['name'],
        'role': data['role'],  # 'mentor' or 'learner'
        'email': data['email']
    }
    return jsonify({"message": "User registered", "user_id": user_id})

# Route: Upload a knowledge module (mentor only)
@app.route('/upload_module', methods=['POST'])
def upload_module():
    data = request.json
    module_id = str(uuid.uuid4())
    modules[module_id] = {
        'title': data['title'],
        'description': data['description'],
        'mentor_id': data['mentor_id'],
        'content': data['content']  # e.g., video URL, PDF link, steps
    }
    return jsonify({"message": "Module uploaded", "module_id": module_id})

# Route: Get all learning modules
@app.route('/get_modules', methods=['GET'])
def get_modules():
    return jsonify(modules)

# Route: Submit learner progress (work samples)
@app.route('/submit_progress', methods=['POST'])
def submit_progress():
    data = request.json
    submission_id = str(uuid.uuid4())
    progress_submissions[submission_id] = {
        'module_id': data['module_id'],
        'learner_id': data['learner_id'],
        'work_sample': data['work_sample'],  # URL to image/video, etc.
        'notes': data['notes']
    }
    return jsonify({"message": "Progress submitted", "submission_id": submission_id})

# Route: Get a mentor's schedule (static demo version)
@app.route('/mentor_schedule/<mentor_id>', methods=['GET'])
def mentor_schedule(mentor_id):
    return jsonify({
        "mentor_id": mentor_id,
        "available_slots": [
            "Monday 10:00-11:00 AM",
            "Wednesday 3:00-4:00 PM",
            "Friday 6:00-7:00 PM"
        ]
    })

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
    