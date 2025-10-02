import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
    RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False