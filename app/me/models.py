from app import db
from flask_sqlalchemy import SQLAlchemy
from app import bcrypt
from app import login_manager
from datetime import datetime
from app.auth.models import *

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
    user_company = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)


    def __init__(self, user_name,user_email, user_mobile_phone, user_work_phone, user_postcode, user_city,user_country,user_bio,user_url,user_twitter,user_company, user_id ):
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
        self.user_company = user_company
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
    sector  = db.Column(db.String(100), nullable = False)
    sub_sector = db.Column(db.String(100), nullable = False)

    def __init__(self, sector, sub_sector):
        self.sector = sector
        self.sub_sector = sub_sector

    @classmethod
    def AddService(cls,sector,sub_sector):
        service = cls(sector = sector, sub_sector= sub_sector)
        db.session.add(service)
        db.session.commit()
        