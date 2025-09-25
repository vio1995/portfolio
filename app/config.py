import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_RECIPIENT = os.environ.get('MAIL_RECIPIENT')

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False