from flask_mail import Mail
import os
from flask import Flask
from .config import ProdConfig, DevConfig

app = Flask(__name__)
mail = Mail()

def create_app():

    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProdConfig)

    else:
        app.config.from_object(DevConfig)

    mail.init_app(app)

    from app.main import routes
    app.register_blueprint(routes.bp)

    return app