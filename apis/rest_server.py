from flask import Flask, request
import json

app = Flask("REST example")

todos = []

@app.route('/todos', methods=['GET'])
def get():
    return json.dumps(todos)

@app.route('/todos/<int:index>', methods=['POST','PUT','DELETE'])
def modify(index):
    if request.method == 'PUT':
        if index < len(todos):
            todos[index] = request.json
        else:
            todos.append(request.json)
        return json.dumps(todos), 200
    elif request.method == 'POST':
        if index < len(todos):
            todos[index].update(request.json)
        else:
            todos.append(request.json)
        return json.dumps(todos), 200
    elif request.method == 'DELETE':
        if index < len(todos):
            todos.pop(index)
            return json.dumps(todos), 200
        else:
            return "Could not find element at {0}".format(index), 404

app.run(debug=False)