# import statements
from . import db
from flask_login import UserMixin

# UserCredentials model defines the login details of the User
# UserMixin provides default implementations for Flask-Login expecting the user objects to have

class Usercredentials(db.Model, UserMixin):    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(150))

# Clientinformation model defines the profile details of the User
class Clientinformation(db.Model):
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), primary_key=True)
    address1 = db.Column(db.String(100))
    address2 = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(9))
    userid = db.Column(db.String(50))
    
# Fuelquote model defines the fuel quote details of the User
class Fuelquote(db.Model):
    userid = db.Column(db.String(50))
    gallons = db.Column(db.Float , primary_key=True)
    deliveryaddress = db.Column(db.String(150))
    deliverydate = db.Column(db.String(10))
    pergallon = db.Column(db.Float)
    total = db.Column(db.Float)
    