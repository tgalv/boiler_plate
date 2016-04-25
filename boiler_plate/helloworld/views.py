"""
The endpoint of the boiler_plate application.
"""

from flask import request, Blueprint, Response, jsonify
from boiler_plate import app

from .calls import DEMO_API

helloworld = Blueprint('helloworld' , __name__)


def request_wants_json():
    print(request.accept_mimetypes)
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']


@helloworld.route('/', methods=["GET"])
def index():
    """
    Say Hello.

    :return: The de-facto greeting.
    :rtype: str
    """
    app.logger.debug("Saying hello...")
    if request_wants_json():
        if app.config.get('CLIENT_MODE'):
            return DEMO_API.greet_boiler_plate()
        else:
            return jsonify({'from' : request.host,
                            'message':'Hello World!'})
    return 'Hello World!'
