from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from chatbot.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    age = IntegerField('Age',
                           validators=[DataRequired()])
    address = StringField('Address',
                           validators=[DataRequired()])
    phone = StringField('Phone',
                           validators=[DataRequired(), Length(min=10, max=10)])
    blood_group = StringField('Blood Group',
                           validators=[DataRequired()])
    guardian = StringField('Guardian Name',
                           validators=[DataRequired()])
    blood_relation = StringField('Blood Relation',
                           validators=[DataRequired()])
    
    
    submit = SubmitField('Sign Up')

    #Custom Validation, Follow the same format
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class QueryPatient(FlaskForm):
    title = StringField('Query', validators=[DataRequired()])
    submit = SubmitField('Enter')

class googleMapBut(FlaskForm):
    #check =  RadioField('Check Button')
    submit = SubmitField('Go to google maps for home')