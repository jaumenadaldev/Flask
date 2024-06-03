from flask import Config

class Config(object):
    SECRET_KEY = "clave_secreta"
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'