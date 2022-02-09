# import statements
from flask import Flask
from views import views

# Flask constructor
app = Flask(__name__)

# register blueprint "views" to our flask app
app.register_blueprint(views)

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
	app.run(debug = True)