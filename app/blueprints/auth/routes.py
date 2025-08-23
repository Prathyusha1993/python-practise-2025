# What are flask blueprints? why use them?
    #A Blueprint in flask is a way to organize related routes, static files, and other code into reusable modules.
    # It helps in structuring large applications by grouping functionality.
    # Modularity - keep features seperated(eg: auth, blog, admin)
    #reusability - reuse blueprints across multiple apps
    # better collaboration - teams can work on different blueprints independently
    # scalability - easier to scale and maintain large apps

from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return render_template('login.html')
