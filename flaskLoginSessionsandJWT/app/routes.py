from flask import Blueprint, request, redirect, url_for, render_template, session
from flask_login import login_user, login_required, logout_user, current_user
from .usermodel import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # user = User.query.filter_by(username=username).first()
        if username == 'user' and password == 'pass':
            session['user_id'] = 1
            # login_user(user)
            return redirect(url_for('auth.dashboard'))
        return 'Invalid credentials', 401
    return render_template('login.html')

@auth.route('/dashboard')
@login_required
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', username='user')
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

