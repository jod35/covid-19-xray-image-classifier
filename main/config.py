import os


BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print(BASEDIR)


class Config:
    SECRET_KEY='fb0e79f78c817d9fa844a8127c87afc4402a41d64f275caac42f5f5ee69e5ddd'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+BASEDIR+'/api.sqlite3'
    DEBUG=True
    SQLALCHEMY_ECHO=True
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+BASEDIR+'/api_test.sqlite3'
    DEBUG=True
    SQLALCHEMY_ECHO=True
    
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')
    DEBUG=True
    SQLALCHEMY_ECHO=True
    