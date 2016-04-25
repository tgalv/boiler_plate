"""
Flask config script for boiler_plate.
"""

import os


class Config(object):
    """
    Production Configuration.
    """
    DEBUG = False
    CLIENT_MODE = False


class DevelopmentConfig(Config):
    """
    Development Configuration.
    """
    DEBUG = True


class DemoClientEndpoint5001(Config):
    """
    Client for Demo.

    Needs another boilerplate deployed.
    """
    DEMO_SERVER_URI = os.getenv('DEMO_URI', "http://0.0.0.0:5001")
    CLIENT_MODE = True


class DemoClientEndpoint5002(Config):
    """
    Client for Demo.

    Needs another boilerplate deployed.
    """
    DEMO_SERVER_URI = os.getenv('DEMO_URI', "http://0.0.0.0:5002")
    CLIENT_MODE = True
