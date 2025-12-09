from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

#variable global
todos_list= [
    { "label": "My first task", "done": False }
    { "label": "Buy milk", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route("/todos", methods=['GET'])
def todos():
    return  jsonify(todos_list)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json 
    print("Incoming request with the following body", request_body)
    todos_list.append(request_body)
    return jsonify(todos_list)
        
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos_list.pop(position)
    return jsonify (todos_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)