from flask_mail import Mail
import os
from flask import Flask
from .config import ProdConfig, DevConfig

app = Flask(__name__)
mail = Mail(app)

def create_app():

    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProdConfig)

    else:
        app.config.from_object(DevConfig)

    # --- DEBUG: VERIFIQUE OS VALORES CARREGADOS ---
    print("\n\n--- DEBUGGING CONFIG VALUES ---")
    print(f"MAIL_SERVER loaded: {app.config.get('MAIL_SERVER')}")
    print(f"MAIL_PORT loaded: {app.config.get('MAIL_PORT')}")
    print(f"MAIL_USERNAME loaded: {app.config.get('MAIL_USERNAME')}")
    # Nunca imprima a senha, apenas verifique se ela existe
    print(f"MAIL_PASSWORD is set: {bool(app.config.get('MAIL_PASSWORD'))}")
    print(f"MAIL_RECIPIENT loaded: {app.config.get('MAIL_RECIPIENT')}")
    print("--- END OF DEBUG ---\n\n")
    # ----------------------------------------------

    from app.main import routes
    app.register_blueprint(routes.bp)

    return app