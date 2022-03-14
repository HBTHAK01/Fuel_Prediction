# import statements
from . import db


# UserCredentials model defines the login details of the User
class Usercredentials(db.Model):    
    username = db.Column(db.String(50), primary_key=True)
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
    
# Fuelquote model defines the fuel quote details of the User
class Fuelquote(db.Model):
    gallons = db.Column(db.Integer, primary_key=True)
    deliverydate = db.Column(db.String(10))
    