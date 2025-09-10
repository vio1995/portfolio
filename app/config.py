import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig:
    DEBUG = True

class ProdConfig:
    DEBUG = False