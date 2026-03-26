from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows your React app to talk to Flask

tasks = [
    {"id": 1, "title": "Connect Flask Backend", "status": "In Progress"},
    {"id": 2, "title": "Setup React Frontend", "status": "Completed"},
    {"id": 3, "title": "Setup Frontend", "status": "Completed"},
    {"id": 4, "title": "Connect Flask Backend", "status": "In Progress"},
    {"id": 5, "title": "Setup React Frontend", "status": "Completed"},
    {"id": 6, "title": "Connect Flask Backend", "status": "In Progress"},
    {"id": 7, "title": "Setup React Frontend", "status": "Completed"},
    {"id": 8, "title": "Connect Flask Backend", "status": "In Progress"}
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    new_task['id'] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)