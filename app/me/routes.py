# app/me/routes

from app.me import me
from app.auth.models import Users
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.me.forms import frmProfile, frmTest, pp_check, frmProfilePic, frmService
from app.me.models import Personal_Info
from app import db


@me.route("/myaccount/profilesummary",methods=["GET","POST"])
@login_required
def myprofile():
    form =  frmTest()
    formpp = frmProfilePic()
    profile_pic = pp_check(current_user.user_email)
        


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


    return render_template("mypage.html", form = form, profile_pic = profile_pic, formpp = formpp )


@me.route("/account/account",methods=["GET","POST"])
@login_required
def myaccount():

    return render_template("myaccount.html")

@me.route("/account/services",methods=["GET","POST"])
@login_required
def myservices():
    frmservice = frmService()
 
    return render_template("myservices.html", form =  frmservice)

@me.route("/account/messages",methods=["GET","POST"])
@login_required
def mymessages():

    return render_template("messages.html")

@me.route("/account/uploads",methods=["GET","POST"])
@login_required
def myuploads():

    return render_template("uploads.html")