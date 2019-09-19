from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):

    __tablename__='users'
    id=db.Column(db.integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    pass_word= db.Column(db.String(255))
    bio=db.Column(db.String(500))

    def __repr__(self):
        return f'Welcome dear {self.username}'