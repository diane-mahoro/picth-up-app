from flask_wtf import FlaskForm

from wtforms.validators import Required,Email
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from ..models import User

class PitchForm(FlaskForm):
    category = StringField('Review title',validators=[Required()])
    pitch = TextAreaField('The pitch', validators=[Required()])
    submit = SubmitField('post')

class CommentForm(FlaskForm):
    comment=TextAreaField('Comment',validators=[Required()])
    submit=SubmitField('Submit')