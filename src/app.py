from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    ]
@app.route('/todos', methods=['GET'])
def hello_world():
    return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    data = request.get_json(force=True)
    print("Incoming request with the following body:", data)
    todos.append(data)
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    return 'something'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)