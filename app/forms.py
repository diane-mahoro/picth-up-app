from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    category = StringField('Review title',validators=[Required()])
    picth = TextAreaField('The pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment=TextAreaField('Comment',validators=[Required()])
    submit=SubmitField('comment')