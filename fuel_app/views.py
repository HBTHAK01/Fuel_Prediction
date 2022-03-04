# import statements
from flask import Blueprint, message_flashed, render_template, request, flash, redirect, url_for
from .models import Usercredentials
from . import db

# Hash passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Defining blueprint named "views"
views = Blueprint("views", __name__)

# Home Page Route
@views.route('/')
def index():
	return render_template("index.html")

# Create Account Page Route
@views.route('/createAccount', methods = ['GET', 'POST'])
def createAccount():
	if request.method == "POST":
		username = request.form.get ("username_Create")
		password = request.form.get ("password_Create")
		confirm_password = request.form.get ("password_Confirm")

		account = Usercredentials.query.filter_by (username = username).first()

		if account:
			flash ("Username already exists", category = "error")

		elif password != confirm_password:
			flash ("Passwords did not match", category = "error")

		else:
			new_user = Usercredentials(username = username, password = generate_password_hash (password, method = "sha256"))
			db.session.add(new_user)
			db.session.commit()
			flash ("Account successfully created", category = "success")
		
	return render_template("createAccount.html")

# Forgot Password Page Route
@views.route('/forgotPassword')
def forgotPassword():
	return render_template("forgotPassword.html")

# Profile Managment Page Route
@views.route('/profile')
def profile():
	return render_template("profile.html")

# Fuel Quote Page Route
@views.route('/fuelQuote')
def fuelQuote():
	return render_template("fuelQuote.html")

# Fuel Quote History Page Route
@views.route('/quoteHistory')
def quoteHistory():
	return render_template("quoteHistory.html")