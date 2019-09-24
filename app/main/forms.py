from flask_wtf import FlaskForm

from wtforms.validators import Required,Email
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,RadioField
from ..models import User

class PitchForm(FlaskForm):
    category = RadioField('Category',choices=[('promotionpitch','promotionpitch'), ('interviewpitch','interviewpitch'),('pickuplines','pickuplines'),('productpitch','productpitch')],validators=[Required()])
    description = TextAreaField('The pitch', validators=[Required()])
    submit = SubmitField('post')

class CommentForm(FlaskForm):
    comment=TextAreaField('Comment',validators=[Required()])
    submit=SubmitField('post')

class UpVoteForm(FlaskForm):
    submit=SubmitField()

class DownVoteForm(FlaskForm):
    submit=SubmitField()