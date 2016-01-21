"""
The endpoint of the Boiler Plate application.
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
    return 'Hello World!'
