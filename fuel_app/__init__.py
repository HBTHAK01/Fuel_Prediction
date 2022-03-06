# import statements
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create db object
db = SQLAlchemy()

# Using pymysql connector to use for SQLALCHEMY
conn = 'mysql+pymysql://root:****@localhost/Fuel_Database'

def create_app():
    # Flask constructor
    app = Flask(__name__)

    # Configuring session cookies
    app.config['SECRET_KEY'] = 'ABC123'

    # Importing and registering blueprint "views" to our flask app
    from .views import views
    app.register_blueprint(views)

    # Connecting SQLALCHEMY to pymysql
    app.config['SQLALCHEMY_DATABASE_URI'] = conn

    # Binding db to app
    db.init_app(app)

    # Importing models
    from .models import Usercredentials

    return app