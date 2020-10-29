#app/me/forms

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, TextField, TextAreaField, FileField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError,InputRequired
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets
from app.auth.models import Users,Personal_Info,Services
from app import bcrypt
from flask_login import  current_user
import os

def num_validate(form, field):
    check = len(field.data)
    if check != 10:
        raise ValidationError('Number is greater than 10 digits')
    
def check_current_password(form, field):
    user= Users.query.filter_by(user_email = current_user.user_email).first()
    if bcrypt.check_password_hash(user.user_password,field.data) == False:
        raise ValidationError('Password does not match current password')

class frmProfile(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    mobile_phone = StringField('Mobile Number', validators=[DataRequired()])
    work_phone = StringField('Work Number', validators=[DataRequired()])
    country = SelectField('Country', choices=[('1', 'Canada'), ('2', 'UK'), ('3', 'USA')])
    postcode = StringField('Postcode', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    province = StringField('Province', validators=[DataRequired()])
    bio = TextAreaField('Bio')
    submit = SubmitField('Update')

class frmContact(FlaskForm):
    mobile_phone = StringField('Mobile Number')
    work_phone = StringField('Work Number')
    country = SelectField('Country', choices=[('1', 'Canada'), ('2', 'UK'), ('3', 'USA')])
    postcode = StringField('Postcode')
    city = StringField('City')
    submit = SubmitField('Save')

#form for web presence to be rendered on profile/editwebpresence
class frmWeb(FlaskForm):
    twitter = StringField("Twitter")
    url = StringField('Website')
    facebook = StringField('Facebook')
    submit= SubmitField("Save")

class frmAboutMe(FlaskForm):
    profile_summary = TextAreaField('Profile Summary') 
    submit= SubmitField("Save")

class frmProfilePic(FlaskForm):
    image = FileField("Upload")

class frmPassChange(FlaskForm):
    current_password = PasswordField("Current Password*",validators=[DataRequired(),check_current_password])
    new_password = PasswordField("New Password*", validators=[DataRequired(),EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm New Password*', validators=[DataRequired()])
    submit= SubmitField("Save")


#class to save profile picture as user email
def save_pp(file_name,user_email):
    f_name, f_ext = os.path.splitext(file_name.filename)
    img_name = user_email + f_ext
    img_path = os.path.join(os.getcwd(),'app/static/profile_pictures', img_name)
    file_name.save(img_path)
    return img_name

#class to save portfolio pictures
def save_uploads(file_name, category,pic_name):
    f_name, f_ext = os.path.splitext(file_name.filename)
    img_name = category + "_"  + pic_name + "_" + f_name + "_" + f_ext
    img_path = os.path.join(os.getcwd(),'app/static/profile_pictures',img_name)
    file_name.save(img_path)
    return img_name

#check if profile picture already exisit so we can render in prilfe , if not render default
def pp_check(filename):
    img_path=os.path.join(os.getcwd(),'app/static/profile_pictures', (filename + "pp.jpg"))
    if os.path.isfile(img_path ):
        profile_pic = filename + "pp.jpg"
    else:
        profile_pic = "default.jpg"
    
    return profile_pic

#form for adding service

class frmService(FlaskForm):

    service =SelectField("Service",  choices=[('1','Gardening'),('2','Lawn Mowing'),('3','Snow Removal')])
    rate = SelectField("Rate", choices=[('a','a')])
    submit = SubmitField('Save')

