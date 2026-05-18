from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Git ve GitHub oyren"},
    {"id": 2, "title": "Docker oyren"}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
