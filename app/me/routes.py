# app/me/routes

from app.me import me
from app.auth.models import *
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.me.forms import frmContact, frmWeb, frmProfile, frmTest, pp_check, frmProfilePic, frmService,frmAboutMe
from app.me.models import Personal_Info,Services
from app import db


@me.route("/myaccount/profilesummary",methods=["GET","POST"])
@login_required
def myprofile():
    formContact = frmContact()
    formpp = frmProfilePic()
    profile_pic = pp_check(current_user.user_email)
    frmweb = frmWeb()  
    frmbio= frmAboutMe()

    if formContact.validate_on_submit():
        #check if user already has info in this table
        user_info = Personal_Info.query.filter_by(user_id=current_user.id).first()
        if user_info:
            user_info.user_mobile_phone = formContact.mobile_phone.data
            user_info.user_work_phone = formContact.work_phone.data
            user_info.user_postcode = formContact.postcode.data
            user_info.user_city = formContact.city.data
            user_info.user_country = formContact.country.data
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile', frmweb= frmweb ,  profile_pic = profile_pic, formpp = formpp, frmContact = formContact,frmbio=frmbio))

        else:
            #create a new record
            mobile_phone = formContact.mobile_phone.data
            work_phone = formContact.work_phone.data
            city = formContact.city.data
            country = formContact.country.data
            postcode = formContact.postcode.data
            user_id = current_user.id

            user_info = Personal_Info(user_name = current_user.user_name, user_email = current_user.user_email, user_mobile_phone= mobile_phone,
                                     user_work_phone =work_phone, user_postcode =postcode,user_city= city, 
                                     user_country="",user_url = "", user_bio = "",
                                     user_twitter ="", user_facebook = "", user_id = current_user.id)
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile', frmweb= frmweb ,  profile_pic = profile_pic, formpp = formpp, frmContact = formContact,frmbio=frmbio))
    elif frmweb.validate_on_submit():
        #check if user already has info in this table
        user_info = Personal_Info.query.filter_by(user_id=current_user.id).first()
        if user_info:
            user_info.user_twitter = frmweb.twitter.data
            user_info.user_facebook = frmweb.facebook.data
            user_info.user_url = frmweb.url.data

            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile', frmweb= frmweb ,  profile_pic = profile_pic, formpp = formpp, frmContact = formContact,frmbio=frmbio))

        else:
            #create a new record
            user_twitter = frmweb.twitter.data
            user_facebook = frmweb.facebook.data
            user_url = frmweb.url.data
            user_id = current_user.id
            user_info = Personal_Info(user_name = current_user.user_name, user_email = current_user.user_email, user_mobile_phone= "",
                                     user_work_phone ="", user_postcode ="",user_city= "", 
                                     user_country="",user_url =user_url, user_bio = "",
                                     user_twitter =user_twitter, user_facebook = user_facebook, user_id = current_user.id)
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile', frmweb= frmweb ,  profile_pic = profile_pic, formpp = formpp, frmContact = formContact,frmbio=frmbio))
    elif frmbio.validate_on_submit():
        #check if user already has info in this table
        user_info = Personal_Info.query.filter_by(user_id=current_user.id).first()
        if user_info:
            user_info.user_bio = frmbio.profile_summary.data
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile', frmweb= frmweb ,  profile_pic = profile_pic, formpp = formpp, frmContact = formContact,frmbio=frmbio))

        else:
            #create a new record
            user_bio = frmbio.profile_summary.data
            user_id = current_user.id
            user_info = Personal_Info(user_name = current_user.user_name, user_email = current_user.user_email, user_mobile_phone= "",
                                     user_work_phone ="", user_postcode ="",user_city= "", 
                                     user_country="",user_url ="", user_bio = user_bio,
                                     user_twitter ="", user_facebook = "", user_id = current_user.id)
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile', frmweb= frmweb ,  profile_pic = profile_pic, formpp = formpp, frmContact = formContact,frmbio=frmbio))

    return render_template("mypage.html", frmweb= frmweb ,  profile_pic = profile_pic, formpp = formpp, frmContact = formContact,frmbio=frmbio)


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