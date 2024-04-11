from flask import Flask

def create_app():                               # utworzenie startowej aplikacji
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'zaq1@WSX'       # klucz do chronienia plików cookies

    return app