import os
from flask import Flask, render_template
from .config import ProdConfig, DevConfig

app = Flask(__name__)

def create_app():

    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProdConfig)

    else:
        app.config.from_object(DevConfig)

    from app.main import routes
    app.register_blueprint(routes.bp)

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('error/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('error/500.html'), 500

    return app