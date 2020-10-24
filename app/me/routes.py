# app/me/routes

from app.me import me
from app.auth.models import *
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.me.forms import frmContact, frmProfile, frmTest, pp_check, frmProfilePic, frmService
from app.me.models import Personal_Info,Services
from app import db


@me.route("/myaccount/profilesummary",methods=["GET","POST"])
@login_required
def myprofile():
    form =  frmTest()
    formContact = frmContact()
    formpp = frmProfilePic()
    profile_pic = pp_check(current_user.user_email)
        
    if formContact.validate_on_submit():
        #check if user already has info in this table
        user_info = Personal_Info.query.filter_by(user_id=current_user.id).first()
        if user_info:
            user_info.user_mobile_phone = formContact.mobile_phone.data
            user_info.user_work_phone = formContact.work_phone.data
            user_user_postcode = formContact.postcode.data
            user_info.user_city = formContact.city.data
            user_info.user_country = formContact.country.data
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile', frmContact = formContact))

        else:
            #create a new record
            mobile_phone = formContact.mobile_phone.data
            work_phone = formContact.work_phone.data
            city = formContact.city.data
            country = formContact.country.data
            postcode = formContact.postcode.data
            user_id = current_user.id

            user_info = Personal_Info(user_name = "", user_email = current_user.user_email, user_mobile_phone= mobile_phone,
                                     user_work_phone =work_phone, user_postcode =postcode,user_city= city, 
                                     user_country="",user_url = "", user_bio = "",
                                     user_twitter ="", user_facebook = "", user_id = current_user.id)
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile', frmContact = formContact))



    if form.validate_on_submit():
        #check if user exist 
        user_info = Personal_Info.query.filter_by(user_email=form.email.data).first()
        if user_info:
            #Edit profile data
            user_info.user_name = form.name.data
            user_info.user_email = form.email.data
            user_info.user_mobile_phone = form.mobile_phone.data
            user_info.user_work_phone = form.work_phone.data
            user_info.user_city = form.city.data
            user_info.user_country = form.country.data
            user_info.user_bio= form.bio.data
            user_id = current_user.id
            db.session.add(user_info)
            db.session.commit()
           
            return redirect(url_for('me.myprofile', formpp= formpp))
        else:

            name = form.name.data
            email = form.email.data
            mobile_phone = form.mobile_phone.data
            work_phone = form.work_phone.data
            city = form.city.data
            country = form.country.data
            postcode = form.postcode.data
            user_id = current_user.id
            # load to database
            Personal_Info.create_personal_info(
                name, email, mobile_phone, work_phone,postcode, city, country,"","","","",user_id)
           
            
            return render_template("mypage.html", form = form , formpp = formpp )


    return render_template("mypage.html", form = form, profile_pic = profile_pic, formpp = formpp, frmContact = formContact )


@me.route("/account/account",methods=["GET","POST"])
@login_required
def myaccount():

    return render_template("myaccount.html")

@me.route("/account/services",methods=["GET","POST"])
@login_required
def myservices():
    frmservice = frmService()
    service_exist = Services.query.filter_by(user_id = current_user.id).all()
    
    if frmservice.validate_on_submit():
        service = frmservice.service.data
        rate   = frmservice.rate.data
        user_service = Services.AddService(service,rate, current_user.id)
        return redirect(url_for('me.myservices', frmservice= frmservice))

    return render_template("myservices.html", title="Services",  service_exist =  service_exist ,form =  frmservice)

@me.route("/account/messages",methods=["GET","POST"])
@login_required
def mymessages():

    return render_template("messages.html")

@me.route("/account/uploads",methods=["GET","POST"])
@login_required
def myuploads():

    return render_template("uploads.html")