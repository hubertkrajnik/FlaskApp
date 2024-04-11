from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Future login.</p>"

@auth.route('/logout')
def logout():
    return "<p>Future logout.</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Future sign up.</p>"