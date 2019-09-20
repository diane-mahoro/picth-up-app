from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies,get_movie,search_movie
from .models import pitchy
from .forms import ReviewForm

Review = reviews.Review


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='YouPitch'
    return render_template('index.html', title = title)