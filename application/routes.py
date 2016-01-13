import json
import requests


from application import app
from flask import request, Response


@app.route('/', methods=["GET"])
def index():
    return 'Hello World!'
