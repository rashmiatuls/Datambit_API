from flask import Flask
import os
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        from . import routes  # Import routes
        return app
