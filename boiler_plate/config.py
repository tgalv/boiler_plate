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
