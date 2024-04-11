from flask import Flask

def create_app():                               # utworzenie startowej aplikacji
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'zaq1@WSX'       # klucz do chronienia plików cookies

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app