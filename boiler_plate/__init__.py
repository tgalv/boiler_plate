import os
import pkg_resources
from flask import Flask

__version__ = "0.1"

app = Flask(__name__)

from .helloworld import views

app.config.from_object(os.environ.get('SETTINGS'))
app.register_blueprint(views.helloworld, url_prefix='/helloworld')

@app.route("/")
def index():
    dist = pkg_resources.get_distribution("boiler_plate")
    return dist.egg_name()
