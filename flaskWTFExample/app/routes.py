# from flask import render_template, flash, redirect,url_for
#
# from flaskWTFExample.app.forms import LoginForm
# from flaskWTFExample.app.main import app
#
# @app.route('/')
# def index():
#     return 'Welcome to homepage!'
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form  = LoginForm()
#     if form.validate_on_submit():
#         flash(f'Login requested for {form.email.data}', 'success')
#         return redirect(url_for('index'))
#     return render_template('login.html', form=form)


from flask import render_template, flash, redirect, url_for
from flaskWTFExample.app.forms import LoginForm

def init_app(app):
    @app.route('/')
    def index():
        return "Welcome to Home Page"

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash(f'Login requested for {form.email.data}', 'success')
            return redirect(url_for('index'))
        return render_template('loginForm.html', form=form)
