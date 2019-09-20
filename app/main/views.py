
from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db,photos
from ..models import User,Pitch
from flask_login import login_required,current_user
import markdown2 
from .forms import PitchForm

# Views
@main.route('/')
def index():
    title='YouPitch'
    return render_template('index.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/write/pitch',methods =['GET','POST'])
@login_required
def new_pitch():
    form =PitchForm()
    if form.validate_on_submit():
        category=form.category.data
        pitch=form.pitch.data
        print(category)
        print(pitch)
        new_pitch=Pitch(category=category,pitch=pitch,user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('.new_pitch'))

        return all_pitches()
    title='YouPitch'
    return render_template('new_pitch.html',title=title,pitch_form=form)

