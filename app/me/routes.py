# app/me/routes

from app.me import me
from app.auth.models import *
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.me.forms import frmContact, frmWeb, frmProfile,  pp_check, frmProfilePic, frmService,frmAboutMe,frmPassChange,save_pp
from app import db


@me.route("/myaccount/profilesummary",methods=["GET","POST"])
@login_required
def myprofile():
    
    formpp = frmProfilePic()
    profile_pic = pp_check(current_user.user_email)
    return render_template("mypage.html",title= "My_Page", formpp = formpp, profile_pic= profile_pic)

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

#route to change password
@me.route("/profile/editlogindetails", methods =["GET","POST"])
@login_required
def editlogindetails():
    form = frmPassChange()
    
    if form.validate_on_submit():
        user = Users.query.filter_by(id = current_user.id).first()
        user.user_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
        db.session.add(user)
        db.session.commit()
        flash("Password has been changed")
        return redirect(url_for('me.myprofile', title="My_Page"))

    return render_template("logindetails.html", frmChangePass= form)

@me.route("/profile/editprofilesummary", methods =["GET","POST"])
@login_required
def editprofilesummary():
   
    frmbio= frmAboutMe()

    if frmbio.validate_on_submit():
        user = Personal_Info.query.filter_by(user_id=current_user.id).first()
        if user:
            user.user_bio = frmbio.profile_summary.data
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('me.myprofile' ))
        else:
            user_info = Personal_Info(user_name = current_user.user_name, user_email = current_user.user_email, user_mobile_phone= "",
                                     user_work_phone ="", user_postcode ="",user_city= "", 
                                     user_country="",user_url ="", user_bio = frmbio.profile_summary.data,
                                     user_twitter ="", user_facebook = "", user_id = current_user.id)
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile'))
    return render_template("profilesummarydetails.html", frmbio = frmbio , title = "Edit about Me")

@me.route("/profile/editwebpresence", methods =["GET","POST"])
@login_required
def editwebpresence():
   
    frmweb= frmWeb()

    if frmweb.validate_on_submit():
        user = Personal_Info.query.filter_by(user_id=current_user.id).first()
        if user:
            user.user_twitter = frmweb.twitter.data
            user.user_url = frmweb.url.data
            user.user_facebook = frmweb.facebook.data

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('me.myprofile'))
        else:
            user_info = Personal_Info(user_name = current_user.user_name, user_email = current_user.user_email, user_mobile_phone= "",
                                     user_work_phone ="", user_postcode ="",user_city= "", 
                                     user_country="",user_url =frmweb.url.data, user_bio = "",
                                     user_twitter =frmweb.twitter.data, user_facebook =frmweb.facebook.data, user_id = current_user.id)
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile' ))
    return render_template("webpresencedetails.html", frmweb = frmweb , title = "Edit web presence")

@me.route("/profile/editcontactdetails", methods =["GET","POST"])
@login_required
def editcontactdetails():
   
    frmcontact= frmContact()

    if frmcontact.validate_on_submit():
        user = Personal_Info.query.filter_by(user_id=current_user.id).first()
        if user:
            user.user_work_phone = frmcontact.work_phone.data
            user.user_mobile_phone = frmcontact.mobile_phone.data
            user.user_postcode = frmcontact.postcode.data
            user.user_city = frmcontact.city.data
            user.user_country = frmcontact.country.data

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('me.myprofile'))
        else:
            user_info = Personal_Info(user_name = current_user.user_name, user_email = current_user.user_email, user_mobile_phone= frmcontact.mobile_phone.data,
                                     user_work_phone =frmcontact.mobile_phone.data, user_postcode =frmcontact.postcode.data,user_city= frmcontact.city.data, 
                                     user_country=frmcontact.country.data,user_url ="", user_bio = "",
                                     user_twitter ="", user_facebook ="", user_id = current_user.id)
            db.session.add(user_info)
            db.session.commit()
            return redirect(url_for('me.myprofile'))
    return render_template("contactdetails.html", frmcontact= frmcontact , title = "Edit Contact Details")


#route to edit profile picture
@me.route("/profile/editprofilepicture", methods = ["GET", "POST"])
@login_required
def editprofilepicture():

    #wtf-form to upload  selectfiled to choose profile picture 
    formpp = frmProfilePic()
    if formpp.validate_on_submit():
        pic_name = save_pp(formpp.image.data,current_user.user_email)
        # get the user that is logged in so that the profilepicture name will be chnaged 
        user= Users.query.filter_by(id = current_user.id).first()
        if user:
            user.user_pp_name = pic_name
            db.session.add(user)
            db.session.commit()
        
        return redirect(url_for('me.myprofile'))

    return render_template("profilepicture.html", title = "Edit_Profile_Picture", formpp= formpp)

