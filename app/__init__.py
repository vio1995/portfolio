import os
from flask import Flask, render_template
from .config import ProdConfig, DevConfig

def create_app():
    app = Flask(__name__)

    if os.environ.get(FLASK_ENV) == 'production':
        app.config.from_object(ProdConfig)

    else:
        app.config.from_object(DevConfig)

    from app.main import routes
    app.register_blueprint(routes.bp)

    return app