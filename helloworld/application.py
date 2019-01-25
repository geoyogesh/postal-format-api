#!flask/bin/python
import json
from flask import request
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get_hello_world():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/expand', methods=['GET'])
def get_expand():
    # here we want to get the value of user (i.e. ?user=some-value)
    user_input = request.args.get('q')
    if (user_input):
        return Response(json.dumps({'Output': 'please provide input query parameter q to complete expand request'}), mimetype='application/json', status=200)
    else:
        from postal.expand import expand_address
        return Response(json.dumps({'Output': 'q=' + user_input}), mimetype='application/json', status=200)

@application.route('/parser', methods=['GET'])
def get_parser():
    # here we want to get the value of user (i.e. ?user=some-value)
    user_input = request.args.get('q')
    if (user_input):
        return Response(json.dumps({'Output': 'please provide input query parameter q to comple parser request'}), mimetype='application/json', status=200)
    else:
        from postal.parser import parse_address
        return Response(json.dumps({'Output': 'q=' + user_input}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post_hollow_world():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

if __name__ == '__main__':
    flaskrun(application)
