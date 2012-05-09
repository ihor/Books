from flask import Flask, Response, render_template, request, jsonify
import json
import shelve
from os import getcwd

app = Flask(__name__)
DB_FILE = getcwd() + '/../data/db.shlv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        data = json.loads(request.data)
        if 'tasks' in data:
            db = shelve.open(DB_FILE)
            db['tasks'] = json.loads(request.data)['tasks']
            db.close()
            return 'Saved'
        return 'Wrong tasks format'
    else:
        result = {}
        db = shelve.open(DB_FILE)
        if 'tasks' in db:
            result = db['tasks']
        db.close()

        # For some reason jsonify doesn't work properly here
        return Response(
            json.dumps(result),
            mimetype='application/json'
        )

if __name__ == '__main__':
    app.run(debug=True)

