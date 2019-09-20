from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,username,email,pass_word):
        self.id =id
        self.username=username
        self.email = email
        self.pass_word=pass_word



class Pitch:

    all_pitches = []

    def __init__(self,id,category,pitch):
        self.id = id
        self. category=category
        self.pitch =pitch


    def save_pitch(self):
        Pitch.all_pitches.append(self)


    # @classmethod
    # def clear_reviews(cls):
    #     Review.all_reviews.clear()

    @classmethod
    def get_pitch(cls,id):

        response = []

        for pitch in cls.all_pitches:
            if pitch.movie_id == id:
                response.append(pitch)

        return response

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
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
    picth_id = db.Column(db.Integer, db.ForeignKey("picthes.id"))
        

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    __tablename__='pitches'
    id=db.Column(db.Integer,primary_key = True)
    category=db.Column(db.String)
    posted=db.Column(db.DateTime, default=datetime.utcnow)
    pitchy=db.relationship('Pitch',backref = 'role',lazy='dynamic')

    def save_picth(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(id=id).all()
        return reviews
