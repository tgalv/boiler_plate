"""
The endpoint of the boiler_plate application.
"""

from flask import request, Blueprint, Response
from boiler_plate import app


helloworld = Blueprint('helloworld' , __name__)


@helloworld.route('/', methods=["GET"])
def index():
    """
    Say Hello.

    :return: The de-facto greeting.
    :rtype: str
    """
    app.logger.debug("Saying hello...")
    return 'Hello World!'
