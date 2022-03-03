# import statements
from fuel_app import create_app

# Instance of create_app
app = create_app()

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
	app.run(debug = True)