# import statements
from re import A

from pytest import Session
from flask import Blueprint, message_flashed, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from .models import Usercredentials, Clientinformation, Fuelquote
from . import db
from . import mail


# Hash passwords
from werkzeug.security import generate_password_hash, check_password_hash






# Defining blueprint named "views"
views = Blueprint("views", __name__)





#####################################
class pricing_module:
    def __init__(self, gallons_requested, isTexas, hasHistory, current_price = 1.50, company_profit = 0.1):
        self.gallons_requested = float(gallons_requested)
        self.current_price = current_price
        self.isTexas = isTexas
        self.hasHistory = hasHistory
        self.company_profit = company_profit

    def get_quote(self):
        if self.isTexas:
            self.location_factor = 0.02
        else:
            self.location_factor = 0.04

        if self.hasHistory:
            self.rate_history_factor = 0.01
        else:
            self.rate_history_factor = 0.00

        gallons_requested_factor = 0.02
        if self.gallons_requested < 1000:
            gallons_requested_factor = 0.03
        
        margin = self.current_price * (self.location_factor - self.rate_history_factor + gallons_requested_factor + self.company_profit)
        # print(margin)
        suggested_price = self.current_price + margin
        total_amt_due = self.gallons_requested * suggested_price

        return (suggested_price, total_amt_due)
##################################################








# Home Page Route
@views.route('/', methods = ['GET','POST'])
def index():

	# Makes sure user is logged out.
	# If a user is logged in and did not logout and tried to access the homepage again, the navbar shows.
	logout_user()

	if request.method == "POST":
		usernamelogin = request.form.get ("username_login")
		passwordlogin = request.form.get ("password_login")

		# checking username and password
		account = Usercredentials.query.filter_by (username = usernamelogin).first()
		if account and check_password_hash(account.password, passwordlogin):
			flash('You were successfully logged in')
			login_user(account)
			return redirect(url_for('views.profile'))	
		else:
			flash ("Incorrect username or password", category = "error")
										
										# Reference the user account as current user
	return render_template("index.html", account = current_user)

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
			return redirect(url_for('views.index'))	

	return render_template("createAccount.html", account = current_user)

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
			return redirect(url_for('views.index'))

	return render_template("forgotPassword.html", account = current_user)

# Profile Managment Page Route

def setUpdateProfile(existing_account, updateProfile):
	existing_account.name = updateProfile[0]

	existing_account.email = updateProfile[1]

	existing_account.address1 = updateProfile[2]

	existing_account.address2 = updateProfile[3]

	existing_account.city = updateProfile[4]

	existing_account.state = updateProfile[5]

	existing_account.zipcode = updateProfile[6]

	existing_account.userid = updateProfile[7]


@views.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
	
	if request.method == "POST":
		name = request.form.get ("name_Profile")
		email = request.form.get ("email_address")
		address1 = request.form.get ("Address1_Profile")
		address2 = request.form.get ("Address2_Profile")
		city = request.form.get ("city_Profile")
		state = request.form.get ("select-state")
		zipcode = request.form.get ("zipcode_Profile")

		existing_account = Clientinformation.query.first()

		if existing_account != None:
			updateProfile = [name, email, address1, address2, city, state, zipcode, current_user.username]

			setUpdateProfile(existing_account, updateProfile)
	
			db.session.commit()
			
			flash("Profile is updated successfully.", category = "success")
			return redirect(url_for('views.fuelQuote'))

		else:
			new_profile = Clientinformation(userid = current_user.username, name = name, email = email, address1 = address1, address2 = address2, city = city, state = state, zipcode = zipcode)
			db.session.add(new_profile)
			db.session.commit()

			# Send welcome/sign up email to the user
			msg = Message('Welcome to FuelMaster!', sender = 'fuelapp03@gmail.com', recipients = [email])
			msg.body = "Hello " + name + ",\n\n" + "Thanks for signing up with FuelMaster, most Reliable and Cheapest Fuel Price Predictor Web Application." + "\n\n" + "Regards,\n" + "FuelMaster Team"
			mail.send(msg)
			
			flash ("Entry added successfully", category = "success")
			return redirect(url_for('views.fuelQuote'))
	
	return render_template("profile.html", account = current_user)

# Fuel Quote Page Route
@views.route('/fuelQuote', methods = ['GET', 'POST'])
@login_required
def fuelQuote():
	if request.method == "POST":
		if request.form["submit_button"] == "getquote":
			# print(1)
			gallons = request.form.get ("gallons_requested")
			deliverydate = request.form.get ("delivery_date")



			



			user_find = Clientinformation.query.filter_by (userid = current_user.username).first()

			if user_find.address2:
				user_address = user_find.address1 + ", " + user_find.address2 + ", " + user_find.city + ", " + user_find.state + ", " + user_find.zipcode	
			else:
				user_address = user_find.address1 + ", " + user_find.city + ", " + user_find.state + ", " + user_find.zipcode

			
			if user_find.state == "TX":
				isTexas = True
			else:
				isTexas = False

			if Fuelquote.query.filter_by (userid = current_user.username).first():
				hasHistory = True
			else:
				hasHistory = False

			print(isTexas, hasHistory)
			price_module = pricing_module(gallons, isTexas, hasHistory, current_price = 1.50, company_profit = 0.1)
			pergallon,total = price_module.get_quote()

			return render_template("fuelQuote.html", gallons = gallons, user_address = user_address, deliverydate = deliverydate, account = current_user, pergallon = pergallon, total = total)




		elif request.form["submit_button"] == "submitquote":
			
			gallons = request.form.get ("gallons_requested")
			deliveryaddress = request.form.get ("delivery_address")
			deliverydate = request.form.get ("delivery_date")
			pergallon = request.form.get ("price_rate")
			total = request.form.get ("total_price")

			new_quote = Fuelquote(userid = current_user.username, gallons = gallons, deliveryaddress = deliveryaddress, deliverydate = deliverydate, pergallon = pergallon, total = total)
			db.session.add(new_quote)
			db.session.commit()
			flash ("Entry added successfully", category = "success")

	user_find = Clientinformation.query.filter_by (userid = current_user.username).first()

	if user_find.address2:
		user_address = user_find.address1 + ", " + user_find.address2 + ", " + user_find.city + ", " + user_find.state + ", " + user_find.zipcode	
	else:
		user_address = user_find.address1 + ", " + user_find.city + ", " + user_find.state + ", " + user_find.zipcode
	
	return render_template("fuelQuote.html", account = current_user, user_address = user_address)

# Fuel Quote History Page Route
@views.route('/quoteHistory')
@login_required
def quoteHistory():

	fuel_history = Fuelquote.query.filter_by (userid = current_user.username).all()
	

	return render_template("quoteHistory.html", account = current_user, fuel_history = fuel_history)

@views.route('/contact',  methods = ['GET', 'POST'])
@login_required
def contact():
	try:
		if request.method == "POST":
			name = request.form.get("contact_name")
			email = request.form.get("contact_email")
			subject = request.form.get("contact_subject")
			message = request.form.get("contact_message")

			msg = Message(name + ': ' + subject, sender = "customeremail", recipients = ['fuelapp03@gmail.com'])
			print(msg)
			msg.body = message
			mail.send(msg)

			flash ("Email sent successfully", category = "success")
	except:
		flash ("An Error Occur", category = "error")

	return render_template("contact.html", account = current_user)

@views.route('/about')
@login_required
def about():
	return render_template("about.html", account = current_user)

@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))