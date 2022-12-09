import json
from flask import Flask, jsonify, request
from prediction import predict

application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/predictions', methods=['GET', 'POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    print(body)
    return jsonify(predict(body))

@application.route('/test', methods=['GET', 'POST'])
def test_connection():
    data = request.data or '{}'
    body = json.loads(data)
    print(body)
    return jsonify({'test': 'get post ok'})

