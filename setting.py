import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "eviter les attaques CSRF(seasurf)"
    
    # SQLALCHEMY_DATABASE_URI database URI
    CLOUD_SQL_USERNAME = os.environ.get("CLOUD_SQL_USERNAME")
    CLOUD_SQL_PASSWORD = os.environ.get("CLOUD_SQL_PASSWORD")
    CLOUD_SQL_DATABASE_NAME = os.environ.get("CLOUD_SQL_DATABASE_NAME")
    CLOUD_SQL_INSTANCE_CONNECTION_NAME = os.environ.get("CLOUD_SQL_INSTANCE_CONNECTION_NAME")
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')