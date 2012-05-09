from flask import Flask, Response, render_template, request, jsonify
import json
import fixtures

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/folder/<id>')
def folder(id):
    # For some reason jsonify doesn't work properly in this case
    return Response(
        json.dumps({'mails': [fixtures.mail[i] for i in fixtures.mail if fixtures.mail[i]['folder'] == id]}),
        mimetype='application/json'
    )

@app.route('/mail/<id>')
def mail(id):
    return jsonify(fixtures.mail[int(id)])

if __name__ == '__main__':
    app.run(debug=True)

