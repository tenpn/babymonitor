from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Andrew' }
    posts = [
        {
            'author': {'username':'john'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Hold on there buster',
        }
    ]
    return render_template('index.html', user=user, posts=posts)
