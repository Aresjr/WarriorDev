import os

from flask import Flask
from flask_babel import Babel
from admin import admin
from database import db
from routes import main

def create_app():
    wapp = Flask(__name__)
    wapp.testing = True
    wapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbw.sqlite3'
    wapp.config['SECRET_KEY'] = os.environ.get('DBW_KEY')

    wapp.register_blueprint(main)
    db.init_app(wapp)
    admin.init_app(wapp)
    babel = Babel(wapp)
    return wapp

if __name__ == '__main__':
    wapp = create_app()
    wapp.app_context()
    wapp.run()
