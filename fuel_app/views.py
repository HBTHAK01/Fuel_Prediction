# import statements
from flask import Blueprint, render_template

# defining blueprint named "views"
views = Blueprint("views", __name__)

# Home Page Route
@views.route('/')
def index():
	return render_template("index.html")

#Create Account Page Route
@views.route('/create')
def create():
	return render_template("accountCreate.html")

#Profile Managment Page Route
@views.route('/profile')
def profile():
	return render_template("profile.html")