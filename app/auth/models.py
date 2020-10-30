# app/auth/models

from app import db
from flask_sqlalchemy import SQLAlchemy
from app import bcrypt
from app import login_manager
from flask_login import UserMixin


from datetime import datetime

class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100),nullable = False)
    user_email = db.Column(db.String(100),nullable = False)
    user_password = db.Column(db.String(100),nullable = False)
    user_pp_name  = db.Column(db.String(100), default= "default.jpg",nullable = False)
    email_confirmation_sent_on = db.Column(db.DateTime, nullable=True, default = datetime.utcnow())
    email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    email_confirmed_on = db.Column(db.DateTime, nullable=True,default = datetime.utcnow())
    profile = db.relationship('Personal_Info', backref = 'users', uselist = False)
   
    def __init__(self, user_name, user_email,user_password):
        self.user_name =user_name 
        self.user_email = user_email
        self.user_password= user_password

    def __repr__(self):
        return ("Account Created")

    @classmethod
    def create_user(cls, name, email, password):
        user = cls(user_name = name,
        user_email= email, 
        user_password = bcrypt.generate_password_hash(password).decode('utf-8'))

        db.session.add(user)
        db.session.commit()
        return user

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Personal_Info(db.Model):
    __tablename__ = 'personal_info'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    user_mobile_phone = db.Column(db.String(100))
    user_work_phone = db.Column(db.String(100))
    user_postcode= db.Column(db.String(100), nullable=False)
    user_city=db.Column(db.String(100))
    user_country =  db.Column(db.String(100))
    user_bio = db.Column(db.String(1000))
    user_url = db.Column(db.String(1000))
    user_twitter=db.Column(db.String(1000))
    user_facebook = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)


    def __init__(self, user_name,user_email, user_mobile_phone, user_work_phone, user_postcode, user_city,user_country,user_bio,user_url,user_twitter,user_facebook, user_id ):
        self.user_name = user_name
        self.user_email = user_email
        self.user_mobile_phone = user_mobile_phone
        self.user_work_phone = user_work_phone
        self.user_postcode = user_postcode
        self.user_city = user_city
        self.user_country = user_country
        self.user_bio = user_bio
        self.user_url= user_url
        self.user_twitter = user_twitter
        self.user_facebook = user_facebook
        self.user_id= user_id

    def __repr__(self):
        return ("Personal Info Created")

    @classmethod
    def create_personal_info(cls, name, email,  mobile_phone, work_phone, postcode,city,country,bio,
                            url, twitter,company, user_id):
        user = cls(user_name=name,
                   user_email= email,
                   user_mobile_phone=mobile_phone,
                   user_work_phone = work_phone,
                   user_postcode = postcode,
                   user_city = city,
                   user_country = country,
                   user_bio = bio,
                   user_url= url,
                   user_twitter = twitter,
                   user_company = company,
                   user_id = user_id)

        db.session.add(user)
        db.session.commit()
        return user
    
class Services(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key = True)
    service  = db.Column(db.String(100), nullable = False)
    rate = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)

    def __init__(self, service, rate, user_id):
        self.service = service
        self.rate= rate
        self.user_id = user_id

    @classmethod
    def AddService(cls,service,rate, user_id):
        service = cls(service = service, rate= rate, user_id = user_id)
        db.session.add(service)
        db.session.commit()
    
'''class ProfilePictureName(db.Model):
    __tablename__ = 'profilepicturename'

    id = db.Column(db.Integer, primary_key = True)
    user_pp_name  = db.Column(db.String(100), default= "default.jpg",nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    
    def __init__(self,user_pp_name,user_id):
        self.user_pp_name = user_pp_name 
        self.user_id = user_id
    
    def __repr__(self):
        return "profile picture changed"'''