from webbrowser import open
from sys import argv
from pyperclip import paste
from chatbot import app, db, bcrypt
from chatbot.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

def getMaps():
   address = current_user.address
   open("http://www.google.com/maps/place/"+address)