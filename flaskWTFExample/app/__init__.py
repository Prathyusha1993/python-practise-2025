from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'

    # Register routes
    from app import routes
    routes.init_app(app)

    return app