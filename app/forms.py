from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

# class ReviewForm(FlaskForm):

#     title = StringField('Review title',validators=[Required()])
#     review = TextAreaField('Movie review', validators=[Required()])
#     submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    category = StringField('Review title',validators=[Required()])
    picth = TextAreaField('The pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment=TextAreaField('Comment',validators=[Required()])
    submit=SubmitField('comment')