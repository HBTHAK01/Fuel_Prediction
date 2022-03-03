# import statements
from . import db


# UserCredentials model defines the Username and password of the User
class UserCredentials(db.Model):    
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))