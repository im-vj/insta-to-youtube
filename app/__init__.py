from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .routes.insta import insta_bp
    app.register_blueprint(insta_bp)

    return app
