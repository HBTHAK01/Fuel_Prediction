# import statements
from flask import Blueprint, message_flashed, render_template, request, flash, redirect, url_for
from .models import Usercredentials, Clientinformation, Fuelquote
from . import db

# Hash passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Defining blueprint named "views"
views = Blueprint("views", __name__)

# Home Page Route
@views.route('/', methods = ['GET','POST'])
def index():
	if request.method == "POST":
		usernamelogin = request.form.get ("username_login")
		passwordlogin = request.form.get ("password_login")

		# checking username and password
		usernamecheck = Usercredentials.query.filter_by (username = usernamelogin).first()
		if usernamecheck and check_password_hash(usernamecheck.password, passwordlogin):
			flash('You were successfully logged in')
			return redirect(url_for('views.profile'))	
		else:
			flash ("Incorrect username or password", category = "error")

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
@views.route('/forgotPassword', methods = ['GET', 'POST'])
def forgotPassword():
	if request.method == "POST":
		username = request.form.get ("username_Reset")
		password = request.form.get ("password_Reset")
		confirm_password = request.form.get ("c_password_Reset")

		account = Usercredentials.query.filter_by (username = username).first()

		if not account:
			flash ("Username doesn't exist", category = "error")

		elif password != confirm_password:
			flash ("Passwords did not match", category = "error")		

		else:
			account.password = generate_password_hash (password, method = "sha256")
			db.session.commit()
			flash ("Password changed successfully", category = "success")

	return render_template("forgotPassword.html")

# Profile Managment Page Route
@views.route('/profile', methods = ['GET', 'POST'])
def profile():
	if request.method == "POST":
		name = request.form.get ("name_Profile")
		email = request.form.get ("email_address")
		address1 = request.form.get ("Address1_Profile")
		address2 = request.form.get ("Address2_Profile")
		city = request.form.get ("city_Profile")
		state = request.form.get ("select-state")
		zipcode = request.form.get ("zipcode_Profile")

		new_profile = Clientinformation(name = name, email = email, address1 = address1, address2 = address2, city = city, state = state, zipcode = zipcode)
		db.session.add(new_profile)
		db.session.commit()

	return render_template("profile.html")

# Fuel Quote Page Route
@views.route('/fuelQuote', methods = ['GET', 'POST'])
def fuelQuote():
	if request.method == "POST":
		gallons = request.form.get ("gallons_requested")
		deliverydate = request.form.get ("delivery_date")

		new_quote = Fuelquote(gallons = gallons, deliverydate = deliverydate)
		db.session.add(new_quote)
		db.session.commit()


	return render_template("fuelQuote.html")

# Fuel Quote History Page Route
@views.route('/quoteHistory')
def quoteHistory():
	return render_template("quoteHistory.html")