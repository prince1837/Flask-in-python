from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	print ("my name is khan")
	return ("sanjay")
if __name__ == '__main__':
    app.run(debug=True)


# =========================================================================================================================================


from flask import Flask, jsonify
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)


# ============================================================================================================================





from flask import Flask,jsonify,abort
app = Flask(__name__)

tasks = [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done":  False,
      "id": 1,GET
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": False,
      "id": 2,
      "title": "Learn Python"
    },
    {"description": "Need to teacher for good good teach ever",
    "done": False,
    "id": 3,
    "title": "learn non-tech activity"
    }
  ]

@app.route('/prince', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
@app.route('/prince/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
if __name__ == '__main__':
    app.run(debug=True,port=8000)



# ===================================================================================================================================





from flask import Flask,make_response,jsonify
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run(debug=True,port=8000)




# =============================================================================================================================================



from flask import Flask,jsonify,request,abort
app = Flask(__name__)
tasks = [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done":  False,
      "id": 1,
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": False,
      "id": 2,
      "title": "Learn Python"
    },
    {"description": "Need to teacher for good good teach ever",
    "done": False,
    "id": 3,
    "title": "non-tech activity"
    }
  ]
@app.route('/prince', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
@app.route('/prince', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task ={
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
        }

    tasks.append(task)
    return jsonify({'task': task}), 201
if __name__=='__main__':
    app.run(debug=True)


# ========================================================================================================================================






from flask import Flask,jsonify,request,abort
app = Flask(__name__)
tasks = [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done":  False,
      "id": 1,
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": False,
      "id": 2,
      "title": "Learn Python"
    },
    {"description": "Need to teacher for good good teach ever",
    "done": False,
    "id": 3,
    "title": "non-tech activity"
    }
  ]
@app.route('/prince', methods=['GET'])
def get_tasks():
    return jsonify({'task': tasks})

@app.route('/prince', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task ={
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
        }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/prince/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/prince/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__=='__main__':
    app.run(debug=True)





# ============================================================================================================================================





from flask import  url_for,Flask,jsonify,abort
app = Flask(__name__)

tasks= [ 
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done":  False,
      "id": 1,
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": False,
      "id": 2,
      "title": "Learn Python"
    },
    {"description": "Need to teacher for good good teach ever",
    "done": False,
    "id": 3,
    "title": "learn non-tech activity"
    } 
]

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/prince/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/prince', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

if __name__=='__main__':
    app.run(debug=True)








