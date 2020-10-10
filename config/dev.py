#config/dev
import os
SECRET_KEY = os.urandom(32)

DEBUG = True
SECRET_KEY = SECRET_KEY
SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db'
SQLALCHEMY_TRACK_NOTIFICATION= False
