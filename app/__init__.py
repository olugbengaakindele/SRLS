from flask import Flask, Blueprint
import os
from flask_mail import  Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager


db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.signin"
login_manager.session_protection = "strong"
mail = Mail()
SECRET_KEY_2= os.urandom(32)

def create_app(config_type): #test/dev/ prod
    
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config' , config_type + '.py')
    mail_config =  os.path.join(os.getcwd(), 'config' , 'mail.py')

    app.config.from_pyfile(configuration)
    app.config.from_pyfile(mail_config)

    #initialize database to flask app
    db.init_app(app)
    mail.init_app(app)
    #initialize bootstrap
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    #register blueprit
    from app.auth import auth 
    app.register_blueprint(auth)

    from app.me import me 
    app.register_blueprint(me)

 
    return app


