"""
Flask config script for boiler_plate.
"""

class Config(object):
    """
    Production Configuration.
    """
    DEBUG = False


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
    DEMO_URI = os.getenv('DEMO_URI', "0.0.0.0:5001")


class DemoClientEndpoint5002(Config):
    """
    Client for Demo.

    Needs another boilerplate deployed.
    """
    DEMO_URI = os.getenv('DEMO_URI', "0.0.0.0:5002")


class DemoServerConfig(Config):
    """
    Server for Demo.
    """
    pass
    
