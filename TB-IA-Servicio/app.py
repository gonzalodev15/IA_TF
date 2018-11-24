from flask import Flask, jsonify, request, Response, json
from TF import Bayes

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "active"

@app.route('/logic', methods=['POST'])
def redBayesiana():
    if request.method == 'POST':
        body = request.get_json(force=True)
        print(body)
        sintomas = body["sintomas"]
        data = {
            'respuesta' : Bayes(sintomas)
        }
        js = json.dumps(data)
        res = Response(js, status=200, mimetype='application/json')
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS"
        res.headers['Access-Control-Allow-Headers'] = "Content-Type"
        return res


@app.errorhandler(404)
def not_found(error):
    return error

if __name__ == "__main__":
    app.run()