# import statements
from flask import Blueprint, render_template, request
from .models import UserCredentials
from . import db

# Defining blueprint named "views"
views = Blueprint("views", __name__)

# Home Page Route
@views.route('/')
def index():
	return render_template("index.html")

# Create Account Page Route
@views.route('/createAccount', methods = ['GET', 'POST'])
def createAccount():
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