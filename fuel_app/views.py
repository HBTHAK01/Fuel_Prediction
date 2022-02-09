# import statements
from flask import Blueprint, render_template

# defining blueprint named "views"
views = Blueprint("views", __name__)

# Home Page Route
@views.route('/')
def index():
	return render_template("index.html")