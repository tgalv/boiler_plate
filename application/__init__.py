import os
from flask import Flask

app = Flask(__name__)
from application import views

app.config.from_object(os.environ.get('SETTINGS'))
