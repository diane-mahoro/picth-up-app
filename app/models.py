from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __ref__(self):
        return f'User {self.username}'

class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key = True)
    comment=db.Column(db.String(255))
    picth_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
        

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    __tablename__='pitches'
    id=db.Column(db.Integer,primary_key = True)
    category=db.Column(db.String)
    pitch=db.Column(db.String)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    commenty=db.relationship('Comment',backref='role',lazy='dynamic')
    
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls):
        pitches = Pitch.query.filter_by(id=id).all()
        return pitches
