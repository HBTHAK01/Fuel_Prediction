# In this file, test all the routes of the application

from app import create_app

# Home Page Route
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    
# Create Account Page Route
def test_createAccount():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/createAccount')
        assert response.status_code == 200
        assert b"FuelMaster" in response.data
        assert b"Create Account" in response.data
        assert b"Already have an account?" in response.data

# Forgot Password Page Route
def test_forgotPassword(client):
    response = client.get('/forgotPassword')
    assert response.status_code == 200

# Profile Managment Page Route
def test_profile(client):
    response = client.get('/profile')
    assert response.status_code == 200
    
# Fuel Quote Page Route
def test_fuelQuote(client):
    response = client.get('/fuelQuote')
    assert response.status_code == 200

# Fuel Quote History Page Route
def test_quoteHistory(client):
    response = client.get('/quoteHistory')
    assert response.status_code == 200


