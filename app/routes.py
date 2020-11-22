from flask import render_template,redirect,flash

from app import app
from app.forms import LoginForm


@app.route('/login',methods=['GET','POST'])
def login():
    loginform = LoginForm()
    if loginform.validate():
        print(loginform.username.data)
        return redirect('/index')
    return render_template('login.html', title='home', form=loginform)


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Miguel'
    }
    posts = [  # fake array of posts
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('./index.html', title='home', user=user, posts=posts)
