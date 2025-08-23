from flask import Flask
from app.blueprints.auth.routes import auth_bp

# Here, the auth blueprint handles all authentication routes, separate from the main app logic.
def create_app():
    app = Flask(__name__)
    # Load configuration
    app.config.from_object('config.Config')
    # Register blueprints
    app.register_blueprint(auth_bp)
    return app

# What is __init__.py in a flask app package?
# __init__.py is a special Python file that turns a directory into a Python package. In Flask, it usually initializes
# the app and registers blueprints, extensions, and configuration.
def db():
    return None


def routes():
    return None