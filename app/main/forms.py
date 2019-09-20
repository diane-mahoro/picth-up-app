from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User

# class ReviewForm(FlaskForm):

#  title = StringField('Review title',validators=[Required()])

#  review = TextAreaField('Movie review')

#  submit = SubmitField('Submit')
# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')


class PitchForm(FlaskForm):

    category = StringField('Category',validators=[Required()])
    picth = TextAreaField('The pitch', validators=[Required()])
    submit = SubmitField('post')

class CommentForm(FlaskForm):
    comment=TextAreaField('Comment',validators=[Required()])
    submit=SubmitField('comment')