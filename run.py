from app import create_app,db
from app.auth.models import Users

if __name__ == '__main__' :
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
        if not Users.query.filter_by(user_email='olutest123@gmail.com').first():
            Users.create_user(name = 'olu', email ='olutest123@gmail.com',password = 'a')
    flask_app.run()