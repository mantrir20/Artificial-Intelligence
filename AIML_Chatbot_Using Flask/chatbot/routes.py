from flask import render_template, url_for, flash, redirect, request
from chatbot.forms import RegistrationForm, LoginForm, QueryPatient, googleMapBut
from chatbot.models import User, Post
from chatbot import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from chatbot.aiml.aiml_run import getResponse
from chatbot.location import getMaps


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    form = QueryPatient()
    posts = ''
   
        #return render_template('home.html', posts=posts, form=form, button_map=button_map)

    if form.validate_on_submit():
        posts = getResponse(form.title.data)
        #title is the query, post is the response
        post = Post(title=form.title.data, content=posts, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        #run query
        flag_given = False
    
    return render_template('home.html', posts=posts, form=form)

    
    
@app.route("/account", methods=['GET', 'POST'])
def getMap():
    button_map = googleMapBut()
    flag_given = True
    if button_map.validate_on_submit():
        getMaps()
    return render_template('account.html', button_map=button_map)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, age=form.age.data, address=form.address.data, phone=form.phone.data, blood_group=form.blood_group.data, guardian=form.guardian.data, blood_relation=form.blood_relation.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
