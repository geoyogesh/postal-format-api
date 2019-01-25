#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get_hello_world():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/expand', methods=['GET'])
def get_expand():
    return Response(json.dumps({'Output': 'Hello World expand'}), mimetype='application/json', status=200)

@application.route('/parser', methods=['GET'])
def get_parser():
    return Response(json.dumps({'Output': 'Hello World parser'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post_hollow_world():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

if __name__ == '__main__':
    flaskrun(application)
