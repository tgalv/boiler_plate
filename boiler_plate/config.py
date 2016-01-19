"""
Flask config script for boilerplate.
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
