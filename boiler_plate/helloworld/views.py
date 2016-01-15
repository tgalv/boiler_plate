"""
The endpoint of the Boiler Plate application.
"""

from boiler_plate import app
from flask import request, Blueprint, Response

helloworld = Blueprint('helloworld' , __name__)


@helloworld.route('/', methods=["GET"])
def index():
    """
    Say Hello.

    :return: The de-facto greeting.
    :rtype: str
    """
    return 'Hello World!'
