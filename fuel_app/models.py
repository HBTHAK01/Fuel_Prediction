# import statements
from . import db


# UserCredentials model defines the Username and password of the User
class Usercredentials(db.Model):    
    username = db.Column(db.String(150), primary_key=True)
    password = db.Column(db.String(150))