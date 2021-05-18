# from flask import Flask


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY']= 'AOURERHHSLHFHFUE'

#     from .views import views
#     from .auth import auth

#     app.register_blueprint(views,url_prefix ='/')
#     app.register_blueprint(auth,url_prefix ='/')
#     return app


# from flask import Flask
# from sqlalchemy import SQLALCHEMY

# db = SQLALCHEMY()
# DB_NAME = 'database.db'


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'DHURIERHIURIE'
#     app.config['SLQALCHEMY_DATABASE_URL'] = f'sqllite:///{DB_NAME}'
#     db.init_app(app)

#     from .views import views
#     from .auth import auth

#     app.register_blueprint(views, url_prefix='/')
#     app.register_blueprint(auth, url_prefix='/')
#     return app


from flask import Flask
from sqlalchemy import SQLALCHEMY
from os import path

db = SQLALCHEMY()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AOURERHHSLHFHFUE'
    app.config['SLQALCHEMY_DATABASE_URL'] = f'sqllite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_app()
    return app


def create_database():
    if path.exists('website/'+DB_NAME):
        db.create_all(app=app)
