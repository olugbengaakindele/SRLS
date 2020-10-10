#app/me/_init_

from flask import Blueprint

me = Blueprint('me',__name__,template_folder = 'templates')

from app.me import routes